
def get_longest_line(lines):
    longest_line = 0
    for line in lines:
        if len(line) > longest_line:
            longest_line = len(line)
    return longest_line

def check_last_char(line):
    forbidden_chars = ['{', '}', ';']
    if line[-1] in forbidden_chars:
        return True
    if line[-2] in forbidden_chars:
        return True
    
# This function takes a file path and will move all the and curly braces to a fixed position 
def format_file(path):
    lines = [] 
    with open(path, 'r') as f:
        lines = f.readlines()
    
    fixed_lines = []
    longest_line = get_longest_line(lines) + 2
    for line in lines:
        if line.strip() == '':
            continue
        if check_last_char(line):
            # insert as many spaces as needed to reach the longest line and then move the char to there
            spaces = longest_line - len(line)
            line = line[:-2] + ' ' * spaces + line[-2:]
            fixed_lines.append(line)
    # write to file
    with open(path, 'w') as f:
        f.write(''.join(fixed_lines))
            

# get arguments from cmd line
import sys
def get_args():
    return sys.argv[1:]

def main():

    file_to_format = input("Enter the file path: ")
    format_file(file_to_format)
    print("file is now fixed!")



if __name__ == '__main__':
    main()
    
    
    