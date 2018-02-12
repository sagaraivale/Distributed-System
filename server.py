import etcd
import random
import time

# Uses the default 'etcd' port on 'localhost'.
server = etcd.Client(host='127.0.0.1', port=2379, allow_redirect=True)

print 'Use ctrl+c to stop the program'

while True:
    try:
        pune_temp = random.randint(20, 40)
        bangalore_temp = random.randint(20, 40)
        server.write('/weather/pune', pune_temp)
        server.write('/weather/bangalore', bangalore_temp)
        time.sleep(3)

    except KeyboardInterrupt:
        print 'interrupt received, stopping'
        sys.exit(1)
