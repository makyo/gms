import json
import os
import sys
import yaml


def get_cameras(cameras_dir: str = 'Cameras') -> dict:
    cameras = {}
    camera_files = os.listdir(cameras_dir)
    for camera_file in camera_files:
        with open(os.path.join(cameras_dir, camera_file)) as f:
            camera = json.load(f)
        cameras[camera_file[:-5]] = camera
    return cameras


def get_movements(movements_file: str) -> list:
    with open(movements_file) as f:
        movements = yaml.safe_load(f.read())
    return movements


def build_frames(cameras: dict, movements: list) -> list:
    frames = []
    i = 0
    for movement in movements:
        camera = cameras[movement['base']]
        frame = {
            'position': camera['targetPos'],
            'rotation': camera['targetRot'],
            'FOV': camera['FOV'],
            'holdTime': float(movement['end']) - float(movement['start']),
            'transition': movement['transition'] if 'transition' in movement else 'Linear'
        }
        if i > 0:
            frame['duration'] = float(movement['start']) - float(movements[i-1]['end'])
        frames.append(frame)
        i += 1
    return frames


def build_script(frames: list, sync_to_song: bool = True) -> str:
    return json.dumps({
        'syncToSong': sync_to_song,
        'frames': frames
    })


if __name__ == '__main__':
    cameras = get_cameras()
    movements = get_movements(sys.argv[1])
    frames = build_frames(cameras, movements)
    print(build_script(frames))

