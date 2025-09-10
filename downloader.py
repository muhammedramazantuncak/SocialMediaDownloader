import yt_dlp
import os

base_path = os.path.join(os.getcwd(), "DownloadVideos") # os.path.join işletim sisteminde klasör ayraçlarını otomatik olarak birleştirir
                                                   # os.getcwd() = (get currently working directory) kodun çalıştığı klasörü getirir
while True:                                        # ve virgülden sonra yazılanı o klasörün içinde yeni klasör olarak açar

    try:
        url = input("Lütfen indirmek istediğiniz videonun linkini giriniz: ")

        if "instagram.com" in url:
            outtmpl = os.path.join( base_path , "INSTAGRAM" , "%(title)s.%(ext)s") # DownloadVideos klasöründe yeni klasör açar aynı mantık
        elif "youtube.com" in url:
            outtmpl = os.path.join( base_path , "YOUTUBE" , "%(title)s.%(ext)s")
        else:
            outtmpl = os.path.join( base_path , "OTHERS" , "%(title)s.%(ext)s")

        ydl_opts = {"outtmpl": outtmpl, # indirilen videonun özelliklerini belirt
                }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # aslında ydl = yt_dlp.YoutubeDL(ydl_opts) ile aynı mantık ama with ile oluşturduğun için otomatik kapanır senin manuel olarak bişey yapmana gerek kalmaz
            ydl.download([url])
        print("İndirme İşleminiz Tamamlandı :)")

        answer = input("İndirme işlemine devam etmek ister misiniz : Y/N ").upper()
        if answer == "Y":
            continue
        else:
            print("İyi günler dilerim :)")
            break

    except:
        print("İndirme İşleminiz Tamamlanamadı :(")