import os
import argparse


parser = argparse.ArgumentParser(description="Log analyzer")
parser.add_argument("folder", help="Folder path")
parser.add_argument("--text", required=True, help="Search text")
parser.add_argument("--full", help="Logs search", action="store_true")
args = parser.parse_args()

log_folder = args.folder
search_text = args.text
search_full = args.full

for filename in os.listdir(log_folder):
    file_path = os.path.join(log_folder, filename)
    with open(file_path, encoding="utf-8", errors="ignore") as new_file:
        for line_number, line in enumerate(new_file, start=1):
            if search_text in line:
                words = line.strip().split()
                try:
                    index = words.index(search_text)
                except ValueError:
                    continue

                start = max(0, index - 5)
                end = min(len(words), index + 6)
                snippet = " ".join(words[start:end])

                print(f"[{filename}:{line_number}] {snippet}")

                if not search_full:
                    break
