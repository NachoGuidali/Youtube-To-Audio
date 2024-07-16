import yt_dlp as youtube_dl
from pydub import AudioSegment
import os

def youtube_to_audio(url):
    try:
        # Obtener la ruta del directorio del script
        output_path = os.path.dirname(__file__)
        audio_output = os.path.join(output_path, 'audio.mp3')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f'Archivo de audio guardado en: {audio_output}')
    except Exception as e:
        print(f'Error: {e}')

# Ejemplo de uso
url = 'https://www.youtube.com/watch?v=qWY8OAhIQWc'
youtube_to_audio(url)





""""from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_audio(url, output_path):
    try:
        # Descargar el video de YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        print(f'Descargando: {yt.title}')
        
        # Descargar el archivo de audio
        audio_file = video.download(output_path)
        base, ext = os.path.splitext(audio_file)
        
        # Convertir a formato de audio mp3
        audio_output = base + '.mp3'
        AudioSegment.from_file(audio_file).export(audio_output, format='mp3')
        
        # Eliminar el archivo de audio original
        os.remove(audio_file)
        
        print(f'Archivo de audio guardado como: {audio_output}')
    except Exception as e:
        print(f'Error: {e}')

# Ejemplo de uso
url = 'https://www.youtube.com/watch?v=qWY8OAhIQWc'
output_path = '/youtube-audio'
download_youtube_video_as_audio(url, output_path) """