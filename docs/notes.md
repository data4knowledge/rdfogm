# General Notes on Python

## Setup
Steps taken to get the project setup

Install Python 3.10 using the download from [main python site](https://www.python.org/downloads/).

Install pytest.
```
pip3 install -U pytest
```

Add in alias to get pip working again. In ```~/.zprofile``` add the line.
```
alias pip=pip3
```

Also updated the pip version using the following. Did so because of a warning.
```
python3 -m pip install --upgrade pip 
```

Had to setup PYTHONPATH as follows
```
daveih@ipad-4 rdfogm % pwd
/Users/daveih/Documents/python/rdfogm
daveih@ipad-4 rdfogm % PYTHONPATH=$PYTHONPATH:/Users/daveih/Documents/python/rdfogm
daveih@ipad-4 rdfogm % export PYTHONPATH
daveih@ipad-4 rdfogm % echo $PYTHONPATH     
```

## Virtual Environment

```
python3 -m venv env    
source env/bin/activate
deactivate    
```

## Running Tests With Debugger And Console Output

```
pytest tests/ --pdb -rP   
```

Breakpoint
```
assert 0
```

Install package being worked on
```
pip install -e .
```