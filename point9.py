# 9.1.1
def are_files_equal(file1, file2):
    with open(file1, "r") as f1:
        content1 = f1.read()
    with open(file2, "r") as f2:
        content2 = f2.read()
    return content1 == content2

# 9.1.2
file_path = input("Enter a file path: ")
task = input("Enter a task (sort / rev / last): ")
with open(file_path, "r") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
if task == "sort":
    words = []
    for line in lines:
        words.extend(line.split())
    unique_words = sorted(set(words))
    print(unique_words)

elif task == "rev":
    for line in lines:
        print(line[::-1])

elif task == "last":
    num = int(input("Enter a number: "))
    for line in lines[-num:]:
        print(line)

# 9.2.2
def copy_file_content(source, destination):
    with open(source, "r") as src_file:
        content = src_file.read()
    with open(destination, "w") as dest_file:
        dest_file.write(content)


# 9.2.3
def who_is_missing(file_name):
    with open(file_name, "r") as file:
        numbers = file.read().split(",")
    numbers = [int(num) for num in numbers]
    n = len(numbers) + 1
    for i in range(1, n + 1):
        if i not in numbers:
            missing = i
            break
    with open("found.txt", "w") as file:
        file.write(str(missing))
    return missing

# 9.3.1
def my_mp3_playlist(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    max_song = ""
    max_duration = 0
    singer_count = {}
    for line in lines:
        parts = line.strip().split(";")
        song = parts[0]
        singer = parts[1]
        duration = parts[2]
        minutes, seconds = duration.split(":")
        total_seconds = int(minutes) * 60 + int(seconds)
        if total_seconds > max_duration:
            max_duration = total_seconds
            max_song = song
        if singer in singer_count:
            singer_count[singer] += 1
        else:
            singer_count[singer] = 1
    most_common_singer = max(singer_count, key=singer_count.get)
    return (max_song, len(lines), most_common_singer)