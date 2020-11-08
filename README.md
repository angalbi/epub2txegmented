# epub2txegmented
This script aims to extract the information of epub format files and represent it as plain text, prodiving an eassy usage and structure.

Both directories and files could be treated with this script; in directories case, the script will find all the .epub files in the specified directory in order to process them. Otherwise, single files also are accepted. All the information will be stored in a destination directory.

Additionally, the option to make a sentece segmentation of the extracted information is algo given. All the plain text files will be read from the output directory and overwrite them with the segmentation structure.

## Let's start 🚀



### Requirements 📋

In order to run properly this script the following software and packages are needed:

* Python 2.x or Python 3.x
* html2text
* numpy
* blingfire


### Installation 🔧

If Python is not installed [here](https://github.com/purcellconsult/Python-Installation-Tutorial) you have a great tutorial to do it.

Installing requierements:

```
pip install -r requirements.txt
```

Get the code downloading the ZIP file or cloning the proyect:
```
git clone https://github.com/angalbi/epub2txegmented.git
```

## Usage ⚙️

_All the result of the function will be stored in a directory. This directory could be specified with '-o Output_dir' parameter. Otherwise, default name 'Output' will be taken. These are the three types of usage of this script:_

### Extracting a single epub file information 📖

```
python main.py -i /path/to/book.epub -o Output_direcory
```

### Extracting information from epub books directories :file_folder:📖

_The specified directory could contain other type of file, the script will only treat the epub format files._

```
python main.py -i /path/to/epub_directory 
```

### Make sentece segmentation :page_facing_up: 

_We can format the extracted information and make a sentece segmentation. Just add -s argument._

```
python main.py -i /path/to/epub_directory -s 
```



