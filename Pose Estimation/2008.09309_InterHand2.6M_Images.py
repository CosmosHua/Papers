#!/usr/bin/python3
# coding: utf-8

import os

##########################################################################################
def download_InterHand(fps=5):
    assert fps in (5,30), 'fps should be 5 or 30'
    url = 'https://fb-baas-f32eacb9-8abb-11eb-b2b8-4857dd089e15.s3.amazonaws.com'
    url += f'/InterHand2.6M/InterHand2.6M.images.{fps}.fps.v1.0/'

    for a in list('ab' if fps==5 else 'abcdefgh'):
        for b in list('abcdefghijklmnopqrstuvwxyz'):
            if fps==30 and a=='h' and b=='q': break
            elif fps==5 and a=='b' and b=='s': break
            os.system(f'wget {url}InterHand2.6M.images.{fps}.fps.v1.0.tar.part{a}{b}')
    os.system(f'wget {url}InterHand2.6M.images.{fps}.fps.v1.0.tar.CHECKSUM')
    os.system(f'wget {url}verify_download.py')
    os.system(f'wget {url}unzip.sh')


##########################################################################################
if __name__ == '__main__':
    download_InterHand(5)

