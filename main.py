# Eye for you main program

import keyboard
import cv2
import time
import argparse
import logging
import pyttsx3
import sys

# OpenCV constant initialization
font = cv2.FONT_HERSHEY_SIMPLEX
green = (0, 255, 0)

logger = logging.getLogger('Eye For You Webcam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

sys.path.append('./object_detection/')
# from yolo import yolo


def read_text(image):
    """Read text contained in image and return it in readable format"""
    return None, None


def obstacle_recognition(image):
    """Detect obstacles in image and return description"""
    return None, None


def face_recognition(image):
    """Detect faces and recognize them, return description"""
    return None, None


def nothing(image):
    return None, None


def say(text):
    engine = pyttsx3.init()
    # Rate of speak determined via trial and error
    rate =  120
    engine.setProperty("rate", rate)
    engine.setProperty("voice", "french")
    # print voice.id
    engine.say(text)
    a = engine.runAndWait()


applications = {
    "read_text": read_text,
    "obstacle_recognition": obstacle_recognition,
    "face_recognition": face_recognition,
    "nothing": nothing
}


def get_key_pressed():
    """
    Return the mode selected depending on the key pressed
    """
    if keyboard.is_pressed('a'):
        return "read_text"
    elif keyboard.is_pressed('z'):
        return "obstacle_recognition"
    elif keyboard.is_pressed('e'):
        return "face_recognition"
    elif keyboard.is_pressed('r'):
        return "nothing"


if __name__ == '__main__':

    # Argument parsing
    parser = argparse.ArgumentParser(description='Main-Code')
    parser.add_argument('--camera', type=bool, default=False, help="True if the webcam should be used")
    parser.add_argument('--resolution', type=str, default='432x368', help="CNN input resolution. Default: 432x368")
    parser.add_argument('--save_video', type=bool, default=False, help="Save the video locally")
    parser.add_argument('--video', type=str, default='')
    args = parser.parse_args()

    # cap = cv2.VideoCapture(args.video)
    cam = cv2.VideoCapture(args.camera)

    if args.save_video != '':
        print('Saving the frames at %s' % args.save)
    fps_time = 0
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))
    frames_counter = 1
    # Default Mode
    mode = "nothing"
    while True:
        now = time.time()
        # Capturing the frame
        _, image = cam.read()
        # Get the mode of treatment
        mode = get_key_pressed()
        if frames_counter % 3 == 0:
            output, texts = applications[mode](image)
            fps = 1.0 / (now - fps_time)
            # Show capture info on image
            cv2.putText(output, "FPS: %f Mode Detection : %s" % (fps, mode), (10, 10), font, 0.5, green, 2)
            cv2.imshow('computation result', output)
            print(texts)

        say("bonjour je suis un ordinateur avec une voix nulle")
        frames_counter += 1

        # Leave the loop is q is pressed
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

        fps_time = time.time()
    cv2.destroyAllWindows()
