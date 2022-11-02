from zipfile import ZipFile
with ZipFile('/Users/pedroarellano/Documents/GitHub/PArellano02/guido_secrets.zip') as zf:
    password = 'BFDL'
    zf.extractall(pwd=password)