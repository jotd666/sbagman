import os,re

f = """screen_base_logical_address_6326
unknown_609F
unknown_60A1
unknown_60D3
unknown_61B6
unknown_61E1
unknown_61F7
unknown_6293
unknown_6294
unknown_6295
unknown_6297
unknown_6298
unknown_6299
unknown_629B
unknown_629C
unknown_629D
unknown_629F
unknown_62A3
unknown_62A4
unknown_62A5
unknown_62A7
unknown_62AC
unknown_62AF
unknown_62B0
unknown_62B2
unknown_62B5
unknown_62B6
unknown_62B9
unknown_62BA
unknown_62BC
unknown_62BD
unknown_62C1
unknown_62C4
unknown_62CB
unknown_62D2
unknown_62D3
unknown_62D6
unknown_62DA
unknown_62DF
unknown_62E0
unknown_62E1
unknown_62E3
unknown_62E5
unknown_62E9
unknown_62EA
unknown_62ED
unknown_62EE
unknown_62F0
unknown_62F5
unknown_62F6
unknown_62F7
unknown_62F9
unknown_62FA
unknown_62FB
unknown_62FC
unknown_6304
unknown_630E
unknown_6310
unknown_6311
unknown_6312
unknown_6314
unknown_6315
unknown_6317
unknown_631A
unknown_631D
unknown_6320
unknown_6323
unknown_6324
unknown_6327
unknown_632A
unknown_632F
unknown_6332
unknown_6334
unknown_6336
unknown_6337
unknown_6338
unknown_633A
unknown_6340
unknown_6341
unknown_6342
unknown_6343
unknown_6345
unknown_6346
unknown_6348
unknown_634A
unknown_634C
unknown_634D
unknown_6351
unknown_6352
unknown_6353
unknown_6356
unknown_6358
unknown_635B
unknown_635D
unknown_6360
unknown_6586
unknown_658D
unknown_658E
unknown_658F
unknown_6595
unknown_699A
unknown_pointer_62F6
unknown_pointer_633D
unknown_rom_address_62F1
unknown_screen_address_62F8
""".splitlines()

rams = [x.strip() for x in f if "_6" in x]

varlist = {int(x.rsplit("_")[-1],16):x  for x in rams}

print(varlist)

prev_offset = 0

with open("out.68k","w") as f:
    lst = []
    variables = []
    next_align = False
    for k,v in sorted(varlist.items()):
        if prev_offset:
            sz = str(k-prev_offset)

            lst.append(f"\tds.b\t{sz}\n")
        if v.startswith("$"):
            v = f"unknown_{v[1:].upper()}"

        variables.append(v)



        lst.append(f"{v}:\n")


        prev_offset = k

    lst.append(f"\tds.b\t{k-prev_offset}\n")
    for k in sorted(variables):
        f.write(f"\t.global\t{k}\n")
    f.write("\n")

    f.writelines(lst)