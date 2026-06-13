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

