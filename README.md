# CommitGenAI
generates git commits using llm

## Command to Run
To activate the virtual environment and run the script on staged Git diffs, use the following command: <br/>
```bash
source /path/to/venv/bin/activate && git diff --staged | python /path/to/main.py && deactivate 
```


## Ideas for Project Improvement

### Contextual Understanding Improvement
Enhance the AI's ability to understand the context of the changes. This could involve training the AI to recognize patterns in code changes that correspond to specific types of modifications (bug fixes, feature additions, refactoring, etc.).

### Customization Options
Allow users to customize the format and verbosity of the commit messages. Different teams or projects might have different standards for what they expect in a commit message.

### Extensive Testing
Rigorously test the bot in diverse scenarios to ensure reliability, including handling edge cases in code changes.

### Performance Optimization
Since the tool interacts with potentially large diff files, optimizing its performance in terms of processing speed would enhance user experience.

### Automated Summaries of Large Diffs
For larger diffs, provide a summary of the changes instead of trying to detail everything, focusing on key changes and their implications.

### Commit Classification
The tool could classify the type of commit (e.g., feature, bug fix, documentation) and tag the commit message accordingly.
