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