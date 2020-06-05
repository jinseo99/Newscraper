
import time
from retrying import retry
list_ = [1,2,3,4,5,6,7,8,9,10]


def wait(attempts, delay):
    print('Attempt #%d, retrying in %d seconds' % (attempts, delay // 1000))
    return delay

@retry(wait_func=wait)
def test(num):
    if 10 / (2-num) == 5:
        print('here')


for num in list_:
    print(num)
    test(num)

