# script which checks word/long writes in source and checks if the data has an ".align"
# directive before it to make it 68000 compliant
import os,re

import config

def split_args(param_string):
    paren = 0
    rval = []
    current_param = []
    for c in param_string:
        if c=="(":
            paren += 1
        elif c==")":
            paren -= 1

        if c == "," and paren==0:
            rval.append("".join(current_param))
            current_param.clear()
        else:
            current_param.append(c)

    if current_param:
        rval.append("".join(current_param))

    return rval

to_check = set()

with open(config.asm_68k_file) as f:
    for line in f:
        m = re.search("\s+\w+\.[wl]\s*([^\s|]*)",line)
        if m:
            params = m.group(1)
            args = split_args(params)
            for oa in args:
                a = oa.lower()
                if a == "sp" or a == "sr" or (len(a)==2 and a[0] in 'ad' and a[1].isdigit):
                    continue
                if any(not (c.isalnum() or c=='_') for c in a):
                    continue
                # not a register: check alignment
                to_check.add(oa)

with open(config.asm_68k_ram_file) as f:
    previous_line = None
    for line in f:
        if line.endswith(":\n"):
            line = line.rstrip(":\n")
            if line in to_check and ".align" not in previous_line:
                print(line)
        previous_line = line