from pathlib import Path

# absolute path: c:\local\user
# relative path: directories in py

path = Path("ecommerce")
print(path.exists())

# rmdir(), mkdir() remove and make new directories
path2 = Path("eemails")
print(path2.rmdir())
print(path2.mkdir())

path3 = Path()
# '*' or '*.*' to get all of the files, directories,... in the program
# '*.py/*.xl,...' to get a specific type of files
for files in path3.glob('*.py'):
    print(files)

# Pypi(Python package index), Pip is a website in which python coder will share their own packages
# https://pypi.org/

