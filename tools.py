# tools.py
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import YoutubeVideoSearchTool

youtube_tool = YoutubeVideoSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini/gemini-3-flash-preview",
            ),
        ),
        embedder=dict(
            provider="google-generativeai",
            config=dict(
                model_name="models/embedding-001",
                task_type="RETRIEVAL_DOCUMENT",
            ),
        ),
    )
)