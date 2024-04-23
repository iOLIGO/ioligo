# oligo5

The oligo database file based on the h5 file structure can contain one or more oligo files.

# OLIGO5

Python object composed of oligo.

```python

from oligo import OLIGO5

oligo5_test = OLIGO5("test")
oligo5_file = "tests/test_data/sample.oligo5"
oligo5_test.read(oligo5_file)

oligo5_test.name
# 'test'
oligo5_test.oligos
# {'G-sample': [<oligo.oligo.OLIGO object at 0x7fcb26336a30>]}


```