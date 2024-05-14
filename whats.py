import pywhatkit
phone_number = 'seu_numero_de_telefone'
message = 'teste de mensagem em python  feito por  @letbarros2 ❤️😂 (https://github.com/letbarros2)'
hours = 19
minutes = 10
pywhatkit.sendwhatmsg(phone_number,message,hours,minutes)
print('Mensagem enviada!')
pywhatkit.start_server()

