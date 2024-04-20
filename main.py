import sys
import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler



# def parse_diff(diff_stream):
#     diff_data = []
#     current_file = None
#     current_hunk = None

#     for line in diff_stream:

#         if line.startswith('+++ ') or line.startswith('--- '):
#             if current_file:
#                 diff_data.append(current_file)
#             current_file = {'filename': line[4:].strip(), 'changes': []}

#         elif line.startswith('@@'):
#             current_hunk = {'added': [], 'removed': []}
#             current_file['changes'].append(current_hunk)

#         # code that had been added
#         elif line.startswith('+') and line[1:].strip() != '':
#             current_hunk['added'].append(line[1:].strip())

#         # code that had been deleted
#         elif line.startswith('-') and line[1:].strip() != '':
#             current_hunk['removed'].append(line[1:].strip())

#     if current_file:
#         diff_data.append(current_file)
        
#     return diff_data



def main(diff_stream):

    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         '''
         Here are instructions from the user outlining your goals and how you should respond:
            As Git Commit Message Pro, your primary role is to craft precise, professional Git commit messages. You are a specialist in analyzing .patch or .diff files, interpreting them as Git patch instructions. When a .patch or .diff file is attached or inputed, You will always write a Git commit message, presenting the title and description together in Markdown format for developers to easily copy and paste. The format will be:
            The git commit title (max 60-character)
            The git commit description (Only readable text)
            Your responses are clear, direct, and tailored for developers. You focus on delivering straightforward, technically accurate messages without explaining the changes at the end.
            Incorporate a type, scope, and subject as per Conventional Commits specification
            You don't need to write the project name on the commit message or title since it will be committed to its repository.
            If you can read the entire file, reread it with more characters to catch all the content.
            Your message must be informative; if you fail to get all the content, write a generic technical explanation about what you understood.
            You don't need to transcribe what the diff does. You must make it human-readable.
            You can make bullet points to explain the overall changes.
            You must avoid mentioning the project name on the commit messages since it is for.
            Do not request additional information.
         '''
            ),
        ("ai", "What are the staged changes? Provide me with a .diff file"),
        ("human", "{changes}")
    ])

    chain = prompt | chat

    chain.invoke({"changes": diff_stream})


if __name__ == "__main__":
    diff_stream = sys.stdin.read()
    main(diff_stream)

# source /Users/jinseokoh/git_commit_msg_autogen/venv/bin/activate && git diff --staged | python /Users/jinseokoh/git_commit_msg_autogen/main.py && deactivate

