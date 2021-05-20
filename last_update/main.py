import telegram
from telegram import message
from telegram.constants import CHATMEMBER_RESTRICTED
import init
import inf
from inf import system_vars as env
from mwt import MWT
from telegram import *
from telegram.ext import *
import time as time_
import random
import time


#value goes for 6
bot = Bot(env.API_KEY)

print(bot.get_me())
updater=Updater(env.API_KEY,use_context=True)
dispatcher=updater.dispatcher





class static:
    var_tr=8

@MWT(timeout=60*60)
def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]



def test(context:CallbackContext):
    if env.interval_key:
        ids = env.chat_id
        messages_interval=env.interval_message
        for id_ in ids:
            if not len(messages_interval)==0:
                for mi in messages_interval:
                    bot.send_message(chat_id=id_,text=str(mi))
    else:
        return None
def start1(update:Update,context:CallbackContext):
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):       
        env.chat_id.insert(env.chat_id_count,update.effective_chat.id)
        env.chat_id_count=env.chat_id_count+1
        bot.send_message(chat_id=update.effective_chat.id,text="interval massage activated")
        updater.job_queue.run_repeating(test, env.interval_message_time, context=update)
    else:
        bot.send_message(chat_id=update.effective_chat.id,text="only admins are allowed to activate this!")

start1_=CommandHandler('start_interval',start1,pass_job_queue=True)
dispatcher.add_handler(start1_)










def admin_s(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text="successfully changed admin mode")
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        init.switch_user()

start_value1=CommandHandler('admin_switch',admin_s)
dispatcher.add_handler(start_value1)
##################
#ENABLE OR DISABLE CAPTCHA
def d_captcha(update:Update,context:CallbackContext): 
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        init.d_cap()
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="captcha disabled")
    else:
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="sorry only admins can use this commands")

start_value5=CommandHandler('d_cap',d_captcha)
dispatcher.add_handler(start_value5)

def e_captcha(update:Update,context:CallbackContext):
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        init.e_cap()
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="captcha enabled")
    else:
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="sorry only admins can use this commands")

start_value6=CommandHandler('e_cap',e_captcha)
dispatcher.add_handler(start_value6)

########################


##################
#ENABLE OR DISABLE INTERVAL
def d_intv(update:Update,context:CallbackContext): 
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        env.interval_key=False
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="interval disabled")
    else:
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="sorry only admins can use this commands")

start_value7=CommandHandler('d_cap',d_captcha)
dispatcher.add_handler(start_value7)

def e_intv(update:Update,context:CallbackContext):
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        env.interval_key=True
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="interval enabled")
    else:
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="sorry only admins can use this commands")

start_value8=CommandHandler('e_cap',e_captcha)
dispatcher.add_handler(start_value8)

########################




def callback_alarm(context: telegram.ext.CallbackContext):
  bot.send_message(chat_id=id, text='Hi, This is a daily reminder')

start_value3=CommandHandler('start',callback_alarm)
dispatcher.add_handler(start_value3)

#@restricted
def echo(update:Update,context:CallbackContext):
   # context.job_queue.run_daily(callback_alarm, time, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None, job_kwargs=None)
    query=update.message.text
    info=bot.getChatMember
    print(info)
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id) and not inf.system_vars.admin_to_general:
        print('admin')
    else:
        http_valid=init.is_other_links(query,update.message.chat.id)
        is_eng=init.language_detect(query)
        if not is_eng:
            bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text=env.if_not_english)
            return 0
        c_val=env.r1[0]+env.r1[1]
        if f'captcha {c_val}' in str(query):
            init.captcha_(query)
            if init.captcha_(query):
                time.sleep(2)
                bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text="thanks for solving the captcha")



        forbidden_lan = init.if_it_is_forbidden_language(query)
        print(forbidden_lan)
        if forbidden_lan:
            user = update.message.from_user
            print('forbidden lan')
            user_id=update.effective_user.id
            bot.kick_chat_member(update.message.chat.id,user_id=user_id,revoke_messages=True)
            return 0

        d=init.give_coustom_messages(query)
        if not len(d)==0:
            for x,y in d.items():
                for i in y:
                    bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text=str(i))
        
        if not http_valid:
            print(update.message.chat.id)
            first_name = update.message.chat.first_name
            user = update.message.from_user
            print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
            t=user['username']
            bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text=f'{t}\n please dont post links')
            time.sleep(3)
            bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
        if env.captcha_is_enabled and not update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
            print('captcha is now on enabled')
            user_id_ = env.new_user[1]
            id_= env.new_user[0]
            bot.kickChatMember(id_,user_id=user_id_)
       

dispatcher.add_handler(MessageHandler(Filters.text,echo))





    ###################################################



def new_member(update:Update,context:CallbackContext):
    if env.captcha_required and not update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        time_.sleep(5)
        bot.send_message(chat_id=update.effective_chat.id,text="welcome")
        time_.sleep(2)
        bot.send_message(chat_id=update.effective_chat.id,text="Please solve the captcha")
        time_.sleep(2)
        env.new_user[0]=update.effective_chat.id
        env.new_user[1]=update.effective_user.id
        env.r1[0]=random.randint(0,22)
        re1=env.r1[0]
        env.r1[1]=random.randint(0,50)
        re2=env.r1[1]
        env.captcha_is_enabled=True
        m=f'{re1}+{re2}\nPlease solve the sum..'
        bot.send_message(chat_id=update.effective_chat.id,text=str(m))
        bot.send_message(chat_id=update.effective_chat.id,reply_to_message_id=update.message.message_id,text=f'{re1}+{re2}\nPlease solve the sum..\ngive your answer by typing \ncaptcha then type space then type your answer')
    else:
        return None    


    



updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))









updater.start_polling()
updater.idle()