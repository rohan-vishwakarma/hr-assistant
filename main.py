# server.py
from mcp.server.fastmcp import FastMCP
from tools.employees import employee_list

# Create an MCP server
mcp = FastMCP("Hr-Assistant")


mcp.add_tool(employee_list)
