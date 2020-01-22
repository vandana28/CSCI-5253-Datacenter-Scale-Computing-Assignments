import sys
import numpy as np
for line in sys.stdin:
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 3:
        citing = splits[1]
        cited = splits[0]
        state = splits[2]
        print('%s\t%s\t%s' %(citing,cited,state))


    else:
        patent = splits[0]
        patent_state = splits[5]
        print('%s\t%s' %(patent,patent_state))





