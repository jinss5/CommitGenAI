import sys
import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler



def parse_diff(diff_stream):
    diff_data = []
    current_file = None
    current_hunk = None

    for line in diff_stream:

        if line.startswith('+++ ') or line.startswith('--- '):
            if current_file:
                diff_data.append(current_file)
            current_file = {'filename': line[4:].strip(), 'changes': []}

        elif line.startswith('@@'):
            current_hunk = {'hunk': line.strip(), 'added': [], 'removed': []}
            current_file['changes'].append(current_hunk)

        # code that had been added
        elif line.startswith('+') and line[1:].strip() != '':
            current_hunk['added'].append(line[1:].strip())

        # code that had been deleted
        elif line.startswith('-') and line[1:].strip() != '':
            current_hunk['removed'].append(line[1:].strip())

    if current_file:
        diff_data.append(current_file)
        
    return diff_data



def main(diff_stream):

    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

    chat.predict("say hello" + diff_stream)


if __name__ == "__main__":
    diff_stream = sys.stdin.read()
    main(diff_stream)

# command to run: source /path/to/venv/bin/activate && git diff --staged | python /path/to//main.py && deactivate
# source /Users/jinseokoh/git_commit_msg_autogen/venv/bin/activate && git diff --staged | python /Users/jinseokoh/git_commit_msg_autogen/main.py && deactivate
