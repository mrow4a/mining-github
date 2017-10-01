#!/usr/bin/env python

from github import Github
import os, json

class Miner:

    JAVA = "java"
    SCALA = "scala"
    PYTHON = "python"

    def __init__(self, user, password):
        self.logfile = os.path.dirname(os.path.realpath(__file__)) + "/results.log"
        self.auth = Github(user, password)

    def get_repos_for_keyword(self, keyword, language):
        if (language not in [self.JAVA, self.SCALA, self.PYTHON]):
            print("WRONG LANGUAGE - Please use Miner.JAVA | Miner.SCALA | Miner.PYTHON")
            return
        print('Mining ' + keyword + '...')
        print

        #For now, lets just write to file, later we can play with appending
        #f = open(self.logfile, 'a+')
        file = open(self.logfile, 'w')

        #Loop over all found repositories with the code
        counter = 0
        for repo in self.auth.search_code(keyword):
            if (counter > 100):
                break
            counter = counter + 1
            json_line = json.dumps({ "url" : repo.url })
            file.write(json_line + '\n')

        print "WROTE %s URLS TO %s"%(counter, self.logfile)
        file.close()
