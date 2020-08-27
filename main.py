from PIL import Image
import numpy as np


def extract_colors(image):
	tmp = []

	# Estrae le distinct value dall'immagine per la conversione a colori
	for i in np.nditer(image):
		if i not in tmp:
			tmp.append(i)

	# Converte da tipo np.ndarray a tipo list
	found = [ndarray_item.tolist() for ndarray_item in tmp]

	return found


def colorize_image(image):
	# Converte l'immagine da GRAYSCALE a RGB mantenendo la size
	rgb_image = Image.new('RGB', image.size)
	rgb_image.paste(image)

	w, h = rgb_image.size

	# Itera sui pixel dell'immagine per cambio colore
	for x in range(0, w - 1):
		for y in range(0, h - 1):
			# Acquisisce il valore RGB del pixel
			r, g, b = rgb_image.getpixel((x, y))

			# Definizione dei colori
			# Red
			new_color_right_arm = 235, 64, 52
			# Yellow
			new_color_pants = 252, 186, 3
			# Green
			new_color_left_arm = 50, 168, 82
			# Blue
			new_color_shirt = 66, 135, 245
			# Purple
			new_color_face = 128, 52, 235
			# Cyan
			new_color_hair = 52, 235, 217

			# Cambia colori
			if r == g == b == 13:
				rgb_image.putpixel((x, y), new_color_right_arm)
			elif r == g == b == 8:
				rgb_image.putpixel((x, y), new_color_pants)
			elif r == g == b == 11:
				rgb_image.putpixel((x, y), new_color_left_arm)
			elif r == g == b == 4:
				rgb_image.putpixel((x, y), new_color_shirt)
			elif r == g == b == 12:
				rgb_image.putpixel((x, y), new_color_face)
			elif r == g == b == 1:
				rgb_image.putpixel((x, y), new_color_hair)

	return rgb_image


def back_to_garyscale(image):
	gs_image = image.convert('L')

	h, w = gs_image.size

	for x in range(0, h - 1):
		for y in range(0 , w -1):
			gs = gs_image.getpixel((x, y))

			if gs == 114:
				gs_image.putpixel((x, y), 13)
			elif gs == 185:
				gs_image.putpixel((x, y), 8)
			elif gs == 123:
				gs_image.putpixel((x, y), 11)
			elif gs == 127:
				gs_image.putpixel((x, y), 4)
			elif gs == 96:
				gs_image.putpixel((x, y), 12)
			elif gs == 178:
				gs_image.putpixel((x, y), 1)

	return gs_image


if __name__ == "__main__":
	img = Image.open('pictures/000988_0.png')

	# data_img = np.asarray(img)

	# Stampa quanti colori diversi ci sono nell'immagine
	# print(extract_colors(data_img))

	# Converte l'immagine in RGB e la colora
	rgb_image = colorize_image(img)

	# data_rgb_image = np.asarray(rgb_image)

	# Dopo aver eseguito le operazioni converte l'immagine nel GRAYSCALE originale
	gs_image = back_to_garyscale(rgb_image)

	# Stampa l'immagine
	# Image._show(gs_image)

	# Salva l'immagine secondo il path specificato
	gs_image.save('./results/' + img.filename[9:])
