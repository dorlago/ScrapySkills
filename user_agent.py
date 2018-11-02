# 构造随机请求头

from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
print(ua.random)