# BRC N4：五值稀疏来源标签的全策略共同 TV 精确最优定理

2026-10-28 · 作者侧科研材料，UNREVIEWED / NOT_ADMITTED。外部严格正 N4 双概率律停止树，不是 P000 原生 X6 动力学。沿用既有数学模型及完整随机策略类别：
[八标签来源研究](https://github.com/awdawmip/enterprise-math/blob/820e7c4afd18efbe031eaa226feb88ac8292e288/research_notes/brc_n4_provenance_refined_tv_exact_20261028_r1/PROOF.md)，及其 [父研究](https://github.com/awdawmip/enterprise-math/blob/9dca7aa2f7c4e0eb5546c5ad7f21b1b8052bb117/research_notes/brc_n4_positive_continuation_tail_relabel_20261028_r1/PROOF.md)。GLOBAL_KNOWLEDGE_V1 本轮只读规范快照 main@b823d6910be15aa43f712cd62f8d408b81da1a81，Enterprise Math 科学输入 main@ae3d46252935d48af75d15d8a9793cc142cc8d4e。

## 模型和新观察器

在 Q 律 t=1 的 A/B 分支各重 1/2；t=2 的 AU/AV/BU/BV 重 1/6、1/3、1/4、1/4；AU、BU 的 P/Q 似然比均为 1。其余 t=3/t=4 严格正历史按所引父研究。每个历史允许独立即时随机 STOP_P、STOP_Q、CONTINUE（末时刻必停）。S2 对 t=2 的等似然比历史实施共同即时行为；S23 还在 t=3/t=4 实施相同约束；S3 仅实施后者。所有竞争策略可调整允许的前后时刻和终端判定，不冻结尾部。

令 0≤δ<1、0≤θ,c0,c1≤1，定义
```
a = 1-θδ,                 b = 1-(1-θ)δ
xA = (1-θ)c0+θ(1-δ)c1,    xB = (1-θ)(1-δ)c0+θc1
cA=xA/a, cB=xB/b
D=xA*b-xB*a=θ(1-θ)δ(2-δ)(c0-c1).
```
F 的 t=1 A/B 继续率为 a/b，否则 STOP_Q；t=2 AU/BU 继续率 cA/cB，否则 STOP_Q；AV/BV STOP_Q；t=3 AU 子历史 STOP_P，BU 子历史 STOP_Q，其余 STOP_Q；t=4 均 STOP_Q。F∈S3。

新互斥路径标签仅五值：A_STOP1、B_STOP1、AU_REACH3、BU_REACH3、OTHER。前二者在对应前缀 t=1 停止时触发，中二者在实际走过 AU/BU 并抵达 t=3 时触发，其余终止路径统一 OTHER。终止观察 O5=(T,Decision,Z5)。它是八标签观察器的确定性粗化，不是原始无标签观察器。

## 定理

在**全部上述实数参数域**，真正共同 TV minimax 为

`d3^[5](F)=0, d2^[5](F)=d23^[5](F)=|D|/(4a+6b)=ab|cA-cB|/(4a+6b)`.

特别地 δ=θ=1/2、c0=1/2、c1=1/4 时 a=b=3/4、cA=5/12、cB=1/3、D=3/64，故 d2^[5]=d23^[5]=1/160>0、d3^[5]=0。八标签同一点的 1/96 和原始无标签观察器的 0 属于**不同观察器**，不可互相代换。

## 对全体合法策略的下界

任取 G∈S2，在 t=1 的 A/B 继续率为 a′,b′∈[0,1]，AU/BU 共享的 t=2 继续率为 c∈[0,1]，其余时刻和 STOP 判定均任意。Z5 的 Q 律边缘概率（与其余行动完全无关）必为
```
qG=((1-a′)/2,(1-b′)/2,a′c/6,b′c/4,1-前四项之和).
```
F 则分别用 a,b,cA,cB。设 α=a/6、β=b/4、x=α(c-cA)、y=β(c-cB)、u=a′-a、v=b′-b。按五值标签顺序 qG−qF 精确为
```
(-u/2, -v/2, x+uc/6, y+vc/4,
 -(x+y)+u(1/2-c/6)+v(1/2-c/4)).
```
因为 c∈[0,1]，非负的 1/2−c/6 和 1/2−c/4 加上 c/6、c/4 各恰为 1/2。对第三、四、五坐标应用 |s+t|≥|s|−|t|，所出现的 |u|、|v| 负项恰好由前两项 |u|/2+|v|/2 补足。于是对**任意** G：
```
2 TV_Q(Z5(F),Z5(G)) ≥ |x|+|y|+|x+y|.
```
固定 c 时，t1 到达率调整无法降低此下界。对 c∈[0,1] 最小化右边的一半：当 c 处于 cA、cB 之间时，x、y 异号，表达式为 max(α|c−cA|,β|c−cB|)，在
```
c*=(α cA+β cB)/(α+β)
```
处取最小值 αβ|cA−cB|/(α+β)；区间外值不更小。借助 TV 数据处理和 max(TV_P,TV_Q)≥TV_Q，得到 d2^[5]≥|D|/(4a+6b)。S23⊂S2，故 d23^[5] 同样满足此下界。证明没有把竞争策略锁定成固定前期、固定尾部或占用流凸松弛。

## 匹配真实策略上界

取 G* 与 F 相同，唯在 t=2 让 AU/BU 均以**同一** c* 继续，否则 STOP_Q。G* 满足 S23 的真正独立即时行为约束。令 x*=α(c*−cA)，y*=β(c*−cB)=−x*。t1 分布完全相同；t2 OTHER 下 STOP_Q 的两种来源变化相加为 −x*−y*=0；t3 只有 AU_REACH3/STOP_P 与 BU_REACH3/STOP_Q 各有差异 x*,y*。由于 AU、BU 及其后代的 P、Q 父质量完全相同，两个概率律都得到完整联合 O5 的 TV=|x*|=|D|/(4a+6b)。F∈S3 因而 d3^[5]=0。上下界匹配，定理成立。

## 验证、边界、下一题

`VERIFY.py` 复用前代已公开的精确 N4 数据和行动函数，以 Python Fraction 在 500 个有理参数点重建所有终止路径、检查正概率、守恒、S23 可执行策略及 P/Q 全联合 TV，并在20个切片核对每片128个竞争策略、额外检查 t1 STOP_P 及 AV/BV 继续流。实数域的全称结论**来自上面的代数证明**，并非采样外推；尚未独立复审或 Lean 形式化。

BRC 本轮保留正权重、分支历史、实际终止来源与两律可观察边缘；零损失和正损失的差异来自选择了哪一个合法观察器，不得将正质量视为有符号抵消。未解决：一个二值标签是否已足以强制原完整策略族上的全策略严格正 TV；若不能，构造真实零损失修复。另待独立证明 P000 原生 X6/三维切片的保真桥接。本文件仅为作者侧研究材料，不等于正式 CLAIM、Result、独立 Driver 接纳或 Foundation。