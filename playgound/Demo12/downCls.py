import requests
from lxml.html import etree

file=open("221.232.159.27.har","r",encoding="utf8")
lines=file.read()
file.close()
# print(lines)

reqData=eval(lines)
pre_headers=reqData["log"]['entries'][0]["request"]["headers"]
url=reqData["log"]['entries'][0]["request"]["url"]
pre_data=reqData["log"]['entries'][0]["request"]["postData"]["params"]

url="http://10.254.0.75:3300/tjkbcx.aspx?xh=2016040121081&xm=%B7%B6%D0%CB%B9%FA&gnmkdm=N121601"

headers={}
for item in pre_headers:
    headers[item["name"]]=item["value"]

headers["Cookie"]="ASP.NET_SessionId=xugevd45d5siof45u3udim45"

data={}
for item in pre_data:
    data[item["name"]]=item["value"]

# file=open("sign.txt","r")
# sign=file.read()
# file.close()

data["__VIEWSTATE"]="dDwtMTQ0Mjk5MTgxMjt0PHA8bDx4c3p5ZG07PjtsPDE5MDI7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDE5PjtpPDIxPjtpPDIzPjtpPDI1Pjs+O2w8dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHhuO3huOz4+Oz47dDxpPDQ+O0A8MjAxOC0yMDE5OzIwMTctMjAxODsyMDE2LTIwMTc7MjAxNS0yMDE2Oz47QDwyMDE4LTIwMTk7MjAxNy0yMDE4OzIwMTYtMjAxNzsyMDE1LTIwMTY7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4cTt4cTs+Pjs+O3Q8aTwyPjtAPDE7Mjs+O0A8MTsyOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxuajtuajs+Pjs+O3Q8aTw3PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7Pj47bDxpPDI+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eW1jO3h5ZG07Pj47Pjt0PGk8MTA+O0A85py655S15bel56iL5a2m6ZmiO+eUteWtkOS/oeaBr+W3peeoi+WtpumZojvorqHnrpfmnLrnp5HlrablrabpmaI755Sf5ZG956eR5a2m5LiO5YyW5a2m5a2m6ZmiO+euoeeQhuWtpumZojvnu4/mtY7lrabpmaI75Lyg5aqS5LiO6Im65pyv6K6+6K6h5a2m6ZmiO+aWh+azleWtpumZojvlpJbor63lrabpmaI75Zu96ZmF5pWZ6IKy5a2m6ZmiOz47QDwxNzsxODsxOTsyMDsyMTsyMjsyMzsyNDsyNTsyNjs+PjtsPGk8Mj47Pj47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHp5bWM7enlkbTs+Pjs+O3Q8aTwxMT47QDzorqHnrpfmnLrnp5HlrabkuI7mioDmnK876L2v5Lu25bel56iLO+iuoeeul+acuuW6lOeUqOaKgOacryjkuJMpO+eJqeiBlOe9keW3peeoizvorqHnrpfmnLrnp5HlrabkuI7mioDmnK/vvIjkuK3ogYzmioDog73pq5jogIPvvIk76L2v5Lu25bel56iL77yI5Lic6L2v54m56Imy54+t77yJO+eJqeiBlOe9keW3peeoi++8iOaWh+aAnea1t+i+ieeJueiJsuePre+8iTvova/ku7blt6XnqIvvvIh677yJO+i9r+S7tuW3peeoi++8iGrvvIk7572R57uc56m66Ze05a6J5YWoO1xlOz47QDwxOTAxOzE5MDI7MTkwMzsxOTA0OzE5MDU7MTkwNjsxOTA3OzE5MDg7MTkwOTsxOTEwO1xlOz4+O2w8aTwxPjs+Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8dGprYm1jO3Rqa2JkbTs+Pjs+O3Q8aTw1PjtAPFxlOzE26L2v5Lu25bel56iLMeePrTsxNui9r+S7tuW3peeoizLnj607MTbova/ku7blt6XnqIsz54+tOzE26L2v5Lu25bel56iLNOePrTs+O0A8XGU7MjAxNjE5MDIyMDE4LTIwMTkxMTYxOTAyMTsyMDE2MTkwMjIwMTgtMjAxOTExNjE5MDIyOzIwMTYxOTAyMjAxOC0yMDE5MTE2MTkwMjM7MjAxNjE5MDIyMDE4LTIwMTkxMTYxOTAyNDs+PjtsPGk8Mj47Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8O2w8aTw1Pjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MT47aTwxPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+O2w8aTwwPjs+O2w8dDw7bDxpPDE+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOS4k+S4muWunuS5oDE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi9r+W4ne+8iOS8geS4mu+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NS4wOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMS0xODs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjs+Pjs+Pjs+NDQnL5Jn1NMzAIi5xALEnb5LXb8="


# if len(sign)<10:
#     data["__VIEWSTATE"]="dDwtMTQ0Mjk5MTgxMjt0PHA8bDx4c3p5ZG07PjtsPDE5MDI7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDE5PjtpPDIxPjtpPDIzPjtpPDI1Pjs+O2w8dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHhuO3huOz4+Oz47dDxpPDQ+O0A8MjAxOC0yMDE5OzIwMTctMjAxODsyMDE2LTIwMTc7MjAxNS0yMDE2Oz47QDwyMDE4LTIwMTk7MjAxNy0yMDE4OzIwMTYtMjAxNzsyMDE1LTIwMTY7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4cTt4cTs+Pjs+O3Q8aTwyPjtAPDE7Mjs+O0A8MTsyOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxuajtuajs+Pjs+O3Q8aTw3PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7Pj47bDxpPDI+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eW1jO3h5ZG07Pj47Pjt0PGk8MTA+O0A85py655S15bel56iL5a2m6ZmiO+eUteWtkOS/oeaBr+W3peeoi+WtpumZojvorqHnrpfmnLrnp5HlrablrabpmaI755Sf5ZG956eR5a2m5LiO5YyW5a2m5a2m6ZmiO+euoeeQhuWtpumZojvnu4/mtY7lrabpmaI75Lyg5aqS5LiO6Im65pyv6K6+6K6h5a2m6ZmiO+aWh+azleWtpumZojvlpJbor63lrabpmaI75Zu96ZmF5pWZ6IKy5a2m6ZmiOz47QDwxNzsxODsxOTsyMDsyMTsyMjsyMzsyNDsyNTsyNjs+PjtsPGk8NT47Pj47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHp5bWM7enlkbTs+Pjs+O3Q8aTwxMz47QDzph5Hono3lraY75Zu96ZmF57uP5rWO5LiO6LS45piTO+WbvemZhei0uOaYk+WunuWKoSjkuJMpO+mHkeiejeeuoeeQhuS4juWunuWKoe+8iOS4k++8iTvmiL/lnLDkuqfnu4/okKXnrqHnkIY75oi/5Zyw5Lqn5byA5Y+R5LiO566h55CGO+W3peeoi+mAoOS7t++8iOS4k++8iTvln47plYfop4TliJLvvIjkuJPvvIk76YeR6J6N5a2m77yIWu+8iTvph5Hono3nrqHnkIbvvIjkuJPvvIk76YeR6J6N5a2m77yIeu+8iTvnqI7mlLblraY7XGU7PjtAPDIyMDE7MjIwMjsyMjAzOzIyMDQ7MjIwNTsyMjA2OzIyMDc7MjIwODsyMjA5OzIyMTA7MjIxMTsyMjEyO1xlOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8dGprYm1jO3Rqa2JkbTs+Pjs+O3Q8aTw5PjtAPFxlOzE26YeR6J6N5a2mMeePrTsxNumHkeiejeWtpjLnj607MTbph5Hono3lraYz54+tOzE26YeR6J6N5a2mNOePrTsxNumHkeiejeWtpjXnj607MTbph5Hono3lraY254+tOzE26YeR6J6N5a2mN+ePrTsxNumHkeiejeWtpjjnj607PjtAPFxlOzIwMTYyMjAxMjAxOC0yMDE5MTE2MjIwMTE7MjAxNjIyMDEyMDE4LTIwMTkxMTYyMjAxMjsyMDE2MjIwMTIwMTgtMjAxOTExNjIyMDEzOzIwMTYyMjAxMjAxOC0yMDE5MTE2MjIwMTQ7MjAxNjIyMDEyMDE4LTIwMTkxMTYyMjAxNTsyMDE2MjIwMTIwMTgtMjAxOTExNjIyMDE2OzIwMTYyMjAxMjAxOC0yMDE5MTE2MjIwMTc7MjAxNjIyMDEyMDE4LTIwMTkxMTYyMjAxODs+PjtsPGk8MT47Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8O2w8aTw1Pjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDY+O2k8Nj47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47PjtsPHQ8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDAyMjAxMjE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDAyMjAxMjE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihpTAwMzA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCgyMDE4LTIwMTktMSktMDIyNDA3LTAyMjAxMjEtMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b6u6K++56iLMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YKx5pmT5oGLICjnu4/mtY7lrabpmaIpJm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YKx5pmT5oGLICjnu4/mtY7lrabpmaIp5ZGoNeesrDHoioLov57nu60y6IqCe+esrDE1LTE15ZGo5Y2V5ZGofS8yLTIwMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxOC0xMS0yOC0wOC01ODs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDAyMkwwNjk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDAyMkwwNjk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiwgzAwMDM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCgyMDE4LTIwMTktMSktMDIyMTQ0LTAyMkwwNjktMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85ZWG5Lia6ZO26KGM57uP6JCl566h55CGOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvpDmhafmlY8o57uP5rWO5a2m6ZmiKeWRqDPnrKwz6IqC6L+e57utMuiKgnvnrKwxLTHlkah9LzItMjA0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvpDmhafmlY8o57uP5rWO5a2m6ZmiKeWRqDXnrKw16IqC6L+e57utMuiKgnvnrKwyLTLlkajlj4zlkah9LzItMjA2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyMDE4LTA5LTA1LTExLTIzOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MDIyTDA0NDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDIyTDA0NDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86LCDMDIwMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8KDIwMTgtMjAxOS0xKS0wMjIzOTYtMDIyTDA0NC0xOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkupLogZTnvZHph5Hono07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWImOS9syjnu4/mtY7lrabpmaIp5ZGoMeesrDHoioLov57nu60y6IqCe+esrDQtNOWRqH0vMy01MDQ7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWImOS9syjnu4/mtY7lrabpmaIp5ZGoNeesrDfoioLov57nu60y6IqCe+esrDQtNOWRqH0vMi0yMDk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTgtMDktMjEtMDktMTE7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwwMjEwMTEwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMjEwMTEwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosIMwOTYxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwoMjAxOC0yMDE5LTEpLTAyMTE0Ny0wMjEwMTEwLTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+S4muWfuuehgDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pu56ZuoKOeuoeeQhuWtpumZoinlkag256ysN+iKgui/nue7rTLoioJ756ysMy0z5ZGofS8zLTMwMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pu56ZuoKOeuoeeQhuWtpumZoinlkag256ysN+iKgui/nue7rTLoioJ756ysMTAtMTDlkajlj4zlkah9LzItNDExOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyMDE4LTExLTA3LTA5LTEzOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MDIyMDAzMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDIyMDAzMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86LCDMTExMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8KDIwMTgtMjAxOS0xKS0wMjIxMDEtMDIyMDAzMS0xOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzorqHph4/nu4/mtY7lrablrp7orq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtmeS4vSjnu4/mtY7lrabpmaIp5ZGoNOesrDHoioLov57nu60y6IqCe+esrDEzLTEz5ZGofS/lrp5ENDAxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlrZnkuL0o57uP5rWO5a2m6ZmiKeWRqDTnrKwz6IqC6L+e57utMuiKgnvnrKwxNC0xNOWRqOWPjOWRqH0v5a6eRDQwMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxOC0xMS0yOC0xNi0wNTs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDAyMjAxMjE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWBnDAwMjM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCgyMDE4LTIwMTktMSktMDIyNDA3LTAyMjAxMjEtMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b6u6K++56iLMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YKx5pmT5oGLICjnu4/mtY7lrabpmaIp5ZGoNeesrDPoioLov57nu60y6IqCe+esrDktOeWRqH0vMi0zMTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTgtMTAtMjktMDgtNTY7Pj47Pjs7Pjs+Pjs+Pjs+Pjs+Pjs+Pjs+YQ/6ueST413xiEWf+xICtPs5O4A="
# else:
#     data["__VIEWSTATE"]=sign
#
majors=[]
for nj in range(2015,2019):
    data["nj"]=str(nj)
    for xy in range(17,27):
        data['xy']=str(xy)
        resp=requests.post(url,headers=headers,data=data)
        html = resp.content.decode("gb2312","ignore")
        htmlE = etree.HTML(html)
        sign = htmlE.xpath('//input[@name="__VIEWSTATE"]')[0].get('value')
        data["__VIEWSTATE"]=sign
        zys=htmlE.xpath('//select[@name="zy"]//option/@value')
        print(zys)
        for zy in zys:
            if len(zy)>1:
                data["zy"]=str(zy)
                data["__EVENTTARGET"]="zy"
                print(data["zy"])
                resp1=requests.post(url,headers=headers,data=data)
                html1=resp1.content.decode("gb2312","ignore")
                print(html1)
                htmlE1 = etree.HTML(html1)
                sign1 = htmlE1.xpath('//input[@name="__VIEWSTATE"]')[0].get('value')
                data["__VIEWSTATE"] = sign1
                kbvs=htmlE1.xpath('//select[@name="kb"]//option/@value')
                print(kbvs)
                for kbv in kbvs:
                    if len(kbv)>1:
                        data["kb"]=kbv
                        resp2 = requests.post(url, headers=headers, data=data)
                        try:
                            html2 = resp2.content.decode("gb2312","ignore")
                            htmlE2 = etree.HTML(html2)
                            sign2 = htmlE2.xpath('//input[@name="__VIEWSTATE"]')[0].get('value')
                            data["__VIEWSTATE"] = sign2
                            print(html2)
                        except:
                            print(data)
                            exit(0)


print(majors)












# data['xn']= '2018-2019'
# data['xq'] ='1'
# data['nj']='2016'
# data["__EVENTTARGET"]="zy"
# data['xy']='17'
# data['zy']='1707'
# data['kb']=''
# data['xq']='1'
# data['xn']='2018-2019'
#
# data["__VIEWSTATE"]="dDwtMTQ0Mjk5MTgxMjt0PHA8bDx4c3p5ZG07PjtsPDE5MDI7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDE5PjtpPDIxPjtpPDIzPjtpPDI1Pjs+O2w8dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHhuO3huOz4+Oz47dDxpPDQ+O0A8MjAxOC0yMDE5OzIwMTctMjAxODsyMDE2LTIwMTc7MjAxNS0yMDE2Oz47QDwyMDE4LTIwMTk7MjAxNy0yMDE4OzIwMTYtMjAxNzsyMDE1LTIwMTY7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4cTt4cTs+Pjs+O3Q8aTwyPjtAPDE7Mjs+O0A8MTsyOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxuajtuajs+Pjs+O3Q8aTw3PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7Pj47bDxpPDI+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eW1jO3h5ZG07Pj47Pjt0PGk8MTA+O0A85py655S15bel56iL5a2m6ZmiO+eUteWtkOS/oeaBr+W3peeoi+WtpumZojvorqHnrpfmnLrnp5HlrablrabpmaI755Sf5ZG956eR5a2m5LiO5YyW5a2m5a2m6ZmiO+euoeeQhuWtpumZojvnu4/mtY7lrabpmaI75Lyg5aqS5LiO6Im65pyv6K6+6K6h5a2m6ZmiO+aWh+azleWtpumZojvlpJbor63lrabpmaI75Zu96ZmF5pWZ6IKy5a2m6ZmiOz47QDwxNzsxODsxOTsyMDsyMTsyMjsyMzsyNDsyNTsyNjs+PjtsPGk8MD47Pj47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHp5bWM7enlkbTs+Pjs+O3Q8aTwxMj47QDznlLXmsJTlt6XnqIvlj4rlhbboh6rliqjljJY75py65qKw6K6+6K6h5Yi26YCg5Y+K5YW26Ieq5Yqo5YyWO+acuuaisOWItumAoOS4juiHquWKqOWMlijkuJMpO+acuueUteS4gOS9k+WMluaKgOacryjkuJMpO+aVsOaOp+aKgOacryjkuJMpO+iHquWKqOWMljvmnLrmorDnlLXlrZDlt6XnqIs75py65qKw6K6+6K6h5Yi26YCg5Y+K5YW26Ieq5Yqo5YyW77yI5pSv5o+05Lit6KW/6YOo5Y2P5L2c77yJO+acuuaisOiuvuiuoeWItumAoOWPiuWFtuiHquWKqOWMlu+8iOS4reiBjOaKgOiDvemrmOiAg++8iTvnlLXmsJTlt6XnqIvlj4rlhbboh6rliqjljJbvvIh677yJO+eUteawlOW3peeoi+WPiuWFtuiHquWKqOWMlihqKTtcZTs+O0A8MTcwMTsxNzAyOzE3MDM7MTcwNDsxNzA1OzE3MDY7MTcwNzsxNzA4OzE3MDk7MTcxMDsxNzExO1xlOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8dGprYm1jO3Rqa2JkbTs+Pjs+O3Q8aTwzPjtAPFxlOzE255S15rCU5bel56iL5Y+K5YW26Ieq5Yqo5YyWMeePrTsxNueUteawlOW3peeoi+WPiuWFtuiHquWKqOWMljLnj607PjtAPFxlOzIwMTYxNzAxMjAxOC0yMDE5MTE2MTcwMTE7MjAxNjE3MDEyMDE4LTIwMTkxMTYxNzAxMjs+PjtsPGk8MT47Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8O2w8aTw1Pjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDQ+O2k8ND47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MDE3MDAzMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDE3MDAzMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86LCDMDM2MTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8KDIwMTgtMjAxOS0xKS0wMTcxMTctMDE3MDAzMy0xOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlLXmsJTlt6XnqIvln7rnoYA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaxquazoijmnLrnlLXlt6XnqIvlrabpmaIp5ZGoMeesrDPoioLov57nu60y6IqCe+esrDQtNOWRqH0vMi0yMTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaxquazoijmnLrnlLXlt6XnqIvlrabpmaIp5ZGoN+esrDPoioLov57nu60y6IqCe+esrDQtNOWRqOWPjOWRqH0vMi0zMTM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTgtMDktMjUtMjAtNTc7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwwMTcwMDM0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMTcwMDM0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosIMwNjIyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwoMjAxOC0yMDE5LTEpLTAxNzA5NC0wMTcwMDM0LTE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeUteWKm+eUteWtkOWfuuehgOWunumqjDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85ZSQ5YuHKOacuueUteW3peeoi+WtpumZoinlkag156ysNeiKgui/nue7rTLoioJ756ysOC045ZGofS/np5FEMzAyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzllJDli4co5py655S15bel56iL5a2m6ZmiKeWRqDbnrKw16IqC6L+e57utMuiKgnvnrKw5LTnlkajljZXlkah9L+enkUQzMDI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTgtMTAtMjItMTAtMDY7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwwMTcwMDM0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMTcwMDM0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosIMwNjIzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwoMjAxOC0yMDE5LTEpLTAxNzA5NC0wMTcwMDM0LTE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeUteWKm+eUteWtkOWfuuehgOWunumqjDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85ZSQ5YuHKOacuueUteW3peeoi+WtpumZoinlkag156ysN+iKgui/nue7rTLoioJ756ysOC045ZGofS/np5FEMzAyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzllJDli4co5py655S15bel56iL5a2m6ZmiKeWRqDbnrKw36IqC6L+e57utMuiKgnvnrKw5LTnlkajljZXlkah9L+enkUQzMDI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTgtMTAtMjItMTAtMDY7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwwMjEwMDU0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMjEwMDU0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosIMwOTE2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwoMjAxOC0yMDE5LTEpLTAyMTE0Ny0wMjEwMDU0LTQ7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+S4muWfuuehgDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b6Q5b2sKOeuoeeQhuWtpumZoinlkag256ysM+iKgui/nue7rTLoioJ756ysMy0z5ZGofS8zLTQxMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b6Q5b2sKOeuoeeQhuWtpumZoinlkag056ysOeiKgui/nue7rTLoioJ756ysMTAtMTDlkajlj4zlkah9LzItNDExOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyMDE4LTExLTAyLTIzLTQxOz4+Oz47Oz47Pj47Pj47Pj47Pj47Pj47Ppoa4XGPnH0eRg72JrRcQ4DMiXni"
# print(data)




# resp=requests.post(url,headers=headers,data=data)
# html=resp.content.decode("gb2312")


# htmlE=etree.HTML(html)
# sign=htmlE.xpath('//input[@name="__VIEWSTATE"]')[0].get('value')
# print(sign)

# file=open("sign.txt","w+",encoding="utf-8")
# file.write(sign)
# file.close()

# print("123")
# print(headers)
# html=requests.get(url,headers=headers).content.decode("gb2312")

# print(html)
# print(sign)

# data["__VIEWSTATE"]=sign



# print(headers)

# url="http://10.254.0.75:3300/tjkbcx.aspx?xh=2016040121081&xm=%B7%B6%D0%CB%B9%FA&gnmkdm=N123101"
# data={'__EVENTTARGET': 'zy', '__EVENTARGUMENT': '', '__VIEWSTATE': 'dDwtMTQ0Mjk5MTgxMjt0PHA8bDx4c3p5ZG07PjtsPDE5MDI7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDE5PjtpPDIxPjtpPDIzPjtpPDI1Pjs+O2w8dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHhuO3huOz4+Oz47dDxpPDQ+O0A8MjAxOC0yMDE5OzIwMTctMjAxODsyMDE2LTIwMTc7MjAxNS0yMDE2Oz47QDwyMDE4LTIwMTk7MjAxNy0yMDE4OzIwMTYtMjAxNzsyMDE1LTIwMTY7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4cTt4cTs+Pjs+O3Q8aTwyPjtAPDE7Mjs+O0A8MTsyOz4+O2w8aTwwPjs+Pjs7Pjt0PHQ8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxuajtuajs+Pjs+O3Q8aTw3PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7PjtAPDIwMTg7MjAxNzsyMDE2OzIwMTU7MjAxNDsyMDEzOzIwMTI7Pj47bDxpPDM+Oz4+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eW1jO3h5ZG07Pj47Pjt0PGk8MTA+O0A85py655S15bel56iL5a2m6ZmiO+eUteWtkOS/oeaBr+W3peeoi+WtpumZojvorqHnrpfmnLrnp5HlrablrabpmaI755Sf5ZG956eR5a2m5LiO5YyW5a2m5a2m6ZmiO+euoeeQhuWtpumZojvnu4/mtY7lrabpmaI75Lyg5aqS5LiO6Im65pyv6K6+6K6h5a2m6ZmiO+aWh+azleWtpumZojvlpJbor63lrabpmaI75Zu96ZmF5pWZ6IKy5a2m6ZmiOz47QDwxNzsxODsxOTsyMDsyMTsyMjsyMzsyNDsyNTsyNjs+PjtsPGk8NT47Pj47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPHp5bWM7enlkbTs+Pjs+O3Q8aTwxMz47QDzph5Hono3lraY75Zu96ZmF57uP5rWO5LiO6LS45piTO+WbvemZhei0uOaYk+WunuWKoSjkuJMpO+mHkeiejeeuoeeQhuS4juWunuWKoe+8iOS4k++8iTvmiL/lnLDkuqfnu4/okKXnrqHnkIY75oi/5Zyw5Lqn5byA5Y+R5LiO566h55CGO+W3peeoi+mAoOS7t++8iOS4k++8iTvln47plYfop4TliJLvvIjkuJPvvIk76YeR6J6N5a2m77yIWu+8iTvph5Hono3nrqHnkIbvvIjkuJPvvIk76YeR6J6N5a2m77yIeu+8iTvnqI7mlLblraY7XGU7PjtAPDIyMDE7MjIwMjsyMjAzOzIyMDQ7MjIwNTsyMjA2OzIyMDc7MjIwODsyMjA5OzIyMTA7MjIxMTsyMjEyO1xlOz4+O2w8aTwxPjs+Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8dGprYm1jO3Rqa2JkbTs+Pjs+O3Q8aTwzPjtAPFxlOzE15Zu96ZmF57uP5rWO5LiO6LS45piTMeePrTsxNeWbvemZhee7j+a1juS4jui0uOaYkzLnj607PjtAPFxlOzIwMTUyMjAyMjAxOC0yMDE5MTE1MjIwMjE7MjAxNTIyMDIyMDE4LTIwMTkxMTUyMjAyMjs+PjtsPGk8MD47Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8O2w8aTw1Pjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MT47aTwxPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+O2w8aTwwPjs+O2w8dDw7bDxpPDE+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOS4k+S4mu+8iOeUn+S6p++8ieWunuS5oDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85byg55C8Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMS0xODs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDI+O2k8Mj47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwwMjJMMDU4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMjJMMDU4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosIMwMzI0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwoMjAxOC0yMDE5LTEpLTAyMjE2NC0wMjJMMDU4LTQ7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWkluaxh+S6pOaYkzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85ZGo6I6O5Li9KOe7j+a1juWtpumZoinlkagx56ysMeiKgui/nue7rTLoioJ756ysNC005ZGofS8yLTQwMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85ZGo6I6O5Li9KOe7j+a1juWtpumZoinlkag156ysMeiKgui/nue7rTLoioJ756ysNi025ZGo5Y+M5ZGofS8yLTIxMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxOC0wOS0yNS0xMS0xMjs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDAyMkwwNTg7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDAyMkwwNTg7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiwgzAzMjU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCgyMDE4LTIwMTktMSktMDIyMTY0LTAyMkwwNTgtNDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85aSW5rGH5Lqk5piTOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlkajojo7kuL0o57uP5rWO5a2m6ZmiKeWRqDHnrKw16IqC6L+e57utMuiKgnvnrKw0LTTlkah9LzItNDEzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlkajojo7kuL0o57uP5rWO5a2m6ZmiKeWRqDPnrKwz6IqC6L+e57utMuiKgnvnrKw0LTTlkah9LzItMTAzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyMDE4LTA5LTI1LTExLTEzOz4+Oz47Oz47Pj47Pj47Pj47Pj47Pj47Pp3zXv8g2OvjrahZ3SagGuW2lMON', 'xn': '2018-2019', 'xq': '1', 'nj': '2015', 'xy': '22', 'zy': '2202', 'kb': '201522022018-201911522021'}

#
#
# resp=requests.post(url,headers=headers,data=data)
# resp=requests.get(url,headers=headers)
# #
# print(resp.content.decode("gb2312","ignore"))