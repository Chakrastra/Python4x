# try except , else , finally


def read_file(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File not found: {filename}")
    else:
        try:
            content = file.read()
            print(content)
        finally:
            file.close()
            print("File operation completed")

read_file('sample.txt')










