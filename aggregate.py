#!/usr/bin/env python

import json
import matplotlib.pyplot as plt

frameworks = ["arabesque.log",
              "gelly.log",
              "giraph.log",
              "goffish.log",
              "graphlab.log",
              "graphx.log",
              "tinkerpop-filter.log",
              "tinkerpop.log"]
exec_type = [["filter"],
             ["gas", "vertex", "sg"],
             ["vertex"],
             ["subgraph"],
             ["gas"],
             ["gas"],
              ["traversal"]]
com_type = [["msg"],
             ["dataflow"],
             ["msg"],
             ["msg"],
             ["memory"],
             ["dataflow"],
             ["msg"]]
app_type = [["motif-count"],
            #gelly supports 3 types, so make duplicates
            ["pagerank", "shortest", "color", "pagerank", "shortest", "weak-conn", "color", "als", "diam", "pagerank", "shortest", "weak-conn", "color", "als", "triangle", "k-means", "tree", "belief", "str-conn", "label", "bfs"],
            ["pagerank", "shortest", "weak-conn", "color", "als", "triangle", "k-means", "tree", "belief", "str-conn", "label", "bfs"],
            ["pagerank", "shortest", "weak-conn", "triangle", "k-means", "clust-coeff", "motif-count", "bfs"],
            ["pagerank", "shortest", "weak-conn", "color", "als", "diam"],
            ["pagerank", "shortest", "weak-conn", "color", "als", "diam"],
              []]
issue_counts = []
subscribers_counts = []
stars_counts = []
contributors_counts = []
projects_counts = []
ranks = []
execution_model_ranks = {}
com_ranks = {}

def populate_counts(filtering, accept_index):
    global issue_counts
    global subscribers_counts
    global stars_counts
    global contributors_counts
    global projects_counts
    global ranks
    issue_counts = []
    subscribers_counts = []
    stars_counts = []
    contributors_counts = []
    projects_counts = []
    ranks = []

    def interesting(j):
        sub = j['subscribers_count'] > 0
        star = j["stargazers_count"] > 0
        contrib = len(j['contributors']) > 0
        return sub and star and contrib

    index = -1
    for framework in frameworks:
        index = index + 1
        if not accept_index[index]:
            continue
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

        rank = (issues_count+contributors)*0.1 + stars*1.0 + subscribers*1.5
        ranks.append(rank)

def populate_ranks():
    global execution_model_ranks
    global com_ranks
    index = -1
    execution_model_ranks = {}
    com_ranks = {}
    for rank in ranks:
        index = index + 1

        execution_models = exec_type[index]
        for execution_model in execution_models:
            if execution_model not in execution_model_ranks.keys():
                execution_model_ranks[execution_model] = 0
            execution_model_ranks[execution_model] = execution_model_ranks[execution_model] + rank

        coms = com_type[index]
        for com in coms:
            if com not in com_ranks.keys():
                com_ranks[com] = 0
            com_ranks[com] = com_ranks[com] + rank


fig, ax = plt.subplots(2, 2)

ind = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
ax[0, 0].set_xticks(ind)
ax[0, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[0, 0].set_title('Issue count')
ax[1, 0].set_xticks(ind)
ax[1, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[1, 0].set_title('Subscribers count')
ax[0, 1].set_xticks(ind)
ax[0, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[0, 1].set_title('Stars count')
ax[1, 1].set_xticks(ind)
ax[1, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[1, 1].set_title('Unique contributors count')

# Just for print out
populate_counts(False, [True, True, True, True, True, True, True, False])
print(issue_counts)
print(subscribers_counts)
print(stars_counts)
print(contributors_counts)
print(projects_counts)

ax[0, 0].bar(ind, issue_counts)
ax[1, 0].bar(ind, subscribers_counts)
ax[0, 1].bar(ind, stars_counts)
ax[1, 1].bar(ind, contributors_counts)
plt.tight_layout()
plt.show()


def safe_div(a, b):
    if b == 0:
        return 0
    return float(a) / b


fig, ax = plt.subplots(2, 2)

ind = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
ax[0, 0].set_xticks(ind)
ax[0, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[0, 0].set_title('Normalized issue count per repo')
ax[1, 0].set_xticks(ind)
ax[1, 0].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[1, 0].set_title('Normalized subscribers count per repo')
ax[0, 1].set_xticks(ind)
ax[0, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[0, 1].set_title('Normalized stars count per repo')
ax[1, 1].set_xticks(ind)
ax[1, 1].set_xticklabels(['Arabesque', 'Gelly', 'Giraph', 'Goffish', 'Graphlab', 'GraphX', 'Tinkerpop'])
ax[1, 1].set_title('Normalized unique contributors count per repo')

populate_counts(False, [True, True, True, True, True, True, True, False])
print(issue_counts)
print(subscribers_counts)
print(stars_counts)
print(contributors_counts)
print(projects_counts)

ax[0, 0].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(issue_counts, projects_counts)))
ax[1, 0].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(subscribers_counts, projects_counts)))
ax[0, 1].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(stars_counts, projects_counts)))
ax[1, 1].bar(ind, map(lambda x: safe_div(x[0], x[1]), zip(contributors_counts, projects_counts)))
#plt.tight_layout()
plt.show()


fig, ax = plt.subplots(2, 2)

ind = [0.5, 1.5, 2.5]
ax[0, 0].set_xticks(ind)
ax[0, 0].set_xticklabels(['GraphX', 'Tinkerpop', 'Tinkerpop \n(with related systems)'])
ax[0, 0].set_title('Issue count')
ax[1, 0].set_xticks(ind)
ax[1, 0].set_xticklabels(['GraphX', 'Tinkerpop', 'Tinkerpop \n(with related systems)'])
ax[1, 0].set_title('Subscribers count')
ax[0, 1].set_xticks(ind)
ax[0, 1].set_xticklabels(['GraphX', 'Tinkerpop', 'Tinkerpop \n(with related systems)'])
ax[0, 1].set_title('Stars count')
ax[1, 1].set_xticks(ind)
ax[1, 1].set_xticklabels(['GraphX', 'Tinkerpop', 'Tinkerpop \n(with related systems)'])
ax[1, 1].set_title('Unique contributors count')

populate_counts(False, [False, False, False, False, False, True, True, True])
print(issue_counts)
print(subscribers_counts)
print(stars_counts)
print(contributors_counts)
print(projects_counts)

ax[0, 0].bar(ind, issue_counts)
ax[1, 0].bar(ind, subscribers_counts)
ax[0, 1].bar(ind, stars_counts)
ax[1, 1].bar(ind, contributors_counts)
plt.tight_layout()
plt.show()

populate_counts(True, [False, False, False, False, False, True, True, True])
print(issue_counts)
print(subscribers_counts)
print(stars_counts)
print(contributors_counts)
print(projects_counts)

print
print "Ranks"
populate_counts(True, [True, True, True, True, True, True, True, False])
print ranks

print
print "Execution models ranks"
populate_counts(True, [True, True, True, True, True, True, True, False])
populate_ranks()
print execution_model_ranks
print
print "Communication type ranks"
print com_ranks

print
print "App type frameworks ranks"

populate_counts(True, [True, True, True, True, True, True, True, False])
populate_ranks()
app_ranks = {}
for apps in app_type:
    for app in apps:
        if app not in app_ranks.keys():
            app_ranks[app] = {}

index = -1
for rank in ranks:
    index = index + 1
    app_types_for_framework = app_type[index]
    framework = frameworks[index]
    for app_type_for_framework in app_types_for_framework:
        if framework not in app_ranks[app_type_for_framework].keys():
            app_ranks[app_type_for_framework][framework] = 0
        app_ranks[app_type_for_framework][framework] = app_ranks[app_type_for_framework][framework] + rank

print app_ranks