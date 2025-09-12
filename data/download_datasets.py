import os

#File originating from ExcapeDB, filtered for the SLC6A4 gene
csv_file = "SLC6A4_active_excape_export.csv"
if not os.path.exists(csv_file):
    import urllib.request
    url = "https://ndownloader.figshare.com/files/25747817"
    urllib.request.urlretrieve(url, csv_file)

# A logP data set from Zenodo
csv_file = "logP.csv"
if not os.path.exists(csv_file):
    import urllib.request
    url = "https://zenodo.org/records/14333718/files/logP.csv"
    urllib.request.urlretrieve(url, csv_file)

