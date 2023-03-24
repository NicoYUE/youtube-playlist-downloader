import os

from moviepy.audio.io.AudioFileClip import AudioFileClip
from mutagen.id3 import ID3, APIC


def mp4_to_mp3(mp4_path: str):

    base = os.path.splitext(mp4_path)[0]
    mp3_path = base + ".mp3"

    mp4_file = AudioFileClip(mp4_path)
    mp4_file.write_audiofile(mp3_path)
    mp4_file.close()
    os.remove(mp4_path)
    return mp3_path


def emb_art_to_mp3(mp3_path: str, art_path: str, delete_art_after_emb=False):
    audio = ID3(mp3_path)

    with open(art_path, "rb") as art:
        audio.add(
            APIC(
                encoding=3,
                mime="image/jpeg",
                type=3, desc=u'Cover',
                data=art.read()))

    audio.save(v2_version=3)

    if delete_art_after_emb:
        os.remove(art_path)
