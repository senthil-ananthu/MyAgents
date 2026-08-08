"""
InfoMCPServer.py
A simple information provider for Claude certification details.
"""

from __future__ import annotations

CLAUDE_CERTIFICATIONS = {
    "Claude Safety Certification": {
        "description": "A training and assessment pathway designed to validate knowledge of Claude's safety guardrails, responsible use practices, and policy compliance.",
        "scope": "Safety principles, content filtering, harmful content mitigation, secure deployment best practices.",
        "audience": "Developers, product managers, and operators working with Claude-powered applications.",
        "validity": "Review recommended annually to stay current with updates.",
    },
    "Claude Developer Certification": {
        "description": "A certificaticon for developers building applications with Claude, focusing on API usage, tool orchestration, prompt design, and system integration.",
        "scope": "API basics, request/response handling, prompt engineering, agent patterns, error handling, and observability.",
        "audience": "Software engineers and technical integrators using Claude SDKs and APIs.",
        "validity": "Applies to the current major Claude release; refresh when new major versions are launched.",
    },
    "Claude Application Review": {
        "description": "A review process to ensure Claude applications meet deployment standards for reliability, compliance, and user experience.",
        "scope": "Application architecture, safety review, privacy controls, logging, monitoring, and fallback behavior.",
        "audience": "Teams preparing Claude-based products for production launch.",
        "validity": "Applicable per application release cycle and updated for significant feature changes.",
    },
}


def list_claude_certifications() -> list[str]:
    """Return the available Claude certification names."""
    return sorted(CLAUDE_CERTIFICATIONS.keys())


def get_claude_certification_info(name: str) -> dict[str, str] | None:
    """Return details for a specific Claude certification name."""
    if not name:
        return None
    return CLAUDE_CERTIFICATIONS.get(name.strip())


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available Claude certifications:")
        for cert in list_claude_certifications():
            print(f"- {cert}")
        sys.exit(0)

    certification_name = " ".join(sys.argv[1:]).strip()
    info = get_claude_certification_info(certification_name)
    if info is None:
        print(f"Certification '{certification_name}' not found.\n")
        print("Available Claude certifications:")
        for cert in list_claude_certifications():
            print(f"- {cert}")
        sys.exit(1)

    print(f"Claude Certification: {certification_name}\n")
    for field, value in info.items():
        print(f"{field}: {value}")
