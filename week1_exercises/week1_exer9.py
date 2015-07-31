#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse as ccp

cfg_obj = ccp('data/cisco_ipsec.txt')
pfs = cfg_obj.find_objects_w_child(parentspec='^crypto map CRYPTO',
                                   childspec='pfs group2')
print pfs
