import getopt
import os, shutil
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
def epub2txt(path,seg,output=DEST_DIR):

    book_num = 0
    err_num = 0

    dest_path = os.getcwd()+"/" + output

    # If the directory already exists, OVERWRITE
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    else:
        os.mkdir(dest_path)

    #Check if we are parsing a file or a hole directory
    if os.path.isfile(os.getcwd()+"/"+path):
        print("Processing %s ..." % path, end=" ")
        try:
            ep.convert(os.getcwd()+"/"+path,os.getcwd() + "/" + output)
            print("OK")
        except:
            print("ERROR : %s " % path)
    elif os.path.exists(os.getcwd()+"/"+path):
        # Transformation process for a hole directory
        # Find every file in epub format
        for root, dirname, files in os.walk(path):
            for f in files:
                if f.endswith('.epub'):
                    print("Processing %s ..." % f, end = " ")
                    try:
                        ep.convert(os.path.join(root, f),os.getcwd() + "/" + output)
                        book_num += 1
                        print("OK")
                    except (KeyError, IOError):
                        print("ERROR : %s " % f)
                        err_num += 1
    else:
        print("This directory does not exist.")
        exit(0)

        if seg:
            print("\n\n|**   CONVERTED: %d  SEGMENTED: %d  ERRORS: %d   **|" % (book_num, book_num, err_num))
        else:
            print("\n\n|**   CONVERTED: %d   ERRORS: %d   **|" % (book_num, err_num))


def usage():
    print("ERROR: bad usage")
    print("python epub_txegmented.py -i [<epub_dir_path> | <epub_file_path>] / -s / -o [output_dir]")

def main(argv):
    output = DEST_DIR
    segmentation = False
    input = ''
    try:
        opts, args = getopt.getopt(argv, "hi:so:", ["help", "input", "segmentation", "output"])
    except getopt.GetoptError:
        usage()
        sys.exit(0)
    for opt, arg in opts:
        if opt in ('-h','--help'):
            usage()
            sys.exit(0)
        elif opt in ('-i','--input'):
            input = arg
        elif opt in ('-s','--segmentation'):
            segmentation = True
        elif opt in ('-o','--output-dir'):
            output = arg
    if input == '':
        usage()
        exit(0)

    try:
        epub2txt(input, segmentation, output)
    except FileNotFoundError:
        print("This file or directory does not exist.")
    if segmentation:
        sentece_segmentation()



if __name__ == "__main__":
    main(sys.argv[1:])


