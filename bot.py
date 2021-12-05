import telebot

bot = telebot.TeleBot('Token of your bot') #Write Token here

class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator'] #Create a custom filter

#arrays of users
    
name = []
surname = []
age = []
idu = []

@bot.message_handler(commands=['reg']) #registration. At this step id of User written to the bot's memory
def get_reg(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What is your name?")
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name, idu
    idu.append(str(message.from_user.id))
    name.append(message.text)
    bot.send_message(message.from_user.id, 'What is your surname?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname.append(message.text)
    bot.send_message(message.from_user.id, 'How old are you?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age.append(message.text)
    bot.send_message(message.from_user.id, 'registration completed!')

@bot.message_handler(is_admin=True)
def all_admin(message):
    #Commands for everyone
    #
    #
    #Commands for admin
    #
    #


@bot.message_handler(content_types=['text'])
def all_text(message):
    #Commands for everyone
    #
    #

bot.add_custom_filter(IsAdmin()) #add your custom filter 

bot.infinity_polling() # check new messages

