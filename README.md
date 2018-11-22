# Quick-cluster
Quick-cluster is a tool for visualizing high dimensional data from a .xlsx file using hypertools and openpyxl. The data are grouped using agglomerative clustering and then plotted into a three dimensional interactive graph using t-SNE. This clustering and visualization serves as a compact method for visualizing high dimensional data, and can intuitively reveal relationships in the data that might be otherwise hidden.
## Getting Started
These instructions will show you how to get quick-cluster to run on your own data.
### Prerequisites
- openpyxl 2.5.10
- numpy >= 1.14.3
- hypertools 0.5.1
- PyQt5 5.11.3
### Installation
Clone this repo
```
git clone https://github.com/blakemoya/quick-cluster
cd quick-cluster
```
Test with
```
python main.py
```
A graph similar to this should appear:

![alt text](http://i.imgur.com/nuYKkyd.jpg "t-SNE graph titled Figure 1")

and a copy of the input spreadsheet will appear in the "output" folder. This new spreadsheet will contain a new worksheet listing the names of the datapoints that were plotted undeir their assigned agglomerative label (where '0' in the legend of the graph corresponds to 'A' in the spreadhseet), like so:

![alt text](http://i.imgur.com/jHyUtUU.jpg "Excel worksheet produced by sample.xlsx")

### Usage
1. Navigate to your quick-cluster directory in command prompt 

2. Run `python dialog.py` and a dialog like this will appear

![alt text](https://i.imgur.com/ctQOMcn.png "Quick-cluster dialog")

3. Click "Select File" and navigate to your spreadsheet. Then select you label column, the column and row range you would like to cluster and reduce, and thenumber of clusters you'd like to separate your data into. Then click OK.

4. Wait for the plot to show up. Will take a long time for larger files.
