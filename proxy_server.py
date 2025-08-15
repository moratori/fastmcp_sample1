# 天気取得
# https://yeasty-xerinae.fastmcp.app/mcp

from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient

backend = ProxyClient("https://yeasty-xerinae.fastmcp.app/mcp")
mcp = FastMCP.as_proxy(backend)
