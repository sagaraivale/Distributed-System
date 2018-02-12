import etcd
import sys


# Connect to the server's localhost and port address
client = etcd.Client(host='127.0.0.1', port=2379, allow_redirect=True)

print 'Use ctrl+c to stop the program'

while True:
    try:
        pune_temperature = client.watch('/weather/pune')
        bangalore_temperature = client.watch('/weather/bangalore')
        print 'The weather of Pune is {} celsius'.format(pune_temperature.value)
        print 'The weather of Bangalore is {} celsius'.format(bangalore_temperature.value)

    except KeyboardInterrupt:
        print 'interrupt received, stopping'
        sys.exit(1)
