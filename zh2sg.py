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
    5. 她 大概 知道
    6. 那只 狗 追 一只 猫
    7. 他 给 了 她
    8. 他 给 了 她 一只 猫
    9. 他 没 有 猫
    10. 追 猫
    11. 他 会 唱歌 吗
    12. 我 和 她 和 他 追 一只 猫
    13. 他 可以 吃 玻璃
    14. 他们 欺负 她
    15. 这只 在 睡觉
    16. 每只 在 吃 东西
    17. 她 觉得 他 不 会 唱歌
    18. 那只 猫 很 可爱
    19. 他 即将要 睡觉
    20. 那只 猫 欺负 一只 大 蚂蚁

    (Singlish)
    1. He does eat the cat.
    2. Happy dogs are singing.
    3. White ant want a big dog.
    4. The cat and the tree chase me.
    5. He can tekan me already.
    6. I never eat the cat.
    7. There got a cat and a dog.
    8. Ants are big and dogs are cute.
    9. I already got everything.
    10. Is that cute.
    11. The tree think he agak can sing.
    12. The glass does hurt the tree.
    13. Those ants think that she will sleep.
    14. A cat kacau the dog.
    15. Everything is big.
    16. Every cat gives me a dog.
    17. I am kacauing the cat.
    18. I want to give you a tree.
    19. She ask me if he sleeps.
    20. is it he give you this.
"""

import sys

pred_map = {
    '"exist_q_rel"': 'exist_q_super_rel',
    "_dog_n_rel": "_dog_n_1_rel",
    "_cat_n_rel": "_cat_n_1_rel",
    "_glass_n_rel": "_glass_n_1_rel",
    "_thing_n_rel": "_thing_n_1_rel",
    "_tree_n_rel": "_tree_n_1_rel",
    "_ant_n_rel": "_ant_n_1_rel",
    "_he_n_rel": "_he_n_1_rel",
    "_she_n_rel": "_she_n_1_rel",
    "_it_n_rel": "_it_n_1_rel",
    "_I_n_rel": "_I_n_1_rel",
    "_you_n_rel": "_you_n_1_rel",
    "_they_n_rel": "_they_n_1_rel",
    "_we_n_rel": "_we_n_1_rel",
    "_person_n_rel": "_person_n_1_rel",
    # "_Xiaoming_n_rel": "",
    # "_there_n_rel": "_there_n_rel",
    # "_cute_a_rel": "_cute_a_rel",
    # "_happy_a_rel": "_happy_a_rel",
    # "_white_a_rel": "_white_a_rel",
    # "_big_a_rel": "_big_a_rel",
    # "_have_v_rel": "_have_v_rel",
    # "_want_v_rel": "_want_v_rel",
    "_know_v_rel": "_know_v_2_rel",
    # "_eat_v_rel": "_eat_v_rel",
    # "_hurt_v_rel": "_hurt_v_rel",
    # "_bully_v_rel": "_bully_v_rel",
    # "_disturb_v_rel": "_disturb_v_rel",
    # "_sing_v_rel": "_sing_v_rel",
    # "_sleep_v_rel": "_sleep_v_rel",
    # "_chase_v_rel": "_chase_v_rel",
    # "_give_v_rel": "_give_v_rel",
    "_think_v_rel": "_think_v_2_rel",
    # "_ask_v_rel": "_ask_v_rel",
    "_can_v_1_rel": "_can_v_rel",
    "_can_v_2_rel": "_can_v_rel",
    "_roughly_v_rel": "_roughly_a_rel",
    "_already_v_rel": "_already_a_rel",
    # "_will_v_rel": "_will_v_rel",
    "neg1_rel": "neg1_rel",
    "_neg2_rel": "neg2_rel",
    # "_that_q_rel": "_that_q_rel",
    "_animal_n_rel": "_animal_n_1_rel",
    # "_a_q_rel": "_a_q_rel",
    # "_this_q_rel": "_this_q_rel",
    # "_these_q_rel": "_these_q_rel",
    # "_those_q_rel": "_those_q_rel",
    # "_every_q_rel": "_every_q_rel",
    # "_and_coord_rel": "_and_coord_rel",
}

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        for k, v in pred_map.items():
            lines[i] = lines[i].replace(k, v)

    return lines

def main():
    lines = read_in()
    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
