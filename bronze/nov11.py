# contest timing
import datetime

start = datetime.datetime(2011,11,11,11,11,00)

test = "12 13 14"
arr = test.split(" ")

end = datetime.datetime(2011,11,int(arr[0]),int(arr[1]),int(arr[2]),00)

diff = end-start
print(diff.total_seconds()/60)

# problem 2
