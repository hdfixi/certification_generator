from PIL import Image
import os

def overlay_images(background_path, overlay_path, output_path='output_overlay.png', overlay_position=(0, 0)):
    # Open the background and overlay images
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    # Resize overlay image to match the background with antialiasing using thumbnail
    overlay.thumbnail(background.size, Image.ANTIALIAS)
    a=(background.size[0]-overlay.size[0])//2
    
    # Paste the overlay onto the background at the specified position
    background.paste(overlay, (a,950), overlay)

    # Save the result
    background.save(output_path, 'PNG')

if __name__ == "__main__":
    f=open("names.txt",'r')
    l=f.readlines()
    #l=["fixi hd","hd fixi","Houssem Dhemaid"]
    for i in l:
        input_text = i.strip()
        background_image = f'{os.getcwd()}/certif.png'  # Replace with your background image path
        overlay_image = "./text_png/"+input_text+".png"  # Replace with your overlay image path
        output_image = "./certif/"+input_text+".png"

        # Set the position where you want to overlay the image (x, y)
        overlay_position = (0,950)  # Adjust the position as needed

        overlay_images(background_image, overlay_image, output_image, overlay_position)
        print(f"Images overlayed and saved at {output_image}")
