import argparse
import os
import re


parser = argparse.ArgumentParser(description="Analize logs")
parser.add_argument("path", type=str, help="path to log file or folder")
parser.add_argument("--text", type=str, required=True, help="text to search")

args = parser.parse_args()
user_path = args.path
search_word = args.text

TIMESTAMP_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}")


if os.path.isfile(user_path):
    logs_files = [user_path]
elif os.path.isdir(user_path):
    logs_files = [
        os.path.join(user_path, filename)
        for filename in os.listdir(user_path)
        if os.path.isfile(os.path.join(user_path, filename))
    ]
else:
    logs_files = []


def get_blocks(file_lines):
    blocks = {}
    current_time = None
    current_lines = []
    for line in file_lines:
        match = TIMESTAMP_PATTERN.match(line)
        if match:
            if current_time is not None:
                blocks[current_time] = "".join(current_lines)
            current_time = match.group()
            current_lines = [line]
        else:
            current_lines.append(line)
    if current_time is not None:
        blocks[current_time] = "".join(current_lines)
    return blocks


def get_context(text, word, window=5):
    words = text.split()
    search_words = word.split()
    n = len(search_words)
    result = []
    for i in range(len(words) - n + 1):
        if words[i:i + n] == search_words:
            start = max(0, i - window)
            end = min(len(words), i + n + window)
            context = " ".join(words[start:end])
            result.append(context)
    return result


for file_path in logs_files:
    with open(file_path, "r", encoding="utf-8") as data:
        lines = data.readlines()
    blocks = get_blocks(lines)
    for block_time, block_text in blocks.items():
        if search_word in block_text:
            contexts = get_context(block_text, search_word)
            for context in contexts:
                print(f"In file {file_path}, time {block_time}: {context}")
