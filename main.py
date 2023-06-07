from login import  LOGIN, get_COOK
from get_uid import UID
from book import BOOK
from submit import submit
from start import RUN
from time import sleep
# book = BOOK["全新版大学进阶英语：综合教程4（思政智慧版）"]
# account = "15517434286"
# pwd = "azj123456"
# account = "19987662119"
# pwd = "20031018ysm"
# account = '18781229161'
# pwd = 'LL545464'
# cid = book['cid']
# scoid = book['sco']

# login = LOGIN(account=account, pwd=pwd)
# uid = UID(cid=cid)

# for i in scoid:
#     submit(cid=cid,uid=uid,scoid = i, cookies=COOKIES)
#     print(i)


if __name__ == "__main__":
    account = input("请输入账号：\n")
    pwd = input("请输入密码：\n")
    cookies = get_COOK()
    try:
        login = LOGIN(account=account, pwd=pwd, cookies=cookies)
    except:
        print("密码错误，请重新登陆！")
        sleep(3)
        exit()

    books = list(BOOK.keys())
    while(True):
        [print(f"{books.index(i)+1}：{i}") for i in books]
        num = int(input(f"请输入所选书籍序列(1-{len(books)})：\n"))
        try:
            book = BOOK[books[num-1]]
            break
        except:
            print("序号输入错误，请重新输入!")
    cid = book['cid']
    scoid = book['sco']
    uid = UID(cid=cid, cookies=cookies)
    print(uid)
    print("开始刷课:\n")
    print(f"准备{len(scoid)}")
    for i in scoid:
        RUN(cid= cid, scoid = i  , uid = uid, cookies = cookies).start()
    while(True):
        pass


