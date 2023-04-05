import creds
from pyChatGPT import ChatGPT

from ..utils import pdf_parser 

api = ChatGPT(creds.session_token)  # auth with session token



mensaje= pdf_parser.single_line_text
resp = api.send_message("Por favor haz un resumen de 5 lineas de la siguiente clase, da un salto de linea, escribe el nombre de la nueva seccion y luego señala conceptos importantes con sus definiciones: \n " + mensaje)

print("\n\n\n" + resp['message'])

# write response to a file

# Open a file in append mode
with open('response.txt', 'a') as f:
    # Append some text to the file
    f.write(resp['message'])



api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page

