import sys
for line in sys.stdin:
    line = line.strip()
    splits= line.split(",")
    if(len(splits)==2):
        citing_number = splits[0]
        count = splits[1]
        print('%s\t%s' %(citing_number,count))
    else:
        patent = splits[0]
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %(splits[0],splits[1],splits[2],splits[3],splits[4],splits[5],splits[6],splits[7],splits[8],splits[9],splits[10],splits[11],splits[12],splits[13],splits[14],splits[15],splits[16],splits[17],splits[18],splits[19],splits[20],splits[21],splits[22]))

