# python face-recognition-video.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

# import library
from imutils.video import VideoStream
from imutils.video import FPS
from consume import consume
from qrGen import newQR
from telebot import telegram_bot_sendtext, telegram_bot_sendImage
from gtts import gTTS 
import os 
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2


# Parsing Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
args = vars(ap.parse_args())

# load file cascade OpenCV
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])

# Pi Camera
print("[INFO] Initializing Pi Camera...")
vs = VideoStream(src=0).start()
time.sleep(1.0)

# FPS (Frame per Second)
fps = FPS().start()

while True:
	# frame resize  500pixel
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	
	# Definition to color spaces
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []

	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		# Get names from folders
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)
		names.append(name)

	# Drawing rectangle on face
	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)
		
		hasMask = consume(name)
		print(hasMask)
		
		if hasMask != b'We apologyze but no acces without FaceMask :(':
			qr = newQR(hasMask)
			telegram_bot_sendtext(hasMask)
			telegram_bot_sendImage(qr)
		else:
			telegram_bot_sendtext(hasMask)
	#break	
	# Draw images
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break

	# update FPS
	fps.update()

# info FPS
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# cleanup
cv2.destroyAllWindows()
vs.stop()
