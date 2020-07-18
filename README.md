# Explore
<br>
Data Manager with Python Integration.
Explore is a REPL Data Manager with Python Integration.

The official documentation can be found in the ``Documentation`` directory in this repository.

The Explore Package can be found in the ``explore-package`` directory.

**Requirements**
> ``git``

> ``python3``

> ``pip3``

> ``node``

> ``docker``  (Optional: For Dockerfile.)

> ``bash`` (Optional: If you decide to use the installer.)

#### Getting Explore

Clone this repository:
```
git clone https://www.github.com/KILLinefficiency/Explore.git
```

**Installing on Linux and WSL**

Installation for Linux can be done either manually or automatically via a script.

*Manual Installation (not recommened for new users):*

1] ``cd`` into the cloned repository.

2] Install the dependencies using ``pip3``.
```
pip3 install -r requirements.txt
```

3] Run ``Explore.py`` file.
```
python3 Explore.py
```

4] For using the server, run ``server.js`` file.
```
node server.js
```
*Automatic Installation (recommended):*

1] ``cd`` into the cloned repository.
```
cd Explore
```

2] Run ``install.sh``.
```
./install.sh
```

This will install Explore at ``~/.Explore``.

Explore can be launched by running ``explore`` in the terminal.

Explore Server can be launched by running ``explore-server`` in the terminal.

**Installing on Windows**

1] ``cd`` into the cloned repository.

2] Install the dependencies using ``pip``.
```
pip install -r requirements.txt
```

3] Run ``Explore.py`` file.
```
python Explore.py
```

4] For using the server, run ``server.js`` file.
```
node server.js
```
