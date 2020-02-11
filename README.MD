# Object tracking system

This system is supposed to be used on Raspberry Pi

## Installation

* Install following packages:
```bash
sudo apt install libhdf5-103 libjasper1 libqt4-dev
```
* Install requirements
```bash
pip install -r ./requirements.txt
```

## Run
There is [issue](https://github.com/piwheels/packages/issues/59#issuecomment-553321689) with `libatomic.so`, so you need to run this system such way:  
```bash
export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1
python ./src/main.py
```

