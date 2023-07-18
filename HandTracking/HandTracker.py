import cv2
import mediapipe as mp
import socket

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(cx)
                # print(cy)
                data = [cx , cy]
                print(data)
                sock.sendto(str.encode(str(data)), serverAddressPort)

                # if id == 9 :
                #     cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Output", image)
    cv2.waitKey(1)