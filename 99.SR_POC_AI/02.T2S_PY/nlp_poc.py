""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Proof of Concept    :   Voice Assistant with Cognitive AI to help complete Warehouse Operations.
Business Requirement:   1.  Get the input from User over microphone, covert the same 
                            to Text and interface with SAP EWM as input.
                        2.  Voice request for  inputs and promots for Error for user 
                            corrections.
                        3.  Train the AI model with L1/L2 Support, assisting the opertors 
                            on realtime exception handling and workarounds.
Developer           :   ROKKAMS(s.rokkam@sap.com) .
#GitReposit         :   https://github.com/sriramrokkam/texttospeech
# Backend Technologies:  
                    1. Azure -Cognitive AI      for NLP Services
                    2. SAP S4 Embedded EWM 9.3   for Warehouse Operations.
                    3. SAP ABAP                  for Server Side Validation.
                    4. Python 3.3               for Client Side Validations
#Integration Technologies:
                    1.Azure Event Hub
                    2.SAP ABAP Webhooks
                    3.Restful API's. 
                    
#Frontend Technologies:
                    1. SAP AppGyver
                    2. Django / CSS / JS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

# Service Class for fetching keys from Azure Cloud


class Get_Azure_Keys:
    def __init__(self):
        # Read Subscription keys and Region (.env)
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')
        print(cog_region)
        pass

# Create Child Class inheriting Get_Keys.


class S2T(Get_Azure_Keys):
    global speech_config

    def config_speech():
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(
            super().cog_key, super().cog_region)
        print('Ready to use speech service in:', speech_config.region)


# Create objects for classes.
obj_get_keys = Get_Azure_Keys()
obj_S2T = S2T()
print(obj_S2T.speech_config)
