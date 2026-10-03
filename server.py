
import json
from fastmcp import FastMCP

mcp = FastMCP("college-assignment-assistant")

ASSIGNMENTS_FILE = "assignments.json"


def load_assignments():
    with open(ASSIGNMENTS_FILE, "r") as f:
        return json.load(f)


def save_assignments(assignments):
    with open(ASSIGNMENTS_FILE, "w") as f:
        json.dump(assignments, f, indent=2)

#tool - add assignment

@mcp.tool()
def add_assignment(
    subject: str,
    assignment: str,
    deadline: str,
    status: str = "Pending"
) -> str:
    """Add a new college assignment."""

    assignments = load_assignments()

    for item in assignments:
        if item["assignment"].lower() == assignment.lower():
            return f"Assignment '{assignment}' already exists."

    new_assignment = {
        "subject": subject,
        "assignment": assignment,
        "deadline": deadline,
        "status": status
    }

    assignments.append(new_assignment)
    save_assignments(assignments)

    return (
        f"Assignment added successfully.\n"
        f"Subject: {subject}\n"
        f"Assignment: {assignment}\n"
        f"Deadline: {deadline}\n"
        f"Status: {status}"
    )

#tool - get assignment status

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

#tool - update assignment

@mcp.tool()
def update_assignment(
    assignment: str,
    status: str | None = None,
    deadline: str | None = None
) -> str:
    """Update the status or deadline of an existing assignment."""

    assignments = load_assignments()

    for item in assignments:
        if item["assignment"].lower() == assignment.lower():

            if status is not None:
                item["status"] = status

            if deadline is not None:
                item["deadline"] = deadline

            save_assignments(assignments)

            return (
                f"Assignment updated successfully.\n"
                f"Subject: {item['subject']}\n"
                f"Assignment: {item['assignment']}\n"
                f"Deadline: {item['deadline']}\n"
                f"Status: {item['status']}"
            )

    return f"Assignment '{assignment}' was not found."


@mcp.tool()
def list_assignments() -> str:
    """List all college assignments with their subject, deadline, and status."""
    assignments = load_assignments()

    if not assignments:
        return "No assignments found."

    result = []

    for item in assignments:
        result.append(
            f"Subject: {item['subject']}\n"
            f"Assignment: {item['assignment']}\n"
            f"Deadline: {item['deadline']}\n"
            f"Status: {item['status']}"
        )

    return "\n\n".join(result)


#resource - get all assignments

@mcp.resource("college://assignments")
def get_all_assignments() -> str:
    """Provide all college assignment information."""

    assignments = load_assignments()

    return json.dumps(assignments, indent=2)


#prompt - planning assignment

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

