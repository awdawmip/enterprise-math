# R282 实际接续记录

本轮科学对象：R281 所固定的正权、有序来源词 BRC 六边辅助自动机；不是 P000 原生六维 Cell 动力学。

## 已完成、不应重复的科学单位

1. 用 $t=\epsilon k$ 构造来源位到等概率 ±1 增量的**逐词双射**，得到全体终态合计的精确二项式恒等式。
2. 找到六状态同步增量字 +++，再加 --+ 强制来源字 000；使用六条长度4尾段构造长度10的 universal dirty synchronizing suffix，完整保留内部状态、来源位、后续可复合仿射效果及多重计数。
3. 无条件的**无限长度整数定理**：对任意终态 $(q,\epsilon)$ 和效果 $(\epsilon,k)$，$D_n^q(\epsilon,k)\ge\binom{n-10}{(n-10+\epsilon k-s_{q,\epsilon})/2}$。通过固定后缀的原始路径单射证明。
4. 峰值候选 $g_n=(+,-4)$（偶 n≥46）、$g_n=(-,-3)$（奇 n≥43）处，三个 dirty 终态的计数均 ≥ $F_{n+2}$ ≥ $\Lambda_n$；明确整数基底、n→n+2 比值归纳，无限长度成立。
5. **依赖式综合推论**：若 R274/R275 clean 支配及 R281 最终唯一峰值确实成立，则 $B_n=\Lambda_n$ 对全部 $n\ge\max(46,N_{\rm peak})$ 成立；其中 $N_{\rm peak}$ 尚无有效界，R281/前两项尚未经独立 Driver 数学接纳。本轮没有推出 $N_{\rm peak}=81$。

## 可回读完整证据

- R282_DIRTY_SYNCHRONIZING_SUFFIX_AUTHOR_PROOF.zh-CN.md：完整可审查证明；
- R282_verify_dirty_suffix.js：已在本轮工具执行同一 verify() 函数，纯 JS BigInt，检验所有固定路由、全 t 总量、7194 个 dirty 下界，长度 0..150；
- EXACT_EVIDENCE.json：上述已实际执行的结果状态 PASS；
- 可下载本轮 Python 标准库扩展证据包：还含0..14共32767条原始来源词独立枚举、48次后缀注入检查及 0..150 DP。Python 和 JS 为不同实现，其共同支持范围是有限核验，不能代替无限归纳。

Source snapshots：GLOBAL_KNOWLEDGE_V1 main@91a7aa5c9136cd6fd154e9f96beb714d8dc93c33；Enterprise Math main@ecc3e10467ed08ed62b7b7438f21e05a6491a81c；R281 source proof@d5fa39cebe5fcd6cda0e19759f23bbcb77bd023a；P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。

作者侧 Research-Activity-ID：RA-EMR3-20261025-1129-R282DIRTYSYNC。原生查询 CONTROL_QUOTA，session_start STATIC_READONLY_SCOPE_DENIED，operation_sent=false；当前 owner、CLAIM、Result、Driver 审查未核实。GitHub 作者侧持久化不等于项目正式数学接纳。

## 唯一最小未解问题

为 R281 的全长度峰值交替结论导出**有效、可审核的阈值** $N_{\rm peak}$，例如为两个竞争符号高斯修正项给出严格余项常数，或找可压缩成有限正锥归纳的证书。然后在本轮 dirty 足量阈值46的基础上，用短长度精确证据搜索最小 $N$，逐项审查 R274/R275/R281 的实际证明义务。
