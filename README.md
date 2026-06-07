# Crewai Demo

A small Python demo that uses the `crewai` and `crewai-tools` libraries to build a two-agent workflow. The first agent researches YouTube videos on a given topic, and the second agent writes a blog post from the research results.

## How it works

1. `main.py` starts the workflow by asking the user for a blog topic.
2. It creates a `Crew` with two agents and two tasks.
3. The first task uses a YouTube search tool to research relevant videos.
4. The second task writes a Markdown blog post using the research results.
5. The final blog post is printed and saved to `blog_output.md`.

## Libraries used

- `crewai`: Provides the core agent, task, and process abstractions used to build the workflow.
- `crewai-tools`: Supplies the YouTube video search tool integration.
- `python-dotenv`: Loads environment variables from a `.env` file.
- `google-genai` / `gemini`: Used implicitly through the `crewai` and `crewai-tools` configuration for the LLM.

## Files and responsibilities

### `main.py`
- Loads environment variables using `dotenv`.
- Imports two agents from `agents.py` and two tasks from `tasks.py`.
- Builds a `Crew` object with:
  - `agents=[video_researcher, blog_writer]`
  - `tasks=[research_task, blog_task]`
  - `process=Process.sequential`
- Runs the workflow with `crew.kickoff(inputs={"user_topic": user_topic})`.
- Prints the final blog output and writes it to `blog_output.md`.

### `agents.py`
- Loads environment variables and configures the language model (`LLM`) using Gemini.
- Defines `video_researcher`, an agent responsible for:
  - Finding relevant YouTube videos
  - Extracting key insights and research information
  - Using the YouTube search tool from `tools.py`
- Defines `blog_writer`, an agent responsible for:
  - Turning research output into a polished blog post
  - Writing in a clear, engaging Markdown format

### `tasks.py`
- Defines the task structure for the workflow using `Task` from `crewai`.
- `research_task` instructs the `video_researcher` to:
  - Search YouTube for videos about the given topic
  - Extract video titles, URLs, summaries, facts, and takeaways
- `blog_task` instructs the `blog_writer` to:
  - Create a complete blog post in Markdown
  - Include a title, introduction, sections, conclusion, and sources
  - Use `research_task` output as context via `context=[research_task]`

### `tools.py`
- Configures the `YoutubeVideoSearchTool` from `crewai_tools`.
- Sets the tool to use Gemini for LLM calls and Google Generative AI embeddings for retrieval.
- The tool enables the `video_researcher` to search and analyze YouTube videos automatically.

### `test.py`
- A small example script that demonstrates direct usage of the Google GenAI client.
- Loads an API key from environment variables and generates a simple text response.
- This file is useful for quick tests of the Gemini API credentials.

## Environment setup

1. Create a `.env` file with keys like:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

(If `requirements.txt` is not present, install from `pyproject.toml` via `pip install .` or with `pip install crewai[google-genai]>=1.14.6 crewai-tools>=1.14.6 python-dotenv`.)

## Run the demo

```bash
python main.py
```

Then enter your blog topic when prompted. The generated blog will be saved to `blog_output.md`.

crewai documentatuion : https://docs.crewai.com/en/tools/search-research/youtubevideosearchtool