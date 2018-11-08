from wxpy import *
#bot = Bot ()

bot = Bot(cache_path=True)  # 扫码登陆,并保留登陆信息
tuling = Tuling(api_key='f39051ab03a74c308b8a5bcaca45d064')  # 初始化图灵机器人


@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)

# 自动回复功能，回复所有消息
bot.join()  # 开始运行