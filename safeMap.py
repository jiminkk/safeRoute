import pandas as pd
import numpy as np
import simplejson, urllib



rqstURL = "https://maps.googleapis.com/maps/api/directions/json?origin=eWestwood,CA&alternatives=true&destination=Hollywood,CA&key=AIzaSyCQ7a-qMPRtVz5mS4XOs2MgcB13JxQVvYk"
testURL2 =
# r = pd.read_json(rqstURL)

r = simplejson.load(urllib.urlopen(rqstURL))


coordPairs2 = np.array((200,200))

'''
def parseRoute(r):
    coordPairs = [np.array((200, 200))]*len(r["routes"])
    for singlePair in coordPairs:
        for idx, x in enumerate(r["routes"][0]["legs"][0]["steps"]):
            coordPairs = np.vstack((coordPairs, (x["start_location"]["lat"], x["start_location"]["lng"])))
        if (idx == len(r["routes"][0]["legs"][0]["steps"])-1):
            coordPairs = np.vstack((coordPairs, (x["end_location"]["lat"], x["end_location"]["lng"])))
    return coordPairs
'''





def parseRoute(r):
    coordPairs = []
    for idx in range(len(r["routes"])):
        singlePair = np.array((200,200))
        for idx2, x in enumerate(r["routes"][idx]["legs"][0]["steps"]):
            singlePair = np.vstack((singlePair, (x["start_location"]["lat"], x["start_location"]["lng"])))
            if (idx2 == len(r["routes"][idx]["legs"][0]["steps"])-1):
                singlePair = np.vstack((singlePair, (x["end_location"]["lat"], x["end_location"]["lng"])))
        coordPairs.append(singlePair)
    return coordPairs

test = parseRoute(r)

    # print "Starting location:", x["start_location"]["lat"], x["start_location"]["lng"]
    # print "Ending location:", x["end_location"]["lat"], x["end_location"]["lng"]

crime = pd.read_csv("~/Documents/3rd year/HackSC/LAPD_Crime.csv")
crime["Location 1"] = [x[1:-1] for x in crime["Location 1"]]
crime["Location 1"] = [x.split(", ") for x in crime["Location 1"]]
crime["Location 1"] = [np.array((float(x), float(y))) for x, y in crime["Location 1"]]



def calc_Crime_Index(coordPairs):
    score = 0
    for lat, lng in crime["Location 1"]:
        for idx in range(len(coordPairs)-1):
            dif_lat = abs(coordPairs[idx][0] - coordPairs[idx+1][0])
            dif_lng = abs(coordPairs[idx][1] - coordPairs[idx+1][1])
            dif_lat1 = abs(coordPairs[idx][0] - lat)
            dif_lat2 = abs(coordPairs[idx+1][0] - lat)
            dif_lng1 = abs(coordPairs[idx][1] - lng)
            dif_lng2 = abs(coordPairs[idx+1][1] - lng)
            if ((dif_lat1 < dif_lat) and (dif_lat2 < dif_lat) and (dif_lng1 < dif_lng) and (dif_lng2 < dif_lng)):
                score += 1
    return score


print calc_Crime_Index(coordPairs = test[0])
print calc_Crime_Index(coordPairs = test[1])
print calc_Crime_Index(coordPairs = test[2])


