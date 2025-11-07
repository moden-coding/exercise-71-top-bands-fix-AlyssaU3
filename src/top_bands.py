#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df= pd.read_csv("src/bands.tsv", sep=("\t"))
    records= pd.read_csv("src/UK-top40-1964-1-2.tsv", sep=("\t"))
    df["Band"]=df["Band"].str.upper() 
    merged= pd.merge(df,records, left_on=("Band"), right_on=("Artist"), how="outer")
    merged=merged.dropna()
    return merged
def main():
    print(top_bands())

if __name__ == "__main__":
    main()
