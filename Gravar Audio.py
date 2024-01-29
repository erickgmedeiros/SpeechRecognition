import speech_recognition as sr

rec = sr.Recognizer()

mic_index = 0  # escolher o microfone desejado
with sr.Microphone(device_index=mic_index) as mic:
    try:
        rec.adjust_for_ambient_noise(mic, duration=1)
        print("Fale algo...")
        
        rec.pause_threshold = 1 # tempo que a biblioteca espera de pausa na fala antes de encerrar o reconhecimento, por padrão = 0.8

        audio = rec.listen(mic, timeout=10)
        print("Gravação de áudio concluída. Salvando como .wav...")

        with open('audio.wav', 'wb') as arquivo: # 'wb' Write with Binary
            arquivo.write(audio.get_wav_data())
            print('Áudio salvo como .wav')

    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")

    except Exception as e:
        print(f"Erro desconhecido: {e}")
