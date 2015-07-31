#!/usr/bin/env python

import yaml
import json


my_list = [1, 2, 3, 4, {'abc': 5, 'xyz': 6}, 7, 8]

with open('output_files/file_yaml.txt', 'a+') as f1:
    f1.write(yaml.dump(my_list, default_flow_style=False))
    
with open('output_files/file_json.txt', 'a+') as f2:
    json.dump(my_list, f2)
