import cv2
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')




import cv2

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it to access other cameras if available

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture a frame.")
        break

    # Display the captured frame in a window
    cv2.imshow('Camera', frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
