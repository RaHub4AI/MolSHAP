import os
import pathlib
import pandas as pd
from rdkit.Chem import PandasTools
from rdkit import RDLogger
import numpy as np


this_script_dir = os.path.dirname(os.path.abspath(__file__))


def get_slc6a4_df():
    csv_file = pathlib.Path(f"{this_script_dir}/ressources/SLC6A4_active_excape_export.csv")
    if not os.path.exists(csv_file):
        import urllib.request
        url = "https://ndownloader.figshare.com/files/25747817"
        urllib.request.urlretrieve(url, csv_file)

    df = pd.read_csv(csv_file)

    df.rename(columns={"pXC50":"target"}, inplace=True)

    np.random.seed(0xFACE)
    df["subset"] = "Train"
    val_mask = np.random.random(len(df)) < 0.25
    df.loc[val_mask, "subset"] = "Validation"
    blind_mask = np.random.random(len(df)) < 0.05
    df.loc[blind_mask, "subset"] = "Blind"
    #Remove invalids
    RDLogger.DisableLog("rdApp.*")
    PandasTools.AddMoleculeColumnToFrame(df, smilesCol="SMILES")
    RDLogger.EnableLog("rdApp.*")
    df = df[~df.ROMol.isna()]

    df.reset_index(inplace=True)

    return df[["SMILES","target","subset","ROMol"]]


def get_logp_df():
    csv_file = pathlib.Path(f"{this_script_dir}/ressources/logP.csv")
    if not os.path.exists(csv_file):
        import urllib.request
        url = "https://zenodo.org/records/14333718/files/logP.csv"
        urllib.request.urlretrieve(url, csv_file)

    df = pd.read_csv(csv_file)
    #column Standardization and check of SMILES validity
    df.rename(columns={"logP": "target", "Subset":"subset"}, inplace=True)
    RDLogger.DisableLog("rdApp.*")
    PandasTools.AddMoleculeColumnToFrame(df, smilesCol="SMILES")
    RDLogger.EnableLog("rdApp.*")
    df = df[~df.ROMol.isna()]
    df.reset_index(inplace=True)
    return df[["SMILES","target","subset","ROMol"]]


if __name__ == "__main__":
    #print("SLC6A4 dataset")
    #df = get_slc6a4_df()
    print("LogP dataset")
    df = get_logp_df()
    print(df.columns)
    print(len(df))
    #print(get_logp_df().head())
