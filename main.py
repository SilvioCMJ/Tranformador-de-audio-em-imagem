import openai
import SpeechRecognition as sr
#key individual da openai
openai.api_key = "sk-..."
#puxando audio
filename = "exemplo.mp3"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    #escutando o audio
    audio_data = r.record(source)
    #convertendo em texto
    text = r.recognize_google(audio_data)
    #transformando o txt em img
    response = openai.Image.create(prompt=text, n=1, size='1024x1024')

    img = response['data'][0]['url']
    print(f'URL da imagem gerada: {img}')

