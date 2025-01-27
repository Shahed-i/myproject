from github import Github

# Authenticate using your GitHub personal access token
ACCESS_TOKEN = ""  
g = Github(ACCESS_TOKEN)

# Get the repository you want to work with
repo = g.get_repo("Shahed-i/myproject")  

# 1. Get all branches
print("Branches:")
for branch in repo.get_branches():
    print(branch.name)

# 2. Get all pull requests created by me
print("\nPull Requests:")
for pr in repo.get_pulls(state="open", sort="created"):
    if pr.user.login == g.get_user().login:  # Check if you created the PR
        print(f"PR Title: {pr.title}, URL: {pr.html_url}")

# 3. Get a list of commits in the main branch
main_branch = repo.get_branch("main")
print("\nCommits in Main Branch:")
for commit in repo.get_commits(sha=main_branch.commit.sha):
    print(commit.commit.message)
