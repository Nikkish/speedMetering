import cv2
import math
import time

from matplotlib import image

def estimateSpeed(location1, location2):
    PTime=0
    d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
    ppm = 8.8
    d_meters = d_pixels / ppm
    while True:
        CTime=time.time()
        fps=1/(CTime-PTime)
        PTime=CTime
    speed = d_meters * fps * 3.6
    return speed

def process_in_while(img,Id,_bbox):
    frameCounter=0
    CurrentCarId=0
    fps=0

    Tracker={}
    Number={}
    Loc1={}
    Loc2={}

    speed=[None]*1000

    while True:
        start_time=time.time()
        
        if type(img)==type(None):
            break

        frameCounter+=1
        IdToDel=[]

        for ID in Tracker.keys():
            trackingQuality = Tracker[ID].update(img)

            if trackingQuality < 7:
                IdToDel.append(ID)

        
        for ID in IdToDel:
            print("Removing ID " + str(ID) + ' from list of trackers. ')
            print("Removing ID " + str(ID) + ' previous location. ')
            print("Removing ID " + str(ID) + ' current location. ')
            Tracker.pop(ID, None)
            Loc1.pop(ID, None)
            Loc2.pop(ID, None)

        
        if not (frameCounter % 10):
            for (_x, _y, _w, _h) in _bbox:
                x = int(_x)
                y = int(_y)
                w = int(_w)
                h = int(_h)
            x_bar = x + 0.5 * w
            y_bar = y + 0.5 * h

            matchCarID = None

            for ID in Tracker.keys():
                trackedPosition = Tracker[ID].get_position()


