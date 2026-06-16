# Pipeline

## Order

Run each module in strict order:

```text
1. 大门 / Da Men
2. 伯乐 / Bo Le
3. 三宅 / San Zhai
4. 托尼 / Tony
5. 黑墙 / Blackwall
6. 阿佐特 / Azoth
```

Use the Chinese names in user-facing responses. The English aliases exist only to keep file names and internal references stable.

## Progress Logging

Report progress as each module completes. Keep logs short and visible to the user.

Use these canonical states:

```text
[母体] 启动角色生成流程
[大门] 已生成基础角色
[伯乐] 已匹配职业与帮派
[三宅] 已匹配工作服
[托尼] 已匹配头脸造型
[黑墙] 审核中
[黑墙] 审核通过
[黑墙] 未通过：<reason>
[母体] 打回：<中文模块名列表>
[阿佐特] 已生成英文提示词与中文提示词
[母体] 完成
```

## Reroute Logic

If 黑墙 finds issues, reroute the smallest possible set of modules:

- 职业或帮派问题：打回伯乐，必要时再跑三宅、托尼。
- 工作服问题：打回三宅。
- 发型、胡子或脸型问题：打回托尼。
- 仅提示词问题：黑墙通过后打回阿佐特。

Run 黑墙 again after rerouted modules finish. Continue only when 黑墙 passes.

## Final Response Shape

Use this final structure. Keep headings and labels in Chinese except the English prompt body itself:

```text
调度日志
...

角色档案
...

黑墙审核
...

英文提示词
...

中文提示词
...
```
