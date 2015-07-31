#!/usr/bin/env python

import re
from ciscoconfparse import CiscoConfParse as ccp

cfg_obj = ccp('data/cisco_ipsec.txt')
cmap = cfg_obj.find_objects_wo_child(parentspec='^crypto map',
                                     childspec='AES-')

trans_set_list = []

for cm in cmap:
    for item in cm.children:
        if 'transform' in item.text: 
            ts_name = re.search('set transform-set (.*)', item.text)
            trans_set_list.append(ts_name.group(1))

print trans_set_list
