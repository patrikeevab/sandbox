fname = "Anton"
sname = "Patrikeev"


def print_name(f, s):
    return f + " " + s


print(f"{fname} {sname}")

print(f"{fname.upper()} {sname.lower()}")

print(f"{fname.startswith('A')} {sname.endswith('w')}")

print(f"{print_name(fname, sname)}")
