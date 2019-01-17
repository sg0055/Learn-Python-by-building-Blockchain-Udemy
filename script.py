import urllib.request

for i in range(1,205):
    url = "https://vs1.coursehunters.net/udemy-maximilian-blockchain-and-crypto/lesson{}.mp4".format(str(i))
    name = str(i)
    name=name+".mp4"
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")