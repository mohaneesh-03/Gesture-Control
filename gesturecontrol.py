import cv2
import mediapipe as mp
import pyautogui


def count_fingers(lst):
    cnt=0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100)>thresh:
        cnt+=1
    if (lst.landmark[9].y*100 - lst.landmark[12].y*100)>thresh:
        cnt+=1
    if (lst.landmark[13].y*100 - lst.landmark[16].y*100)>thresh:
        cnt+=1
    if (lst.landmark[17].y*100 - lst.landmark[20].y*100)>thresh:
        cnt+=1
    if (lst.landmark[5].x*100 - lst.landmark[4].x*100)>5:
        cnt+=1

    return cnt

def seek(lst):
    cnt =1

    th = (lst.landmark[5].x*100-lst.landmark[17].x*100)/2
    if ((lst.landmark[4].x*100-lst.landmark[2].x*100) > th):
        if (lst.landmark[4].x < lst.landmark[2].x):
            cnt = 0
        else:
            cnt=-1
    return cnt

def vol(lst):
    cnt=0

    if (lst.landmark[4].y*100 - lst.landmark[2].y*100)>17:
        cnt =1
    elif (lst.landmark[4].y*100 - lst.landmark[2].y*100)<-17:
        cnt=-1


    return cnt

cap = cv2.VideoCapture(0)

drawing =mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

prev = -1
prev2 = 5
prev3 = 5

while True:
    success, frm = cap.read()

    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:

        hand_keypoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keypoints)
        cnt2 = seek(hand_keypoints)
        cnt3 = vol(hand_keypoints)

        # print(cnt3)

        if(prev3 != cnt3):
            if(cnt!=5 and cnt3 == -1):
                pyautogui.press("up")
            elif(cnt!=5 and cnt3 ==1):
                pyautogui.press("down")


        if(prev2 != cnt2):
            if(cnt!=5 and cnt2 == 1):
                pyautogui.press("left")
            elif(cnt!=5 and cnt2==-1):
                pyautogui.press("right")

        if(prev !=cnt):
            if(cnt == 5):
                pyautogui.press("space")

        prev = cnt
        prev2 = cnt2
        prev3 = cnt3

        drawing.draw_landmarks(frm, hand_keypoints, hands.HAND_CONNECTIONS)


    cv2.imshow("win", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break