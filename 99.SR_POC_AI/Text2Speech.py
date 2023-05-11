from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import os

load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')


def speech_synthesis_with_auto_language_detection_to_speaker(text):
    """performs speech synthesis to the default speaker with 
       auto language detection"""

    speech_config = speechsdk.SpeechConfig(
        subscription=cog_key, region=cog_region)

    # create the auto detection language configuration without specific languages
    auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig()

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, auto_detect_source_language_config=auto_detect_source_language_config)

    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
        stream = speechsdk.AudioDataStream(result)
        stream.save_to_wav_file(r"C:\05.TexttoSpeech\output.wav")


'''read_text = input("Enter Text to Read :")'''
read_text = "Sriram, gib mir zehn Rupien"

speech_synthesis_with_auto_language_detection_to_speaker(read_text)
