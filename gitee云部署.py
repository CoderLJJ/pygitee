import requests
import time

d_url = "https://gitee.com/qzjiajia/仓库名/pages/rebuild"
check_url = "https://gitee.com/qzjiajia/仓库名/pages"
headers = {
    "Cookie":"",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "X-CSRF-Token":"p5FjYzU7NpTXq3HxUXh8PSuoHkTXMkaQER8Gq7VfIu0=",
    "X-Requested-With":"XMLHttpRequest"
    }
data = {
    "branch":"master",
    "build_directory":"",
    "force_https":"true"
    }

# 开始部署
res = requests.post(d_url,data=data,headers=headers)

# 判断是否部署成功
success = "正在部署，请耐心等待..."
if success in res.text:
    print(success)
    # 检测是否成功
    while 1:# 循环判断
        time.sleep(2) #延时2秒后再判断

        res = requests.post(check_url,data=data,headers=headers)
        pd = "已开启 Gitee Pages 服务"
        if pd in res.text:
            print(pd)
            break
        else:
            if success in res.text:
                print(success)
            else:
                print(res.text)
                print("发生未知错误！")
                input("回车退出！")#让小黑框停留一下
else:
    print(res.text)
    input("回车退出！")#让小黑框停留一下