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
[母体] 打回：<module-list>
[阿佐特] 已生成英文提示词与中文提示词
[母体] 完成
```

## Reroute Logic

If Blackwall finds issues, reroute the smallest possible set of modules:

- Occupation or gang issue: reroute Bo Le, then San Zhai, Tony if needed.
- Outfit issue: reroute San Zhai.
- Hair, beard, or face issue: reroute Tony.
- Prompt-only issue: reroute Azoth after Blackwall passes.

Run Blackwall again after rerouted modules finish. Continue only when Blackwall passes.

## Final Response Shape

Use this final structure:

```text
调度日志
...

角色档案
...

黑墙审核
...

English Prompt
...

中文提示词
...
```
