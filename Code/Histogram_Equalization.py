import cv2 
import numpy as np 
import matplotlib.pyplot as plt  

ori_img = cv2.imread('../StudyOpenCV/images/hist_equal.jpg')
ori_img = cv2.resize(ori_img, (450, 600))

hist,bins = np.histogram(ori_img.flatten(),256,[0,256])
#cdf = hist.cumsum()
#cdf_m = np.ma.masked_equal(cdf,0)
#cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#cdf = np.ma.filled(cdf_m,0).astype('uint8')
#img = cdf[img]

print(type(hist))
print(type(bins))

cv2.imshow('img', ori_img)
plt.hist(ori_img.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.show()

'''
cv2.imshow('test', ori_img) 
cv2.waitKey(0)
cv2.destrayAllWindows()
'''