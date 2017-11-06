#!/usr/bin/env python
# -*- python -*-
#
# The mining-github Project.

import getopt
import sys
import lib.mining
import getpass
import os

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

    # Set username, password and output directory
    outputdir = os.path.dirname(os.path.realpath(__file__))
    miner = lib.mining.Miner(username, password, outputdir)

    # Start searching for keyword

    miner.clear_results("gelly")
    miner.get_repos_for_keyword(
        "import org.apache.flink.graph",
        [miner.JAVA, miner.SCALA],
        "gelly"
    )

    miner.clear_results("graphx")
    miner.get_repos_for_keyword(
        "import org.apache.spark.graphx",
        [miner.JAVA, miner.SCALA],
        "graphx"
    )

    miner.clear_results("giraph")
    miner.get_repos_for_keyword(
        "import org.apache.giraph",
        [miner.JAVA, miner.SCALA],
        "giraph"
    )


if __name__ == '__main__':
    main(sys.argv[1:])
