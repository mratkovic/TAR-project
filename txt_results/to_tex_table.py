import sys
import re
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    nums = re.split(' +', line)
    print r'$ %s $ \\' % ' $ & $ '.join(nums)

