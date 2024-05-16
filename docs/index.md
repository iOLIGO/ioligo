
# oligo

Currently, there are very few file formats and database formats for saving oligonucleotides (probes). Most files are saved in bed or tsv format. However, this is extremely unfriendly for recording the source of oligonucleotides and subsequent processing in standard procedures.

## Features

oligo can change this situation. 

+ oligo: simultaneously record the sequence information and characteristic information of the oligonucleotide in oligo format, such as the source species, which tools are used, and parameter design.
+ oligo5: one or more oligonucleotide files are designed to be compressed and saved in the oligo5 format based on the h5 file format.

## Installation

To install oligo with github:


```shell

git clone git@github.com:iOLIGO/oligo.git

pip install oligo/dist/oligo-1.0.0.tar.gz

```

## usage

### CLI

```shell

oligo --help

# oligo to oligo5
oligo -ft OstoO5 -o test_data/oligo/test.oligo -n5 test_cli -ot test_data/oligo

# oligo dir to oligo5
oligo -ft OstoO5 -od test_data/oligo -n5 test_cli_dir -ot test_data/oligo

# oligo5 ot oligo
oligo -ft O5toOs -o5 test_data/oligo/test_cli_dir.oligo5 -ot test_data/oligo/O5toOs_cli
```

### API

```python

from oligo import OLIGO,OLIGO5

```


### More usage help

- [oligo](./oligo.md)
- [oligo5](./oligo5.md)


### jupyter sample

more sample: https://github.com/iOLIGO/oligo/blob/main/tests/oligo.ipynb