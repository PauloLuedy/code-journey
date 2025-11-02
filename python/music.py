from moviepy.editor import *

# Caminhos dos arquivos
music = "accompaniment.wav"  # faixa instrumental
lyrics = "lyrics.txt"  # arquivo com as letras (vamos gerar dinamicamente)

# Texto das letras
text = """We go all or nothing\nAll or nothing\nWhy not make it count for something?\n\nAll or nothing\nAll or nothing\nFight for something we believe in\n\nIf we never stop hoping\nWe will never be broken\nEven if our heart aches\n\nWe go all or nothing\nAll or nothing\nWhy not make it count for something?\n\nWhen the city lights are calling at night\nAnd you lay in bed rethinking your life\nWill it ever stop the worrying mind\nYou will find\n\nIf we're running away from the problems we see\nKeep giving up on our hopes and our dreams\nWe got the power to be who we want to be\nYou see\n\nWe go all or nothing\nAll or nothing\nWhy not make it count for something?\n\nAll or nothing\nAll or nothing\nFight for something we believe in\n\nIf we never stop hoping\nWe will never be broken\nEven if our heart aches\n\nWe go all or nothing\nAll or nothing\nWhy not make it count for something?\n\nWe go all or nothing\nAll or nothing\nWhy not make it count for something?\n\nAll or nothing\nAll or nothing\nFight for something we believe in"""

# Criar um clipe de fundo (preto ou imagem opcional)
background = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=120)

# Adicionar o texto (rolando ao longo da música)
text_clip = TextClip(text, fontsize=40, color='white', font='Arial-Bold')
text_clip = text_clip.set_pos('center').set_duration(background.duration)

# Sincronizar o texto e o áudio
final_video = CompositeVideoClip([background, text_clip])
audio = AudioFileClip(music)
final_video = final_video.set_audio(audio)

# Exportar o vídeo
final_video.write_videofile("all_or_nothing_lyrics.mp4", fps=24, codec='libx264', audio_codec='aac')
