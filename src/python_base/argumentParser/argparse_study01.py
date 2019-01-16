# -*- coding=utf-8 -*-
from argparse import ArgumentParser

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)d %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

log = logging.getLogger(__name__)


def get_arguments():
    parser = ArgumentParser(description="Run test")
    parser.add_argument("--input_file_name", help="input file name", dest="input_file_name")
    parser.add_argument("--input_path", "-i", help="input path", dest="input_path")
    parser.add_argument("--output_path", "-o", help="output path", dest="output_path")

    parser.set_defaults(input_file_name="/Users/suyongjie/programs/pssh.py")
    parser.set_defaults(input_path="/Users/suyongjie/programs/pssh.py")
    parser.set_defaults(output_path="/Users/suyongjie/programs/pssh.py")
    try:
        args = parser.parse_args()
    except Exception, e:
        parser.print_help()
        exit(1)
    return args

def main(args):
    args.output_path = args.output_path.upper()

if __name__ == "__main__":
    log.info(sys.argv)
    args = get_arguments()
    main(args)
    print args
