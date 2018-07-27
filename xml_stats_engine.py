# -*- coding: utf-8 -*-
import os
import glob
import zipfile
from xml.etree import ElementTree
import pandas as pd
import shutil
import sys

class xml_stats_engine:

    root_folder = "./test-lams-community-scripts/"
    extract_root = "./extract-lams-community-scripts/"
    # root_folder = sys.argv[1]
    # extract_root = sys.argv[2]
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
    graph_length = pd.DataFrame(columns=['script','length'])
    node_freq = pd.DataFrame(columns=['node_name','frequency'])

    def __init__(self):
        self.get_zip()
        self.unzip_files()
        self.parse_xml()
        self.display_stats()
        self.df = self.df.sort_values(by=['frequency'],ascending=False)
        self.df.to_csv('stats.csv',index=False)
        self.graph_length = self.graph_length.sort_values(by=['length'],ascending=False)
        self.graph_length.to_csv('graph_length.csv',index=False)
        self.node_freq = self.node_freq.sort_values(by=['frequency'],ascending=False)
        self.node_freq.to_csv('node_frequency.csv',index=False)


    def get_zip(self):
        for path, _, files in os.walk(self.root_folder):
            for file in files:
                if(file[-3:]=="zip"):
                    self.zip_files.append(os.path.abspath(os.path.join(path,file)))


    def unzip_files(self):
        for file in self.zip_files:
            try:
                print("UNZIPPING > {}".format(file))
                zip_ref = zipfile.ZipFile(file, 'r')
                file_name = os.path.basename(file).rstrip(".zip")
                zip_ref.extractall("{}/{}/".format(os.path.abspath(self.extract_root),file_name))
                zip_ref.close()
                self.extract_files.append(file_name)
            except:
                pass


    def parse_xml(self):
        length = 0

        for file in self.extract_files:
            try:
                file_path = self.extract_root + '{}/learning_design.xml'.format(file)
                
                tree = ElementTree.parse(file_path)
                root = tree.getroot()

                for activity_uiid in root.iter('activityUIID'):
                    self.activityUIID.append(activity_uiid.text)

                length = len(self.activityUIID) - length
                print("READING  >",os.path.abspath(file_path))
                print("LENGTH   >",length)

                self.graph_length = self.graph_length.append({'script':file,'length':length},ignore_index=True)

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
                        self.list_transitions.append(t)

                del_file = os.path.abspath(self.extract_root) + "/" + file
                shutil.rmtree(del_file)

            except:
                pass


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

        for t in self.tool:
            if(len(t)>max_l):
                max_l = len(t)
        
        print("\nNode"," " * (max_l-len("Node")),"Frequency")
        print("*"*max_l,"","*"*len("Frequency"))

        self.tool.sort(key=lambda x: x[1], reverse=True)

        for t in list(set(self.tool)):
            self.node_freq = self.node_freq.append({'node_name': t,'frequency':self.tool.count(t)},ignore_index=True)
            print(t, " " * (max_l-len(t)), self.tool.count(t))
            

if __name__ == "__main__":
    obj = xml_stats_engine()
