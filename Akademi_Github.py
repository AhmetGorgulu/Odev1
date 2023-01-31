from pytube import YouTube

link = str(input("Linki Giriniz: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("ok")








