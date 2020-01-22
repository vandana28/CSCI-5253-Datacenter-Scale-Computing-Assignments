import sys
citing = dict()
patent= dict()
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    if(len(splits) == 2):
        citing_number = splits[0]
        count = splits[1]
        citing[citing_number] = count
        
    else:
        patent_number = splits[0]
        patent[patent_number] = splits[1:22]

for k,v in citing.items():
        if k in patent:
             patent[k].append(v)

for k,v in patent.items():
    print(k,v)
