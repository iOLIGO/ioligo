<img src="./imgs/oligo_logo.png">

Currently, there are very few file formats and database formats for saving oligonucleotides (probes). Most files are saved in bed or tsv format. However, this is extremely unfriendly for recording the source of oligonucleotides and subsequent processing in standard procedures.

## Features

oligo can change this situation. 

+ oligo: simultaneously record the sequence information and characteristic information of the oligonucleotide in oligo format, such as the source species, which tools are used, and parameter design.
+ oligo5: one or more oligonucleotide files are designed to be compressed and saved in the oligo5 format based on the h5 file format.

## Installation

### pip

To install oligo with pip:

```python

pip install oligo

```

### github

To install oligo with github:

#### git clone from github

```shell

git clone git@github.com:iOLIGO/oligo.git

```

#### installation in python

```python

pip install oligo/dist/oligo-1.0.0.tar.gz

```

## Example

### CLI

```shell

oligo --help

```

### API

```python

from oligo import OLIGO,OLIGO5

```
