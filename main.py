from FunctionLibrary import *
import cv2
import time

class NewW:
    def estimateSpeedNew(self): 
        tracker=EuclideanDistTracker()
        PTime=0
        obj_det=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)

        WebcamIsUsing=False
        if WebcamIsUsing: 
            cap=cv2.VideoCapture(0)
        else:
            cap=cv2.VideoCapture("IMG_0501 (online-video-cutter.com).mp4")
            example_array = []
            Arr = []
            while True:
                _,img=cap.read()

                h,w,_,=img.shape
                roi=img[50: 350,900: 1600]
                mask=obj_det.apply(roi)
                _,mask=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
                cont,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                det=[]
                for cnt in cont:
                    area=cv2.contourArea(cnt)
                    if area>100:
                        #cv2.drawContours(roi,[cnt],-1,(0,255,0),2)
                        x,y,w,h=cv2.boundingRect(cnt)
                        det.append([x,y,w,h])
                
                CTime=time.time()
                fps=1/(CTime-PTime)
                PTime=CTime
                
                boxes_ids=tracker.update(det)
                for box in boxes_ids:
                    x,y,w,h,id=box
                    SpeedEstimatorTool=SpeedEstimator([x,y],fps)
                    speed=SpeedEstimatorTool.estimateSpeed()
                    example_array.append(speed)
                    if w>120 and h>100: 
                        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),3)
                    


                cv2.imshow("mask",mask)
                cv2.imshow("roi",roi)
                cv2.imshow("img",img)
                Arr.append(example_array) 
                key=cv2.waitKey(125)
                if key==13: #113=Q
                    itog=0
                    ind = (len(Arr)-1)/1.5
                    ind = int(ind)
                    for sum in Arr[ind]:
                        itog += sum
                    print("Результат: " + str(itog/len( Arr[ind])))
                    res = str(itog/len( Arr[ind]))
                    break
        return (res)


