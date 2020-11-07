# epub2txegmented
This script aims to extract the information of epub format files and represent it as plain text, prodiving an eassy usage and structure.

Both directories and files could be treated; in directories case, the script will find all the .epub files in the specified directory in order to process them. Otherwise, single file also are accepted. All the information will be stored in a destination directory.

Additionally, it contains the option to make a sentece segmentation of the extracted information. The functionality will read all the plain text files from the output directory and overwrite them with the segmentation structure.

## Let's start 🚀

_Apart from the a small epub books directory is provided to make the first tries._



### Requirements 📋

In order to run properly this script the following software and package are needed:

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

_These are the three types of usage of this script:_

### Extracting a single epub file information 📖

```
python main.py /path/to/book.epub
```

### Extracting information from epub books directories 📖📖📖

_The specified directory could contain other type of file, the script will only treat the epub format files._

```
python main.py /path/to/epub_directory 
```

## Make sentece segmentation 📦

_We can format the extracted information and make a sentece segmentation. Just add -s argument._

```
python main.py -s /path/to/epub_directory
```

## Used tools 🛠️

_This are the tools used to develop this script._

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS



## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

