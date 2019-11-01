import cv2

sample1 = cv2.imread("sample01-damaged.jpg")
mask1 = cv2.imread("sample01-mask.jpg")
mask1 = mask1[:, :, 0] # mask needs to be one channel only

radius = 15
result1 = cv2.inpaint(sample1, mask1, radius, cv2.INPAINT_TELEA)

cv2.imwrite("sample01-restored.jpg", result1)
