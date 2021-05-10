import os
import re
from mp3_tagger import MP3File, VERSION_2, VERSION_1
import eyed3
import click



def hascyr(s):
     lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
     return lower.intersection(s.lower()) != set()


@click.command()
@click.option('--src-dir','-s',default='.', type=str, help="Исходная директория")
@click.option('--dst-dir', '-d', default='.',type=str, help="Целевая директория")
def main(src_dir,dst_dir):
    count = False
    for file in os.listdir(src_dir):
        if file.endswith(".mp3"):
            count = True
            if(hascyr(file)):
                mp3 = MP3File(f"{src_dir}/{file}")
                mp3.set_version(VERSION_1)
                artist = mp3.artist
                album = mp3.album
                song = mp3.song
            
            else:
                mp3 = eyed3.load(f"{src_dir}/{file}")
                artist = mp3.tag.artist
                album = mp3.tag.album
                song = mp3.tag.title
            
            if(album and artist):
                if(not os.path.exists(f"{dst_dir}/{artist}/{album}")):
                    artist = re.sub('\|\|\.|\!|\/|\;|\:|\?', '', artist)
                    album = re.sub('\|\|\.|\!|\/|\;|\:|\?', '', album)
                    song = re.sub('\|\|\.|\!|\/|\;|\:|\?', '', song)
                    os.makedirs(f"{dst_dir}/{artist}/{album}")
                    if(song):
                        os.rename(f"{src_dir}/{file}", f"{dst_dir}/{artist}/{album}/{song}-{artist}-{album}.mp3")
                        print(f"{src_dir}/{file}","->", f"{dst_dir}/{artist}/{album}/{song}-{artist}-{album}.mp3")
                    else:
                        os.rename(f"{src_dir}/{file}", f"{dst_dir}/{artist}/{album}/{file}")
                        print(f"{src_dir}/{file}","->", f"{dst_dir}/{artist}/{album}/{file}.mp3", "(Отсутствует информация о названии песни)")
            else:
                print(f"{src_dir}/{file}","(Нет информации о испольнителе или альбоме)" )
    if not count:
        print("В заданной директории нет mp3 файлов")

try:
    if __name__ == "__main__":
        main()
            
except FileNotFoundError:
    print("Некорректная директория. Убедитесь что вы ввели директоию правильно")
except PermissionError:
    print("Нет доступа к назначенной директории")

