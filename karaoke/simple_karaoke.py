from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

def create_karaoke_video(audio_file, lyrics_file, output_file="karaoke_video.mp4"):
    # Ler letras
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lyrics = f.read().strip().split('\n')
    
    # Filtrar linhas vazias
    lyrics = [line for line in lyrics if line.strip()]
    
    # Obter duração do áudio
    result = subprocess.run(['ffprobe', '-v', 'quiet', '-show_entries', 
                           'format=duration', '-of', 'csv=p=0', audio_file], 
                          capture_output=True, text=True)
    duration = float(result.stdout.strip())
    
    # Calcular tempo por linha
    time_per_line = duration / len(lyrics)
    
    # Criar frames
    frame_rate = 24
    total_frames = int(duration * frame_rate)
    
    # Criar diretório temporário para frames
    os.makedirs('temp_frames', exist_ok=True)
    
    for frame_num in range(total_frames):
        t = frame_num / frame_rate
        
        # Criar imagem
        img = Image.new('RGB', (1280, 720), color='black')
        draw = ImageDraw.Draw(img)
        
        # Só mostrar texto após 7 segundos
        if t >= 7.0:
            adjusted_time = t - 7.0
            current_line_idx = int(adjusted_time / time_per_line)
            if current_line_idx >= len(lyrics):
                current_line_idx = len(lyrics) - 1
            
            try:
                font = ImageFont.truetype('/System/Library/Fonts/Arial.ttf', 40)
            except:
                font = ImageFont.load_default()
            
            # Mostrar 3 linhas
            y_positions = [300, 360, 420]
            colors = ['gray', 'white', 'gray']
            
            for i, (y_pos, color) in enumerate(zip(y_positions, colors)):
                line_idx = current_line_idx - 1 + i
                if 0 <= line_idx < len(lyrics):
                    text = lyrics[line_idx]
                    bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = bbox[2] - bbox[0]
                    x_pos = (1280 - text_width) // 2
                    draw.text((x_pos, y_pos), text, fill=color, font=font)
        
        img.save(f'temp_frames/frame_{frame_num:06d}.png')
        
        if frame_num % 100 == 0:
            print(f"Processando frame {frame_num}/{total_frames}")
    
    # Criar vídeo com ffmpeg
    cmd = [
        'ffmpeg', '-y',
        '-framerate', str(frame_rate),
        '-i', 'temp_frames/frame_%06d.png',
        '-i', audio_file,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-shortest',
        output_file
    ]
    
    subprocess.run(cmd)
    
    # Limpar frames temporários
    import shutil
    shutil.rmtree('temp_frames')
    
    print(f"Vídeo de karaokê salvo como: {output_file}")

if __name__ == "__main__":
    create_karaoke_video("accompaniment.wav", "lyrics.txt")
