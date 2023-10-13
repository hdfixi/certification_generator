import matplotlib.pyplot as plt
import os
from matplotlib.font_manager import FontProperties

def text_to_image(text, output_path='output.png', font_path='spellkid.ttf'):
    # Specify the font
    custom_font = FontProperties(fname=font_path, size=190)

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.text(0.15, 0.8, text, ha='left', va='top', fontproperties=custom_font, backgroundcolor='none')
    ax.axis('off')

    # Save the figure with a transparent background
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1, transparent=True)
    plt.close()

if __name__ == "__main__":
    f=open("names.txt",'r')
    l=f.readlines()
    l=["fixi hd","hd fixi","Houssem Dhemaid"]
    for i in l:

        input_text = i.strip()
        output_file = "text_png/"+input_text+".png"

        # Replace "spellkid.ttf" with the correct path to your "spellkid" font file
        text_to_image(input_text, output_file, font_path=f'{os.getcwd()}/Spellkid.ttf')

        print(f"Image generated and saved at {output_file}")
