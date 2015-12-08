import re
import json
f = open('counts')

l = f.readlines()

yy = set(range(0,920))
xx = []
for y in l:
# [x] Received '{"job_class":"FilCleanupJob","job_id":"22bceaa7-7052-4844-8675-f3550a7632c6","queue_name":"filippos","arguments":[1]}'
    #print y
    m = re.search('^.*({.*}).*', y)
    if m is None:
        continue
    z = m.group(1)
    z = json.loads(z)['arguments'][0]
    xx.append(z)
    if z in yy:
        yy.remove(z)
    else:
        print "WARNING: {} WAS NOT IN YY".format(z)

print yy


