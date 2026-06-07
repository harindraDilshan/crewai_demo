import os
from dotenv import load_dotenv
load_dotenv()

# agents.py
import os
from crewai import Agent, LLM
from tools import youtube_tool
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini as the LLM for both agents
gemini_llm = LLM(
    model="gemini/gemini-3-flash-preview",
    api_key=os.getenv("GEMINI_API_KEY"),
)

# Agent 1: Finds and researches YouTube videos
video_researcher = Agent(
    role="YouTube Video Researcher",
    goal="Find the most relevant YouTube videos for the user's topic and extract key insights from them.",
    backstory=(
        "You are an expert video researcher with a sharp eye for quality content. "
        "You know how to identify the most informative and relevant YouTube videos "
        "on any topic and extract the essential points from them."
    ),
    tools=[youtube_tool],
    llm=gemini_llm,
    verbose=True,
)

# Agent 2: Writes a blog post using the research
blog_writer = Agent(
    role="Blog Writer",
    goal="Write an engaging, well-structured blog post based on the video research provided.",
    backstory=(
        "You are a skilled content writer who specializes in turning raw research "
        "into compelling blog posts. You write in a clear, engaging style that "
        "keeps readers hooked from introduction to conclusion."
    ),
    llm=gemini_llm,
    verbose=True,
)