#!/usr/bin/env python

import json
import matplotlib.pyplot as plt

frameworks = ["arabesque.log", "gelly.log", "giraph.log", "goffish.log", "graphlab.log", "graphx.log"]
issue_counts = []
subscribers_counts = []
stars_counts = []
contributors_counts = []
projects_counts = []

filtering = True

def interesting(j):
	issue = j['issues_count'] > 0
	sub = j['subscribers_count'] > 1
	star = j["stargazers_count"] > 0
	contrib = len(j['contributors']) > 1
	return issue and sub and star and contrib

for framework in frameworks:
	cont = set()
	data = dict()
	with open(framework) as f:
	    for line in f:
	        j = json.loads(line)
	        if not filtering or interesting(j):
	        	data[j['id']] = j
	
	def handle_contributors(cs):
		n = 0
		for c in cs:
			if not c in cont:
				n += 1
				cont.add(c)
		return n
	
	issues_count = sum(map(lambda j: j['issues_count'], data.values()))
	issue_counts.append(issues_count)
	subscribers = sum(map(lambda j: j['subscribers_count'], data.values()))
	subscribers_counts.append(subscribers)
	stars = sum(map(lambda j: j['stargazers_count'], data.values()))
	stars_counts.append(stars)
	contributors = sum(map(lambda j: handle_contributors(j['contributors']), data.values()))
	contributors_counts.append(contributors)
	projects_counts.append(len(data))

ind = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]

print(issue_counts)
print(subscribers_counts)
print(stars_counts)
print(contributors_counts)
print(projects_counts)

fig, ax = plt.subplots(2, 2)
ax[0, 0].set_xticks(ind)
ax[0, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[0, 0].set_ylabel('Issue count')
ax[0, 0].set_title('Usage of graph processing frameworks on github')
ax[0, 0].bar(ind, issue_counts)
ax[1, 0].set_xticks(ind)
ax[1, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[1, 0].set_ylabel('Subscribers count')
ax[1, 0].set_title('Usage of graph processing frameworks on github')
ax[1, 0].bar(ind, subscribers_counts)
ax[0, 1].set_xticks(ind)
ax[0, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[0, 1].set_ylabel('Stars count')
ax[0, 1].set_title('Usage of graph processing frameworks on github')
ax[0, 1].bar(ind, stars_counts)
ax[1, 1].set_xticks(ind)
ax[1, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[1, 1].set_ylabel('Unique contributors count')
ax[1, 1].set_title('Usage of graph processing frameworks on github')
ax[1, 1].bar(ind, contributors_counts)

plt.show()

#plt.bar(ind, issue_counts)
#plt.show()
#plt.bar(ind, subscribers_counts)
#plt.show()
#plt.bar(ind, stars_counts)
#plt.show()
#plt.bar(ind, contributors_counts)
#plt.show()

def safe_div(a, b):
	if b == 0:
		return 0
	return float(a) / b

fig, ax = plt.subplots(2, 2)

ax[0, 0].set_xticks(ind)
ax[0, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[0, 0].set_ylabel('Issue count per repo')
ax[0, 0].set_title('Usage of graph processing frameworks on github')
ax[0, 0].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(issue_counts, projects_counts)))
ax[1, 0].set_xticks(ind)
ax[1, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[1, 0].set_ylabel('Subscribers count per repo')
ax[1, 0].set_title('Usage of graph processing frameworks on github')
ax[1, 0].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(subscribers_counts, projects_counts)))
ax[0, 1].set_xticks(ind)
ax[0, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[0, 1].set_ylabel('Stars count per repo')
ax[0, 1].set_title('Usage of graph processing frameworks on github')
ax[0, 1].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(stars_counts, projects_counts)))
ax[1, 1].set_xticks(ind)
ax[1, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX'])
ax[1, 1].set_ylabel('Unique contributors count per repo')
ax[1, 1].set_title('Usage of graph processing frameworks on github')
ax[1, 1].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(contributors_counts, projects_counts)))

#plt.bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(issue_counts, projects_counts)))
#plt.show()
#plt.bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(subscribers_counts, projects_counts)))
#plt.show()
#plt.bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(stars_counts, projects_counts)))
#plt.show()
#plt.bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(contributors_counts, projects_counts)))

plt.show()
