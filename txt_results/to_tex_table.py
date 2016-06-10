path = './in.tmp'
with open(path, 'r') as in_file:
    for line in in_file:
        nums = line.strip().split(' ')
        print '$ %s $ \\' % ' $ & $ '.join(nums)

