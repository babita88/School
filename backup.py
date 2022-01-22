import shutil

source = input("Source Directory: ")
destination = input("Destination Directory: ")

try:
    shutil.copytree(source, destination)
except (FileNotFoundError, FileExistsError) as F:
    print("Please chck the source / destination! For Details see this message:")
    print(F.args)
    exit(1)
else:
    print("Directory Backedup Successfully!")
    exit(0)
finally:
    print("--- Thanks for Checking out our Program! ---")
