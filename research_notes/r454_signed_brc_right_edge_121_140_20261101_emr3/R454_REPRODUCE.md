# R454 复现与接续

## 输入边界

- 研究来源：R453 proof/checker commit `147f35867e406429d0c8727d6aa09c094d9a7854`；R447 left window commit `adb2f26bee7e47f36991879f1b975a0fc7fbf3bc`；R450 local criterion commit `6d79677bda1fbce91c8b5f5af70dc830a33bd9dd`。
- 固定配置读取：GLOBAL_KNOWLEDGE_V1 `main@7b33f8066e9993e7c941959a9d738ed405248eb8`，Enterprise Math source `b3c681ad9428613ef1e9e63b3451fde8a6903ff2`。P000 ACTIVE，不改世界观。
- `R454_VERIFY.py` 与 R453 原证明使用的实际执行源码字节相同，故成功消息仍为 `R453_EXACT_PASS`。**它不代表结果属于 R453 的 s 区间**；命令行范围决定本轮真实范围。

## 精确验证命令

需要 Python 3.10+ 标准库。按单行/小批量复算、避免长任务被执行时限截断：

```bash
for s in $(seq 121 140); do
  python3 -u R454_VERIFY.py "$s" "$s" > "R454_RECHECK_${s}.log" 2>&1 || exit 1
done
python3 R454_INDEPENDENT_CROSSCHECK.py
```

主验证器对每个 `s` 完整构造 `F B_t(k_0+u)`、二三阶多项式 `P2/P3`，验证严格正系数与精确 Turán–Desnanot–Jacobi 多项式恒等式，然后输出行摘要 SHA256。检查 `R454_EVIDENCE_ALL.json` 中逐 s 的行摘要，20个 s、40个多项式、26,140个严格正系数和总摘要。有限整数交叉核验须独立匹配 `R454_CROSSCHECK_EVIDENCE.json`。

## 实际已完成的分片

本轮真实执行曾受单次运行时限影响，但日志含有21世纪大整数严格计算已经完成的逐行输出。仅消费完整哈希行，未完成的尾行不计；最终独立汇总的完成分片：

- `121..124` 来自原 `121..132` 中断日志；
- `125..127` 来自原 `125..128` 中断日志；
- `128..130` 完整；
- `131..133` 完整；
- `134..135` 来自原 `134..136` 中断日志；
- `136..137`、`138..139`、`140` 完整。

这20个行的摘要、次数、度数均在 `R454_EVIDENCE_ALL.json`；本轮完整本地证据包保留原始分片日志和 SHA256 文件清单。证书哈希不是独立数学审阅，但代码可确定性重建全部大整数系数。

## 新的结构结论与下一单元

由 R447 的 `j≤22` 左端局部证书，与 R452–R454 的 `s≤140` 右端证书拼接，再用 R450 线性数量局部判据，得 **所有奇数 `99≤r≤163` 的完整半无限 Toeplitz `PF3`**。该范围先前已有其他逐行精确验证；本轮增量是不同的**两端无限参数符号证书拼接法**。

下一精确最小问题是 `s=141` 的两个完整 `ℤ[u]` 多项式正性判号。若通过，右端窗口扩至141，拼接边界将扩至奇数 `r=165`；若有非正系数，不等于找到真正负子式，需另核验整数 `k` 的子式数值并寻找不同正性基底。

## 权限与状态

GitHub author-side 保存不是原生会话、Research-Activity、CLAIM、Result 或 Driver Review。当前原生 `research_authority_granted=false`，活跃 task owner 查询返回 `CONTROL_QUOTA`，故不能断言空闲 owner。未在 P000/ACTIVE 世界观或 task publication/claim 中作变更。当前成果为 `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`。
