"""
ADKMCPServer.py
ADK information provider for tools and topic lookup.
"""

from __future__ import annotations

ADK_TOPICS = {
    "Agent Development Kit Overview": {
        "description": "A high-level introduction to the ADK, its purpose, and the core components used for building AI agents.",
        "focus": "Architecture, agent patterns, tool integration, and developer workflows.",
        "audience": "Developers and architects designing agents with the ADK.",
        "notes": "Use this topic to understand how the ADK connects components and manages interactions.",
    },
    "ADK Tool Integration": {
        "description": "Guidance on registering, configuring, and using tools within the ADK ecosystem.",
        "focus": "Tool wrappers, input/output schemas, orchestration, and middleware hooks.",
        "audience": "Developers implementing ADK tools and agent capabilities.",
        "notes": "Includes best practices for safe and reliable tool invocation.",
    },
    "ADK Prompt Engineering": {
        "description": "Best practices for writing effective prompts and controlling agent behavior through the ADK.",
        "focus": "Prompt templates, context management, instruction design, and response filtering.",
        "audience": "Developers and prompt engineers using the ADK to tune agent outputs.",
        "notes": "Helps create more predictable and user-friendly agent interactions.",
    },
}


def list_adk_topics() -> list[str]:
    """Return a sorted list of available ADK topics."""
    return sorted(ADK_TOPICS.keys())


def get_adk_topic_info(topic_name: str) -> dict[str, str] | None:
    """Return ADK topic details by name."""
    if not topic_name:
        return None
    return ADK_TOPICS.get(topic_name.strip())


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available ADK topics:")
        for topic in list_adk_topics():
            print(f"- {topic}")
        sys.exit(0)

    topic_name = " ".join(sys.argv[1:]).strip()
    info = get_adk_topic_info(topic_name)
    if info is None:
        print(f"Topic '{topic_name}' not found.\n")
        print("Available ADK topics:")
        for topic in list_adk_topics():
            print(f"- {topic}")
        sys.exit(1)

    print(f"ADK Topic: {topic_name}\n")
    for field, value in info.items():
        print(f"{field}: {value}")
