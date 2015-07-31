#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse as ccp


cfg_obj = ccp('data/cisco_ipsec.txt')

crypto = cfg_obj.find_objects(r'^crypto map CRYPTO')

for item in crypto:
    print item.text
