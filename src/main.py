# python 3.8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 100)

    # wait for yt playlist page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "style-scope ytd-playlist-video-list-renderer")))

    # Scroll playlist down to load all the videos in it
    videoCountXPATH = "//*[@id='stats']//span[1]"
    videoCount = int(driver.find_element_by_xpath(videoCountXPATH).text)

    while True:
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        nVideosLoaded = len(driver.find_elements_by_xpath("//*[@id='contents' and @class='style-scope ytd-playlist-video-list-renderer']/*"))
        if nVideosLoaded >= videoCount:
            break

    # Get the url of all the excluded videos in the playlist
    excludedVideoXPATH = "//a[contains(text(),'[Vídeo excluído]')]"
    excludedVideosElements = driver.find_elements_by_xpath(excludedVideoXPATH)

    infoToSearch = []
    for excludedVideoElement in excludedVideosElements:
        videoUrl = excludedVideoElement.get_attribute("href")
        infoToSearch.append(videoUrl.split("=")[1].split("&")[0])

    print(">> number of excluded videos:", len(infoToSearch))

    infoToSearch = infoToSearch
    for info in infoToSearch:
        searchURL = "https://www.google.com/search?q=" + info
        driver.execute_script('window.open("'+ searchURL +'");')

    while True:
        pass

main()
