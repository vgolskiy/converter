import sys
import os.path
import pandas as pd


def convert_file_to_tml(path, filename, extension):
    if extension == '.csv':
        try:
            data = pd.read_csv(path, encoding="ISO-8859-1", dtype=object, keep_default_na=False)
        except:
            print("Unsupported file encoding", file=sys.stderr)
            return
    elif extension == '.prn':
        try:
            data = pd.read_fwf(path, encoding="ISO-8859-1", dtype=object, keep_default_na=False)
        except:
            print("Unsupported file encoding", file=sys.stderr)
            return
    else:
        print("Wrong file type: .csv or .prn are accepted only")
        return
    data.to_html(filename + ".html")
    print("Converted to HTML: " + filename + ".html was created")
    return


def main(argv):
    path = argv[0]
    if not os.path.isfile(path):
        print("Wrong file path provided", file=sys.stderr)
    else:
        filename, extension = os.path.splitext(path)
        convert_file_to_tml(path, filename, extension)


if __name__ == "__main__":
    main(sys.argv[1:])
