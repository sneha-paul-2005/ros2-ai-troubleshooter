import os
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import requests

MCP_URL = "http://localhost:8000"

# Detect mode — local Ollama or Groq API
ROSA_MODE = os.getenv("ROSA_MODE", "local")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

if ROSA_MODE == "groq" and GROQ_API_KEY:
    from langchain_groq import ChatGroq
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        max_tokens=2028,
        api_key=GROQ_API_KEY
    )
else:
    from langchain_ollama import ChatOllama
    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0,
        num_predict=2028,
        extra_body={"think": False}
    )

@tool
def get_active_nodes() -> str:
    """Get all active ROS2 nodes currently running."""
    try:
        response = requests.get(f"{MCP_URL}/get_active_nodes", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_robot_status() -> str:
    """Get current robot status and active topics."""
    try:
        response = requests.get(f"{MCP_URL}/get_robot_status", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_lidar_snapshot() -> str:
    """Get a snapshot of LiDAR sensor data from /scan topic."""
    try:
        response = requests.get(f"{MCP_URL}/get_lidar_snapshot", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_navigation_status() -> str:
    """Get current navigation and odometry status."""
    try:
        response = requests.get(f"{MCP_URL}/get_navigation_status", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_tf_tree() -> str:
    """Get the TF transformation tree of the robot."""
    try:
        response = requests.get(f"{MCP_URL}/get_tf_tree", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_full_health_check() -> str:
    """Get a complete health check of the robot including nodes, topics, lidar and odometry all at once."""
    try:
        response = requests.get(f"{MCP_URL}/get_full_health_check", timeout=15)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def search_knowledge_base(query: str) -> str:
    """Search the ROS2 knowledge base for known errors, fixes, and documentation."""
    try:
        from rag.rag_engine import search_ros2_knowledge
        return search_ros2_knowledge(query)
    except Exception as e:
        return f"Error: {e}"

tools = [
    get_active_nodes,
    get_robot_status,
    get_lidar_snapshot,
    get_navigation_status,
    get_tf_tree,
    get_full_health_check,
    search_knowledge_base
]

system_prompt = """You are ROSA, an intelligent ROS2 AI Assistant.
You help robotics developers diagnose, troubleshoot and fix ROS2 problems.
Always search the knowledge base first, then check live robot data if needed.
Give clear, specific answers with exact commands."""

agent = create_react_agent(llm, tools, prompt=system_prompt)

def ask_ros2(question: str) -> str:
    """Send a question to ROSA."""
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].content