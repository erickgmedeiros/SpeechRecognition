import speech_recognition as sr

# Criar um recognizer
rec = sr.Recognizer()

# Listar os microfones disponíveis
#print(sr.Microphone.list_microphone_names())

mic_index = 0  # escolher o microfone desejado
with sr.Microphone(device_index=mic_index) as mic:
    try:
        rec.adjust_for_ambient_noise(mic, duration=1)
        print("Fale algo...")
        
        rec.pause_threshold = 1 # tempo que a biblioteca espera de pausa na fala antes de encerrar o reconhecimento, por padrão = 0.8

        audio = rec.listen(mic, timeout=10)
        print("Captura de áudio concluída. Reconhecendo...")

        texto = rec.recognize_google(audio, language='pt-BR')
        print(f"Texto reconhecido: {texto}")

    except sr.UnknownValueError:
        print("Não entendi.")

    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")

    except Exception as e:
        print(f"Erro desconhecido: {e}")

