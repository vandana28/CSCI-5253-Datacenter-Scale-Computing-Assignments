import sys
import string

last_cited = None
cur_location = "-"
citing_id_list = []

for line in sys.stdin:
    cited, citing, location = [x.strip() for x in line.split('\t')]
    if not last_cited or last_cited == cited:
        last_cited = cited
        if location and location != "-":
            cur_location = location
        else:
            citing_id_list.append(citing)
        # print ('%s\t%s\t%s' % (cited,cited,location))
    elif cited != last_cited:
        for citing1 in citing_id_list:
            print ('%s,%s,%s' % (last_cited,citing1,cur_location))
        last_cited = cited
        cur_location = "-"
        citing_id_list = []
        if location and location != "-":
            cur_location = location
        else:
            citing_id_list.append(citing)

for citing1 in citing_id_list:
            print ('%s,%s,%s' % (last_cited,citing1,location))