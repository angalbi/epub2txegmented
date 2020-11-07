import os,sys,shutil
from glob import glob
import sys
import epub2txt as ep
from blingfire import text_to_sentences

# Define the destination folder to store the resulting txt files
DEST_DIR = "Output"

# Function to make the sentence segmentation of a plain text file.
def convert_into_sentences(lines):
    stack = []
    sent_L = []
    n_sent = 0
    text = ''
    for chunk in lines:
        if not chunk.strip():
            if stack:
                sents = text_to_sentences(text.join(stack).strip().replace('\n', ' ')).split('\n')
                sent_L.extend(sents)
                n_sent += len(sents)
                sent_L.append('\n')
                stack = []
            continue
        stack.append(chunk.strip())

    if stack:
        sents = text_to_sentences(
            text.join(stack).strip().replace('\n', ' ')).split('\n')
        sent_L.extend(sents)
        n_sent += len(sents)
    return sent_L, n_sent

# Make the segmentation of the text and write in the same file.
def sentece_segmentation():
    book_path = os.path.join(os.getcwd()+DEST_DIR, u'*.txt')

    file_list = list(sorted(glob(book_path)))

    for i, file_path in enumerate(file_list):
        sents, n_sent = convert_into_sentences(open(file_path).readlines())
        print('\n'.join(sents))
        print('\n\n\n\n')
        sys.stderr.write(
            '{}/{}\t{}\t{}\n'.format(i, len(file_list), n_sent, file_path))

# Function to extract info from epub files and store as plain text in txt files.
def epub2txt(path):
    # Initialize the book and error counters
    book_num = 0
    err_num = 0
    
    # Complete destination directory path
    dest_path = os.getcwd()+"/"+DEST_DIR

    # If the directory already exists, OVERWRITE
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    else:
        os.mkdir(os.getcwd() + "/" + DEST_DIR)

    #Check if we are parsing a file or a hole directory
    if os.path.isfile(os.getcwd()+"/"+path):
        # Transformation process for a single file
        print("Processing %s ..." % path, end=" ")
        try:
            ep.convert(os.getcwd()+"/"+path,os.getcwd() + "/" + DEST_DIR)
            print("OK")
        except:
            print("ERROR : %s " % path)
    else:
        # Transformation process for a hole directory
        # Find every file in epub format
        for root, dirname, files in os.walk(path):
            for f in files:
                if f.endswith('.epub'):
                    print("Processing %s ..." % f, end = " ")
                    # Error control
                    try:
                        ep.convert(os.path.join(root, f),os.getcwd() + "/" + DEST_DIR)
                        book_num += 1
                        print("OK")
                    except (KeyError, IOError):
                        print("ERROR : %s " % f)
                        err_num += 1

        print("\n\n|**   Books converted in txt: %d  ERRORS: %d   **|" % (book_num, err_num))
        
def usage():
    print("USAGE: python epub_txegmented.py <epub_dir_path> | <epub_file_path>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(0)
    path = sys.argv[1]
    # A folder will be created with the files containing the extracted information
    epub2txt(path)
    # This function will make the segmentation of all the files in DEST_DIR and overwrite the files
    sentece_segmentation()






