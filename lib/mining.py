#!/usr/bin/env python

from github import Github
import json
import time
import Queue
import os

class Miner:

    JAVA = "java"
    SCALA = "scala"
    PYTHON = "python"
    CPLUS = "c++"

    repos = set()

    def __init__(self, user, password, outputdir):
        self.logfiledir = outputdir
        self.auth = Github(user, password, per_page = 100)
        self.suffix = '.log'

    def __get_output_for_id(self, outid):
        return os.path.join(self.logfiledir, outid + self.suffix)

    def clear_results(self, outid):
        outputfile = self.__get_output_for_id(outid)
        open(outputfile, 'w').close()

    def get_contrib(self, res):
        contrib_pages = res.get_contributors()

        print "Fetch contributors for", res.full_name
        contribs = []
        for i in range(0, 10000):
            try:
                page = contrib_pages.get_page(i)
                if not page:
                    break
                for contrib in page:
                    contribs.append(contrib.login)
                time.sleep(0.1)
            except Exception as e:
                print e

        return contribs

    def get_forks(self, res):
        fork_pages = res.get_forks()

        print "Fetch forks for", res.full_name
        forks = []
        for i in range(0, 10000):
            try:
                page = fork_pages.get_page(i)
                if not page:
                    break
                for fork in page:
                    forks.append(fork)
                time.sleep(0.1)
            except Exception as e:
                print e

        return forks

    def __write_results(self, paged_results, outid):
        outputfile = self.__get_output_for_id(outid)
        file = open(outputfile, 'a')

        to_visit = Queue.Queue()
        for res in paged_results:
            to_visit.put(res.repository.id)
            print res.repository.id
            time.sleep(0.1)

        filtered_out = 0

        while not to_visit.empty():
            repo_id = to_visit.get()
            if not repo_id in self.repos:
                self.repos.add(repo_id)

                print "Fetch ", repo_id
                try:
                    res = self.auth.get_repo(repo_id)
                    forks = self.get_forks(res)
                    for fork in forks:
                        to_visit.put(fork.id)

                    contributors = self.get_contrib(res)

                    json_line = json.dumps({"name": res.full_name, "id": res.id,
                        "stargazers_count": res.stargazers_count,
                        "subscribers_count": res.subscribers_count,
                        "contributors": contributors,
                        "open_issues_count": res.open_issues_count})
                    print json_line
                    file.write(json_line + '\n')
                    time.sleep(0.73)
                except Exception as e:
                    print e
                    continue

            else:
                filtered_out += 1
        file.close()
        print("Filtered out " + str(filtered_out))

        print "WROTE URLS TO %s"%(outputfile)

    def get_repos_for_keyword(self, keyword, languages, id):
        # Validate languages are supported
        for language in languages:
            if (language not in [self.JAVA, self.SCALA, self.PYTHON, self.CPLUS]):
                print("LANGUAGE NOT SUPPORTED- Please use Miner.JAVA | Miner.SCALA | Miner.PYTHON | Miner.CPLUS")
                return

        # Escape keyword to make it unique search
        escaped_keyword = "\"" + keyword + "\""
        print('Mining ' + escaped_keyword + '...')
        print

        # Get results for each language
        for language in languages:
            paged_results = self.auth.search_code(
                escaped_keyword, language=language
            )
            self.__write_results(paged_results, id)