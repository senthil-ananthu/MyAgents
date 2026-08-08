from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_http_headers



class LoggingMiddleware(Middleware):
    async def on_message(self, context: MiddlewareContext, call_next):
        print("Before tool call")
       
        headers =  get_http_headers()
        allowed_roles = headers.get("allowed_roles", "Unknown Client")
        allowed_countries = headers.get("allowed_countries", "Unknown Client")
        
        print(f"→ {context.method} - {allowed_roles} - {allowed_countries}")

        if allowed_roles == "Unknown Client" or allowed_roles != "Admin":
            print("Unauthorized role attempt detected. Rejecting request.")
            return {"error": "Unauthorized role. Missing or invalid headers."}

        if allowed_countries == "Unknown Client" or allowed_countries != "US":
            print("Unauthorized Countries attempt detected. Rejecting request.")
            return {"error": "Unauthorized Countries. Missing or invalid headers."}
        
        result = await call_next(context)
        print(f"← {context.method}")
        return result

    async def on_request(self, context: MiddlewareContext, call_next):
        print("After tool call")
        print(f"→ {context.method}")
        result = await call_next(context)
        print(f"→ {context.method}")
        return result
    
mcp = FastMCP("My First MCP Server")
mcp.add_middleware(LoggingMiddleware())

@mcp.tool(description="A simple greeting tool.")
def greet(name: str) -> str:
    print(f"Received name: {name} - in version 1.0")
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8001)