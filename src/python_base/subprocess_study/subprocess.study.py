# -*- coding=utf-8 -*-

import logging
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)d %(levelname)s - fun:%(funcName)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

log = logging.getLogger(__name__)

NATIVE_HADOOP = 'native-hadoop'


def run_shell(cmd, print_cmd=False):
    if print_cmd:
        log.info("=== " + cmd)
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = popen.communicate()
    if stderr and NATIVE_HADOOP not in stderr:
        log.error(stderr)
    return popen.returncode, stdout




if __name__ == "__main__":
    cmd = "ls"
    re, stdout = run_shell(cmd, True)
    print re
    print stdout
