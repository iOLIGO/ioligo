# oligo
oligo format tools based on h5df


## oligo format

### groups

groups -> [oligo1, oligo2, ..., oligon]

### attrs
attrs -> [columns, index, type, date, target_genome, negative_genome, temperature, temperature_info, secondary_structure, secondary_structure_info, location, date, author, email, other_info]

1. columns -> [nameid, oligobase, temperature, secondary_structure, chrid, start, end...]

2. index(name_listid) -> [oligoid1, oligoid2,..., oligon]

3. type -> 'DNA' or 'RNA'

4. target_genome -> dict_URL: keys=['fa', 'gtf', 'nt', '16sRNA']; values=['URL1',..., 'URL2']

    4.1 nt: nt_URL

    4.2 16sRNA: 16sRNA_URL

5. negative_genome -> dict_URL: keys=['fa', 'gtf', 'nt', '16sRNA']; values=['URL1',..., 'URL2']

    5.1. nt: ntid

    5.2. 16sRNA: datbaseid

6. temperature -> (t_low, t_high)

7. temperature_info -> (tools, version, params)

8. secondary_structure -> (s_low, s_high)

9. secondary_structure_info -> (tools, version, params)

10. location -> (fa_URL, gtf_URL, 'chr1,chr2,chr3')

11. date -> '20240417'

12. author -> 'wangcong'

13. email -> '2119452560@qq.com'

14. other_info -> 'a nice oligo database'


### data

df.dtype  raw -> str ; str -> np.array -> b'str'

df.dtype  str -> raw ; b'str' -> str -> df


## requirements.txt

conda envirment oligo

conda install anaconda::scikit-bio

conda install anaconda::h5py





