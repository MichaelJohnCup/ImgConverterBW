from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Otevře obrázek
    img = Image.open(input_image_path)
    
    # Převede obrázek na černobílý
    grayscale_img = img.convert("L")
    
    # Uloží černobílý obrázek
    grayscale_img.save(output_image_path)

# Zadej cesty k obrázkům
input_image_path = 'C:\Project\skripty\images\Origin.jpg'
output_image_path = 'C:\Project\skripty\images\Originbw.jpg'

# Zavolá funkci
convert_to_grayscale(input_image_path, output_image_path)