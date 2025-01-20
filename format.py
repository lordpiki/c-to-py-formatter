
def get_longest_line(lines):
    longest_line = 0
    for line in lines:
        if len(line) > longest_line:
            longest_line = len(line)
    return longest_line

def check_last_char(line):
    forbidden_chars = ['{', '}', ';']
    if line[-2] in forbidden_chars:
        return True
    
# This function takes a file path and will move all the and curly braces to a fixed position 
def format_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        longest_line = get_longest_line(lines) + 2
        for line in lines:
            if line.strip() == '':
                continue
            if check_last_char(line):
               # insert as many spaces as needed to reach the longest line and then move the char to there
                spaces = longest_line - len(line)
                line = line[:-2] + ' ' * spaces + line[-2:]
                print(line, end='') 

def main():
    file_to_format = 'main.c'
    format_file(file_to_format)



if __name__ == '__main__':
    main()
    
    
    