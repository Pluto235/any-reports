# CLAUDE.md

User 的多设备工作报告归档站。每份报告是一个 HTML 页面，通过 GitHub Pages
静态托管，分享 URL 永久有效。**Public 仓库** —— 不要传 API key / 任何敏感数据。

## URLs

- 首页：<https://pluto235.github.io/any-reports/>
- 单份报告：`https://pluto235.github.io/any-reports/<slug>.html`

## Git remote

```
origin: git@github.com:Pluto235/any-reports.git  (main branch)
```

## 仓库布局

```
.
├── .nojekyll                          # 关 Jekyll，保留下划线/中文文件名
├── README.md
├── CLAUDE.md                          # 本文件
├── index.html                         # 首页 — 手维护的报告列表（最新在上）
├── assets/
│   ├── style.css                      # 站点共享样式（Notion 文档站风）
│   └── highlight.css                  # Pygments 代码高亮（auto light/dark）
├── scripts/
│   ├── md2html.py                     # MD → HTML 转换器
│   └── template.html                  # HTML 渲染模板（占位符 {{TITLE}} 等）
└── <slug>.html                        # 一份报告一个 HTML
```

**文件名约定**：ASCII 小写 + 减号分隔，避免空格/中文。例如
`claude-code-advanced-guide.html`、`q1-experiment-notes-2026-05-12.html`。

## 加新报告流程（**重要 — 每次都做这 4 步**）

### A. 源是 Markdown

```bash
cd ~/any-reports

# 1. MD → HTML （会用 scripts/template.html 套站点样式）
~/miniconda3/envs/tritondft/bin/python scripts/md2html.py \
    /path/to/foo.md \
    --slug foo-report \
    --title "Foo 报告"

# 2. 编辑 index.html，在 <ul class="report-list"> 顶部加一行 <li class="...">
#    填四个字段：标题、url、desc、meta（日期 + 标签）

# 3. 提交 + 推
git add -A
git commit -m "report: <一句话主题>"
git push origin main

# 4. 等 1-2 min Pages 自动重建。验证：
curl -sI https://pluto235.github.io/any-reports/foo-report.html | head -1
# 期待 HTTP/2 200
```

### B. 源已经是 self-contained HTML

```bash
cd ~/any-reports
cp /path/to/foo-report-2026-MM-DD.html .       # 文件名按约定改
# 编辑 index.html 加 <li>
git add -A && git commit -m "report: <主题>" && git push
```

## 转换器细节（md2html.py）

支持的 markdown 扩展：

- `fenced_code` + `codehilite` — `` ``` `` 围栏代码块 + Pygments 高亮
- `tables` — GFM 表格
- `toc` — 自动 `id` 锚点 + 嵌套 TOC（H2-H4，H1 当文档标题）
- `attr_list` / `def_list` / `footnotes` / `sane_lists` / `nl2br` /
  `admonition` / `md_in_html`

转换后会自动：

- 外链（非 pluto235.github.io）加 `target="_blank" rel="noopener"`
- 以特定 emoji（📢 🎓 💡 ⚠️ 🚀 等）开头的 blockquote 加 `.callout` 样式

侧栏 nav 从 TOC tokens 抽，最多 3 级嵌套（H2 / H3 / H4），右侧锚点列扁平
H2 列表。

## GitHub Pages 配置

- **必须 public 仓库**（免费账号限制）
- Source: `main` 分支根目录
- 已通过 `gh api -X POST /repos/Pluto235/any-reports/pages -f 'source[branch]=main' -f 'source[path]=/'` 启用

如果哪天 Pages build 卡住，看：

```bash
gh api /repos/Pluto235/any-reports/pages/builds/latest --jq '{status, error, updated_at}'
```

## 坑提醒

- 必须改 `index.html`，否则首页不显示新报告（虽然 URL 直接访问能看到）
- 文件名不要带空格 / 中文 / 特殊字符 — 用 ASCII 减号分隔
- 仓库 **public**，会被搜索引擎索引 — 不要发包含敏感数据 / API key 的报告
- `scripts/md2html.py` 依赖 `markdown` + `pygments`，装在 `tritondft` conda env
  里（`~/miniconda3/envs/tritondft/bin/python -m pip install markdown pygments`）
- 改 CSS 或模板后，所有用 `md2html.py` 转过的旧报告**不会自动重新生成**；如要
  让旧报告同步新样式，需要重跑一次转换
