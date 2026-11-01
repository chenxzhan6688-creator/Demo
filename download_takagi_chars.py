import os
import requests

save_dir = "takagi_characters"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Bangumi 官方开放 API：《高木同学》(Subject ID: 103803) 的角色列表
api_url = "https://api.bgm.tv/v0/subjects/103803/characters"

headers = {
    "User-Agent": "MyAnimeSpider/1.0 (contact: test@example.com)"
}

print("正在通过 Bangumi 官方 API 获取角色数据...")

try:
    res = requests.get(api_url, headers=headers, timeout=10)
    if res.status_code == 200:
        characters = res.json()
        print(f"成功获取到 {len(characters)} 个角色数据，开始下载图片...\n")

        for idx, char in enumerate(characters, 1):
            name = char.get("name", f"character_{idx}")
            # 优先使用中文译名
            if char.get("name_cn"):
                name = char["name_cn"]

            # 清理文件名中的非法字符
            for c in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
                name = name.replace(c, "_")

            # 拿高清大图链接 (images -> large)
            images = char.get("images", {})
            img_url = images.get("large") or images.get("medium") or images.get("grid")

            if img_url:
                try:
                    img_data = requests.get(img_url, headers=headers, timeout=10).content
                    file_path = os.path.join(save_dir, f"{name}.jpg")
                    with open(file_path, "wb") as f:
                        f.write(img_data)
                    print(f"[{idx}] 成功下载角色: {name}.jpg")
                except Exception as e:
                    print(f"[{idx}] {name} 下载失败: {e}")
            else:
                print(f"[{idx}] {name} 没有图片")

        print(f"\n全部下载完毕！快去 '{save_dir}' 文件夹看看吧！")
    else:
        print("API 请求失败，状态码:", res.status_code)

except Exception as e:
    print("发生错误:", e)