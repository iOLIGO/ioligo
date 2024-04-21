from oligo import OLIGO, OLIGO5
import argparse

def main():
    argparser_oligo = argparse.ArgumentParser(description="oligo file to OLIGO5 format, or oligo5 file to oligo format")
    argparser_oligo.add_argument("-ft", "--format_type",choices=['OstoO5', 'O5toOs'], dest="ft",
                            help="file in format: ")
    argparser_oligo.add_argument("-o", "--oligo", default=None, dest="oligo",
                            help="oligo file")
    argparser_oligo.add_argument("-n5", "--oligo5_name", default="sample", dest="oligo5_name",
                            help="oligo5 name")
    argparser_oligo.add_argument("-od", "--oligos_dir", default=None, dest="oligos_dir",
                            help="the dir of oligos file")
    argparser_oligo.add_argument("-ot", "--out_dir", default="./", dest="out_dir",
                            help="out dir")
    argparser_oligo.add_argument("-o5", "--oligo5", default=None, dest="oligo5",
                            help="oligo5 file")
    args = argparser_oligo.parse_args()
    
    ft = args.ft 
    oligo_file = args.oligo
    oligo5_name = args.oligo5_name
    oligos_dir = args.oligos_dir
    oligo5_file = args.oligo5
    out_dir = args.out_dir

    if ft == "OstoO5":
        if oligo_file:
            oligo = OLIGO()
            oligo.read(oligo_file)
            oligo.to_oligo5(oligo.name, out_dir)
        elif oligos_dir:
            oligo5 = OLIGO5(oligo5_name)
            oligo5.read_doligo(oligos_dir)
            oligo5.to_oligo5(oligo5_name, out_dir)
        else:
            raise ValueError("please check params of oligo or oligo_dir!")
    elif ft == "O5toOs":
        if oligo5_file:
            oligo5 = OLIGO5()
            oligo5.read(oligo5_file)
            oligo5.to_oligo(out_dir)
        else:
            raise ValueError("please check params of oligo5")

    return