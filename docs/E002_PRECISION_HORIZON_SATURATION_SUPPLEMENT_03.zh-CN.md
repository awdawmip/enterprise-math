# E002 — 精度视野与饱和执行，补充 03

状态：`ACTIVE ENGINEERING RESEARCH NOTE`  
范围：有限未来精度增长、可达余数修复与饱和整数平移  
父文档：`docs/E002_PRECISION_LOCKED_ACTUATION_SUPPLEMENT_02.zh-CN.md`  
依赖：P023 operation-word 语义与 E002 中心化执行理论

## 1. 问题

第二阶段针对中心化胞元宽度 `w=2d-1` 和物理动作族 `A`，已经得到任意有限未来下的安全宽度

\[
g=\gcd(w,|a_1|,\ldots,|a_m|),
\]

因此每个原胞元内部需要

\[
\frac wg
\]

个未来可区分子胞元。

本补充进一步追问两个更严格的工程问题：

1. 如果只关心长度不超过 `h` 的未来动作 word，在到达任意未来固定点之前到底需要多少细节？
2. 有限执行器 clipping 是否会改变第二阶段的整除兼容判据？

## 2. 有限视野可达余数

仍写中心化状态为

\[
e=wq+r-c,
\qquad c=(w-1)/2,
\qquad0\le r<w.
\]

对任意动作 word `v`，把总增量写成

\[
\Sigma(v)=k_vw+s_v,
\qquad0\le s_v<w.
\]

则

\[
\boxed{Q_w^c(e+\Sigma(v))=q+k_v+\mathbf1_{r+s_v\ge w}.}
\]

令 `W_h` 表示所有长度不超过 `h` 的动作 word，并包含空 word，定义

\[
\boxed{S_h=\{\Sigma(v)\bmod w:v\in W_h\}.}
\]

于是

\[
S_0\subseteq S_1\subseteq\cdots,
\qquad0\in S_h.
\]

## 3. E002-T20 — 精确有限视野类别数

同一个原宽度 `w` 胞元内的两个细节 `r,r'`，对于所有长度不超过 `h` 的动作 word，其未来粗商完全相同，当且仅当

\[
\mathbf1_{r+s\ge w}=\mathbf1_{r'+s\ge w}
\quad\text{对每个 }s\in S_h.
\]

每个非零可达余数都会贡献一条不同边界

\[
w-s.
\]

因此细节 fiber 恰好被切分成

\[
\boxed{c_h=|S_h|}
\]

个未来可区分类。

### 证明

对固定 word，上述运输公式说明：同一个原胞元中的两个细节，只可能被该 word 的 carry bit 区分。余数 0 永远不产生 carry。不同的非零余数在有序整数细节 fiber 上产生不同阈值。`|S_h|-1` 条不同阈值恰好形成 `|S_h|` 个非空连续类别。∎

## 4. E002-T20a — 标量最小修复

这些边界在一维细节 fiber 上完全有序，因此完整 carry 向量可以精确压缩为一个整数 rank：

\[
\boxed{
\rho_h(r)=
\#\{s\in S_h\setminus\{0\}:r+s\ge w\}.
}
\]

于是

\[
\boxed{(q,\rho_h(r))}
\]

就是已声明 horizon-`h` 粗商输出语言的最粗修复状态：rank 相同意味着所有 word carry 都相同；rank 不同则至少被一个可达余数阈值区分。

这是 P023 task-relative repair 的算术特化。

## 5. E002-T21 — 有限稳定到 gcd 修复

令

\[
g=\gcd(w,|a_1|,\ldots,|a_m|).
\]

动作余数在 `Z/wZ` 中生成的子群为

\[
H_A=\{0,g,2g,\ldots,w-g\},
\]

其大小为

\[
|H_A|=w/g.
\]

集合 `S_h` 会在有限步后恰好稳定为 `H_A`。因此

\[
\boxed{c_h\nearrow w/g}
\]

是一个有限稳定过程，不需要任何无限精度极限。

而且首次稳定的 horizon 满足

\[
\boxed{h_*\le w/g-1.}
\]

### 证明

所有 word 余数都属于 `H_A`。如果某一步出现

\[
S_{h+1}=S_h,
\]

则 `S_h` 对加入任意生成元都已封闭。又因为它包含 0，所以反复加入生成元不会产生新余数；于是它已经包含整个有限生成 monoid。在有限群 `Z/wZ` 中，该 monoid 就是 `H_A`。所以在稳定之前，每一轮至少新增一个余数。从 1 个余数增长到 `w/g` 个余数，最多需要 `w/g-1` 轮。∎

因此第二阶段的 gcd 安全精度，正是一个显式 horizon-indexed 精度增长过程的有限固定点。

## 6. E002-T22 — 单一重复动作

对单一动作 `a`，令

\[
P=\frac w{\gcd(w,|a|)}.
\]

余数

\[
0,a,2a,\ldots,(P-1)a\pmod w
\]

两两不同，而下一步重新回到 0。因此

\[
\boxed{c_h=\min(h+1,P)}
\]

即

\[
\boxed{
c_h=\min\left(h+1,\frac w{\gcd(w,|a|)}\right).
}
\]

所以对一个重复执行步长，每多看一步未来，胞元内部恰好多暴露一个类别，直到完整 gcd-safe 状态为止。

多个动作时增长可以更快。例如在

\[
w=15
\]

且

\[
A=\{6,10\}
\]

时，horizon `0,1,...` 的类别数精确为

\[
1,3,6,9,12,14,15,15,\ldots.
\]

最终 gcd 只记录终值 `15`，而有限 horizon profile 还记录达到它之前的增长结构。

## 7. 饱和整数平移

定义包含端点的整数 clipping：

\[
\operatorname{clip}_{L,U}(x)=\max(L,\min(U,x)),
\qquad L\le U,
\]

以及

\[
F_{a,L,U}(e)=\operatorname{clip}_{L,U}(e+a).
\]

## 8. E002-T23 — 精确 saturation 兼容判据

饱和平移能够下降到中心化宽度 `w` 的粗商，当且仅当

\[
\boxed{
w\mid a
\quad\text{或}\quad
Q_w^c(L)=Q_w^c(U).}
\]

### 对齐情形

若 `a=kw`，每个输入中心化胞元都会精确平移到另一个中心化胞元。clipping 只可能保持该胞元、把整个胞元压到一个饱和端点，或截掉一端/两端。只要 clipping 边界实际与该平移胞元相交，这个边界本身也属于该胞元。因此来自同一输入 fiber 的全部细状态仍具有同一个粗输出。

### 单胞元 saturation 情形

若

\[
Q_w^c(L)=Q_w^c(U),
\]

则所有 clipped 输出本来就属于同一个粗胞元，所以不论物理步长或输入状态如何，粗输出都恒定。

### 其余情形下的必要性

假设 `w` 不整除 `a`，写成

\[
a=kw+s,
\qquad0<s<w.
\]

每个平移后的输入胞元都会跨过一条中心化胞元边界；随着输入胞元编号变化，这些跨越会覆盖全部中心化边界。如果

\[
Q_w^c(L)\ne Q_w^c(U),
\]

那么未饱和整数区间 `[L,U]` 至少跨过一条粗边界，可取其首个整数点 `B` 满足

\[
L<B\le U.
\]

选择恰好跨过 `B` 的输入胞元。同一输入 fiber 内有两个相邻细状态分别映到

\[
B-1
\quad\text{和}\quad
B.
\]

二者都没有被 clipping 改写，但其粗输出不同，所以 fiber constancy 失败。∎

## 9. Saturation 边界

只要 saturation 输出范围跨越多个精度胞元，便有

\[
\boxed{F_{a,L,U}\text{ 粗安全 }\iff w\mid a.}
\]

因此普通 actuator clipping 既不会破坏已经 precision-locked 的平移，也不会一般性地挽救失配平移。唯一例外，是整个输出范围已经被强行压进一个粗胞元的退化情形。

对于具有共同非退化 clipping 区间的有限饱和动作族，第二阶段的奇因子精度谱因此保持不变。

## 10. 三个 E002 阶段的统一层次

目前三阶段已经可以清晰分离：

1. **响应层：**有限目标精度加状态保持会产生迟滞式切换，但单看继电黑箱行为仍可由传统控制完全复现；
2. **执行闭包层：**目标 fiber 是精确中心化商，物理动作族通过 gcd 选择任意未来下的安全精度；
3. **未来视野层：**到达固定点之前所需的精度恰好由 `|S_h|` 控制，而 saturation 除非把整个输出退化为一个胞元，否则不会改变整除定律。

逐渐稳定下来的可复用原则是

\[
\boxed{
\text{已声明精度商}
+
\text{已声明未来操作语言}
\longrightarrow
\text{最粗 future-safe 精度状态}.
}
\]

P023 拥有通用商理论；E002 只给出平移控制问题上的显式整数公式。

## 11. 可执行审计

实现：

- `src/enterprise_math/precision_horizon_saturation.py`

测试：

- `tests/test_precision_horizon_saturation.py`

确定性探针：

- `experiments/e002_horizon_saturation_probe.py`

仓库 CI 之外的独立有界重建已经检查：

- 奇宽小于 `20`、多组单/多动作 alphabet、horizon 至 `4` 时，直接枚举全部 operation word 得到的胞元内 signature 类别数恰好等于 `|S_h|`；
- 标量 repair rank `rho_h` 与完整 word-signature 划分完全相同；
- 大量有符号单动作与 horizon 上，闭式 `min(h+1,w/gcd(w,a))` 与直接余数枚举一致；
- 有限 horizon 类别数单调增长并有限稳定到第二阶段 gcd 类别数；
- 数千组小 `(w,a,L,U)` 直接 fiber 枚举与判据 `w|a 或 Q(L)=Q(U)` 完全一致，未发现反例。

## 12. 前人工作与新颖性边界

有限循环群、可达余数、gcd/order 计算、有限 horizon 自动机可区分性、clipping 与 congruence closure 都是成熟数学或工程工具。E002 不把这些成分声称为原创。

当前研究对象是它们在 E002 有限精度状态中的组合方式，以及“已声明未来视野”与“可安全坍缩多少胞元内部细节”之间的精确联系。整体解释的历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 13. 下一批压力测试

下一批目标：

- 只允许部分 action word 的 controller-policy language；
- 状态相关动作 alphabet；
- 正负方向采用不同精度胞元的非对称坐标；
- 整数向量动作，检验 scalar gcd 是否应被 module/normal-form 不变量替代；
- 允许在有限 horizon 停止、而不是立即使用完整任意未来修复的自适应计算策略。
