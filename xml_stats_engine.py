import os
import glob
import zipfile
from xml.etree import ElementTree

class xml_stats_engine:

    root_folder = "./test-lams-community-scripts/"
    extract_root = "./extract-lams-community-scripts/"
    zip_files = list()
    zip_contents = list()
    extract_files = list()

    def __init__(self):
        self.get_zip()
        self.unzip_files()
        self.parse_xml()

    def get_zip(self):
        for file in glob.glob(self.root_folder + "*.zip"):
            self.zip_files.append(os.path.abspath(file))

    def unzip_files(self):
        for file in self.zip_files:
            zip_ref = zipfile.ZipFile(file, 'r')
            file_name = os.path.basename(file).rstrip(".zip")
            zip_ref.extractall("./extract-lams-community-scripts/{}/".format(file_name))
            zip_ref.close()
            self.extract_files.append(file_name)

    def parse_xml(self):
        for file in self.extract_files:
            file_path = self.extract_root + '{}/learning_design.xml'.format(file)
            # print(os.path.abspath(file_name))
            dom = ElementTree.parse(file_path)
            title = dom.findall('title')
            for t in title:
                print(t.text)



if __name__ == "__main__":
    obj = xml_stats_engine()

# file_name = 'GettingStarted/EMBEDDING/learning_design.xml'
# file_path = os.path.abspath(os.path.join('lams-community-scripts',file_name))
# print(file_path)

# dom = ElementTree.parse(file_path)
# title = dom.findall('title')
#
# for t in title:
#     print(t.text)
