

<div align="center">

<img src="./docs/imgs/oligo_logo.png">

</div>


# ioligo

Currently, there are very few file formats and database formats for saving oligonucleotides (probes). Most files are saved in bed or tsv format. However, this is extremely unfriendly for recording the source of oligonucleotides and subsequent processing in standard procedures.

## Features

ioligo can change this situation. 

+ oligo: simultaneously record the sequence information and characteristic information of the oligonucleotide in oligo format, such as the source species, which tools are used, and parameter design.
+ oligo5: one or more oligonucleotide files are designed to be compressed and saved in the oligo5 format based on the h5 file format.

## Installation

To install ioligo with github:

### pip

```shell

pip install ioligo

```

## usage

### CLI

```shell

ioligo --help

# oligo to oligo5
ioligo -ft OstoO5 -o test_data/oligo/test.oligo -n5 test_cli -ot test_data/oligo

# oligo dir to oligo5
ioligo -ft OstoO5 -od test_data/oligo -n5 test_cli_dir -ot test_data/oligo

# oligo5 ot oligo
ioligo -ft O5toOs -o5 test_data/oligo/test_cli_dir.oligo5 -ot test_data/oligo/O5toOs_cli
```

### API

```python

from ioligo import OLIGO,OLIGO5

```

### More usage help

- [oligo](https://github.com/iOLIGO/oligo/blob/main/docs/oligo.md)
- [oligo5](https://github.com/iOLIGO/oligo/blob/main/docs/oligo5.md)

### jupyter sample

more sample: https://github.com/iOLIGO/oligo/blob/main/tests/oligo.ipynb