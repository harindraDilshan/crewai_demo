# tasks.py
from crewai import Task
from agents import video_researcher, blog_writer

# Task 1: Research YouTube videos on the user's topic
research_task = Task(
    description=(
        "Search YouTube for videos about: {user_topic}.\n"
        "Find the most relevant video URLs related to this topic, then use the "
        "YouTube search tool to extract key insights, main points, and important "
        "details from the video content.\n"
        "Provide a detailed research summary including: video titles/URLs found, "
        "main topics covered, key facts, expert opinions, and any actionable takeaways."
    ),
    expected_output=(
        "A structured research report containing:\n"
        "- The YouTube video(s) found and their URLs\n"
        "- A summary of the key points covered\n"
        "- Important facts, stats, or quotes from the videos\n"
        "- Main takeaways relevant to: {user_topic}"
    ),
    agent=video_researcher,
)

# Task 2: Write a blog post from the research
blog_task = Task(
    description=(
        "Using the research findings provided, write a comprehensive and engaging "
        "blog post about: {user_topic}.\n"
        "The blog post should:\n"
        "- Have a catchy title\n"
        "- Include an introduction, multiple body sections with subheadings, and a conclusion\n"
        "- Be between 600–900 words\n"
        "- Reference the YouTube video(s) as sources\n"
        "- Be written for a general audience"
    ),
    expected_output=(
        "A complete blog post in Markdown format with:\n"
        "- A title (# Heading)\n"
        "- Introduction paragraph\n"
        "- 3–4 sections with subheadings (## Heading)\n"
        "- Conclusion\n"
        "- A 'Sources' section linking the YouTube videos"
    ),
    agent=blog_writer,
    context=[research_task],  # Blog writer receives the researcher's output
)