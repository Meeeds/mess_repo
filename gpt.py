python_code = """
print("Hello, World!")
"""

cpp_code = """
#include <iostream>

int main() {{
    std::cout << "{0}";
    return 0;
}}
"""

# Replace newline and double-quote characters in Python code
escaped_python_code = python_code.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n")

# Insert Python code into C++ code
cpp_program = cpp_code.format(escaped_python_code)

# Print the C++ code
print(cpp_program)
