filename = 'example_file'

################################################################################
# opening a file
################################################################################

# b = binary (think bytes)
# r = read
with open(filename, 'br') as f:
    text = f.read()
    text = text.decode('utf-8') #if encoded in utf-16 just modify inside the function
print("text=",text)


# If remove the b, then pythonwill automatically conveert from bytes to string
# called opening the file in text mode
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
print("text=",text)

################################################################################
# absolute vs relative paths
################################################################################

import os
os.getcwd()
