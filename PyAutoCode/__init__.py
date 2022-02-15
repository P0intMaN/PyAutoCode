from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
