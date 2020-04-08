import urllib
import urllib.request
import cv2
import numpy as np

IN = input ('your IP Webcam IP: ')
url=IN + ':8080/shot.jpg'
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640,480))

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        output.write(img)
        exit(0)
