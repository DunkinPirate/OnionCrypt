import os
import sys
import time
import random
import uuid
import pyAesCrypt
import MainFuncs as mainFuncs
from random import randint

bufferSize = 64 * 1024
localName = ''

class Login:
    cryptPass = ''
    username = ''
    password = ''
    def Login(self):
        print('[+]Please login below. If you have forgotten your info, decrypt your Login.txt.OnionCrypt file.')
        user = input('[+]USERNAME:')
        if user == "guest":
            print('[+]OnionCrypt is running in guest mode. Your files will not be encrypted.')
            time.sleep(3)
            pass
    def SetInfo(self):
        print('''
//////////////////////////////////////////////////////////////////
/ Welcome to OnionCrypt! OnionCrypt is an encrypted web browsing /
/ and web request program that uses the Tor network (.onion).    /
/ In addition to the anonymity provided to you through Tor, this /
/ program also encrypts your browsing info and your history so   /
/ governments, corporations, and other people cannot spy on you. /
/                                                                /
/ To get started, enter a desired username and password below.   /
/ OnionCrypt will immediately write this info to a text file to  /
/ be encrypted upon the information being successfuly saved.     /
//////////////////////////////////////////////////////////////////
''')
        user = input('[+]DESIRED USERNAME:')
        localName = user
        password = input('[+]DESIRED PASSWORD:')
        Login.username = user
        Login.password = password
        info_file = open("Login.txt", "w")
        info_file.write(user)
        info_file.write(password)
        info_file.close()
        print('[+]Login info saved. Encrypting...')
        cryptPass = ''.join(random.choice('0123456789ABCDEF')for i in range(16))
        Login.cryptPass = cryptPass
        crypt_file = open("Key.txt", "w")
        crypt_file.write(cryptPass)
        crypt_file.close()
        print('[+]Decryption key written to Key.txt.')
        time.sleep(1)
        Login().Encrypt()
        print('''
///////////////////////////////////////////////////////
/ All done! OnionCrypt has encrypted your login data. /
/ The key to decrypt your login file has been saved   /
/ as "Key.txt" in this directory. It's a good idea to /
/ write your key down and delete this file.           /
///////////////////////////////////////////////////////''')
        Boot.firstSetup = False
        confirm = input('[+]Enter your decryption key to continue.')
        if confirm == Login.cryptPass:
            print('[+]Valid decryption key submitted.')
            time.sleep(2)
            pass
        else:
            print('[+]Invalid key. Shutting down.')
            time.sleep(3)
            sys.exit()
    def Encrypt(self):
        pyAesCrypt.encryptFile("Login.txt", "Login.txt.OnionCrypt", Login.cryptPass, bufferSize)

class Boot:
    firstSetup = True
    def Banner(self):
        print('''
  ______             __                       ______                                   __     
 /      \           /  |                     /      \                                 /  |    
/$$$$$$  | _______  $$/   ______   _______  /$$$$$$  |  ______   __    __   ______   _$$ |_   
$$ |  $$ |/       \ /  | /      \ /       \ $$ |  $$/  /      \ /  |  /  | /      \ / $$   |  
$$ |  $$ |$$$$$$$  |$$ |/$$$$$$  |$$$$$$$  |$$ |      /$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$/   
$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |   __ $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ 
$$ \__$$ |$$ |  $$ |$$ |$$ \__$$ |$$ |  $$ |$$ \__/  |$$ |      $$ \__$$ |$$ |__$$ |  $$ |/  |
$$    $$/ $$ |  $$ |$$ |$$    $$/ $$ |  $$ |$$    $$/ $$ |      $$    $$ |$$    $$/   $$  $$/ 
 $$$$$$/  $$/   $$/ $$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/        $$$$$$$ |$$$$$$$/     $$$$/  
                                                                /  \__$$ |$$ |                
                                                                $$    $$/ $$ |                
                                                                 $$$$$$/  $$/                 
Developed by DunkinPirate''')
        print('-' * 80)
        time.sleep(3)
    def FirstCheck(self):
        print('[+]Performing system check...')
        time.sleep(2)
        if Boot.firstSetup == True:
            print('[+]OnionCrypt has detected that this is your first time running the program.')
            print('[+Performing first time setup...')
            print('-' * 80)
            Login().SetInfo()
        else:
            Login().Login()
def main():
    Boot().Banner()
    Boot().FirstCheck()
    mainFuncs.Terminal()

if __name__ == "__main__":
    main()