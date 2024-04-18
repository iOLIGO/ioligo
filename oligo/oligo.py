import pandas as pd
import h5py
import numpy as np
from skbio import DNA, RNA
import json


class OLIGO:
    """
    """
    def __init__(self, name):
        self.name = name
        self.group = ""
        self.type = ""
        self.target_genome = {"fa":[], "gtf":[]}
        self.negative_genome = {"fa":[], "gtf":[]}
        self.negative_tools = {"tools":"", "version":"", "params":""}
        self.temperature = {"low":"", "high":""}
        self.temperature_tools = {"tools":"", "version":"", "params":""}
        self.secondary_structure = {"low":"", "high":""}
        self.secondary_structure_tools = {"tools":"", "version":"", "params":""}
        self.location = {"fa":"", "gtf":""}
        self.date = ""
        self.author = ""
        self.email = ""
        self.other_info = ""
        self.data = pd.DataFrame()
    

    def tsv_read(self, header, data):

        with open(header, "r") as fh:
            for line in fh:
                line_list = line.strip().split("\t")
                feature = line_list[0]
                value = line_list[1]
                len_value = len(value.split(";"))
                if feature == "type":
                    self.type = value
                elif feature == "target_genome":
                    if len_value > 0:
                        self.target_genome["fa"] = value.split(";")[0].split(",")
                    if len_value > 1:
                        self.target_genome["gtf"] = value.split(";")[1].split(",")
                elif feature == "negative_genome":
                    if len_value > 0:
                        self.negative_genome["fa"] = value.split(";")[0].split(",")
                    if len_value > 1:
                        self.negative_genome["gtf"] = value.split(";")[1].split(",")
                elif feature == "negative_tools":
                    if len_value > 0:
                        self.negative_tools["tools"] = value.split(";")[0]
                    if len_value > 1:
                        self.negative_tools["version"] = value.split(";")[1]
                    if len_value > 2:
                        self.negative_tools["params"] = value.split(";")[2]
                elif feature == "temperature":
                    if len_value > 0:
                        if value.split(";")[0]:
                            self.temperature["low"] = float(eval(value.split(";")[0]))
                    if len_value > 1:
                        self.temperature["high"] = float(eval(value.split(";")[1]))
                elif feature == "temperature_tools":
                    if len_value > 0:
                        self.temperature_tools["tools"] = value.split(";")[0]
                    if len_value > 1:
                        self.temperature_tools["version"] = value.split(";")[1]
                    if len_value > 2:
                        self.temperature_tools["params"] = value.split(";")[2]
                elif feature == "secondary_structure":
                    if len_value > 0:
                        if value.split(";")[0]:
                            self.secondary_structure["low"] = float(eval(value.split(";")[0]))
                    if len_value > 1:
                        self.secondary_structure["high"] = float(eval(value.split(";")[1]))
                elif feature == "secondary_structure_tools":
                    if len_value > 0:
                        self.secondary_structure_tools["tools"] = value.split(";")[0]
                    if len_value > 1:
                        self.secondary_structure_tools["version"] = value.split(";")[1]
                    if len_value > 2:
                        self.secondary_structure_tools["params"] = value.split(";")[2]
                elif feature == "location":
                    if len_value > 0:
                        self.location["fa"] = value.split(";")[0]
                    if len_value > 1:
                        self.location["gtf"] = value.split(";")[1]
                elif feature == "date":
                    self.date = value
                elif feature == "author":
                    self.author = value
                elif feature == "email":
                    self.email = value
                elif feature == "other_info":
                    self.other_info = value
                else:
                    print(f"no {feature} in oligo format!")
        
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
                    elif feature == "target_genome":
                        if len_value > 0:
                            self.target_genome["fa"] = value.split(";")[0].split(",")
                        if len_value > 1:
                            self.target_genome["gtf"] = value.split(";")[1].split(",")
                    elif feature == "negative_genome":
                        if len_value > 0:
                            self.negative_genome["fa"] = value.split(";")[0].split(",")
                        if len_value > 1:
                            self.negative_genome["gtf"] = value.split(";")[1].split(",")
                    elif feature == "negative_tools":
                        if len_value > 0:
                            self.negative_tools["tools"] = value.split(";")[0]
                        if len_value > 1:
                            self.negative_tools["version"] = value.split(";")[1]
                        if len_value > 2:
                            self.negative_tools["params"] = value.split(";")[2]
                    elif feature == "temperature":
                        if len_value > 0:
                            if value.split(";")[0]:
                                self.temperature["low"] = float(eval(value.split(";")[0]))
                        if len_value > 1:
                            self.temperature["high"] = float(eval(value.split(";")[1]))
                    elif feature == "temperature_tools":
                        if len_value > 0:
                            self.temperature_tools["tools"] = value.split(";")[0]
                        if len_value > 1:
                            self.temperature_tools["version"] = value.split(";")[1]
                        if len_value > 2:
                            self.temperature_tools["params"] = value.split(";")[2]
                    elif feature == "secondary_structure":
                        if len_value > 0:
                            if value.split(";")[0]:
                                self.secondary_structure["low"] = float(eval(value.split(";")[0]))
                        if len_value > 1:
                            self.secondary_structure["high"] = float(eval(value.split(";")[1]))
                    elif feature == "secondary_structure_tools":
                        if len_value > 0:
                            self.secondary_structure_tools["tools"] = value.split(";")[0]
                        if len_value > 1:
                            self.secondary_structure_tools["version"] = value.split(";")[1]
                        if len_value > 2:
                            self.secondary_structure_tools["params"] = value.split(";")[2]
                    elif feature == "location":
                        if len_value > 0:
                            self.location["fa"] = value.split(";")[0]
                        if len_value > 1:
                            self.location["gtf"] = value.split(";")[1]
                    elif feature == "date":
                        self.date = value
                    elif feature == "author":
                        self.author = value
                    elif feature == "email":
                        self.email = value
                    elif feature == "other_info":
                        self.other_info = value
                    else:
                        print(f"no {feature} in oligo format!")
                else:
                    break
        
        self.data = pd.read_csv(oligo_file, sep="\t", comment='#')


        return


    def to_oligo(self, name=None, out_dir="./"):
        
        if name:
            file_name = name
        else:
            file_name = self.name
        
        with open(f"{out_dir}/{file_name}.oligo", "w") as f:
            if self.type:
                f.write(f"#type\t{self.type}\n")
            if self.target_genome:
                str_w = ""
                if len(self.target_genome["fa"]) > 0:
                    str_w = str_w + ",".join(self.target_genome["fa"])
                if len(self.target_genome["gtf"]) > 0:
                    str_w = str_w + ";" + ",".join(self.target_genome["gtf"])
                f.write(f"#target_genome\t{str_w}\n")
            if self.negative_genome:
                str_w = ""
                if len(self.negative_genome["fa"]) > 0:
                    str_w = str_w + ",".join(self.negative_genome["fa"])
                if len(self.negative_genome["gtf"]) > 0:
                    str_w = str_w + ";" + ",".join(self.negative_genome["gtf"])
                f.write(f"#negative_genome\t{str_w}\n")
            if len(self.negative_tools) > 0:
                f.write("#negative_tools\t" + ";".join([self.negative_tools["tools"], self.negative_tools["version"], self.negative_tools["params"]]) + "\n")
            if len(self.temperature) > 0:
                low = str(self.temperature["low"])
                high = str(self.temperature["high"])
                f.write(f"#temperature\t{low};{high}\n")
            if len(self.temperature_tools) > 0:
                f.write("#temperature_tools\t" + ";".join([self.temperature_tools["tools"], self.temperature_tools["version"], self.temperature_tools["params"]]) + "\n")
            if len(self.secondary_structure) > 0:
                low = str(self.secondary_structure["low"])
                high = str(self.secondary_structure["high"])
                f.write(f"#secondary_structure\t{low};{high}\n")
            if len(self.secondary_structure_tools) > 0:
                f.write("#secondary_structure_tools\t" + ";".join([self.secondary_structure_tools["tools"], self.secondary_structure_tools["version"], self.secondary_structure_tools["params"]]) + "\n")
            if self.location:
                str_w = ""
                if len(self.location["fa"]) > 0:
                    str_w = str_w + self.location["fa"]
                if len(self.location["gtf"]) > 0:
                    str_w = str_w + ";" + self.location["gtf"]
                f.write(f"#location\t{str_w}\n")
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

        with h5py.File(f"{out_dir}/{file_name}.oligo5", "w") as f:
            
            if self.group:
                group_name = self.group
            else:
                group_name = f"G_{self.name}"
            group = f.create_group(group_name)
            dataset = group.create_dataset(self.name, data=self.data.astype("str").values)
            dataset.attrs["name"] = self.name
            dataset.attrs["type"] = self.type
            dataset.attrs["target_genome"] = json.dumps(self.target_genome)
            dataset.attrs["negative_genome"] = json.dumps(self.negative_genome)
            dataset.attrs["negative_tools"] = json.dumps(self.negative_tools)
            dataset.attrs["temperature"] = json.dumps(self.temperature)
            dataset.attrs["temperature_tools"] = json.dumps(self.temperature_tools)
            dataset.attrs["secondary_structure"] = json.dumps(self.secondary_structure)
            dataset.attrs["secondary_structure_tools"] = json.dumps(self.secondary_structure_tools)
            dataset.attrs["location"] = json.dumps(self.location)
            dataset.attrs["date"] = self.date
            dataset.attrs["author"] = self.author
            dataset.attrs["email"] = self.email
            dataset.attrs["other_info"] = self.other_info
            dataset.attrs["clomuns"] = json.dumps({col: str(dtype) for col, dtype in self.data.dtypes.items()})



class OLIGO5:
    """
    """
    def __init__(self, name):
        self.name = name
        self.group = []
        self.oligos = {}
    
    def to_oligo5(self, name=None, out_dir="./"):
        return
    
    def read(self, oligo5_file):
        return
    
    def read_oligos(self, ):
        return
    
    def read_oligof(self, ):
        return
