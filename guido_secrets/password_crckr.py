
from fileinput import filename
from zipfile import ZipFile
# with ZipFile('whitehouse_secrets.zip') as zf:

#     password = b'BFDL'
#     zf.extractall(pwd=password)
    # password_str = 'BFDL'
    # password = password_str.encode('ascii')/

def crackZip(filename,password):
    try:
        with ZipFile(filename) as zf:
            zf.extractall(pwd = password)
        return True
    except:
        pass

f = open("/Users/pedroarellano/Documents/GitHub/PArellano02/guido_secrets/Ashley-Madison.txt", "r") 
file = (f.read())
passwords = file.encode('utf-8')
passwords = passwords.split()

# passwords = file.split()
for password in passwords:
    ok_status = crackZip("/Users/pedroarellano/Documents/GitHub/PArellano02/guido_secrets/whitehouse_secrets.zip", password)
    if ok_status == True :
        print ('password =', password )
        break
    else:
        continue
open('/Users/pedroarellano/Documents/GitHub/PArellano02/guido_secrets/whitehouse_secrets.zip')


