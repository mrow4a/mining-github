#!/usr/bin/env python
# -*- python -*-
#
# The mining-github Project.

import getopt
import sys
import lib.mining
import getpass

def print_help():
    print ('Please supply with Github username and password')
    print ('./graphproc_frameworks_mining.py -u <username> -d <password>')

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "u:p:", ["user", "password"])
    except getopt.GetoptError:
        sys.exit(2)

    username = None
    password = None
    for opt, arg in opts:
        if opt in ("-u", "--user"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg

    if (username is None or password is None):
        username = raw_input("Username: ")
        password = getpass.getpass("Password for " + username + ": ")

    miner = lib.mining.Miner(username, password)
    miner.get_repos_for_keyword("import org.apache.flink.gelly", miner.JAVA)


if __name__ == '__main__':
    main(sys.argv[1:])
