# -*- coding: utf-8 -*-
import os
import glob
import zipfile
from xml.etree import ElementTree
import pandas as pd

class xml_stats_engine:

    root_folder = "./test-lams-community-scripts/"
    extract_root = "./extract-lams-community-scripts/"
    zip_files = list()
    zip_contents = list()
    extract_files = list()
    toUIID = list()
    fromUIID = list()
    activityTitle = list()
    activityUIID = list()
    transitions = list()
    tool = list()
    list_transitions = list()
    activities = dict()
    stats = list()

    df = pd.DataFrame(columns=['from','to','frequency'])

    def __init__(self):
        self.get_zip()
        self.unzip_files()
        self.parse_xml()
        self.display_stats()
        self.df = self.df.sort_values(by=['frequency'])
        self.df.to_csv('stats.csv',index=False)


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
            tree = ElementTree.parse(file_path)
            root = tree.getroot()

            for activity_uiid in root.iter('activityUIID'):
                self.activityUIID.append(activity_uiid.text)

            for to_uiid in root.iter('toUIID'):
                self.toUIID.append(to_uiid.text)

            for from_uiid in root.iter('fromUIID'):
                self.fromUIID.append(from_uiid.text)

            for activity_title in root.iter('activityTitle'):
                self.activityTitle.append(activity_title.text)

            for tool_name in root.iter('toolDisplayName'):
                self.tool.append(tool_name.text)
                        
            for i in range(0,len(self.activityTitle)):
                try:
                    self.activities[self.activityUIID[i]] = self.tool[i]
                except:
                    pass

            for i in range(0,len(self.toUIID)):
                try:
                    node1 = self.activities[self.fromUIID[i]]
                    node2 = self.activities[self.toUIID[i]]
                    temp = [node1,node2]
                    self.transitions.append(temp)
                except:
                    pass

            for t in self.transitions:
                if t not in self.list_transitions:
                    # element = self.transitions[t][0] + "->" + self.transitions[t][1]
                    self.list_transitions.append(t)
        
            os.system("rm -rf {}{}".format(self.extract_root,file))

    def display_stats(self):
        for stat in self.list_transitions:
            trans = stat[0]," -> ",stat[1]
            element = [''.join(trans), self.transitions.count(stat)]
            self.stats.append(element)
            self.df = self.df.append({'from':stat[0],'to':stat[1],'frequency':self.transitions.count(stat)},ignore_index=True)
        
        max_l = 0

        for s in self.stats:
            if(len(s[0])>max_l):
                max_l = len(s[0])
        
        print("\nTransition"," " * (max_l-len("Transition")),"Frequency")
        print("*"*max_l,"","*"*len("Frequency"))

        self.stats.sort(key=lambda x: x[1], reverse=True)

        for stat in self.stats:
            print(stat[0], " " * (max_l-len(stat[0])), stat[1])
            

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
