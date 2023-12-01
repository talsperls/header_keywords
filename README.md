
# TLS Certificate Scanner

Author: Tal Sperling

This code is to be used for educational purposes or legal penetration testing only.
I do not take responsibility for any misuse or illegal action/use of this code.

## Description

Scans a list of URLs from a text file and exports the headers along with if a given keyword was found in the header

## Use

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```


```bash
python cert_scan.py url_list.txt keyword
```

The app exports the data to an excel file therefore Microsoft Excel is needed to view the exported data