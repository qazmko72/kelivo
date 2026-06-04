import re, sys

path = sys.argv[1]
with open(path) as f:
    c = f.read()
c = re.sub(r'(DEVELOPMENT_TEAM\s*=\s*)[^;]+;', r'\1;', c)
with open(path, 'w') as f:
    f.write(c)
print("DEVELOPMENT_TEAM cleared from", path)
