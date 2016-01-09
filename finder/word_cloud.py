__author__ = 'lipidong'


#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

def create_cloud(word, img, out_path):

    # Read the whole text.
    # text = open(word_path).read()
    text = word.read().decode('utf-8')
    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    alice_mask = np.array(Image.open(img))
    # alice_mask = np.array(img_path)
    wc = WordCloud(font_path = '华文黑体.ttf' ,background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=STOPWORDS.add("said"), width=1000, height=2300, ranks_only=True, mode='RGBA')
    # generate word cloud
    wc.generate(text)
    # wc.generate_from_frequencies([()])
    # store to file
    wc.to_file(out_path)


# create_cloud('/Volumes/lpdbxy/learn/python/PycharmProjects/wordcloud/alice_license.txt', '/Volumes/lpdbxy/learn/python/PycharmProjects/wordcloud/alice_color.png',
#              '/Volumes/lpdbxy/learn/python/PycharmProjects/wordcloud/out.png')
