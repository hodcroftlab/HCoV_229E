import pandas as pd
import os
import argparse
from Bio import SeqIO


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile1', required=True, help='First TSV input file')
    parser.add_argument('--inputfile2', required=True, help='Excel with unpublished metadata')
    parser.add_argument('--inputfile3', required=True, help='Excel with published clades')
    parser.add_argument('--inputfile4', required=True, help='Excel with updated dates')
    parser.add_argument('--outputfile',  required=True, help='Merged output file')
    
    return parser.parse_args()


def merge_tsv(inputfile1, inputfile2, inputfile3, inputfile4,outputfile):
    df1 = pd.read_csv(inputfile1, sep="\t",dtype=str)
    df2 = pd.read_excel(inputfile2,dtype=str)
    df2["date"] = pd.to_datetime(df2["date"], errors="coerce").dt.strftime("%Y-%m-%d")
    
    df3 = pd.read_excel(inputfile3)
    df4 = pd.read_excel(inputfile4)
    
    merged12 = pd.merge(df1, df2, on=["accession", "country", "date", "region", "host"], how="outer")
    merged123 = pd.merge(merged12, df3, on=["accession"], how="outer")
    merged123.set_index('accession', inplace=True)
    df4.set_index('accession', inplace=True)
    merged123.update(df4)
    # merged123["date"] = pd.to_datetime(merged123["date"], errors="coerce")

    merged123["clade"] = merged123["clade"].astype(str)  
    
    merged123.to_csv(outputfile, sep="\t", index=True)





if __name__ == "__main__":
    args = parse_args()
    merge_tsv(args.inputfile1, args.inputfile2, args.inputfile3, args.inputfile4,args.outputfile)