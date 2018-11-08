from wxpy import *
#bot = Bot ()

bot = Bot(cache_path=True)  # 扫码登陆,并保留登陆信息
#tuling = Tuling(api_key='f39051ab03a74c308b8a5bcaca45d064')  # 初始化图灵机器人

friend = bot.friends().search(u'予你')[0]
friend.send(u"dsb")
#指定某个好友并向其发送消息

#@bot.register()
#def reply_msg(msg):
#    msg.reply(u'本人正忙，请稍后回复')
#embed()
# 统一回复

#@bot.register(msg_types=TEXT)
#def auto_reply_all(msg):
#    tuling.do_reply(msg)
# 自动回复功能，回复所有消息
#bot.join()  # 开始运行
