import cv2
import numpy as np
from moviepy.editor import AudioFileClip, VideoClip
import librosa

def create_karaoke_video(audio_file, lyrics_file, output_file="karaoke_video.mp4"):
    # Carregar áudio
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    
    # Ler letras
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lyrics = f.read().strip().split('\n')
    
    # Filtrar linhas vazias
    lyrics = [line for line in lyrics if line.strip()]
    
    # Calcular tempo por linha
    time_per_line = duration / len(lyrics)
    
    def make_frame(t):
        # Criar frame preto
        frame = np.zeros((720, 1280, 3), dtype=np.uint8)
        
        # Calcular linha atual
        current_line_idx = int(t / time_per_line)
        if current_line_idx >= len(lyrics):
            current_line_idx = len(lyrics) - 1
        
        # Mostrar 3 linhas: anterior, atual, próxima
        y_positions = [300, 360, 420]
        colors = [(100, 100, 100), (255, 255, 255), (100, 100, 100)]
        
        for i, (y_pos, color) in enumerate(zip(y_positions, colors)):
            line_idx = current_line_idx - 1 + i
            if 0 <= line_idx < len(lyrics):
                text = lyrics[line_idx]
                
                # Calcular posição central
                text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
                x_pos = (1280 - text_size[0]) // 2
                
                cv2.putText(frame, text, (x_pos, y_pos), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        return frame
    
    # Criar vídeo
    video = VideoClip(make_frame, duration=duration)
    video = video.set_audio(audio)
    
    # Salvar
    video.write_videofile(output_file, fps=24, codec='libx264')
    print(f"Vídeo de karaokê salvo como: {output_file}")

if __name__ == "__main__":
    create_karaoke_video("accompaniment.wav", "lyrics.txt")
