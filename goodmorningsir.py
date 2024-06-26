import time
timestamp = int(time.strftime('%H'))
if timestamp>0 and timestamp<12:
    print('Good Morning, Sir')
elif timestamp>=12 and timestamp<5:
    print('Good Afternoon, Sir')
elif timestamp>=5 and timestamp<9:
    print('Good Evening, Sir')
else:
    print('Good Night, Sir')