# Mika 技能市场 · 测试目录

用于测试 Mika 的「记忆与数据 → 技能 → 获取技能 → 技能市场」。这是个人测试源，不是 Mika 官方市场。这里只分发可读的技能文本，不提供脚本，不收集使用数据。

| 技能 | 试试这样说 |
| --- | --- |
| [会议纪要转行动清单](skills/meeting-action-list/SKILL.md) | 把这份会议记录整理成决定和待办，标出负责人。 |
| [比较指定时段的高铁车次](skills/train-fare-compare/SKILL.md) | 比较周五下午广州南到长沙南有余票的二等座。 |
| [三款商品比价](skills/product-price-sheet/SKILL.md) | 帮我对比这三款商品的到手价和规格。 |

## 作为另一个测试源使用

复制此仓库，在 main 分支下编辑 skills/<id>/SKILL.md。运行 `python3 build_index.py` 重新生成 index.json，将两者一同提交。在 Mika 的市场里点「技能来源」，输入你的 GitHub 用户名/仓库名即可。索引版本为 1，最多 100 份技能；每项的 sha256 是原始 UTF-8 文件的摘要。市场仅在你打开页面时读取目录；点击技能才读取全文，加入待确认不会自动启用。
