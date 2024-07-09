import cv2
from deepface import DeepFace

def capture_video_with_emotion_detection():
    # Initialize video capture from the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # Use DeepFace to analyze the emotions in the frame
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            
            if isinstance(result, list) and len(result) > 0:
                result = result[0]  # Get the first result if it's a list
            
            # Get the dominant emotion
            dominant_emotion = result['dominant_emotion']

            # Draw a rectangle around the face and display the emotion
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
        except Exception as e:
            print(f"Error: {e}")

        # Display the resulting frame
        cv2.imshow('Emotion Detection', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

# Run the emotion detection
capture_video_with_emotion_detection()
