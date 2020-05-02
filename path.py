from pathlib import Path
#Absolute path
#Relative path
#path = Path("ecommerce4")
#print(path.exists()) #Returns True if the path exists
#print(path.mkdir())  #Creates a directory
#print(path.rmdir())  #Removes a directory
path = Path()
#print(path.glob("*.*"))
#print(path.glob("*.py"))

for file in path.glob("*.py"):
    print(file)
