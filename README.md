MyPyROOTModules
====

- Python modules for PyROOT

## Requirement
- Python 2.x
- numpy
- ROOT 6.x

## Install

### 1.Clone this repository
```bash
$ git clone https://github.com/haru-same-same/MyPyROOTModules ~/
```

### 2.Add PYTHONPATH
Edit .bashrc or .zshrc and add PYTHONPATH
```bash:.bashrc
export PYTHONPATH="$HOME/MyPyROOTModules"
```

## Usage

### resmat

1. Import the module
```python
import resmat
```

2. Create an instace
```python
my_resmat = resmat.Resmat()
```

3. Set ROOTFile, Tree name, Branch name
```python
my_resmat.SetFileTreeBranch('path/to/ROOTFile', 'Tree name', 'Branch name for Xaxis', 'Branch name foy Yaxis')
```

4. Set edges of matrix element
```python
my_resmat.SetBinEdge([List of Bin Edges])
```

5. Set the number of events
```python
my_resmat.SetNEvents(NEvents)
```

6. Create the Response matrix
```python
my_resmat.CreateResMat()
```
