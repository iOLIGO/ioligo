import pandas as pd
import warnings
import h5py
import json

import os

def Mk_no_dir(dir, recover="N"):
    if os.path.exists(dir):
        if dir == "./":
            pass
        else:
            if recover == "N":
                print(f"warning {dir} exist")
            else:
                print(f"warning {dir} will be recovered")
                os.rmdir(dir)
                os.mkdir(dir)
    else:
        os.mkdir(dir)

# origin/target/negative: genome1,genome2,...,genomen;annotation1,annotation2,...,annotationn;location1,location2,...,location3
## genome/annotation: file_download_URL/NCBI_URL/Ensembl_URL/version
# location: chromosome:start:end:strand
# tools: tools;version;params
# temp/ss: low;high
# temp: temperature
# ss: secondary_structure

class OLIGO:
    """
    """
    def __init__(self):
        self.name = ""
        self.group = ""
        self.type = ""
        self.date = ""
        self.author = ""
        self.email = ""
        self.other_info = ""
        self.data = pd.DataFrame()
        self.origin = {"fa":[], "gtf":[], "location":[]}
        self.origin_tools = {"tools":[], "version":[], "params":[]}
        self.target = {"fa":[], "gtf":[], "location":[]}
        self.target_tools = {"tools":[], "version":[], "params":[]}
        self.negative = {"fa":[], "gtf":[], "params":[]}
        self.negative_tools = {"tools":[], "version":[], "params":[]}
        self.temp = {"low":"", "high":""}
        self.temp_tools = {"tools":"", "version":"", "params":""}
        self.ss = {"low":"", "high":""}
        self.ss_tools = {"tools":"", "version":"", "params":""}
    

    def tsv_read(self, header, data):

        with open(header, "r") as fh:
            for line in fh:
                line_list = line.strip().split("\t")
                feature = line_list[0]
                value = line_list[1]
                len_value = len(value.split(";"))

                if feature == "type":
                    self.type = value
                elif feature == "name":
                    self.name = value
                elif feature == "group":
                    self.group = value
                elif feature == "origin":
                    if len_value > 0:
                        self.origin["fa"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.origin["gtf"] += value.split(";")[1].split(",")
                    if len_value > 2:
                        self.origin["location"] += value.split(";")[2].split(",")
                elif feature == "origin_tools":
                    if len_value > 0:
                        self.origin_tools["tools"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.origin_tools["version"] += value.split(";")[1].split(",")
                    if len_value > 2:
                        self.origin_tools["params"] += value.split(";")[2].split(",")
                elif feature == "target":
                    if len_value > 0:
                        self.target["fa"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.target["gtf"] += value.split(";")[1].split(",")
                    if len_value > 2:
                        self.target["location"] += value.split(";")[2].split(",")
                elif feature == "target_tools":
                    if len_value > 0:
                        self.target_tools["tools"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.target_tools["version"] += value.split(";")[1].split(",")
                    if len_value > 2:
                        self.target_tools["params"] += value.split(";")[2].split(",")
                elif feature == "negative":
                    if len_value > 0:
                        self.negative["fa"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.negative["gtf"] += value.split(";")[1].split(",")
                    if len_value > 1:
                        self.negative["gtf"] += value.split(";")[1].split(",")
                elif feature == "negative_tools":
                    if len_value > 0:
                        self.negative_tools["tools"] += value.split(";")[0].split(",")
                    if len_value > 1:
                        self.negative_tools["version"] += value.split(";")[1].split(",")
                    if len_value > 2:
                        self.negative_tools["params"] += value.split(";")[2].split(",")
                elif feature == "temp":
                    if len_value > 0:
                        if value.split(";")[0]:
                            self.temp["low"] = float(eval(value.split(";")[0]))
                    if len_value > 1:
                        self.temp["high"] = float(eval(value.split(";")[1]))
                elif feature == "temp_tools":
                    self.temp_tools["tools"] = value.split(";")[0]
                    self.temp_tools["version"] = value.split(";")[1]
                    self.temp_tools["params"] = value.split(";")[2]
                elif feature == "ss":
                    if len_value > 0:
                        if value.split(";")[0]:
                            self.ss["low"] = float(eval(value.split(";")[0]))
                    if len_value > 1:
                        self.ss["high"] = float(eval(value.split(";")[1]))
                elif feature == "ss_tools":
                    self.ss_tools["tools"] = value.split(";")[0]
                    self.ss_tools["version"] = value.split(";")[1]
                    self.ss_tools["params"] = value.split(";")[2]
                elif feature == "date":
                    self.date = value
                elif feature == "author":
                    self.author = value
                elif feature == "email":
                    self.email = value
                elif feature == "other_info":
                    self.other_info = value
                else:
                    warnings.warn(f"{feature} is not in oligo format, will be ignored!", UserWarning)
        
        df_data = pd.read_csv(data, sep="\t")

        self.data = df_data

        return
    
    def read(self, oligo_file):

        with open(oligo_file, "r") as f:
            for line in f:
                if line.startswith("#"):
                    line_list = line.strip()[1:].split("\t")
                    feature = line_list[0]
                    value = line_list[1]
                    len_value = len(value.split(";"))
                    if feature == "type":
                        self.type = value
                    elif feature == "name":
                        self.name = value
                    elif feature == "group":
                        self.group = value
                    elif feature == "origin":
                        if len_value > 0:
                            self.origin["fa"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.origin["gtf"] += value.split(";")[1].split(",")
                        if len_value > 2:
                            self.origin["location"] += value.split(";")[2].split(",")
                    elif feature == "origin_tools":
                        if len_value > 0:
                            self.origin_tools["tools"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.origin_tools["version"] += value.split(";")[1].split(",")
                        if len_value > 2:
                            self.origin_tools["params"] += value.split(";")[2].split(",")
                    elif feature == "target":
                        if len_value > 0:
                            self.target["fa"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.target["gtf"] += value.split(";")[1].split(",")
                        if len_value > 2:
                            self.target["location"] += value.split(";")[2].split(",")
                    elif feature == "target_tools":
                        if len_value > 0:
                            self.target_tools["tools"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.target_tools["version"] += value.split(";")[1].split(",")
                        if len_value > 2:
                            self.target_tools["params"] += value.split(";")[2].split(",")
                    elif feature == "negative":
                        if len_value > 0:
                            self.negative["fa"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.negative["gtf"] += value.split(";")[1].split(",")
                        if len_value > 1:
                            self.negative["gtf"] += value.split(";")[1].split(",")
                    elif feature == "negative_tools":
                        if len_value > 0:
                            self.negative_tools["tools"] += value.split(";")[0].split(",")
                        if len_value > 1:
                            self.negative_tools["version"] += value.split(";")[1].split(",")
                        if len_value > 2:
                            self.negative_tools["params"] += value.split(";")[2].split(",")
                    elif feature == "temp":
                        if len_value > 0:
                            if value.split(";")[0]:
                                self.temp["low"] = float(eval(value.split(";")[0]))
                        if len_value > 1:
                            self.temp["high"] = float(eval(value.split(";")[1]))
                    elif feature == "temp_tools":
                        self.temp_tools["tools"] = value.split(";")[0]
                        self.temp_tools["version"] = value.split(";")[1]
                        self.temp_tools["params"] = value.split(";")[2]
                    elif feature == "ss":
                        if len_value > 0:
                            if value.split(";")[0]:
                                self.ss["low"] = float(eval(value.split(";")[0]))
                        if len_value > 1:
                            self.ss["high"] = float(eval(value.split(";")[1]))
                    elif feature == "ss_tools":
                        self.ss_tools["tools"] = value.split(";")[0]
                        self.ss_tools["version"] = value.split(";")[1]
                        self.ss_tools["params"] = value.split(";")[2]
                    elif feature == "date":
                        self.date = value
                    elif feature == "author":
                        self.author = value
                    elif feature == "email":
                        self.email = value
                    elif feature == "other_info":
                        self.other_info = value
                    else:
                        warnings.warn(f"{feature} is not in oligo format, will be ignored!", UserWarning)
                else:
                    break
        
        if not self.group:
            warnings.warn(f"oligo group is not exists, use defualt name", UserWarning)
            self.group = f"G-{self.name}"
        
        self.data = pd.read_csv(oligo_file, sep="\t", comment='#')

        return


    def to_oligo(self, name=None, out_dir="./"):
        
        if name:
            file_name = name
        else:
            file_name = self.name
        
        Mk_no_dir(out_dir)
        with open(f"{out_dir}/{file_name}.oligo", "w") as f:
            if self.name:
                f.write(f"#name\t{self.name}\n")
            else:
                raise ValueError("oligo name is not exists!")
            
            if self.group:
                f.write(f"#group\t{self.group}\n")
            else:
                warnings.warn(f"oligo group is not exists!", UserWarning)
            
            if self.type:
                f.write(f"#type\t{self.type}\n")
            else:
                warnings.warn(f"oligo type is not exists!", UserWarning)
            
            
            if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.origin.values()):
                str_w = ""
                if len(self.origin["fa"]) > 0:
                    str_w = str_w + ",".join(self.origin["fa"])
                if len(self.origin)["gtf"] > 0:
                    str_w = str_w + ";" + ",".join(self.origin["gtf"])
                if len(self.origin["location"]) > 0:
                    str_w = str_w + ";" + ",".join(self.origin["location"])
                f.write(f"#origin\t{str_w}\n")
                
                if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.origin_tools.values()):
                    f.write(f"#origin_tools\t" + ";".join([self.origin_tools["tools"], self.origin_tools["version"], self.origin_tools["params"]]) + "\n")
                else:
                    warnings.warn(f"oligo origin is exists, but tools is not exists!", UserWarning)

            if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.target.values()):
                str_w = ""
                if len(self.target["fa"]) > 0:
                    str_w = str_w + ",".join(self.target["fa"])
                if len(self.target)["gtf"] > 0:
                    str_w = str_w + ";" + ",".join(self.target["gtf"])
                if len(self.target["location"]) > 0:
                    str_w = str_w + ";" + ",".join(self.target["location"])
                f.write(f"#origin_tools\t{str_w}\n")
                
                if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.target_tools.values()):
                    f.write(f"#origin_tools\t" + ";".join([self.target_tools["tools"], self.target_tools["version"], self.target_tools["params"]]) + "\n")
                else:
                    warnings.warn(f"oligo origin is exists, but tools is not exists!", UserWarning)
            
            if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.negative.values()):
                str_w = ""
                if len(self.negative["fa"]) > 0:
                    str_w = str_w + ",".join(self.negative["fa"])
                if len(self.negative)["gtf"] > 0:
                    str_w = str_w + ";" + ",".join(self.negative["gtf"])
                if len(self.negative["location"]) > 0:
                    str_w = str_w + ";" + ",".join(self.negative["location"])
                f.write(f"#negative\t{str_w}\n")
                
                if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.negative_tools.values()):
                    f.write(f"#negative_tools\t" + ";".join([self.negative_tools["tools"], self.negative_tools["version"], self.negative_tools["params"]]) + "\n")
                else:
                    warnings.warn(f"oligo negative is exists, but tools is not exists!", UserWarning)


            if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.temp.values()):
                low = str(self.temp["low"])
                high = str(self.temp["high"])
                f.write(f"#temp\t{low};{high}\n")
                if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.temp.values()):
                    f.write(f"#temp_tools\t" + ";".join([self.temp["tools"], self.temp["version"], self.temp["params"]]) + "\n")
                else:
                    warnings.warn(f"oligo temp is exists, but tools is not exists!", UserWarning)

            if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.ss.values()):
                low = str(self.ss["low"])
                high = str(self.ss["high"])
                f.write(f"#ss\t{low};{high}\n")
                if not all(value == '' or value is None or (isinstance(value, (list, dict)) and not value) for value in self.ss.values()):
                    f.write(f"#ss_tools\t" + ";".join([self.ss["tools"], self.ss["version"], self.ss["params"]]) + "\n")
                else:
                    warnings.warn(f"oligo ss is exists, but tools is not exists!", UserWarning)
            if self.date:
                f.write(f"#date\t{self.date}\n")
            if self.author:
                f.write(f"#author\t{self.author}\n")
            if self.email:
                f.write(f"#email\t{self.email}\n")
            if self.other_info:
                f.write(f"#other_info\t{self.other_info}\n")

        self.data.to_csv(f"{out_dir}/{file_name}.oligo", mode="a", sep="\t", index=None)     

       

    def to_oligo5(self, name=None, out_dir="./"):

        if name:
            file_name = name
        else:
            file_name = self.name
        
        Mk_no_dir(out_dir)
        with h5py.File(f"{out_dir}/{file_name}.oligo5", "w") as f:
            
            if self.group:
                group_name = self.group
            else:
                group_name = f"G_{self.name}"
            group = f.create_group(group_name)
            dataset = group.create_dataset(self.name, data=self.data.astype("str").values)
            dataset.attrs["name"] = self.name
            dataset.attrs["type"] = self.type
            dataset.attrs["group"] = self.group
            dataset.attrs["origin"] = json.dumps(self.origin)
            dataset.attrs["origin_tools"] = json.dumps(self.origin_tools)
            dataset.attrs["target"] = json.dumps(self.target)
            dataset.attrs["target_tools"] = json.dumps(self.target_tools)
            dataset.attrs["negative"] = json.dumps(self.negative)
            dataset.attrs["negative_tools"] = json.dumps(self.negative_tools)
            dataset.attrs["temp"] = json.dumps(self.temp)
            dataset.attrs["temp_tools"] = json.dumps(self.temp_tools)
            dataset.attrs["ss"] = json.dumps(self.ss)
            dataset.attrs["ss_tools"] = json.dumps(self.ss_tools)
            dataset.attrs["date"] = self.date
            dataset.attrs["author"] = self.author
            dataset.attrs["email"] = self.email
            dataset.attrs["other_info"] = self.other_info
            dataset.attrs["columns"] = json.dumps({col: str(dtype) for col, dtype in self.data.dtypes.items()})


class OLIGO5:
    """
    """
    def __init__(self, name):
        self.name = name
        self.oligos = {}
    
    def to_oligo(self, out_dir="./"):
        Mk_no_dir(out_dir)
        for group, oligos in self.oligos.items():
            Mk_no_dir(f"{out_dir}/{group}")
            for oligo in oligos:
                oligo.to_oligo(f"{out_dir}/{group}")


    def to_oligo5(self, name=None, out_dir="./"):

        if name:
            file_name = name
        else:
            file_name = self.name

        Mk_no_dir(out_dir)
        with h5py.File(f"{out_dir}/{file_name}.oligo5", "w") as f:
            for group, oligos in self.oligos.items():
                group = f.create_group(group)
                for oligo in oligos:
                    dataset = group.create_dataset(oligo.name, data=oligo.data.astype("str").values)
                    dataset.attrs["name"] = oligo.name
                    dataset.attrs["type"] = oligo.type
                    dataset.attrs["group"] = oligo.group
                    dataset.attrs["origin"] = json.dumps(oligo.origin)
                    dataset.attrs["origin_tools"] = json.dumps(oligo.origin_tools)
                    dataset.attrs["target"] = json.dumps(oligo.target)
                    dataset.attrs["target_tools"] = json.dumps(oligo.target_tools)
                    dataset.attrs["negative"] = json.dumps(oligo.negative)
                    dataset.attrs["negative_tools"] = json.dumps(oligo.negative_tools)
                    dataset.attrs["temp"] = json.dumps(oligo.temp)
                    dataset.attrs["temp_tools"] = json.dumps(oligo.temp_tools)
                    dataset.attrs["ss"] = json.dumps(oligo.ss)
                    dataset.attrs["ss_tools"] = json.dumps(oligo.ss_tools)
                    dataset.attrs["date"] = oligo.date
                    dataset.attrs["author"] = oligo.author
                    dataset.attrs["email"] = oligo.email
                    dataset.attrs["other_info"] = oligo.other_info
                    dataset.attrs["columns"] = json.dumps({col: str(dtype) for col, dtype in oligo.data.dtypes.items()})
    
    
    def read(self, oligo5_file):
        
        with h5py.File(oligo5_file, "r") as f:
            for group in f:
                oligos_name = []
                if group in self.oligos:
                    oligos = self.oligos[group]
                    for oligo in oligos:
                        oligos_name.append(oligo.name)
                else:
                    oligos = []
                for dataset_name in f[group]:
                    if dataset_name in oligos_name:
                        raise ValueError(f"{dataset_name} already exists in {group}")
                    else:
                        dataset = f[group][dataset_name]
                        oligo = OLIGO()
                        oligo.name = dataset.attrs["name"]
                        oligo.group = group
                        oligo.type = dataset.attrs["type"]
                        oligo.origin = json.loads(dataset.attrs["origin"])
                        oligo.origin_tools = json.loads(dataset.attrs["origin_tools"])
                        oligo.target = json.loads(dataset.attrs["target"])
                        oligo.target_tools = json.loads(dataset.attrs["target_tools"])
                        oligo.negative = json.loads(dataset.attrs["negative"])
                        oligo.negative_tools = json.loads(dataset.attrs["negative_tools"])
                        oligo.temp = json.loads(dataset.attrs["temp"])
                        oligo.temp_tools = json.loads(dataset.attrs["temp_tools"])
                        oligo.ss = json.loads(dataset.attrs["ss"])
                        oligo.ss_tools = json.loads(dataset.attrs["ss_tools"])
                        oligo.date = dataset.attrs["date"]
                        oligo.author = dataset.attrs["author"]
                        oligo.email = dataset.attrs["email"]
                        oligo.other_info = dataset.attrs["other_info"]
                        np_data = dataset.asstr()[:]
                        columns_dict = json.loads(dataset.attrs["columns"])
                        df_data = pd.DataFrame(np_data, columns=columns_dict.keys())
                        oligo.data = df_data.astype(columns_dict)
                        oligos.append(oligo)
                self.oligos[group] = oligos
        return
    
    # oligos -> list
    def read_soligo(self, oligos):
        
        for oligo in oligos:

            if oligo.group:
                group = oligo.group
            else:
                group = f"G_{oligo.name}"

            if group in self.oligos:
                list_oligos = self.oligos[group]
                list_oligos.append(oligo)
                self.oligos[group] = list_oligos
            else:
                self.oligos[group] = [oligo]

        return
    
    # oligo_files
    def read_foligo(self, *oligo_files):

        list_oligos = []
        for oligo_file in oligo_files:
            oligo = OLIGO()
            oligo.read(oligo_file)
            list_oligos.append(oligo)
        self.read_soligo(list_oligos)
        return
    

    def read_doligo(self, oligo_dir):

        import glob
        oligo_files = glob.glob(f"{oligo_dir}/*.oligo")       
        self.read_foligo(oligo_files)

        return
    
    def del_group(self, group):

        self.oligos.pop(group)

        return
    
    def del_oligo(self, group, oligo):
        new_oligos = self.oligos[group].remove(oligo)
        self.oligos[group] = new_oligos
        return
