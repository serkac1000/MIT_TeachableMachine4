
import cv2
import tensorflow as tf
import numpy as np

def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        print(f"[DEBUG] Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"[ERROR] Failed to load model: {str(e)}")
        return None

def test_camera():
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("[DEBUG] Camera initialized successfully")
            ret, frame = cap.read()
            if ret:
                print("[DEBUG] Camera frame captured successfully")
            cap.release()
        else:
            print("[ERROR] Failed to open camera")
    except Exception as e:
        print(f"[ERROR] Camera error: {str(e)}")

def main():
    print("[DEBUG] Starting pose recognition debug")
    
    # Test model loading
    model = load_model('modelLHRHBOTHHAND.mdl')
    
    # Test camera
    test_camera()
    
    print("[DEBUG] Debug complete")

if __name__ == "__main__":
    main()
