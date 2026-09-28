from ultralytics import YOLO
import cv2

# Load trained Fire/Smoke YOLO model
model = YOLO("best.pt")

# Open laptop webcam
cap = cv2.VideoCapture(0)

print("Fire/Smoke Detection Started")
print("Press Q to stop")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    # Run YOLO detection
    results = model.predict(frame, conf=0.10)

    # Draw detection boxes
    annotated_frame = results[0].plot()

    # Display result
    cv2.imshow("YOLO Fire & Smoke Detection", annotated_frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()