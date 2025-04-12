import cv2
import mediapipe as mp
import numpy as np


cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


obj_x, obj_y = 300, 300
obj_width, obj_height = 100, 100
dragging = False

def calculate_distance(landmark1, landmark2):
    """Calcula la distancia entre dos puntos de referencia"""
    x1, y1 = landmark1
    x2, y2 = landmark2
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while cap.isOpened():
    ret, frame = cap.read()
    

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            

            h, w, _ = frame.shape
            index_x, index_y = int(index_finger.x * w), int(index_finger.y * h)
            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)
            

            distance = calculate_distance((index_x, index_y), (thumb_x, thumb_y))
            

            if distance < 40:  
                if not dragging:
                    dragging = True
                    print("Agarrando objeto")
                obj_x, obj_y = index_x - obj_width // 2, index_y - obj_height // 2
            else:
                if dragging:
                    dragging = False
                    print("Soltando objeto")
    

    cv2.rectangle(frame, (obj_x, obj_y), (obj_x + obj_width, obj_y + obj_height), (255, 0, 0), -1)
    

    cv2.imshow("Drag & Drop", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
