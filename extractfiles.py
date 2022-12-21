# pylint: disable=too-many-instance-attributes,invalid-name,unspecified-encoding, unused-wildcard-import
# pylint: disable=too-few-public-methods,attribute-defined-outside-init
"""Extracts files matching the regular expression"""

import os
import zipfile
import sys
import re

fn = sys.argv[1]
regex = sys.argv[2]

with zipfile.ZipFile(fn) as zfile:
    total = 0
    name_list = zfile.namelist()
    for i in name_list:
        fname = i.split('/')[-1]
        try:
            file = re.search(regex, fname).group()
            zfile.extract(i, os.path.abspath('part3'))
            total += 1
        except AttributeError:
            pass

print(f'{total} files extracted')
