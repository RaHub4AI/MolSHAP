import os

#File originating from ExcapeDB, filtered for the SLC6A4 gene
csv_file = "SLC6A4_active_excape_export.csv"
if not os.path.exists(csv_file):
    import urllib.request
    url = "https://ndownloader.figshare.com/files/25747817"
    urllib.request.urlretrieve(url, csv_file)

