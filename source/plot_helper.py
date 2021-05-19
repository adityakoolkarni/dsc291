import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def plotImages(paths,titles):
    fig,ax = plt.subplots(ncols=2,nrows=1)
    fig.dpi = 175
    fig.set_size_inches(12, 24)
    i = 0
    for path,title in zip(paths,titles):
        ax[i].imshow(cv2.imread(path)[:,:,::-1])
        ax[i].set_title(title)
        ax[i].axes.xaxis.set_visible(False)
        ax[i].axes.yaxis.set_visible(False)
        i += 1
        