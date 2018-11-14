# Quick-cluster
Quick-cluster is a small script to cluster and display data from a contiguous table in a .xlsx file with agglomerative clustering and then embed that data into a three dimensional interactive plot using hypertools and openpyxl. This clustering and visualization serves as a compact method for visualizing high dimensional data, and can intuitively reveal relationships in the data that might be otherwise hidden.
## Getting Started
These instructions will show you how to get quick-cluster to run on your own data.
### Prerequisites
- openpyxl 2.5.10
- numpy >= 1.14.3
- hypertools 0.5.1
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

![alt text](https://i.imgur.com/Vp9KEms.png "t-SNE graph titled Figure 1")

and a copy of the input spreadsheet will appear in the "output" folder. This new spreadsheet will contain a new worksheet listing the names of the datapoints that were plotted next to their agglomerated cluster number listed in the legend of the graph, like so:

![alt text](https://i.imgur.com/Ux7LadC.png "Excel worksheet produced by sample.xlsx")

### Usage
1. Copy your xlsx file into the "input" folder int the quick-cluster directory

2. Run

```
python main.py --filename='your_filename.xlsx' --label_column=column_with_datapoint_names 
  --columns=number_of_columns --start_column=table_start --rows=number_of_rows --start_row=table_start
```

  * Note that rows are indexed as integers, not letters as in Excel, and that both column and row indices begin at 1, not 0.

  * Something like `python main.py --filename='spreadsheet.xlsx'--columns=10 --rows=559` will produce a graph of points plotted from "spreadsheet.xlsx" columns B-K and rows 2-560 labeled by their value in column A.
  * The output worksheet will show that the names in its column B belong to the group in column A according to the agglomerative cluster.
  * We begin reading from row 2 and column B by default to avoid reading labels and attributes as data.

3. Run `python main.py --help` for a list of possible arguments. Currently, the default on all arguments will read in the first 1000 rows of the sample.xlsx file.
