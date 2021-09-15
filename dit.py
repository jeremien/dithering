from PIL import Image
import hitherdither

SIZE = (950, 633)

img = Image.open('image.jpg')
img_nb = img.convert('L')
img_rz = img_nb.resize(SIZE, resample=0)


palette = hitherdither.palette.Palette(
  [0x080000, 0x201A0B, 0x432817, 0x492910,
  0x234309, 0x5D4F1E, 0x9C6B20, 0xA9220F,
  0x2B347C, 0x2B7409, 0xD0CA40, 0xE8A077,
  0x6A94AB, 0xD5C4B3, 0xFCE76E, 0xFCFAE2]
)

img_dith = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img_rz, palette, order=8)
img_dith.save('image_dit.png')
