# 五项零服务积压的数学结果

2026-11-18。延续[同日的八分支研究](../README.md)。15:27（北京时间）的科研状态机回放将下列五项均列为 READY / NEEDS_DISPATCH / NO_RUNTIME_EVENT。GitHub 后续三条原始事件至评论 6973051614 都属于其它任务。16:16 的公平派发回执从 252 个候选中再次选中已有研究产出的原生旋转任务。本组依用户的公平推进目标，转向四项 P2 和一项 P1，读取每项现行不可变任务书和已完成前沿。发表模式为独立科研活动；此处报告数学结论、计算范围与反例，正式审阅由项目相应角色进行。

| 任务及不可变发布 | 本轮可复用数学与边界 |
|---|---|
| 惰性素数 Legendre 伴随 · TP2-2677708537A63FEBEC8F | 2013 年 CM 定理在 p≡13,19 (mod 24) 的符号和约化条件全部满足。结合有限 Clausen 乘积和 Wronskian，第一位在两个无穷素数类成立；第二位仍开放。[推导](inert.md) · [45 个素数的核验](inert_check.js) |
| 有限窗素数/半素数零模型 · TP2-CED1A3712793223C0ABE | 已公开的 2,016 个地址上，保持全部一、二点分布时，一行余 29 类零计数概率的精确区间为 [0,5/92]。两个留出窗口按原方案保留。[真实输入与端点构造](pfss.md) · [共享地址枚举](pfss_check.py) · [任意无放回层的尖锐公式](moments.md) · [965 组小例回归](moment_check.py) |
| 一根具名轴的闭路字符 · TP2-F15DD27ED7553E98C36E | 指定轴固定后，整闭路同调余不变量仍为 Z/2；U(1) 字符恰有恒等与末框奇偶两种。[定理](anchored.md) · [整数路径及有限域核验](anchored_check.js) |
| 三槽部分来源辨识 · TP2-C84DF1BDB591C2290D0D | 单树只读两项弯支权与乘积 z=at；有同根条件独立的后代时，一个二阶统计量 v=at² 足以在 z>0 时恢复 a,t。未知同根率有自校准公式和失效边界。[反演与反例](triad.md) · [具名路径复算](triad_check.js) |
| Fermat–Landau 局部筛 · TP2-A3769AB88B65DCB73E47 | 分段 Lucas 迹的正确下标是指数乘积；原实现拼接了二进制数字。轮筛原来漏掉的轮模数素因子现在在统一预算内检查。局部修复在原反例上取到 107 和 3；无命中不判素性。[算法与工作计数](fermat.md) · [修复源码](fermat/repair.py) · [独立回归](fermat/test_repair.py) |

逐项核验可在本目录分别运行 `node inert_check.js`、`node anchored_check.js`、`node triad_check.js`、`python pfss_check.py`、`python moment_check.py` 和 `python fermat/test_repair.py`。每篇研究稿给出冻结来源、定义、推理和有限实验的界限。[本组任务及领取状态](queue.json) · [上轮队列基准](../queue.json) · [截至核对时的最近事件](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-6973051614)
