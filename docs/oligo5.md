<div align="center">

<img src="./imgs/oligo_logo.png">

<p> The oligo database file based on the h5 file structure can contain one or more oligo files(tests/test_data/sample.oligo5). </p>

</div>

## OLIGO5

Python object composed of oligo.

```python

from oligo import OLIGO5

oligo5_test = OLIGO5("test")
oligo5_file = "tests/test_data/oligo/sample.oligo5"
oligo5_test.read(oligo5_file)

oligo5_test.name
# 'test'
oligo5_test.oligos
# {'G-sample': [<oligo.oligo.OLIGO object at 0x7fcb26336a30>]}
type(oligo5_test.oligos["G-sample"])
# <class 'list'>
oligo5_test.oligos["G-sample"][0].name
# 'sample'
olgio5_test.help()
# "more info: https://github.com/iOLIGO/oligo/blob/main/docs/oligo5.md"
```

## More usage

- Read multiple oligo files at the same time to form an oligo5 file.

```python
oligo1 = "./test.oligo"
oligo2 = "./test/test2.oligo"
oligo3 = "./test/test3.oligo"
from oligo import OLIGO5
oligo5_test = OLIGO5("test")
oligo5_test.read_foligo(oligo1, oligo2, oligo3)
```

- Read all oligo files in the directory at the same time to form an oligo5 file.

```python
oligos_dir = "./test"
from oligo import OLIGO5
oligo5_test = OLIGO5("test")
oligo5_test.read_doligo(oligos_dir)
```