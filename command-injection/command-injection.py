import subprocess

filename = input("Please provide a file name to search and display:\n")
command = ["cat", filename]
subprocess.run(command, check=True)
