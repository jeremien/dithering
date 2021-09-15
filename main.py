import os
from PIL import Image
import hitherdither

SIZE = (950, 633)
PATH_SRC = 'src/'
PATH_DIST = 'dist/'

def readConvertImg(file):
  img = Image.open(PATH_SRC + file)
  img_rz = img.resize(SIZE, resample=0)
  palette = hitherdither.palette.Palette.create_by_median_cut(img_rz)
  img_dith = hitherdither.ordered.bayer.bayer_dithering(
                                                      img_rz,
                                                      palette,
                                                      [256/4,256/4,256/4],
                                                      order=8
                                                      )
  
  img_nb = img_dith.convert('L')
  img_nb.save(PATH_DIST + file)

files = os.listdir(PATH_SRC)

print('start')
for f in files:
  readConvertImg(f)

print('complet')

