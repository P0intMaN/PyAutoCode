from PyAutoCode import ACCESS_TOKEN 
from github import Github

g = Github(ACCESS_TOKEN)
result = g.search_repositories(query="python")

for repository in result:
    print(repository.clone_url)
    break
