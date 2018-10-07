import os
import sys
import time
import random
import uuid
import pyAesCrypt
import socket
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from random import randint
import Cryption as cryption
import OnionCrypt as onionCrypt

userIP = socket.gethostbyname(socket.gethostname())

def Exit():
    sys.exit()

def Terminal():
    print('')
    print('[+]Welcome')
    print('[+]Your IP: {}'.format(userIP))
    print('''
////////////////////////////////////////////////
/                ***MAIN MENU***               /
/ 1. Tor Browser                               /
/ 2. Decrypt Login Data                        /
/ 3. Decrypt Browing Data                      /
/ 4. Exit                                      /
////////////////////////////////////////////////''')
    command = int(input('[+]Please enter a command.'))
    command = {
        1 : TorBrowser().GetRequest(),
        2 : cryption.DecryptLogin(),
        3 : cryption.DecryptBrowser(),
        4 : Exit()
    }
class TorBrowser:
    def GetRequest(self):
        pass
