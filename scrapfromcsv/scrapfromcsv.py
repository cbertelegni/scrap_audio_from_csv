#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, urllib2
from time import sleep

class Scrapfromcsv:
    def __init__(self, csv_file, column_src, output_dir, referer_url= None):

        self.csv_file = csv_file
        self.column_src = column_src
        self.output_dir = output_dir
        self.referer_url = referer_url


    def scrap(self):

        # print self.OUTPUT_DIR
        """ check if OUTPUT_DIR exists"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        """ load source audios """
        csv_file = csv.reader(open(self.csv_file, "rb"))

        for row in csv_file:
            src =  row[self.column_src]
            file_name = src.split('/')[-1]

            if file_name:
                f_path = os.path.join(self.output_dir, file_name)

                if not os.path.exists(f_path):
                    self.save_file(src, file_name, f_path)
                else:
                    print "%s --> Exists!" % f_path
    

    def save_file(self, src, file_name, f_path):

        req = urllib2.Request(src)
        try:
            req = urllib2.Request(src)
            req.add_header('User-agent', 'Mozilla/5.0')

            """ set referer for scrap """
            if self.referer_url:
                req.add_header('Referer', self.referer_url)
            r = urllib2.urlopen(req)

            with open(f_path,'wb') as output:
                output.write(r.read())
                print "saved %s \n" % file_name
                
                sleep(1)
              

        except Exception, e:
            print "%s --> Error: %s" % (f_path, e)
