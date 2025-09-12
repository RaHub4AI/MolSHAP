import os
import pathlib
import pandas as pd
from rdkit.Chem import PandasTools
from rdkit import RDLogger


this_script_dir = os.path.dirname(os.path.abspath(__file__))


def get_slc6a4_df():
    csv_file = pathlib.Path(f"{this_script_dir}/ressources/SLC6A4_active_excape_export.csv")
    if not os.path.exists(csv_file):
        import urllib.request
        url = "https://ndownloader.figshare.com/files/25747817"
        urllib.request.urlretrieve(url, csv_file)

    df = pd.read_csv(csv_file)
    return df


def get_logp_df():
    csv_file = pathlib.Path(f"{this_script_dir}/ressources/logP.csv")
    if not os.path.exists(csv_file):
        import urllib.request
        url = "https://zenodo.org/records/14333718/files/logP.csv"
        urllib.request.urlretrieve(url, csv_file)

    df = pd.read_csv(csv_file)
    #column Standardization and check of SMILES validity
    df.rename(columns={"logP": "target", "Subset":"subset"}, inplace=True)
    df = df[["SMILES","target", "subset"]]
    RDLogger.DisableLog("rdApp.*")
    PandasTools.AddMoleculeColumnToFrame(df, smilesCol="SMILES")
    RDLogger.EnableLog("rdApp.*")
    df = df[~df.ROMol.isna()]

    return df


if __name__ == "__main__":
    #print(get_slc6a4_df().head())
    print(get_logp_df().head())
