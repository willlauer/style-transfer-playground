import sys
import numpy as np
from PIL import Image

img = Image.open('./a-rain.jpg')
arr = np.array(img)

print(arr.shape)

tmp = np.zeros(arr.shape)
tmp[:, :, 0] = arr[:, :, 2]
tmp[:, :, 1] = arr[:, :, 1]
tmp[:, :, 2] = arr[:, :, 0]

tmp = tmp.astype(np.int)
print(tmp.dtype)

print(tmp.shape)

print(tmp[0, 0, 1])

img2 = Image.fromarray(tmp.astype(np.uint8))
img2.save('tmp.jpg')