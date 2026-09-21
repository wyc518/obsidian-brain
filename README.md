# ObsidianBrain

用自己 218 篇 Obsidian 笔记搭建的个人知识库 RAG 问答 Agent。

> 状态：第 1 天（2026-09-21 起）。当前仅含脚手架，功能逐步填充。
> 目标：10/15 前达到「可写进简历」的 v0.8，10/31 前完成 4 组对比实验并发布。

## 为什么做它

- 语料是真实的：我个人知识库里的 200+ 篇中文笔记（嵌入式、数据库、GPU、AI 工作台等），不是玩具数据集。
- 我自己就是用户，能给出真实的使用体感与耗时对比。
- 一个项目覆盖 RAG 面试的全部考点：分块、向量化、检索、重排、引用溯源、幻觉兜底、评测、成本、延迟。

## 技术栈

| 层 | 选型 |
|---|---|
| 语言 | Python 3.13 |
| LLM / Embedding | 硅基流动（免费档：`BAAI/bge-m3`、`Qwen/Qwen3-8B`）· 备用：智谱 `GLM-4-Flash`（永久免费） |
| 向量库 | Chroma（本地持久化） |
| 检索 | BM25 + 向量 + RRF 融合 |
| 结构化输出 | Pydantic |
| 演示 | Gradio |
| 评测 | 自建评测集（50 题），指标：Recall@3/5、命中率、P95 延迟、单次成本 |

## 目录结构

```
obsidian-brain/
├── src/
│   ├── scan_vault.py     # 扫描 vault → notes_index.json
│   ├── chunk.py          # Markdown 结构感知切分 → chunks.jsonl
│   ├── embed.py          # 向量化 → Chroma
│   ├── retrieve.py       # 三路检索（向量 / BM25 / 混合 RRF）
│   ├── generate.py       # 生成 + 引用溯源 + 拒答
│   ├── eval.py           # 评测与指标
│   └── app.py            # Gradio 界面
├── data/                 # notes_index.json / chunks.jsonl / eval_set.jsonl
├── .env                  # API Key（不入库）
└── requirements.txt
```

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # 填入 API Key
```

## 数据来源声明

语料为本人的私人 Obsidian 笔记，全部本地处理；调用云 API 时仅发送检索命中的片段。
README 与简历中所有指标均为实测值，未使用任何预设或占位数字。
