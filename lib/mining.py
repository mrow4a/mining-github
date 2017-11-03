#!/usr/bin/env python

from github import Github
import os, json
import time

class Miner:

    JAVA = "java"
    SCALA = "scala"
    PYTHON = "python"

    repos = set()

    def __init__(self, user, password):
        self.logfile = os.path.dirname(os.path.realpath(__file__)) + "/results.log"
        self.auth = Github(user, password)

    def get_results(self, paged_results):
        file = open(self.logfile, 'w')
        for i in range(0,paged_results.totalCount):
            page = paged_results.get_page(i)
            for res in page:
                if not res.repository.id in repos:
                    json_line = json.dumps({"name": res.repository.full_name, "id": res.repository.id})
                    repos.add(res.repository.id)
                    print json_line
                    file.write(json_line + '\n')
            #print pages
            time.sleep(2)
        file.close()

        print "WROTE URLS TO %s"%(self.logfile)

    def get_repos_for_keyword(self, keyword, language):
        if (language not in [self.JAVA, self.SCALA, self.PYTHON]):
            print("WRONG LANGUAGE - Please use Miner.JAVA | Miner.SCALA | Miner.PYTHON")
            return
        print('Mining ' + keyword + '...')
        print

        paged_results = self.auth.search_code(keyword)
        self.get_results(paged_results)