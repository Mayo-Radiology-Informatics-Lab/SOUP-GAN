import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
import matplotlib.style as style


MAX_VAL = 10000

def load_data(DIR_dicom):
    slices = len(os.listdir(DIR_dicom))


    files = [0 for i in range(slices) ]
    ll = os.listdir(DIR_dicom)

    data = [0 for i in range(slices) ]
    order = [0 for i in range(slices) ]

    for i in range(slices):
        data[i] = (pydicom.dcmread(DIR_dicom+'/'+ll[i])).pixel_array

    for i in range(slices):
        order[i] = (pydicom.dcmread(DIR_dicom+'/'+ll[i])).SliceLocation

    zipped = zip(data,order)
    sort_zipped = sorted (zipped, key = lambda x : int(x[1]))

    result = zip(*sort_zipped)
    data,_ =[list(x) for x in result]

    return (np.moveaxis(np.array(data),0,-1))

def rescale_img(image, max_val=MAX_VAL):
    image = image - np.min(image)
    image = (np.maximum(image, 0) / image.max()) * max_val
    return (image)


def imgshow(img,cmap ='gray'):
    ww = max(100, 5.0 * img.std())
    wl = img.mean()

    # Plot image on clean axes with specified window level
    vmin = wl - ww // 2
    vmax = wl + ww // 2

#  plt.imshow(img, cmap='gray',aspect='auto', vmin=vmin, vmax=vmax)
    plt.imshow(img, cmap='gray', vmin=vmin, vmax=vmax)
    plt.xticks([])
    plt.yticks([])
    return

def plot_scans(thins_raw, thins, thins_gen,prep_type):

    plt.figure(figsize=(10, 10))
    plt.subplot(2, 3, 1)
    plt.title('Thick Slices', fontsize=14)
    #plt.imshow(thins_resize[123, :, 260:390],cmap='gray')
    imgshow(thins_raw[100, :, :],cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.title('', fontsize=14)
    #plt.imshow(thins_resize[123, :, 260:390],cmap='gray')
    imgshow(thins_raw[:, 100, :],cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.title('Cubic Interpolation', fontsize=14)
    #plt.imshow(thins[123, :, 260:390],cmap='gray')
    imgshow(thins[100, :, :],cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.title('', fontsize=14)
    #plt.imshow(thins[123, :, 260:390],cmap='gray')
    imgshow(thins[:, 100, :],cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.title('SR Interpolation', fontsize=14)
    #plt.imshow(thins_resize[123, :, 260:390],cmap='gray')
    imgshow(thins_gen[100, :, :],cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.title('', fontsize=14)
    #plt.imshow(thins_resize[123, :, 260:390],cmap='gray')
    imgshow(thins_gen[:, 100, :],cmap='gray')
    plt.axis('off')

    plt.show()
    plt.savefig('Example_'+str(prep_type)+'.png')



