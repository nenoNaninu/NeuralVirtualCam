import pyfakewebcam
import cv2
import sys
import torch
import re
from torchvision import transforms
from fast_neural_style.neural_style.transformer_net import TransformerNet


def get_model(path, device="cuda:0"):
    style_model = TransformerNet()
    state_dict = torch.load(path)
    # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
    for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
    style_model.load_state_dict(state_dict)
    style_model.to(device)

    return style_model


def stylize_img(model, img, device="cuda:0"):
    # device = torch.device("cuda" if args.cuda else "cpu")

    # content_image = utils.load_image(args.content_image, scale=args.content_scale)
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])

    content_image = content_transform(img)
    content_image = content_image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(content_image).cpu()

    img = output[0].clone().clamp(0, 255).numpy()
    img = img.transpose(1, 2, 0).astype("uint8")
    return img


if __name__ == '__main__':
    cam_id = int(sys.argv[1])
    virtual_device_path = sys.argv[2]

    cap = cv2.VideoCapture(cam_id)
    virtual_camera = pyfakewebcam.FakeWebcam(virtual_device_path, 640, 480)

    model0 = get_model('fast_neural_style/saved_models/candy.pth')
    model1 = get_model('fast_neural_style/saved_models/mosaic.pth')
    model2 = get_model('fast_neural_style/saved_models/rain_princess.pth')
    model3 = get_model('fast_neural_style/saved_models/udnie.pth')

    model = model0

    while (True):
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
