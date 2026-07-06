"""网易云音乐 MCP Server"""

import sys
import argparse
import asyncio
import os

from .main import mcp


def main():
    """MCP Server CLI 入口"""
    parser = argparse.ArgumentParser(
        description="网易云音乐 MCP Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Transport type (default: stdio)",
    )

    args = parser.parse_args()

    if args.transport == "sse":
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", "8080"))
        print(f"Starting SSE server on {host}:{port}")
        mcp.run(transport="sse", host=host, port=port)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
