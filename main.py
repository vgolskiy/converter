import sys
import os.path
import pandas as pd

def read_file_to_table(path, filename, extension):
    if extension == '.csv':
        try:
            data = pd.read_csv(path, encoding="ISO-8859-1")
        except:
            print("Unsupported file encoding", file=sys.stderr)
            return
    elif extension == '.prn':
        try:
            data = pd.read_fwf(path, encoding="ISO-8859-1")
        except:
            print("Unsupported file encoding", file=sys.stderr)
            return
    else:
        print("Wrong file type: .csv or .prn are accepted only")
        return
    data.to_html(filename + ".html")
    print("Converted to HTML: " + filename + ".html was created")
    return

# path = sys.argv[1]
path = "dat.csv"
if not os.path.isfile(path):
    print("Wrong file path provided", file=sys.stderr)
else:
    filename, extension = os.path.splitext(path)
    read_file_to_table(path, filename, extension)
