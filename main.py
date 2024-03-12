import sys

def parser(input):
    return input

def main(input_stream):

    changes = parser(input_stream)

    for line in changes:

        print(line, end='')

if __name__ == "__main__":
    main(sys.stdin)

# command to activate: git diff --cached | /path/to/venv/bin/python path/to/process_diff.py
