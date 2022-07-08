import time
from pil import Image, ImageFilter
import concurrent.futures
import fnmatch
import os
## List of images with extension pf .jpg
im_names = [f for f in os.listdir(os.getcwd()+'\\DownloadImages') if fnmatch.fnmatch(f, '*.jpg')]
start = time.perf_counter() ## Start counter
size = (1000, 1000) ## Specified size
def image_processing(im_name): ## Function to resize and blur the images
    image = Image.open(f'DownloadImages/{im_name}') ## the image name from Folder
    image = image.filter(ImageFilter.GaussianBlur(15)) ## To add Gaussian Noise
    image.thumbnail(size) ## Resize the Image
    image.save(f'ModifiedImages/{im_name}') ## Save image to a specified folder
    print(f'{im_name} completed...') ## Printing completed statement
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor: ## Multiprocessing
        executor.map(image_processing, im_names) ## Maping Function with Input image list
    finish = time.perf_counter() ##End Counter
    print(f'Finished in {finish-start} seconds') ## Execution time of complete process
