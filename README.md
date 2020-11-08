# epub2txegmented
This script aims to extract the information of epub format files and represent it as plain text, prodiving an eassy usage and structure.

Both directories and files could be treated; in directories case, the script will find all the .epub files in the specified directory in order to process them. Otherwise, single file also are accepted. All the information will be stored in a destination directory.

Additionally, it contains the option to make a sentece segmentation of the extracted information. The functionality will read all the plain text files from the output directory and overwrite them with the segmentation structure.

## Let's start 🚀

_Apart from the code, a small free epub books directory is provided to make the first tries._



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

## Usage ⚙️

_All the result of the function will be stored in a directory. This directory could be specified with '-o Output_dir' parameter. Otherwise, default name 'Output' will be taken. These are the three types of usage of this script:_

### Extracting a single epub file information 📖

```
python epub2txegmented.py -i /path/to/book.epub -o Output_direcory
```

### Extracting information from epub books directories :file_folder:📖

_The specified directory could contain other type of file, the script will only treat the epub format files._

```
python main.py -i /path/to/epub_directory 
```

## Make sentece segmentation :page_facing_up: 

_We can format the extracted information and make a sentece segmentation. Just add -s argument._

```
python main.py -i /path/to/epub_directory -s 
```



