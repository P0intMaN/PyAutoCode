from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
print(GITHUB_ACCESS_TOKEN)
