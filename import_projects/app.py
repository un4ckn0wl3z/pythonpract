from utils.common.file_operation import save_to_file, read_file


if __name__ == '__main__':
    save_to_file('Hello', 'data.txt')
    print(read_file('data.txt'))