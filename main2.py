import cv2

cap = cv2.VideoCapture(0)

## some videowriter props
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fps = 20
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv2.VideoWriter_fourcc('m', 'p', 'e', 'g')
fourcc = cv2.VideoWriter_fourcc(*'divx')

## open and set props
# vout = cv2.VideoWriter()
# vout.open('output.mp4',fourcc,fps,sz,True)
# import time; time.sleep(10000)

vout = cv2.VideoWriter()
size=(400, 400)
success = vout.open('output.mp4',fourcc,fps,size,True)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # frame = cv2.flip(frame, -1)

    vout.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
vout.release()
cv2.destroyAllWindows()
print('Sleep')
import time; time.sleep(10000)
