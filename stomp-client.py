import time
import sys
import argparse
import logging

import stomp
import json
import os


def set_args():
    parser.add_argument('--broker', type=str, help='Broker IP with port.')
    parser.add_argument('--conn-username', type=str, help='Set username for connection.')
    parser.add_argument('--conn-password', type=str, help='Set password for connection.')
    parser.add_argument('--address', type=str, help='Set dest address for messages.')
    parser.add_argument('--timeout', type=int, help='Set timeout for subscriber.')
    parser.add_argument('--count', type=int, help='Count of messages which are going to be send.')
    parser.add_argument('--msg-content', type=str, help='Message content.')
    parser.add_argument('--dest-type', type=str, help='Destination type (ANYCAST / MULTICAST).')
    parser.add_argument('action', metavar='N', type=str)


sys.tracebacklimit = 0
parser = argparse.ArgumentParser(description='Process stomp connection arguments.')
set_args()
args = parser.parse_args()
host_and_port = args.broker.split(":")
hosts = [(host_and_port[0], int(host_and_port[1]))]
conn = stomp.Connection(hosts)


class MyListener(stomp.ConnectionListener):
    receive = {}

    def __init__(self, rec, prefetch=None):
        self.receive = rec

    def on_error(self, headers, message):
        logging.error('Received an error "%s"' % message)
        os._exit(1)

    def on_message(self, headers, message):
        print('%s' % json.dumps({'message': message}))
        a = self.receive['recv']
        self.receive['recv'] = a + 1


def connect():
    conn.set_listener('', MyListener(received))
    conn.set_ssl(hosts)
    conn.start()
    conn.connect(args.conn_username, args.conn_password, wait=True, headers={'client-id': 'test'})


def wait_until_message_received(timeout, period=0.25):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if received["recv"] == args.count:
            return True
        time.sleep(period)
    return False


def send():
    logging.info('Ready to send ' + str(args.count) + ' messages')
    for x in range(args.count):
        conn.send(body=args.msg_content, destination=args.address, headers={'destination-type': args.dest_type})
        print(json.dumps({'Message': args.msg_content}))
        time.sleep(1)
    conn.disconnect()


def recv():
    logging.info('Ready to receive ' + str(args.count) + ' messages')
    conn.subscribe(destination=args.address, id=1, ack='auto',
                   headers={'subscription-type': args.dest_type})
    if wait_until_message_received(args.timeout):
        logging.info('Received all ' + str(received["recv"]) + ' messages')
    else:
        logging.error("Haven't received all messages. Received: " + str(received["recv"]))
    conn.disconnect()


def main():
    connect()
    if args.action == 'sender':
        send()
    else:
        recv()


if __name__ == "__main__":
    received = {"recv": 0}
    main()



