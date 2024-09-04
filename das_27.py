import os
# from datetime import datetime as dt, timedelta
#
# es_pahin = dt.now()
#
# erreq_tari_heto = es_pahin + timedelta(days=1070)
# print(erreq_tari_heto)
# jam_plus_12 = es_pahin + timedelta(days=7*365)
# print(jam_plus_12)

# def loop_recurs(count):
#     print(count)
#     loop_recurs(count+1)
# loop_recurs(count=0)

# def recursiv_makedir():
#     file_name = f"./backup/{dt.now().strftime('%m-%Y')}"
#     print(file_name)
#     os.mkdir(file_name)
#
#
# recursiv_makedir()

for i in range(1, 4):
    for x in range(0, i):
        print(i, end=' ')

