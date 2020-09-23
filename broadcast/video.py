import cv2
import numpy as np
import tensorflow as tf


RESNET = tf.keras.applications.ResNet50V2(
    weights='imagenet',
    classes=1000
)


def capture_video(video_in: cv2.VideoCapture) -> np.ndarray:
    success, frame = video_in.read()
    if success is not True:
        # handle errors eventually maybe
        pass
    return frame


def isolate_bg(frame):
    return None


def loopback(device: str, width: int, height: int, framerate: int):
    video_in = cv2.VideoCapture(device)
    video_in.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    video_in.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    video_in.set(cv2.CAP_PROP_FPS, framerate)

    while True:
        frame = capture_video(video_in)
        isolate_bg(frame)

    return None
