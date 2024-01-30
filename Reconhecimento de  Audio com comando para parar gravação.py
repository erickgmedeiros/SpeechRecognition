import speech_recognition as sr
import time

fim = False
# Criar um recognizer
rec = sr.Recognizer()

def tratar_audio(rec, audio):
    global fim
    try:
        frase_fim = 'encerrar gravação'
        texto = rec.recognize_google(audio, language='pt-BR')
        print(f"{texto}")
        if frase_fim in texto:
            fim = True

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")

    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")

    except Exception as e:
        print(f"Erro desconhecido: {e}")

# Listar os microfones disponíveis
#print(sr.Microphone.list_microphone_names())

def reconhecimento_fala():
    global fim
    mic_index = 0  # escolher o microfone desejado
    with sr.Microphone(device_index=mic_index) as mic:
            rec.adjust_for_ambient_noise(mic, duration=1)
            rec.dynamic_energy_adjustment_ratio = 3
            print('Pode começar a falar, para encerrar a transcrição basta falar "encerrar gravação"')

    try:
        #thread 1
        parar_ouvir = rec.listen_in_background(mic, tratar_audio) 

        # thread 2
        while True:
            time.sleep(0.1)
            if fim: # falar 'encerrar gravação'
                break

        # thread 1
        parar_ouvir(wait_for_stop= False)
        print('\n----Transcrição encerrada----')

    except Exception as e:
            print(f"Erro: {e}")

reconhecimento_fala()


    