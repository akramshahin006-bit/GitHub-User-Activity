import sys
import json
import urllib.request
import urllib.error
def fetch_usr_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    req=urllib.request.Request(url, headers={'User-Agent':'Github-Activity-CLI'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code == 403:
            print("Error: API rate limit exceeded. Please try again later.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: Failed to reach GitHub servers ({e.reason}).")
        sys.exit(1)

           
def format_event(event):
    event_type= event.get("type")
    repo_name = event.get("repo",{}).get("name","unknown repopsitory")
    payload = event.get("payload",{})
    if event_type == "PushEvent":
        commit_count = len(payload.get("commits",[]))
        return f"PushEvent: {commit_count} commit(s) pushed to {repo_name}"
    elif event_type == "IssueEvent":
        action = payload.get("action","modified")
        return f"-{action.capitalize()} an issue in {repo_name}"
    elif event_type == "WatchEvent":
        return f"-Started watching {repo_name}"
    elif event_type == "CreateEvent":
        ref_type = payload.get("ref_type","resource")
        
        return f"-Created a new {ref_type} in {repo_name}"
    elif event_type == "PullRequestEvent":
        action = payload.get("action", "updated")
        return f"- {action.capitalize()} a pull request in {repo_name}"
    elif event_type == "IssueCommentEvent":
        return f"- Commented on an issue in {repo_name}"
    else:
        # Fallback for unhandled GitHub event types
        clean_type = event_type.replace("Event", "") if event_type else "Action"
        return f"- Executed {clean_type} in {repo_name}"

def main():
    if len (sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
    username = sys.argv[1]
    events = fetch_usr_activity(username)
    if not events:
        print(f"No recent public activity found for user '{username}'.")
        sys.exit(0)
    print(f"\n Recent public activity for user '{username}':")
    for event in events:
        print(format_event(event))


if __name__ == "__main__":
    main()     
