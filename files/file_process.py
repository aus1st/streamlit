from pathlib import Path


class FileProcess:
    def __init__(self):
        pass

    def read_file(self, file_path):
        try:
            path = Path('./' + file_path)
            contents = path.read_text().rstrip()
        except FileNotFoundError:
            print('File not found')
        else:    
            print(contents)
        
    def read_file_lines(self, file_path):
        path = Path('./' + file_path)
        contents = path.read_text().rstrip()
        lines = contents.splitlines()
        count = 0
        for l in lines:
            count += 1
            print(f'{count}: {l}')

    def read_file_lines_len(self, file_path):
        path = Path('./' + file_path)
        contents = path.read_text().rstrip()
        lines = contents.splitlines()
        pi_string = ''
        for l in lines:
            pi_string += l

        print(f'{pi_string}')
        print(f'Length:{len(pi_string)}')

    def read_file_lines_slice(self, file_path):
            path = Path('./' + file_path)
            contents = path.read_text().rstrip()
            lines = contents.splitlines()
            pi_string = ''
            for l in lines:
                pi_string += l

            print(f'{pi_string[:52]}...')
            print(f'Length:{len(pi_string)}')

    def write_line(self, message,file_path):
        path = Path('./'+file_path)
        path.write_text(message+'\n')
        print('write done')

    def count_words(self,file_path):
        try:
            path = Path('./'+file_path)
            print(path)
            contents = path.read_text('encoding="utf-8"').rstrip()
        except FileNotFoundError:
            print('File not found')
        else:
            words = contents.split()
            print(f'There are {len(words)} words in {file_path}')
        

file = FileProcess()
file.count_words('alice_in_the_wonderland.txt')
#file.read_file('pi_digit.txt')
#file.read_file_lines_slice('pi_digits.txt')
#file.write_line("Hello, i love programming"
#                  " i love to code each day"
#                  " i love to learn new things and compete with others",'write_file.txt')
#file.read_file_lines('write_file.txt')