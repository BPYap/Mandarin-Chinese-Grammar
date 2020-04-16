#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
usage:
cat about.txt | python soinput.py
'''

"""
Test sentences:
    (Mandarin Chinese)
    1. 他 要 唱歌
    2. 他 不 会 唱歌 吗
    3. 我 和 他 追 一只 猫
    4. 她 要 一只 白 猫 
    5. 她 大概 会 知道

    (Singlish)
    1. He does eat the cat
    2. The happy cat sings
    3. I ask if he happy
    4. The cat and the dog chase me.
    5. He can eat already
"""

import sys

pred_map = {
    '_cat_n_rel': '_cat_n_1_rel',
    '_dog_n_rel': '_dog_n_1_rel',
    '"exist_q_rel"': 'exist_q_super_rel',
    '_he_n_rel': '_he_n_1_rel',
    # '_know_v_rel': '',
    '_roughly_v_rel': 'roughly_rel',
    '_can_v_1_rel': '_can_v_rel'
}

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        for k, v in pred_map.items():
            lines[i] = lines[i].replace(k, v)

    #print lines
    return lines

def main():
    lines = read_in()
    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
