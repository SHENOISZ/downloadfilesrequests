#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "SHENOISZ"

import requests

lista = []
prefix = 'https://storage.googleapis.com/files-download/files_backup/apks/'
to = '/home/ziggi/files/apks/'
#to = '/home/shenoisz/Documents/estudos/python/load-files/files/'


with open('apks_storage.txt', 'r') as f:
    lista = f.read().split(';')
    f.close()

def main():
    for l in lista:
        try:
            response = requests.get(l)
            name = str(l).replace(prefix, '')
            with open(to + name, 'wb') as f:
                f.write(response.content)
                f.close()
                print(name)
        except:
            pass    

if __name__ == '__main__':
    main()
        
