from functions.get_files_info import get_file_content

print('\nTest 1: Read main.py')
print(get_file_content("calculator", "main.py"))

print('\nTest 2: Read pkg/calculator.py')
print(get_file_content("calculator", "pkg/calculator.py"))

print('\nTest 3: Attempt to read /bin/cat')
print(get_file_content("calculator", "/bin/cat"))

print('\nTest 4: Attempt to read non-existent file')
print(get_file_content("calculator", "pkg/does_not_exist.py"))
