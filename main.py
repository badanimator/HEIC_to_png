from PIL import Image
import pillow_heif
from os import listdir
from os.path import join, abspath

def getHeifFileListFromDir(path="./"):
    heif_files = [ abspath(file) for file in listdir('./')]
    heif_files = map(lambda x: x if x.endswith("HEIC") or x.endswith("heic") else None, heif_files)
    heif_files = filter(lambda x:x!=None, heif_files)
    return list(heif_files)


if __name__=="__main__":
    for file in getHeifFileListFromDir():
        filename = file.split('\\')[-1].split('.')[0]
        heif_file = pillow_heif.read_heif(file)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        file_path = join(abspath('./new_png'), filename+".png")
        image.save(file_path, format("png"))
        print(f"Save '{file_path}'")
    print("Finished")
