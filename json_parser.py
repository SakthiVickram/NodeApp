import json
import sys
json_f = sys.argv[1]
with open(json_f) as json_data:
    data = json.load(json_data)
outf = open(sys.argv[2],"w")
outf.write(data['access_token'])
outf.write("\n")
outf.close()
