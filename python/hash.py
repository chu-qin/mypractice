import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

for page_num in range(1, 11):  # 查询页数：1-10页
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