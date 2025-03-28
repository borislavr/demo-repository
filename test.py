#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import yaml

with open('./.github/.child-modules.yaml', 'r') as f:
    data = yaml.safe_load(f)
for module in data['child_modules']:
    search_str = module['module_string'].replace('${version}', '.*$')
    ver_str = module['module_string'].replace('${version}', module['version'])
    print(f"{search_str} -> {ver_str}")
    os.system(f"sed -i 's|{search_str}|{ver_str}|' {data['config_file']}")
