
import requests
from PIL import Image
from io import BytesIO


breeds = requests.get('https://dog.ceo/api/breeds/list/all')
breed = input('Hello Jonathan, please enter a dog breed : ')

#validation
while list != '1' or list != '0':
    list = input('Do you want to know the sub-breeds  (yes = 1 \ no = 0) ? : ')
    if list == '1':
        breed_list = breeds.json()['message'][breed]
        if not breed_list:
            print("Theres no sub-breeds.")
        else:
            print(breed_list)
        break
    elif list == '0':
        break
    else:
        print('Enter only 1 for yes and 0 for no')

count = 'a'
while count != '1' or count != '0':
    count = input('Do you want to know how many sub-breeds are (yes = 1 \ no = 0) ? : ')
    if count == '1':
        print('number of sub-breeds are : ', len(breed_list))
        break
    elif count == '0':
        break
    else:
        print('Enter only 1 for yes and 0 for no')

#return image of a breed

images = requests.get('https://dog.ceo/api/breed/'+breed+'/images')
image = images.json()['message'][0]
image_url = image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
