
li = [{"name": "dd", "sex": "girl"}, {"name": "dd", "sex": "girl"},
         {"name": "yy", "sex": "boy"}, {"name": "dan", "sex": ""}, {"name": "bob"}]


#sex=[lis['sex']for lis in li if 'sex' in lis]

from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as ply

frame=DataFrame(li)

sex_clear=frame['sex'].fillna('Missing')
sex_clear[sex_clear=='']='Unknown'
sex_counts=sex_clear.value_counts()

print(sex_counts)

sex_counts.plot(kind='barh',rot=0)
#ply.show()

results=Series([x.split()[0] for x in frame.name.dropna()])
res_counts=results.value_counts()
print(res_counts)

l=frame[frame.name.notnull()]
l_girl=np.where(l['name'].str.contains('dd'),'dd','not dd')
by_tz_os=l.groupby([sex_clear,l_girl])
agg_counts=by_tz_os.size().unstack().fillna(0)

print('--------------')
print(agg_counts)

indexer=agg_counts.sum(1).argsort()

print('--------------')
print(indexer)

import ipdb
ipdb.set_trace()





