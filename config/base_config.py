# 基础配置
# current only xueqiu
PLATFORM = "xueqiu"
# qrcode or phone or cookie
LOGIN_TYPE = "qrcode"
# cookies
COOKIES = ""
# 爬取类型 stock: 股票
CRAWLER_TYPE = "stock"

# 是否开启 IP 代理
ENABLE_IP_PROXY = False
# 代理IP池数量
IP_PROXY_POOL_COUNT = 2
# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "jishuhttp"

# 设置为True不会打开浏览器（无头浏览器），设置False会打开一个浏览器（小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码）
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# mysql配置
RELATION_DB_URL = ""

# redis配置
REDIS_DB_HOST = ""
REDIS_DB_PWD = ""

# 数据保存类型选项配置,支持三种类型：csv、db、json
# csv or db or json
SAVE_DATA_OPTION = "json"
