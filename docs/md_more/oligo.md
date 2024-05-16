<div align="center">

<img src="./imgs/oligo_logo.png">

<p> Oligo is essentially a txt file, contains head and body. Sample file is in path(tests/test_data/test.oligo) </p>

</div>

## OLIGO

Python object for reading oligo files

```python

from oligo import OLIGO
oligo_file = "tests/test_data/oligo/test.oligo"
oligo_test = OLIGO()
oligo_test.read(oligo_file)
oligo_test.name 
# 'sample'
oligo_test.origin
# {'fa': ['hg19', 'mm10'], 'gtf': ['gtf1', 'gtf2'], 'location': ['1:chr1:0:5000:+', '1:chr2:2000:3000:-']}
oligo_test.origin_tools
# {'tools': ['tools1', 'tools2'], 'version': ['version1', 'version2'], 'params': ['params1', 'params2']}
oligo_test.temp
# {'low': 35.0, 'high': 45.0}
oligo_test.to_oligo()
# ./sample.oligo
oligo_test.to_oligo5()
# ./sample.oligo5
oligo_test.help()
# "more info: https://github.com/iOLIGO/oligo/blob/main/docs/oligo.md"
```


## header

All start with '#', which records the characteristic information of the oligonucleotide.

| Attributes | Use | Sample |
|:-----------:|:-----:|:------:|
|name|info|oligo1|
|group|info|G-oligo1|
|type|Nucleotide species|DNA|
|origin|source of oligonucleotides|hg19;hg19_gtf;1:chr1:1:10000:+|
|origin_tools|tools|bedtools;v1.0;default|
|target|target region|hg19;hg19_gtf;1:chr1:1:10000:+|
|origin_tools|tools|bowtie2;v1.0;default|
|negative|negative region|mm10;;1:chr2:1:10000:-|
|negative_tools|tools|blast;v1.0;default|
|temp|Binding temperature range|35;45|
|temp_tools|tools|nupcak;v1.0;default|
|ss|secondary structures range|0;0.3|
|ss_tools|tools|nupcak;v1.0;default|
|date|info|20240423|
|author|info|ilead-cong|
|email|info|2119452560@qq.com|
|add|info|5'-AATTCC|
|other_info|info|nice oligo|


### name

For an oligo file, oligo name is required.

### group

Group is used to classify and organize oligo files and is optional. If it does not exist, the default is to add 'G-' in front of the name attribute, like ' G-{oligo.name}'

### type

types of oligonucleotides: DNA or RNA.

### origin

The source of oligonucleotides, including genome, annotation, and location. The three are separated by semicolons, like '`{genome;annotation;location}`' or '`{genome1,genome2,genome3;annotation1,annotation2,annotation3;location1,location2,location3}`'. More info: 'genome1 <-> annotation1 <-> location1'.

- genome: Record the identity information of the reference genome fa file, such as version name or download address, separated by commas, like '`{fa1_URL,fa2_URL,fa3_version}`'.

- annotation: Record the identity information of the reference genome gtf file, such as version name or download address, separated by commas, like '`{gtf1_URL,gtf2_URL,fa3_version}`'.

- location: Record the identity information of the reference genome location information,separated by commas, like '`{location1,location2,location3}`'.

- more info: The location attribute consists of genomeid, chromosome name, starting position, ending position, and positive and negative [strands](https://www.biostars.org/p/3423/), separated by colons, like '`{geonemid,chrom,start,end,strand}`' or '`{genomeid,all}`'.

### target

The target region targeted by the oligonucleotide. The format refers to the origin attribute.

### negative

The negative target region targeted by the oligonucleotide. The format refers to the origin attribute.

### hkmer

The [high frequency k-mers](https://github.com/gmarcais/Jellyfish/blob/master/doc/Readme.md#Counting-high-frequency-k-mers) target region targeted by the oligonucleotide. The format refers to the origin attribute.

### origin_tools

Record the tools used by origin, including tool name, version, and parameters, separated by semicolons, like '`{tools;version;params}`' or '`{tools1,tools2;version1,version2;param1,param2}`'.

More info: if the location attribute of the origin exists, it corresponds to one; otherwise, it corresponds to the genome attribute.

### target_tools

Record the tools used by target, the format refers to the origin_tools attribute.

### negative_tools

Record the tools used by negative, the format refers to the origin_tools attribute.

### hkmer_tools

Record the tools used by hkmer, the format refers to the hkmer_tools attribute.

### temp

Binding temperature of oligonucleotide and its reverse complement, like '`{low,high}`'

### temp_tools

Record the tools used by temp, like '`{tools,version,param}`'

### ss

Probability of oligonucleotides forming secondary structures, like '`{low,high}`'

### ss_tools

Record the tools used by ss, like '`{tools,version,param}`'

### date

Date the oligonucleotide was produced

### author

Creator of oligonucleotide generation

### email

The creator's email address of the oligonucleotide generated

### add

Add fixed sequence at the 3' or 5' end of the oligo sequence

### other_info

Other information that needs to be recorded


## body

Tab-delimited matrix file with column names, used to record oligonucleotide details.