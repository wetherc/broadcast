import argparse
from broadcast.video import loopback


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--device',
        dest='device',
        default='/dev/video0',
        help='The device identifier of your video input. Defaults to /dev/video0'
    )
    parser.add_argument(
        '--width',
        dest='width',
        default=1280,
        help='Video width in pixels to emit. Defaults to 720p'
    )
    parser.add_argument(
        '--height',
        dest='height',
        default=720,
        help='Video height in pixels to emit. Defaults to 720p'
    )
    parser.add_argument(
        '-f',
        '--framerate',
        dest='framerate',
        default=30,
        help='The max framerate to sample at. Defaults to 30 FPS'
    )
    args = parser.parse_args()
    loopback(args.device, args.width, args.height, args.framerate)


if __name__ == '__main__':
    serve()
