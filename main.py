#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, urllib2

BASE  = os.path.dirname(__file__)

# audio_csv = "input_src.csv"
# column_src = 1 # column src audio on csv
audio_csv = "src.csv"
column_src = 0 # column src audio on csv


INPUT_SRC = os.path.join(BASE, audio_csv);
OUTPUT_DIR = os.path.join(BASE, "output");



""" Scrap audios """
if __name__ == "__main__":

    """ check if OUTPUT_DIR exists"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    """ load source audios """
    csv_file = csv.reader(open(INPUT_SRC, "rb"))

    for row in csv_file:
        src =  row[column_src]
        file_name = src.split('/')[-1]

        if file_name:
            f_path = os.path.join(OUTPUT_DIR, file_name)

            if not os.path.exists(f_path):
                req = urllib2.Request(src)
                try:
                    req = urllib2.Request(src)

                    """ uncomment you need set the referer"""
                    # req.add_header('Referer', 'http://www.example.com/')
                    # req.add_header('User-agent', 'Mozilla/5.0')
                    r = urllib2.urlopen(req)

                    with open(f_path,'wb') as output:
                      output.write(r.read())

                except:
                    print "%s --> Error!" % f_path
            else:
                print "%s --> Exists!" % f_path
                
