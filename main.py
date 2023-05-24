
import os
  
  
# Source file path
source = 'main2.txt'
  
# destination file path
dest = 'newfile.txt'
  
  
# Now rename the source path
# to destination path
# using os.rename() method
os.rename(source, dest)
print("Source path renamed to destination path successfully.")