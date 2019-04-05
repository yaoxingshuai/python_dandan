li = [
    (16, 'caodan', 18),
    (10, 'yaoxing1', 18),
    (13, 'caodan2', 20),
]
li.sort(key=lambda item: (item[2], len(item[1])), reverse=False)
print(li)

import ipdb
ipdb.set_trace()

#
# import numpy as np
# import pandas as pd
# r
# li1=np.array(li)
# li2=pd.DataFrame(li1)
# print(li2)
#
# # li2.sort_index(axis=1,by='2')
#
# import ipdb
# ipdb.set_trace()
#
