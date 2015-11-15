import pandas as pd
import numpy as np
import simplejson, urllib

#might need to import pandas into requirements.txt


UIorigin = "456 Landfair Ave, Los Angeles, CA"
UIdestination = "1000 Tiverton Ave, Los Angeles, CA"

test = "https://maps.googleapis.com/maps/api/directions/json?origin=456 Landfair Ave, Los Angeles, CA&alternatives=true&destination=1000 Tiverton Ave, Los Angeles, CA&key=AIzaSyCQ7a-qMPRtVz5mS4XOs2MgcB13JxQVvYk"

def grabJson(UIorigin, UIdestination):
    rqstURL = "https://maps.googleapis.com/maps/api/directions/json?origin="+UIorigin+"&alternatives=true&destination="+UIdestination+"&key=AIzaSyCQ7a-qMPRtVz5mS4XOs2MgcB13JxQVvYk"
    return simplejson.load(urllib.urlopen(rqstURL))
    # return simplejson.load(urllib.urlopen(test))


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


# This function returns the collection of coordinates for all of the routes
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

    # print "Starting location:", x["start_location"]["lat"], x["start_location"]["lng"]
    # print "Ending location:", x["end_location"]["lat"], x["end_location"]["lng"]

def readCSVfunc(crime):
    crime["Location 1"] = [x[1:-1] for x in crime["Location 1"]]
    crime["Location 1"] = [x.split(", ") for x in crime["Location 1"]]
    crime["Location 1"] = [np.array((float(x), float(y))) for x, y in crime["Location 1"]]
    return crime

def calc_Crime_Index(coordPairs):
    score = 0
    csv_file = pd.read_csv("/static/content/LAPD_Crime_and_Collision_Raw_Data_-_2014.csv")
    crime = readCSVfunc(csv_file)
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


def return_Best_Route(UIorigin, UIdestination):
    JSON_raw = grabJson(UIorigin, UIdestination)
    routes = parseRoute(JSON_raw)
    minimum = None
    min_idx = -1
    for idx, x in enumerate(routes):
        score = calc_Crime_Index(x)
        print score
        if ((not minimum) or (score < minimum)):
            min_idx = int(idx)
            minimum = score
    # print "min_idx is", min_idx


    # The return type is a JSON object, with key="points", and val= THE POLYLINE DATA
    return JSON_raw["routes"][min_idx]["overview_polyline"]




