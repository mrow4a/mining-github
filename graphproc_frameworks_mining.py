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
    print ('Please supply with Github username and password, and optionaly --cleanrun flag to reset result for framework')
    print ('./graphproc_frameworks_mining.py -u <username> -d <password> [all/gelly/graphx/giraph/tinkerpop/tinkerpop-filter/arabesque/graphlab]')
    print ('./graphproc_frameworks_mining.py -u foo -d foopass gelly')
    print ('./graphproc_frameworks_mining.py gelly')
    print ('./graphproc_frameworks_mining.py --cleanrun gelly')

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "u:p:c", ["user", "password", "cleanrun"])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    if (len(args)) < 1:
        print_help()
        sys.exit(2)
    framework = args[0]

    username = None
    password = None
    clean = False
    for opt, arg in opts:
        if opt in ("-u", "--user"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-c", "--cleanrun"):
            clean = True

    if (username is None or password is None):
        username = raw_input("Username: ")
        password = getpass.getpass("Password for " + username + ": ")

    # Set username, password and output directory
    outputdir = os.path.dirname(os.path.realpath(__file__))
    miner = lib.mining.Miner(username, password, outputdir)

    # Start searching for keyword

    if framework == "gelly" or framework == "all":
        if clean:
            miner.clear_results("gelly")

        miner.get_repos_for_keyword(
            "import org.apache.flink.graph",
            [miner.JAVA, miner.SCALA],
            ["apache/flink"],
            "gelly"
        )
    if framework == "graphx" or framework == "all":
        if clean:
            miner.clear_results("graphx")

        miner.get_repos_for_keyword(
            "import org.apache.spark.graphx",
            [miner.JAVA, miner.SCALA],
            ["apache/spark"],
            "graphx"
        )
        miner.get_repos_for_keyword(
            "import org.apache.spark.graphx.GraphLoader",
            [miner.SCALA],
            ["apache/spark"],
            "graphx"
        )
    if framework == "giraph" or framework == "all":
        if clean:
            miner.clear_results("giraph")

        miner.get_repos_for_keyword(
            "import org.apache.giraph.graph",
            [miner.JAVA, miner.SCALA],
            ["apache/giraph"],
            "giraph"
        )
    if framework == "tinkerpop" or framework == "all":
        if clean:
            miner.clear_results("tinkerpop")

        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop"],
            "tinkerpop"
        )
        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.structure.io.graphml",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop"],
            "tinkerpop"
        )
        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.structure.Graph",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop"],
            "tinkerpop"
        )
    if framework == "tinkerpop-filter" or framework == "all":
        if clean:
            miner.clear_results("tinkerpop-filter")

        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop", "clojurewerkz/ogre", "mpollmeier/gremlin-scala", "blazegraph/tinkerpop3", "Azure/azure-cosmosdb-spark", "MartinHaeusler/chronos", "datastax/java-dse-graph", "graknlabs/grakn", "apache/incubator-s2graph", "rayokota/hgraphdb", "awslabs/dynamodb-janusgraph-storage-backend", "graknlabs/janusgraph", "classmethod/tupl-titan-storage-backend", "thinkaurelius/titan", "unipop-graph/unipop", "pietermartin/sqlg", "orientechnologies/orientdb-gremlin", "HuygensING/timbuctoo", "rmagen/elastic-gremlin", "JanusGraph/janusgraph"],
            "tinkerpop-filter"
        )
        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.structure.io.graphml",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop", "clojurewerkz/ogre", "mpollmeier/gremlin-scala", "blazegraph/tinkerpop3", "Azure/azure-cosmosdb-spark", "MartinHaeusler/chronos", "datastax/java-dse-graph", "graknlabs/grakn", "apache/incubator-s2graph", "rayokota/hgraphdb", "awslabs/dynamodb-janusgraph-storage-backend", "graknlabs/janusgraph", "classmethod/tupl-titan-storage-backend", "thinkaurelius/titan", "unipop-graph/unipop", "pietermartin/sqlg", "orientechnologies/orientdb-gremlin", "HuygensING/timbuctoo", "rmagen/elastic-gremlin", "JanusGraph/janusgraph"],
            "tinkerpop-filter"
        )
        miner.get_repos_for_keyword(
            "import org.apache.tinkerpop.gremlin.structure.Graph",
            [miner.JAVA, miner.SCALA],
            ["apache/tinkerpop", "clojurewerkz/ogre", "mpollmeier/gremlin-scala", "blazegraph/tinkerpop3", "Azure/azure-cosmosdb-spark", "MartinHaeusler/chronos", "datastax/java-dse-graph", "graknlabs/grakn", "apache/incubator-s2graph", "rayokota/hgraphdb", "awslabs/dynamodb-janusgraph-storage-backend", "graknlabs/janusgraph", "classmethod/tupl-titan-storage-backend", "thinkaurelius/titan", "unipop-graph/unipop", "pietermartin/sqlg", "orientechnologies/orientdb-gremlin", "HuygensING/timbuctoo", "rmagen/elastic-gremlin", "JanusGraph/janusgraph"],
            "tinkerpop-filter"
        )
    if framework == "arabesque" or framework == "all":
        if clean:
            miner.clear_results("arabesque")

        miner.get_repos_for_keyword(
            "import io.arabesque",
            [miner.JAVA, miner.SCALA],
            ["qcri/Arabesque"],
            "arabesque"
        )
    if framework == "goffish" or framework == "all":
        if clean:
            miner.clear_results("goffish")

        miner.get_repos_for_keyword(
            "import in.dream_lab.goffish",
            [miner.JAVA],
            ["dream-lab/goffish_v3"],
            "goffish"
        )
    if framework == "graphlab" or framework == "all":
        if clean:
            miner.clear_results("graphlab")

        miner.get_repos_for_keyword(
            "import graphlab.graph",
            [miner.JAVA, miner.SCALA],
            ["jegonzal/PowerGraph", "turi-code/SFrame", "turi-code/GraphLab-Create-SDK"],
            "graphlab"
        )
        miner.get_repos_for_keyword(
            "from graphlab import SGraph",
            [miner.PYTHON],
            ["jegonzal/PowerGraph", "turi-code/SFrame", "turi-code/GraphLab-Create-SDK"],
            "graphlab"
        )
        miner.get_repos_for_keyword(
            "graphlab.SGraph",
            [miner.PYTHON],
            ["jegonzal/PowerGraph", "turi-code/SFrame", "turi-code/GraphLab-Create-SDK"],
            "graphlab"
        )
        miner.get_repos_for_keyword(
            "<graphlab.hpp>",
            [miner.CPLUS],
            ["jegonzal/PowerGraph", "turi-code/SFrame", "turi-code/GraphLab-Create-SDK"],
            "graphlab"
        )

if __name__ == '__main__':
    main(sys.argv[1:])
