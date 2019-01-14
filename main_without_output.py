# Eye for you main program

import keyboard
import cv2
import time
import argparse
import logging
import pyttsx3
import sys

logger = logging.getLogger('Eye For You Webcam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

sys.path.append('./object_detection/')
from yolo import yolo


def read_text(image):
    return (image, [])


def obstacle_recognition(image):
    return (image, [])


def face_recognition(image):
    return (image, [])


def do_nothing(image):
    return (image, [])


def say(text):
    '''engine = pyttsx3.init()
    engine.say("Object Recognized " + text)
    a=engine.runAndWait()'''
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    # for voice in voices:
    engine.setProperty('voice', 'english-us')
    # print voice.id
    engine.say('Object Recognized' + text)
    a = engine.runAndWait()  # blocks


functions = {'read Text': read_Text, 'obstacle Recognition': yolo, 'Face Recognition': Face_Recognition,
             'Do Nothing': Do_Nothing}


def get_key_pressed():
    """
    Return the mode selected depending on the key pressed
    """
    if keyboard.is_pressed('a'):
        return 'read_text'
    elif keyboard.is_pressed('z'):
        return 'obstacle_recognition'
    elif keyboard.is_pressed('e'):
        return 'face_recognition'
    elif keyboard.is_pressed('r'):
        return 'nothing'


if __name__ == '__main__':

    # All the args argument:
    parser = argparse.ArgumentParser(description='Main-Code')
    # parser.add_argument('--video', type=str, default='')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--save_video', type=str, default='', help='Save in a video format')
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
    Mode = 'Do Nothing'
    while True:
        # Capturing the frame:
        ret_val, image = cam.read()
        # Get the mode of treatment
        mode = get_key_pressed()
        if frames_counter % 3 == 0:
            output, textes = function[Mode](image)

            cv2.putText(output, "FPS: %f Mode Detection : %s" % ((1.0 / (time.time() - fps_time)), Mode), (10, 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.imshow('computation result', output)
            print(textes)
            # for text in textes:
            # say(text)

        frames_counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps_time = time.time()
    cv2.destroyAllWindows()

################################################


################### Outputs ####################


################################################
