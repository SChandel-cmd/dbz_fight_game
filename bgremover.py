import requests
import os
from PIL import Image


def convert_bmp_to_png(bmp_path, png_path):
    with Image.open(bmp_path) as img:
        img.save(png_path, 'PNG')

folder_path = 'D:\\Coding Stuff\\gamedev\\brawl\\assets\\sprites\\entities'


# Path to the folder containing the photos
folder_path = "D:\\Coding Stuff\\gamedev\\brawl\\assets\\sprites\\entities"

# # Iterate over the files in the folder
# for filename in os.listdir(folder_path):
#     # Check if the file name starts with 'goku' and ends with '.png'
#     if filename.startswith("goku") and filename.endswith(".png"):
#         # Construct the new file name by replacing 'goku' with 'vegeta'
#         new_filename = filename.replace("goku", "vegeta")
        
#         # Rename the file
#         os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
#         print(f"Renamed {filename} to {new_filename}")
        
# for file_name in os.listdir(folder_path):
# 		file_path = os.path.join(folder_path, file_name)
# 		if os.path.isfile(file_path):
# 			try:     	
# 				new_file_path = os.path.join('D:\\Coding Stuff\\gamedev\\brawl\\assets\\sprites\\entities', file_name[0:-3]+'png')
# 				convert_bmp_to_png(file_path, new_file_path)
# 			except Exception as err:
# 				print(err)
# 				pass

for file_name in os.listdir(folder_path):
		file_path = os.path.join(folder_path, file_name)
		if file_path[-3:]!='png':
			continue
		if file_name[:6] != 'galick':
			continue
		if os.path.isfile(file_path):
			try:     	
				response = requests.post(
					'https://api.remove.bg/v1.0/removebg',
					files={'image_file': open(file_path, 'rb')},
					data={'size': 'auto'},
					headers={'X-Api-Key': 'QgW3L2wr8MRBvKjM8QgwcPf2'},
				)
				new_file_path = os.path.join('D:\\Coding Stuff\\gamedev\\brawl\\assets\\sprites\\entities_processed', file_name)
				if response.status_code == requests.codes.ok:
					with open(new_file_path, 'wb') as out:
						out.write(response.content)
				else:
					print("Error:", response.status_code, response.text)
			except Exception:
				pass
