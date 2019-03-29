import numpy as np
import cv2

for device_id in range(5):
    print('Capturing from device', device_id)
    cap = cv2.VideoCapture(device_id)

    color = (0,255,0)
    line_width = 3
    radius = 100
    point = (0,0)

    def click(event, x, y, flags, param):
            global point, pressed
            if event == cv2.EVENT_LBUTTONDOWN:
                    print("Pressed",x,y)
                    point = (x,y)

    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame",click)

    while(True):
            ret, frame = cap.read()

            try:
                frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
            except cv2.error:
                print('*' * 20, 'device doesnt work', device_id)
                break
            cv2.circle(frame, point, radius, color, line_width)
            cv2.imshow("Frame",frame)

            ch = cv2.waitKey(1)
            if ch & 0xFF == ord('q'):
                print('Closing device', device_id)
                break

    cap.release()
    cv2.destroyAllWindows()
