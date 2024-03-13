import sys

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

    print(parse_diff(diff_stream))


if __name__ == "__main__":
    main(sys.stdin)

# command to activate: git diff --cached | /path/to/venv/bin/python path/to/process_diff.py
