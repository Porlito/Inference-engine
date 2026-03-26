from PIL import Image

def keep_left_strip(input_path, output_path, keep_ratio=0.10):
    img = Image.open(input_path)
    width, height = img.size
    
    # Define the crop box: (left, top, right, bottom)
    left = 0
    top = 0
    # This keeps only the first 10% of the image width
    right = int(width * keep_ratio)
    bottom = height
    
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(output_path)

# This keeps the leftmost 10% and removes the right 90%
keep_left_strip("B.png", "scale_only.png", keep_ratio=0.20)
