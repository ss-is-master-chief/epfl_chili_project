import os
import glob
import zipfile
from xml.etree import ElementTree

file = "./extract-lams-community-scripts/Mindmap_Looping/learning_design.xml"

tree = ElementTree.parse(file)
root = tree.getroot()

toUIID = list()
fromUIID = list()
activityTitle = list()
activityUIID = list()
transitions = list()
activities = dict()

for activity_uiid in root.iter('activityUIID'):
    activityUIID.append(activity_uiid.text)

for to_uiid in root.iter('toUIID'):
    toUIID.append(to_uiid.text)

for from_uiid in root.iter('fromUIID'):
    fromUIID.append(from_uiid.text)

for activity_title in root.iter('activityTitle'):
    activityTitle.append(activity_title.text)

for i in range(0,len(activityTitle)):
    activities[activityUIID[i]] = activityTitle[i]

# print("toUIID\n",toUIID)
# print("fromUIID\n",fromUIID)
# print("acitivityUIID\n",activityUIID)
# print("activityTitle\n",activityTitle)
# print(activities)

for i in range(0,len(toUIID)):
    node1 = activities[fromUIID[i]]
    node2 = activities[toUIID[i]]
    temp = [node1,node2]
    transitions.append(temp)

print(transitions)

# for activity in root.findall("activities"):
#     origin = "org.lamsfoundation.lams.learningdesign.dto.AuthoringActivityDTO"
#     for thread in activity.findall(origin):
#         print(thread)
    #     if(thread.tag=="activityTitle"):
    #         print(thread.tag)
    # if(child.tag=="activities"):
    #     for c in child:
    #         print(c.tag)
    # print(activity)
# activities = root.findall("activities")
# org = activities.findall("org.lamsfoundation.lams.learningdesign.dto.AuthoringActivityDTO")
# uiid = org.findall("activityUIID")
# print(uiid.text)
