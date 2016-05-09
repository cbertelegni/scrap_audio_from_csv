#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, urllib2
from time import sleep
from scrapfromcsv.scrapfromcsv import Scrapfromcsv

BASE  = os.path.dirname(__file__)

# audio_csv = "input_src.csv"
# column_src = 1 # column src audio on csv
audio_csv = "src.csv"
column_src = 0 # column src audio on csv


INPUT_SRC = os.path.join(BASE, audio_csv);
OUTPUT_DIR = os.path.join(BASE, "output");

""" Scrap audios """
if __name__ == "__main__":

   scraper = Scrapfromcsv(INPUT_SRC, column_src, OUTPUT_DIR)

   scraper.scrap(referer_url = "http://example.com")