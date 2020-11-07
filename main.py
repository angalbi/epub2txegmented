import os,sys,shutil
from glob import glob
import sys
import epub2txt as ep
from blingfire import text_to_sentences

DEST_DIR = "Output"


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

def epub2txt(path):

    book_num = 0
    err_num = 0

    dest_path = os.getcwd()+"/"+DEST_DIR

    # If the directory already exists, OVERWRITE
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    else:
        os.mkdir(os.getcwd() + "/" + DEST_DIR)

    #Check if we are parsing a file or a hole directory
    if os.path.isfile(os.getcwd()+"/"+path):
        print("Processing %s ..." % path, end=" ")
        try:
            ep.convert(os.getcwd()+"/"+path,os.getcwd() + "/" + DEST_DIR)
            print("OK")
        except:
            print("ERROR : %s " % path)
    else:
        for root, dirname, files in os.walk(path):
            for f in files:
                if f.endswith('.epub'):
                    print("Processing %s ..." % f, end = " ")
                    try:
                        ep.convert(os.path.join(root, f),os.getcwd() + "/" + DEST_DIR)
                        book_num += 1
                        print("OK")
                    except (KeyError, IOError):
                        print("ERROR : %s " % f)
                        err_num += 1

        print("\n\n|**   Books converted in txt: %d  ERRORS: %d   **|" % (book_num, err_num))

def sentece_segmentation():
    book_path = os.path.join(os.getcwd()+DEST_DIR, u'*.txt')

    file_list = list(sorted(glob(book_path)))

    for i, file_path in enumerate(file_list):
        sents, n_sent = convert_into_sentences(open(file_path).readlines())
        print('\n'.join(sents))
        print('\n\n\n\n')
        sys.stderr.write(
            '{}/{}\t{}\t{}\n'.format(i, len(file_list), n_sent, file_path))

def usage():
    print("USAGE: python epub_txegmented.py <epub_dir_path> | <epub_file_path>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(0)
    path = sys.argv[1]
    epub2txt(path)
    sentece_segmentation()






