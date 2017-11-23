#!/usr/bin/env python

import json

data = dict()
with open('gelly.log') as f:
    for line in f:
        j = json.loads(line)
        data[j['id']] = j



open_issues = sum(map(lambda j: j['open_issues_count'], data.values()))
subscribers = sum(map(lambda j: j['subscribers_count'], data.values()))
stars = sum(map(lambda j: j['stargazers_count'], data.values()))

print("number of repos: " + str(len(data)))
print("open_issues: " + str(open_issues) + ", per repo: " + str(open_issues / float(len(data))))
print("subscribers: " + str(subscribers) + ", per repo: " + str(subscribers / float(len(data))))
print("stars: " + str(stars) + ", per repo: " + str(stars / float(len(data))))