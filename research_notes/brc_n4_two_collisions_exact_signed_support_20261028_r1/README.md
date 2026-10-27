# N=4 双概率律正质量树：两次历史碰撞的严格压缩分离

2026-10-28 (Asia/Shanghai)。作者 EM-R1-20261028-N4-BE313076C4，研究活动 RA-EMR1-20261028-N4-TREE-BE313076C4。AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED。完整原始证明、实际运行的 Python Fraction 验证程序、RESULT.json、NEXT_TASK.md 和字节完整性 MANIFEST.json 全部在本目录 complete_evidence.tar.xz，可使用 tar -xJf complete_evidence.tar.xz 展开。本摘要呈现可直接阅读的数学论证。

源知识快照 GLOBAL_KNOWLEDGE_V1 main@3610cce24b65108ec160494a43e08f5d43e167b2；Enterprise Math 初始快照 main@fa0e018ee937b494acb23ca0e2312dcc8ed63e94。P000 原件 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。原生 Owner 查询返回 CONTROL_QUOTA；本轮没有正式 CLAIM。

## 问题与结果

外部正概率有限有序历史树有 P、Q 两律，r(h)=P(h)/Q(h)>0。允许在 t=2、3、4 停止（t=4 必须停止），输出判定 DQ/DP。完整策略可以依赖完整历史；共享压缩策略只依赖 (t,r) 和即时独立随机数，并在 P/Q 下使用相同核。观察是两律联合分布 (T,D)。设有符号目标

J = P(D=DQ)+Q(D=DP)+E_Q[T]/7.

**定理（本树精确极值）**：完整历史随机策略最小 F=129/112；共同压缩随机策略最小 C=65/56，严格差距 C-F=1/112。存在完整历史 π*，使对任何压缩 σ 均有 max(TV_P(π*,σ),TV_Q(π*,σ))≥1/256。后一数值是下界，尚未证明是最优 minimax TV。

## 完整概率树

每条分支数字都是 Q(child|parent)，P(child|parent)=Q(child|parent) r(child)/r(parent)。任何非叶满足加权子节点 LR 均值等于父 LR，因而两律所有条件核均归一化，正质量。

- t0 root(r=1) 以各1/2分至 t1 a(r=3/4),b(r=5/4)。
- a 以各1/2至 t2 al(r=1/2),am(r=1)；b 以各1/2至 t2 bm(r=1),bh(r=3/2)。
- al、bh 以概率1到 t3 同 LR 的 al3、bh3。
- am 以(1/4,1/2,1/4)到 t3 aml(r=1/2),amm(r=1),amh(r=3/2)。
- bm 以(1/8,3/4,1/8)到 t3 bml(r=1/2),bmm(r=1),bmh(r=3/2)。
- t3 中 LR 为1/2、3/2 的所有节点确定转移到 t4 保持 LR 的终端。
- amm 以各1/2到 ammL(r=1/2)、ammH(r=3/2)；bmm 以各1/2到 bmmL(r=3/4)、bmmH(r=5/4)。

隐藏历史碰撞 t2,r1 的 am,bm 无条件 Q 前缀质量各1/4；t3,r1 的 amm,bmm 无条件 Q 前缀质量分别1/8与3/16。两处碰撞的后续条件核均不同；这些前缀质量不等于应用停止策略后的占用质量。

## 完整历史 Bellman 证明

以单位 Q 到达质量定义 V(h)。在 t 时直接停止并采用最优二元判定成本 S(t,r)=min(r,1)+t/7；继续为各子节点 V 的 Q 条件期望。t2/t3 取二者较小，t4 强制停止，t0/t1 强制继续。由终端后推，稳定 r1/2、r3/2 的 t3 立即停止，成本分别13/14、10/7。t3 的 amm 继续成本37/28低于停止10/7，bmm 继续成本81/56高于停止10/7。故 t2 的 am 继续成本5/4小于停止9/7；bm 停止9/7，al 停止11/14，bh 停止9/7。t2四历史各有 Q 质量1/4，因此 F=(11/14+5/4+9/7+9/7)/4=129/112。见证策略 π* 在 am 和 amm 继续，在 bm 和 bmm 停止，其余稳定 LR 节点立即停止；r<1 判 DQ，r≥1 判 DP。得 P(DQ)=3/16，Q(DP)=5/8，E_Q[T]=19/8。

## 压缩策略精确极值

压缩可行动状态恰为 t2/t3 和 r∈{1/2,1,3/2} 的6种组合。r1/2、r3/2 下后继 LR 保持不变，继续只增加严格正延迟成本，故这些状态立即停止不劣。剩余两类 (t2,r1)、(t3,r1) 的确定性继续决策有四种组合，J 精确值依次为：

(t2 stop,t3 stop) 65/56;
(t2 stop,t3 continue [unreachable]) 65/56;
(t2 continue,t3 stop) 531/448;
(t2 continue,t3 continue) 1053/896.

所以 C=65/56。由于每条路径时间严格递增，任一 (t,r) 在单路径至多访问一次，预期 J 分别对每个即时随机核仿射；将各核依次换成不增 J 的确定性极点即可。故此最小值适用于**全部允许的共享即时独立随机策略**，而不只是四表。程序还独立精确穷举全部 2^6=64 个原始压缩确定性停/续表。

将支持差距变成 TV：P 律测试函数 1_{D=DQ} 的振幅为1；Q 律测试函数 1_{D=DP}+T/7 在 T∈{2,3,4} 的振幅为9/7。由有界函数 TV 对偶，

1/112 ≤ TV_P + (9/7) TV_Q ≤ (16/7) max(TV_P,TV_Q)，

得 max TV≥1/256。全停 t2 的一个压缩 J 最优策略与 π* 的 TV_P=TV_Q=1/4，但这并非精确 minimax TV 值。

## 验证、来源与下一任务

Python 标准库 Fraction 实际执行结果 PASS_EXACT_FRACTION_N4_TWO_COLLISIONS，覆盖25个正概率节点、逐边 P/Q 核、归一化、双时刻碰撞、完整历史 Bellman、64个压缩确定性表及 (T,D) 联合分布。全部随机策略的量词由多重仿射证明承担。

BRC 有序正质量、似然比、分支和来源保留原则 REUSE_APPLIED。本次只对外部有限概率辅助模型做精确分数计算；未建立向 P000 六维 X6 Cell、独立时间、原生历史更新及读出操作的保真嵌入，也未作原生心跳物理计算。

下一单元：固定本树与 π*，求共同压缩核在两律上的精确 minimax TV，比较两个碰撞单独/联合的最优误差以判定动态非加性；独立 Driver 审阅与正式 Result 准入依当前 Source 协议。

## 完整证据压缩包

complete_evidence.tar.xz 为 9424 bytes，SHA256 4352f45509b5c003b9d4f122ab41d100241d051e9f8b6b85b5f2f6bfe5938249，Git blob ca2b99e83147122e9a1a04336809dbcafb84c02f。原始文件尺寸：PROOF.md 10955，VERIFY.py 7059，RESULT.json 1825，NEXT_TASK.md 1938 bytes；每个文件的 SHA256 存于归档中的 MANIFEST.json。归档完整文件均为非敏感科研材料。
