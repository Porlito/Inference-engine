from PIL import Image

def full_scan_cut_below(input_path, output_path, target_hex):
    # Load image
    img = Image.open(input_path).convert("RGB")
    width, height = img.size
    
    # Convert hex to RGB
    target_hex = target_hex.lstrip('#')
    target_rgb = tuple(int(target_hex[i:i+2], 16) for i in (0, 2, 4))

    found_y = None

    # OUTER LOOP: Move from bottom row (height-1) up to the top row (0)
    for y in range(height - 1, -1, -1):
        
        # INNER LOOP: Check every pixel (x) in the current row (y)
        for x in range(width):
            if img.getpixel((x, y)) == target_rgb:
                found_y = y
                break  # Stop checking this row
        
        if found_y is not None:
            break  # Stop searching entirely, we found the first line!

    if found_y is not None:
        # Keep everything from the TOP (0) down to that found line (found_y)
        cropped_img = img.crop((0, 0, width, found_y))
        cropped_img.save(output_path)
        print(f"Success! Found color at row {found_y}. Bottom section removed.")
    else:
        print(f"Color {target_hex} not found anywhere in the image.")

# Usage
full_scan_cut_below("A.png", "cropped_result.png", "#FF6956")
