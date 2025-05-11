import os
import random
from PIL import Image
import matplotlib.pyplot as plt

def show_art_for_emotion(emotion):
    base_path = f"data/train/{emotion.lower()}"
    
    if not os.path.exists(base_path):
        print(f"No artwork found for emotion: {emotion}")
        return

    images = os.listdir(base_path)
    if not images:
        print(f"No images found in {base_path}")
        return

    selected_image = random.choice(images)
    img_path = os.path.join(base_path, selected_image)
    image = Image.open(img_path)

    print(f"Displaying sample artwork for: {emotion}")
    plt.imshow(image)
    plt.axis("off")
    plt.title(f"Emotion: {emotion}")
    plt.show()
