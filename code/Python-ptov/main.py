# -*- coding:utf-8 -*-
import os
from generate_img.generate_img import generate_bg_img
from generate_img.generate_img import generate_img
from generate_img.generate_img import get_text
from generate_img.generate_img import img_to_video
from generate_img.generate_img import video_to_img
from generate_img.generate_img import get_radio
from generate_img.generate_img import get_radio_2

if __name__ == '__main__':
    if os.path.exists('bg.png') == False:
        generate_bg_img()

    text_list_all = get_text()
    if len(text_list_all) > 0:
        radio = 1
        for text_list in text_list_all:
            i = 1
            get_radio(','.join(text_list), radio)
            for text in text_list:
                generate_img(text, i, 50)
                i += 1
            img_to_video(len(text_list), radio)
            radio += 1
