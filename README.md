# College Assignment Assistant MCP

## Overview

The **College Assignment Assistant MCP** is a simple Model Context Protocol (MCP) server designed to help students manage their college assignments. It provides assignment information, allows the client to check the status of a particular assignment, and provides a reusable prompt for creating a step-by-step completion plan.

The project demonstrates the three main MCP primitives: **Tool, Resource, and Prompt**, with each primitive being used for a different purpose.

## Why This Project Was Chosen

College students often have multiple assignments with different subjects, deadlines, and completion statuses. This project provides a simple and practical use case where assignment information can be accessed and interacted with through MCP.

The project was chosen because assignment management clearly demonstrates the difference between an MCP Tool, Resource, and Prompt without requiring external APIs or complex dependencies.

## MCP Primitives Used

### Tool – `get_assignment_status()`

The tool is used to check the status and deadline of a specific assignment.

**Why a Tool was chosen:**

A tool is appropriate when the client needs to perform an action based on user input. In this project, the user provides an assignment name, and the tool searches the stored assignment data and returns the relevant subject, deadline, and status.

The Tool was selected because checking an assignment requires an operation to be performed based on the user's input.

### Resource – `college://assignments`

The resource provides access to the complete stored assignment information.

**Why a Resource was chosen:**

A resource is suitable for providing data or context to the MCP client without performing an action or modifying the data. The assignment information is stored in `assignments.json`, so it can be exposed through an MCP resource using a fixed URI.

The Resource was selected because assignment information is data that the client can access as context rather than an operation that needs to be performed.

### Prompt – `plan_assignment()`

The prompt provides a reusable instruction for creating a step-by-step plan for completing an assignment.

**Why a Prompt was chosen:**

A prompt is useful when a user wants to intentionally select a predefined instruction for a particular task. In this project, the planning instruction provides a consistent structure for organizing the work required to complete an assignment.

The Prompt was selected because assignment planning is a repeatable task where a predefined instruction can be reused whenever required.


## System Design

```text
                    MCP Client
                  / MCP Inspector
                         |
                         | MCP
                         ↓
          College Assignment MCP Server
                         |
          +--------------+--------------+
          |              |              |
          ↓              ↓              ↓
        TOOL          RESOURCE         PROMPT
          |              |              |
 get_assignment_   college://      plan_assignment()
     status()       assignments
          |              |
          ↓              ↓
          +-------- assignments.json



## Project Structure

college-assignment-mcp/
│
├── server.py              # MCP server
├── assignments.json       # Assignment data
├── README.md              # Project documentation
├── pyproject.toml         # Project configuration
├── uv.lock                # Dependencies
