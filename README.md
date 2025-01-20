# C-to-Python Code Formatter

## Revolutionizing C Code Formatting!

Are you tired of the rigid, bracket-heavy structure of C code? Do you wish your C programs could exude the elegance and readability of Python? Look no further! **C-to-Python Code Formatter** is here to transform the way you view and write C code. Experience the magic of code that reads like Python, the way it was always meant to be seen!

---

## Features

- **Pythonic Indentation**: Goodbye, curly braces! Your C code will now flow beautifully using indentation.
- **Simplified Syntax**: `if`, `while`, and `for` blocks look clean and Pythonic.
- **Improved Readability**: Easier for new programmers to understand and follow C code.
- **Fast and Efficient**: Quickly reformats your code without altering its functionality.

---

## Sample Transformation

### Input (Traditional C Code):
```c
#include <stdio.h>

int main() {
    int x = 10;
    if (x > 5) {
        printf("x is greater than 5\n");
    } else {
        printf("x is less than or equal to 5\n");
    }
    return 0;
}
```

### Output (Python-Style C Code):
```c
int main()                                        {
    int x = 10                                    ;
    if (x > 5)                                    {
        printf("x is greater than 5\n")           ;
    } else                                        {
        printf("x is less than or equal to 5\n")  ;
                                                  }
    return 0                                      ;
                                                   }
```

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lordpiki/c-to-py-formatter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd c-to-py-formatter
    ```

3. Run the formatter:
    ```bash
    python3 format.py
    ```

---

## Why?

Programming is about communication. While C's traditional syntax has served well for decades, its heavy reliance on braces can make code less approachable. By adopting a Pythonic formatting style, we aim to:

- Improve **readability** for new programmers.
- Provide a modern and clean look to C code.
- Enhance the overall **developer experience**.

---

## Contributing

We welcome contributions from developers who share our vision! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## Acknowledgments

Special thanks to the Python and C programming communities for inspiring this project. Together, we’re shaping the future of code readability!