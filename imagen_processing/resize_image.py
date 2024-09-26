import cv2

image = cv2.imread("galaxy.jpeg")
print(image.shape)

def calulate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage /100)
    new_height = int(height * scale_percentage /100)
    return (new_width, new_height)

def resize(image_path, scale_percentage):
    image =  cv2.imread(image_path)
    new_dim = calulate_size(scale_percentage, image.shape[1], image.shape[0])
    new_img = cv2.resize(image, new_dim)
    cv2.imwrite("resize/galaxy.jpeg", new_img)

resize("galaxy.jpeg",10)