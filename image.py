from PIL import Image
import numpy as np

def apply_blue_tints(pixel):
    r, g, b = pixel
    return (0, 0, b)  # Conserve uniquement les teintes de bleu

def pixelate_image(image_path, output_path, pixel_size):
    # Ouvre l'image et convertit en mode RGB
    img = Image.open(image_path).convert('RGB')

    # Réduit l'image pour l'effet pixel art
    small_img = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        Image.NEAREST
    )

    # Agrandit l'image pour retrouver la taille originale
    pixel_art_img = small_img.resize(
        (small_img.width * pixel_size, small_img.height * pixel_size),
        Image.NEAREST
    )

    # Transforme l'image en tableau numpy
    data = np.array(pixel_art_img)

    # Applique les teintes de bleu à chaque pixel
    blue_tinted_data = np.apply_along_axis(apply_blue_tints, 2, data).astype(np.uint8)

    # Convertit le tableau numpy en image
    img = Image.fromarray(blue_tinted_data, 'RGB')
    img.save(output_path)

if __name__ == "__main__":
    input_image = 'background.jpg'  # Remplace par le chemin de ton image
    output_image = 'output_pixel_art.jpg'  # Chemin de sauvegarde de l'image pixel art
    pixel_size = 5  # Taille des pixels de l'art

    pixelate_image(input_image, output_image, pixel_size)
