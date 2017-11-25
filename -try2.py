import json
import pandas as pd
from glob import glob
     
def convert(x):
    data = json.loads(x)
    for k, v in data.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                data['%s_%s' % (k, kk)] = vv
                del data[k]
                return data

for json_filename in glob('data.lint.json'):
    csv_filename = '%s.csv' % json_filename[:-5]
    print ('Converting %s to %s' % (json_filename, csv_filename))
    df = pd.DataFrame([convert(line) for line in file(json_filename)])
    df.to_csv(csv_filename, encoding='utf-8', index=False)