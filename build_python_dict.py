import csv
import datetime

FILE = 'results\\full-list.csv'
TARGET_FILE = "dictionary.py"


def build_python_dict(lines):
    hdr = f"""
    # Automatically generated file on date {datetime.datetime.now()} by snomedsrt2sct

    # sample usage:
    # ...

    # SNOMED Fully Specified Name

    dictionary = [
    """
    with open(TARGET_FILE, "w") as out_file:
        out_file.write(hdr)
        for line in lines:
            line['Name'] = line["SNOMED Fully Specified Name"]
            out_file.write(' {{ "SRT": "{SRT}", "SCT": "{SCT}", "SNOMED Fully Specified Name": "{Name}"}} ,\n'.format(**line))
        out_file.write("]")
    pass

lines = []
with open(FILE, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        lines.append(line)
    build_python_dict(lines)
