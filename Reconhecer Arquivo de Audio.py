import speech_recognition as sr

# Criar um recognizer
rec = sr.Recognizer()

with sr.AudioFile('audio.wav') as arquivo_audio:
    try:
        audio = rec.record(arquivo_audio)
        print('Reconhecendo áudio')

        texto = rec.recognize_google(audio, language='pt-BR')
        print(f"Texto reconhecido: {texto}")

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")

    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")

    except Exception as e:
        print(f"Erro desconhecido: {e}")
