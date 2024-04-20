# CommitGenAI
generates git commits using llm

## Command to Run
To activate the virtual environment and run the script on staged Git diffs, use the following command: <br/>
source /Users/jinseokoh/git_commit_msg_autogen/venv/bin/activate && git diff --staged | python /Users/jinseokoh/git_commit_msg_autogen/main.py && deactivate
