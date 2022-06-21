import cv2
import time
video = cv2.VideoCapture(0)

# Counter
a = 0

# start the loop
while True:
    a = a+1     # Counter variable
    check, frame = video.read()
    print(check)  # reads the video
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("capturing", gray)  # Shows the video
    key = cv2.waitKey(1)
    if key == ord('q'):  # breaks the loop with "q" key
        break
print(a)
video.release()
cv2.destroyAllWindows()
