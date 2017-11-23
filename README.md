# Mining Github

- Piotr Mrowczynski
- Mátyás Manninger

#### Description

Work based on ```https://github.com/PyGithub/PyGithub```

```
chmod +x graphproc_frameworks_mining.py
```

With prompt:
```
./graphproc_frameworks_mining.py -u <username> -d <password>
```

Without prompt:
```
./graphproc_frameworks_mining.py
```

The above will display help message on how to use this repository

```
Please supply with Github username and password, and optionaly --cleanrun flag to reset result for framework
./graphproc_frameworks_mining.py -u <username> -d <password> [all/gelly/graphx/giraph/tinkerpop/arabesque/graphlab]
./graphproc_frameworks_mining.py -u foo -d foopass gelly
./graphproc_frameworks_mining.py gelly
./graphproc_frameworks_mining.py --cleanrun gelly
./graphproc_frameworks_mining.py --cleanrun all
```

#### Prerequisites

To start with, run the following after checking out your branch:

```
sudo pip install -r requirements.txt
```

#### PROJECT STRUCTURE:

<pre>

   mining-github
   ├── lib/
   │   └── mining.py                    : Miner class responsible
   │                                      for Github code mining
   │
   ├── graphproc_frameworks_mining.py   : Example
   │
   └── README

</pre>