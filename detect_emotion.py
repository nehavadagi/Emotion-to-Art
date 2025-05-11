import cv2
from deepface import DeepFace
from display_art import show_art_for_emotion

# Start webcam
cap = cv2.VideoCapture(0)
print("Press 'q' to capture and analyze emotion")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam - Press 'q' to Analyze", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            print("Detected Emotion:", emotion)

            show_art_for_emotion(emotion)
        except Exception as e:
            print("Error detecting emotion:", e)
        break

cap.release()
cv2.destroyAllWindows()
