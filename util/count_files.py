from collections import Counter
from datetime import datetime
import os


def count_files():
    files_info = []
    total_file_count = 0
    directory_list = [directory for directory in os.listdir("./") if "Level" in directory]
    for directory in directory_list:
        file_list = os.listdir(f"./{directory}")
        file_count = len(file_list)
        temp = [directory, file_count]
        files_info.append(temp)
        total_file_count += file_count
    return files_info, total_file_count
  
  
def make_info(files_info, total_file_count):
    info = f"## Files Count In Folders\nTotal File Count: {total_file_count}\n"
    for directory_files_info in files_info:
        temp = f"- {directory_files_info[0]}: {directory_files_info[1]}\n"
        info += temp
    return info
    


def make_read_me(info):
    return f"""# ✏️프로그래머스 알고리즘 문제 풀기✏️
목표 : 프로그래머스 알고리즘 문제를 1일 1커밋한다.
{info}
"""


def update_readme():
    files_info, total_file_count = count_files()
    info = make_info(files_info, total_file_count)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)