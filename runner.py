from issue_handler import get_latest_issue
from prompt_context_builder import create_prompt_context
from change_applier import main as run_patch
from pr_reviewer import leave_review

def main():
    print("📥 Fetching latest issue...")
    issue = get_latest_issue()
    if issue:
        print("🛠️ Running patch routine...")
        run_patch()
        print("✅ Patch process done. You can now review or open a PR.")

if __name__ == "__main__":
    main()
