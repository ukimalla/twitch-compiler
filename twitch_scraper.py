import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tqdm import tqdm
import os

# Download video using link
def download_video_from_link(br, video_link, folder):

    br.get(video_link)

    TIMEOUT_MAX = 20 # Variable for timeout length

    
    WebDriverWait(br, TIMEOUT_MAX).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    video_elem = br.find_element_by_tag_name("video")
    link = video_elem.get_attribute("src")

    while link == "":
        # Waiting for the video to load.
        sleep(1)    
        link = video_elem.get_attribute("src")


    # Checking if the the video was found. 
    if not video_elem:
        print("Could not find the video element.")
        return

    # Parsing the filename and saving the video. 
    file_name = link.split('/')
    file_name = file_name[-1]

    # Creating a directory using string folder
    if not folder in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), folder))

    # Downloading the video and saving it as file_name
    urllib.request.urlretrieve(link,  os.path.join(folder, file_name))

    

if __name__ == "__main__":
    br = webdriver.Firefox()
    CLIP_THUMBNAIL = '//a[@data-a-target="preview-card-image-link"]'
    # Modify this dict to add/remove clips category. 
    cat_dict = {

        "counter_strike" : "https://www.twitch.tv/directory/game/Counter-Strike%3A%20Global%20Offensive/clips?range=24h",
      
        "valorant"       : "https://www.twitch.tv/directory/game/VALORANT/clips?range=24h", 
       
        "cod"            : "https://www.twitch.tv/directory/game/Call%20of%20Duty%3A%20Modern%20Warfare/clips?range=24hr",

        "minecraft"      : "https://www.twitch.tv/directory/game/Minecraft/clips?range=24hr",

        "league"         : "https://www.twitch.tv/directory/game/League%20of%20Legends/clips?range=24hr",

        "apex"         : "https://www.twitch.tv/directory/game/Apex%20Legends/clips?range=24hr",

    }
       

    # Iterating through each category and downloading them in their respective
    # folders
    for name, link in cat_dict.items():

        clip_links = [] # Container for Clips
      
        # Opening the Clips Page for the Category
        br.get(link)

        sleep(7) #Waiting

        # Getting each clip item element
        clips = br.find_elements_by_xpath(CLIP_THUMBNAIL)

        # Iterating through each clip to get the link
        for clip in clips:
            clip_links.append(clip.get_attribute("href")) # Getting the video link

        # Downloading each link
        print("Downloading " + str(len(clip_links)) + " clips for " + name)
        for link in tqdm(clip_links):
            download_video_from_link(br, link, name) # Downloading Video

    br.close()


