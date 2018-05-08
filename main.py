#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "SHENOISZ"

import requests, os

lista = []
prefix = 'https://storage.googleapis.com/files-download/files_backup/exes/'
to = '/home/ziggi/files/exes/'
#to = '/home/shenoisz/Documents/estudos/python/load-files/files/'

log = os.path.abspath(__file__)
log = str(log).replace(__file__, '') + 'exes.log'

with open('exes_storage.txt', 'r') as f:
    lista = f.read().split(';')
    f.close()

def main():

    count = 0
    errors = 0

    for l in lista:
        try:
            response = requests.get(l)
            name = l.replace(prefix, '')
            with open(to + name, 'wb') as f:
                f.write(response.content)
                f.close()
                #print(name)
                count += 1
                with open(log, 'a+') as a:
                    a.write('Count: ' + str(count) + ', ' + l + '\n')
                    a.close()   
        except Exception as e:
            #print(e)
            errors += 1

    with open(log, 'a+') as f:
        f.write('Total: ' + str(count + errors) + ', Count: ' + str(count) + ', Errors: ' + str(errors))
        f.close()           

if __name__ == '__main__':
    main()
        
