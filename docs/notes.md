# Setup
Steps taken to get the project setup
Install Python 3.10 using the download from [main python site](https://www.python.org/downloads/)

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