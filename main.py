import pyfakewebcam
import cv2
from fast_neural_style.neural_style.neural_style import stylize_img, get_model
import sys

cam_id = sys.argv[1]
virtual_device_path = sys.argv[2]

cap = cv2.VideoCapture(cam_id)
virtual_camera = pyfakewebcam.FakeWebcam(virtual_device_path, 640, 480)

model0 = get_model('fast_neural_style/saved_models/candy.pth')
model1 = get_model('fast_neural_style/saved_models/mosaic.pth')
model2 = get_model('fast_neural_style/saved_models/rain_princess.pth')
model3 = get_model('fast_neural_style/saved_models/udnie.pth')

model = model0

while(True):
    ret, frame = cap.read()

    dst_img = stylize_img(model, frame)

    cv2.imshow('frame', dst_img)
    virtual_camera.schedule_frame(cv2.cvtColor(dst_img, cv2.COLOR_BGR2RGB))

    key = cv2.waitKey(5)

    if key == ord('a'):
        model = model0

    if key == ord('s'):
        model = model1

    if key == ord('d'):
        model = model2

    if key == ord('f'):
        model = model3

    if key == ord('q'):
        break
