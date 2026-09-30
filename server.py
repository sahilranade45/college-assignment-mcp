import json
from mcp.server import MCPServer

mcp = MCPServer("college-assignment-assistant")


def load_assignments():
    with open("assignments.json", "r") as f:
        return json.load(f)



@mcp.tool()
def get_assignment_status(assignment: str) -> str:
    """Check the status and deadline of a college assignment."""

    assignments = load_assignments()

    for item in assignments:
        if item["assignment"].lower() == assignment.lower():
            return (
                f"Subject: {item['subject']}\n"
                f"Assignment: {item['assignment']}\n"
                f"Deadline: {item['deadline']}\n"
                f"Status: {item['status']}"
            )

    return f"Assignment '{assignment}' was not found."



@mcp.resource("college://assignments")
def get_all_assignments() -> str:
    """Provide all college assignment information."""

    assignments = load_assignments()

    return json.dumps(assignments, indent=2)



@mcp.prompt()
def plan_assignment(assignment: str) -> str:
    """Create a reusable prompt for planning an assignment."""

    return (
        f"Create a simple step-by-step plan for completing the "
        f"college assignment '{assignment}'. "
        f"Include the main tasks, suggested order, and important points "
        f"to complete it before the deadline."
    )



if __name__ == "__main__":
    mcp.run()