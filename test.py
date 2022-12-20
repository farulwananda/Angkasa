import glob
import os

list_of_files = glob.glob('static/uploads/*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
