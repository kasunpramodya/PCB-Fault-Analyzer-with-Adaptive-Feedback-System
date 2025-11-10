import pathlib
import detect

# Uncomment this line if you are using Windows
pathlib.PosixPath = pathlib.WindowsPath

if __name__ == "__main__":
    opt = detect.parse_opt()
    opt.source=r'f:\yolo\archive\dataset\images\train\01_missing_hole_01.jpg'
    opt.weights=r'F:\yolo\runs-pcb\content\drive\MyDrive\yolo\yolov5\runs\train\pcb_1st11\weights\best.pt'
    detect.main(opt)