from xml.dom import minidom

import re
import os
import sys
import glob


def prettier(content):
    return minidom.parseString(content).toprettyxml(indent="\t")


def linearize(content):
    content = content.replace("\n", "").replace("\t", "").replace("  ", " ")
    content = re.sub(" *< *", "<", content)
    content = re.sub(" *> *", ">", content)
    return content


def read(path):
    with open(path) as f:
        return f.read()


def write(path, content):
    with open(path, "w") as f:
        f.write(content)


def format(from_path, to_path):
    content = linearize(read(from_path))
    xml = prettier(content)
    write(to_path, xml)


def list_files(path, extension):
    return glob.glob(path + "/*." + extension)


def process(from_path, from_extension):
    if os.path.isdir(from_path):
        files = list_files(from_path, from_extension)
        for path in files:
            format(path, path)


if __name__ == "__main__":
    from_path = sys.argv[1]
    from_extension = sys.argv[2]
    process(from_path, from_extension)
