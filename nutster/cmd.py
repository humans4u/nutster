#!/usr/bin/env python3
from nutster import node
from nutster.utils import cmd, naming
from nutster.models import Neighbour
from nutster.pipeline import Pipeline, Process, PipelineExecutionError
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="nutster",
    description="Network and Job cluster management."
)

parser.add_argument(
    '-q', '--quiet',
    help='Surpress the output',
    action='store_true'
)

parser.add_argument(
    '-d', '--debug',
    help="Debug output",
    action='store_true'
)

parser.add_argument(
    '-i', '--interface',
    help='Network interface, if specified, it cannot go with the -n(--ip) flag as it uses the interface to get the main IP address.' 
)

parser.add_argument(
    '-n', '--ip',
    help='IP address to be assigned, if specified, it cannot go with the -i(--interface) flag as it uses the interface to get the main IP address.' 
)

parser.add_argument(
    '-p', '--port',
    help='Port to be specified, and binded to the RX pipeline',
    default=8080
)

parser.add_argument(
    '-m', '--me',
    help='Name of the node',
    default='node-'+naming.server_name()
)

args = parser.parse_args()
cmd.QUIET = args.quiet
cmd.info("Welcome to ncluster")
if args.debug:
    cmd.DEBUG = True
    cmd.warn("Debug output is enabled") 

if args.interface and args.ip:
    cmd.fatal('Do not use the -i or -n flag together.')
    sys.exit(-1)
elif not args.interface and not args.ip:
    cmd.fatal('Please specify the IP or the interface.')
    sys.exit(-1)

SNAME=args.me

IP = ""
# get the IP
if args.interface:
    try:
        import netifaces as ni
        IP = ni.ifaddresses(args.interface)[ni.AF_INET][0]['addr']
    except Exception as e:
        if type(e) == ValueError:
            cmd.fatal("Please specify a good interface.")
        else:
            cmd.fatal("Something went wrong.")
        sys.exit(-1)
else:
    IP = args.ip

PORT = args.port
cmd.debug("Trying to run server @", IP, PORT, f'w/ name {SNAME}')

# NOW we should start the servers
node.ip = IP
node.port = PORT
node.sname = SNAME

sys.exit(0)
