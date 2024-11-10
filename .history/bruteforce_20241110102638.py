'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'r') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            contents = f.read()
            pwds = contents.split()
            pwdlist= [str(value) for value in pwds]
            print(pwdlist)
            for fx in pwdlist:
                try:
                    zf.extractall("../EncryptedFilePack", pwd=fx.encode())

                    print(f"Successfully extracted files with password: {fx}")
                    return True
                except RuntimeError:
                    pass
            return False


            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")

if __name__ == "__main__":
    main()