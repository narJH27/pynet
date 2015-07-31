#!/usr/bin/env python

import yaml
import json
import pprint


with open('output_files/file_yaml.txt') as f1:
    pprint.pprint(yaml.load(f1))

with open('output_files/file_json.txt') as f2:
    pprint.pprint(json.load(f2))
