import telebot

#token = "491287822:AAHSo7d7j6unkuUCrm5xgA99slx8IH0sIIw"
bot = telebot.TeleBot("491287822:AAHSo7d7j6unkuUCrm5xgA99slx8IH0sIIw")

@bot.message_handler(commands=['start', 'help', 'w'])
#def send_welcome(message):
	#bot.reply_to(message, "Введите нужное слово, пожалуйста")

#@bot.message_handler(commands=['w'])
def w(message):
    #a = input()
    file_read = open("/home/arsolga/Documents/Ozhegov/ozhegov_part.txt", "r+")
    dict_l = {}

    for line in file_read:
        tmp_lst = line.split("|")
        tmp_lst = str(tmp_lst)
        tmp_sems = tmp_lst[1:(tmp_lst.find(","))]
        voc_entry = line[(line.find("|")):(line.rfind("\n"))].replace("|||||", " ")

        dict_o = {tmp_sems:voc_entry}
        dict_l.update(dict_o)
    bot.reply_to(message, dict_l["'абонимент'"])

    #print(dict_l)
    #print()
    #print(dict_l["'абонент'"])
    file_read.close()
    
bot.polling()
