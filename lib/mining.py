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
        to_visit = Queue()
        for res in paged_results:
            to_visit.put(res.repository.id)
        while not to_visit.empty():
            repo_id = to_visit.get()
            if not repo_id in repos:
                repos.add(repo_id)
                res = self.auth.get_repo(repo_id)
                fork_pages = res.get_forks()
                for fork in fork_pages:
                    to_visit.put(fork.id)
                json_line = json.dumps({"name": res.full_name, "id": res.id})
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