from dotenv import load_dotenv
load_dotenv()

# main.py
from crewai import Crew, Process
from agents import video_researcher, blog_writer
from tasks import research_task, blog_task

def run_crew(user_topic: str):
    crew = Crew(
        agents=[video_researcher, blog_writer],
        tasks=[research_task, blog_task],
        process=Process.sequential,  # Agent 1 runs first, then Agent 2
        verbose=True,
    )

    result = crew.kickoff(inputs={"user_topic": user_topic})
    return result

if __name__ == "__main__":
    topic = input("Enter your blog topic: ")
    output = run_crew(topic)

    print("\n" + "="*60)
    print("FINAL BLOG POST:")
    print("="*60)
    print(output)

    # Save the blog to a file
    with open("blog_output.md", "w") as f:
        f.write(str(output))
    print("\nBlog saved to blog_output.md")