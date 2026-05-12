# any-reports

我自己的工作报告归档站。各种项目生成的 HTML 报告丢这里，靠 GitHub Pages 托管，
在任何设备的浏览器里都能打开。

- **首页**：<https://pluto235.github.io/any-reports/>
- **加新报告流程**：见 [`CLAUDE.md`](CLAUDE.md)

## 仓库布局

```
.
├── .nojekyll                          # 关 Jekyll
├── index.html                         # 首页 — 手维护的报告列表
├── assets/
│   ├── style.css                      # 站点共享样式（Notion 文档站风）
│   └── highlight.css                  # 代码高亮（Pygments）
├── scripts/
│   ├── md2html.py                     # MD → HTML 转换器
│   └── template.html                  # HTML 渲染模板
└── <report-slug>.html                 # 一份报告一个 HTML
```

## 新报告快速发布

如果手头是 **Markdown**：

```bash
cd ~/any-reports
~/miniconda3/envs/tritondft/bin/python scripts/md2html.py \
    path/to/your.md --slug your-slug --title "你的标题"
# 编辑 index.html，在 <ul class="report-list"> 顶部加一条 <li>
git add -A && git commit -m "report: <主题>" && git push
```

如果手头已经是 **self-contained HTML**：

```bash
cd ~/any-reports
cp /path/to/foo.html .
# 编辑 index.html 加链接
git add -A && git commit -m "report: <主题>" && git push
```

GitHub Pages 在 push 后 1~2 min 自动重建。
