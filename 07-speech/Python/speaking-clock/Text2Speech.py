from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
speech_key="37d48b0c67b74a87b7eb5ad2b788c335"
service_region="eastasia"

def speech_synthesis_with_auto_language_detection_to_speaker(text):
    """performs speech synthesis to the default speaker with auto language detection
       Note: this is a preview feature, which might be updated in future versions."""
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

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
            stream.save_to_wav_file(r"C:\Users\user\Desktop\outputfff.wav")

speech_synthesis_with_auto_language_detection_to_speaker("హలో గౌతమి. నేను ఒక AI రోబోట్! నా పేరు శ్రీరామ్! మీరు ఏలా ఉన్నారు ?")