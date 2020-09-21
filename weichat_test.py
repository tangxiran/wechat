from wxpy import *
import re

# 生成机器人实例，启动缓存避免重复登录
bot = Bot(cache_path=False)
# 在好友列表中搜索名字是‘Girl【你自己设置的备注名】'性别为男的一项
found = bot.friends().search('唐翕然', sex=1)
# 确保只有一个结果
friend = ensure_one(found)

bf_rules = {
    r'呵': '呵*999',

}


@bot.register([friend, bot.self], msg_types=TEXT, except_self=True)
def reply_bf(msg):
    for rule in bf_rules:
        if re.match(rule, msg.text):
            try:
                # 尝试向消息发送者回复消息
                msg.sender.send_msg(bf_rules[rule])
            except ResponseError as e:
                # 查看错误号和错误消息
                print(e.err_code, e.err_msg)
            return
    return '我有点笨，能不能迁就下我，我们说点别的？'


# 进入 python 命令行、让程序保持运行
embed()