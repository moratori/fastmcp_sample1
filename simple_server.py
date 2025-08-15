from fastmcp import FastMCP
import random

mcp = FastMCP("MyServer")

random.seed()

@mcp.tool
def get_japanese_weather(japanese_prefecture_name: str) -> str:
    """
    Get today's weather for the specified prefecture in Japan and return either “sunny,” “cloudy,” or “rainy.”
    """
    return random.choice(["sunny", "cloudy", "rainy"])