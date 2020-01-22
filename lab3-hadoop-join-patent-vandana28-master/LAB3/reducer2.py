#!/usr/bin/env python
import sys
c= dict()
p = dict()
k = dict()
l = dict()
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    if(len(splits)==3):
        citing = splits[0]
        cited = splits[1]
        cited_state = splits[2]
        # c[citing] = cited_state

        c[splits[0]+"-"+splits[1]]= splits[2]

    else:
        patent = splits[0]
        patent_state= splits[1]
        p[patent]=patent_state


for citing,value in c.items():
    s = citing.split("-")
    citing = s[0]
    cited = s[1]
    if citing in p:
        k[citing+"-"+value+"-"+cited] =p[citing]
          

for citing,citing_state in k.items():
    t = citing.split("-")
    citing = t[0]
    cited_state=t[1]
    cited = t[2]
    if citing in l:
        if (citing_state == cited_state):
            l[citing] = l[citing] + 1
        else: 
            if (l[citing]):
                l[citing] = l[citing]
            else:
                l[citing] = 0

    else:
        if (citing_state == cited_state):
            l[citing] = 1

        else:
            l[citing] = 0

for k,v in l.items():
    print('%s,%s' % (k,v))

