import time, os
from PyAutoCode import ACCESS_TOKEN 
from github import Github
from datetime import datetime

g = Github(ACCESS_TOKEN)

end_time = time.time()
start_time = end_time - 86400

# gather all the Python repos from previous 2 days (1000 repos each day | API limit :/)
# collecting 2000 repositories in total
for i in range(2):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d")
    end_time_str = datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d")

    query = f"language:python created:{start_time_str}..{end_time_str}"

    end_time -= 86400
    start_time -= 86400 

    result = g.search_repositories(query=query)
    print(result.totalCount)

    for repository in result:
        print(f"{repository.clone_url}")
        os.system(f"git clone {repository.clone_url} PyAutoCode/PyAutoCode/resources/repos/{repository.owner.login}/{repository.name}")
