import requests
import threading
import os
from sys import stdout

# Function to download and save an image from a URL
def download_image(thread_id):
    i = 0
    while True:
        try:
            response = requests.get('https://upfollowcreators.s3.us-east-2.amazonaws.com/settings/January2024/QrugMjtC5qfOBrMooGBq.png')
            if response.status_code == 200:
                with open('./test', 'wb') as f:
                    f.write(response.content)
            else:
                print(response.status_code)
        except Exception as e:
            print(f"Error downloading image: {e}")
        i += 1
        if i % 100 == 0:
            print('-', end='')
            stdout.flush()


# Create and start a thread for each image download
nb_threads = 8
threads = []
for thread_id in range(nb_threads):
    thread = threading.Thread(target=download_image, args=(thread_id,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
