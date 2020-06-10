# Important modules
# bs4 to parse the web data
from bs4 import BeautifulSoup as bs
# used to handle the images data
from PIL import Image
# used to handle the bytes data
from io import BytesIO
# used to make requests to webpages and extract data from it
import requests
# used to handle the directories
import os



def start_search():

    # search request form the user
    search = input("What you want to search : ")
    params = {'q':search}
    # create a directory name
    dir_name = search.replace(" ", "_").lower()

    # if dir not present create one
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # request on web for the user search
    req = requests.get("http://bing.com/images/search", params=params)
    # making of the bs4 object with html parser to parse the webdata in html format
    soup = bs(req.text, "html.parser")
    # find links of all the images
    links = soup.findAll('a', {"class":"thumb"})

    # loop through the list of all the links
    for item in links:
        try:
            # again make request for image link
            img_obj = requests.get(item.attrs['href'])
            # console print to see what we get from web
            print("Getting ", item.attrs['href'])
            # title of the image
            title = item.attrs["href"].split('/')[-1]

            # try and except block to handle errors
            try:
                # making of an image object and save the web image data to it
                image = Image.open(BytesIO(img_obj.content))
                # save the data in image object to the scraped_images directory with same title and format
                image.save("./"+ dir_name +"/"+ title , image.format)

            except:
                print("Unable to save image !!!")
        except:
            print("Unable to open image !!!")
    start_search()


# main start point
if __name__ == "__main__":
    start_search()

