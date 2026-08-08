from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext

class LoggingMiddleware(Middleware):
    async def on_message(self, context: MiddlewareContext, call_next):
        print("Before tool call")
        print(f"→ {context.method}")
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