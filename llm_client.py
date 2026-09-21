import os, time, json, requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SILICONFLOW_API_KEY")
base_url = os.getenv("SILICONFLOW_BASE_URL")
model = os.getenv("CHAT_MODEL")

if not api_key:
    raise SystemExit("没读到 Key：检查 .env 里 SILICONFLOW_API_KEY= 后面是否填了值")
if not base_url:
    raise SystemExit("没读到地址：检查 .env 里 SILICONFLOW_BASE_URL= 后面是否填了网址")

start = time.time()
try:
    resp = requests.post(
        f"{base_url}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": model, "messages": [{"role": "user", "content": "用一句话解释什么是 RAG。"}]},
        timeout=60,
    )
    print("状态码：", resp.status_code)
    if resp.status_code != 200:
        print("返回内容：", resp.text[:500])
        raise SystemExit("调用未成功，把上面的内容发给我")
    data = resp.json()
    print("回答：", data["choices"][0]["message"]["content"])
    print("耗时：%.2f 秒" % (time.time() - start))
    print("用量：", json.dumps(data.get("usage", {}), ensure_ascii=False))
except requests.exceptions.Timeout:
    print("超时了：重跑一次；仍失败就把脚本里的 SILICONFLOW 换成 ZHIPU、模型换成 glm-4-flash 再试")