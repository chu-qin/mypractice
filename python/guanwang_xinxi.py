import requests
import hashlib
from bs4 import BeautifulSoup

def get_page_hash(url):
    # 获取网页内容
    response = requests.get(url)
    content = response.text
    hasher = hashlib.sha256()# 创建哈希对象（推荐使用SHA-256）
    hasher.update(content.encode('utf-8'))# 更新哈希内容（需要编码为字节）
    return hasher.hexdigest()# 获取十六进制哈希值

'''headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}#伪装浏览器访问
for list_nun in range(1,11):#查询页数：1-页（左闭右开）
    response = requests.get(f"https://it.chd.edu.cn/7382/list{list_nun}.htm",headers=headers)
    response.encoding="utf-8"#强制UTF—8编码，防止汉字无法正常显示
    html=response.text
    soup = BeautifulSoup(html,"html.parser")#用该函数解析网页源码

    times = soup.findAll("span", attrs={"class":"right"})
    titles = soup.findAll("a", attrs={"class":"left"})
    arr_time =[]
    arr_title = []
    for a in times:
        atime = a.string
        time = atime.strip()
        arr_time.append(time)
    for b in titles:
        btitle = b.string
        title = btitle.strip()
        arr_title.append(title)
    for i in range(0,14):
        print(arr_time[i],arr_title[i])

current_hash = get_page_hash("https://it.chd.edu.cn/7382/list1.htm")
print(current_hash)
'''
#优化后代码
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

for page_num in range(1, 3):  # 查询页数：1-10页
    url = f"https://it.chd.edu.cn/7382/list{page_num}.htm"
    try:
        response = requests.get(url, headers=headers, timeout=5)  # 添加超时
        response.encoding = "utf-8"  # 强制 UTF-8 编码
        soup = BeautifulSoup(response.text, "html.parser")

        # 使用列表推导式提取时间和标题，并直接 strip()
        times = [span.get_text(strip=True) for span in soup.find_all("span", class_="right")]
        titles = [a.get_text(strip=True) for a in soup.find_all("a", class_="left")]

        # 确保时间和标题数量一致，避免 IndexError
        min_length = min(len(times), len(titles))
        for i in range(min_length):
            print(f"时间: {times[i]}, 标题: {titles[i]}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败（第 {page_num} 页）: {e}")
        continue  # 跳过当前页，继续下一页