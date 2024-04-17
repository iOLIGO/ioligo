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
    

    def to_oligo(self, name=None, out_dir="./"):

        if name:
            file_name = name
        else:
            file_name = self.name

        with h5py.File(f"{out_dir}/{file_name}.oligo", "w") as f:
            
            group = f.create_group(self.name)

            group.attrs["name"] = self.name
            group.attrs["type"] = self.type
            group.attrs["target_genome"] = json.dumps(self.target_genome)
            group.attrs["negative_genome"] = json.dumps(self.negative_genome)
            group.attrs["negative_tools"] = json.dumps(self.negative_tools)
            group.attrs["temperature"] = json.dumps(self.temperature)
            group.attrs["temperature_tools"] = json.dumps(self.temperature_tools)
            group.attrs["secondary_structure"] = json.dumps(self.secondary_structure)
            group.attrs["secondary_structure_tools"] = json.dumps(self.secondary_structure_tools)
            group.attrs["location"] = json.dumps(self.location)
            group.attrs["date"] = self.date
            group.attrs["author"] = self.author
            group.attrs["email"] = self.email
            group.attrs["other_info"] = self.other_info

            if "name" in list(self.data.columns):
                np_names = np.array(self.data["name"])
            else:
                np_names = np.zeros((self.data.sahpe[0], 1))
            dataset_name = group.create_dataset("name", data=np_names)

            if "chr" in list(self.data.columns):
                np_chr = np.array(self.data["chr"])
            else:
                np_chr = np.zeros((self.data.sahpe[0], 1))
            dataset_chr = group.create_dataset("chr", data=np_chr)

            if "oligo" in list(self.data.columns):
                if self.type == "DNA":
                    list_oligo = list(self.data["oligo"])
                    encoded_oligo = [DNA(seq).values for seq in list_oligo]
                    oligo_array = np.vstack(encoded_oligo)
                elif self.type == "RNA":
                    list_oligo = list(self.data["oligo"])
                    encoded_oligo = [RNA(seq).values for seq in list_oligo]
                    oligo_array = np.vstack(encoded_oligo)
                else:
                    oligo_array = np.zeros((self.data.sahpe[0], 1))
            else:
                oligo_array = np.zeros((self.data.sahpe[0], 1))
            dataset_oligo = group.create_dataset("oligo", data=oligo_array)
            


        return

