# P018 —— 商根状态数的精确三值进位

状态：`DISCOVERY / NONCANONICAL`  
范围：固定整数状态下，正商根观测状态的精确基数  
依赖：P018 精确总除数纤维、分级合流界、整数根  
纪律：全程整数化。经典 floor quotient 分块与 Bernoulli 不等式属于既有数学工具；本文件不对这些基础工具主张优先权。

## 1. 设置

固定

\[
n\ge1,\qquad r\ge1,
\]

考虑观测

\[
\phi_{n,r}(d)=R_r\!\left(\left\lfloor\frac nd\right\rfloor\right),
\qquad 1\le d\le n.
\]

记 \(N_r(n)\) 为 \(\phi_{n,r}\) 所取得的不同**正**状态数量。

已有 P018 root-state atlas 定义

\[
H=H_r(n)=R_{r+1}(rn-1),
\qquad
D=\left\lfloor\frac{n}{(H+1)^r}\right\rfloor.
\]

总除数轴精确分为两张 chart：

- \(1\le d\le D\)：root 全部大于 \(H\)，且两两不同；
- \(d>D\)：root 全部不超过 \(H\)；其中 \(1,\ldots,H-1\) 必然全部出现，只有 \(H\) 是否出现还剩一个边界 bit。

因此在 \(H\ge1\) 时，

\[
N_r(n)=D+H-1+\kappa,
\qquad \kappa\in\{0,1\}.
\]

本文件把剩余的 \((D,\kappa)\) 进一步压成一个精确的三值进位。

## 2. 总除数阈值只有三个相邻可能值

记

\[
q=\left\lfloor\frac Hr\right\rfloor.
\]

则

\[
\boxed{\max(0,q-1)\le D\le q+1.}
\]

### 上界

由 \(H\) 的定义，

\[
rn-1<(H+1)^{r+1}.
\]

两边均为整数，因此

\[
rn\le(H+1)^{r+1}.
\]

又因为 \(D(H+1)^r\le n\)，所以

\[
rD(H+1)^r\le rn\le(H+1)^{r+1}.
\]

消去正因子 \((H+1)^r\) 后得到

\[
rD\le H+1,
\]

因此

\[
D\le\left\lfloor\frac{H+1}{r}\right\rfloor\le q+1.
\]

### 下界

当 \(q=0\) 时显然成立。以下设 \(q\ge1\)，于是 \(H\ge r\)。

利用离散 tangent/Bernoulli 界

\[
(H+1)^r-H^r\le r(H+1)^{r-1},
\]

可得

\[
\begin{aligned}
H^{r+1}-(H-r)(H+1)^r
&=r(H+1)^r-H\bigl((H+1)^r-H^r\bigr)\\
&\ge r(H+1)^r-rH(H+1)^{r-1}\\
&=r(H+1)^{r-1}>0.
\end{aligned}
\]

于是

\[
(H-r)(H+1)^r<H^{r+1}\le rn-1<rn.
\]

而 \(rq\le H\)，故

\[
r(q-1)\le H-r,
\]

从而

\[
r(q-1)(H+1)^r<rn.
\]

利用整数性得到

\[
(q-1)(H+1)^r\le n,
\]

所以 \(D\ge q-1\)。

因此粗总除数阈值只有三个相邻候选值。

## 3. 最低一档会强迫 horizon bit 出现

若 \(q>0\) 且

\[
D=q-1,
\]

则 horizon root \(H\) 必然出现。

因为 \(rq\le H\)，所以

\[
rqH^r\le H^{r+1}\le rn-1<rn.
\]

于是

\[
qH^r<n,
\]

故

\[
\left\lfloor\frac n{H^r}\right\rfloor\ge q=D+1.
\]

因此 \(\kappa=1\)。这说明三点 \(D\)-band 与二值 horizon carry 并不是六个独立组合。

## 4. 精确三值进位

定义

\[
A=\max\left\{q(H+1)^r,(q+1)H^r\right\},
\]

以及

\[
B=(q+1)(H+1)^r.
\]

再定义

\[
\tau_r(n)=
\begin{cases}
0,&n<A,\\
1,&A\le n<B,\\
2,&n\ge B.
\end{cases}
\]

则精确状态数为

\[
\boxed{
N_r(n)=H+q-1+\tau_r(n).
}
\]

### 按三个 \(D\) 值分情况证明

因为

\[
D=\left\lfloor\frac n{(H+1)^r}\right\rfloor,
\]

所以：

1. 在低于 \(q(H+1)^r\) 的最低区间，\(D=q-1\)。上一节已经证明此时 \(\kappa=1\)，故 \(N=H+q-1\)。
2. 中间区间中 \(D=q\)。此时 \(\kappa=1\) 当且仅当 \(n\ge(q+1)H^r\)。所以状态数从 \(H+q-1\) 跳到 \(H+q\) 的真正阈值，是 \(q(H+1)^r\) 与 \((q+1)H^r\) 中较大的那个，也就是 \(A\)。
3. 当 \(n\ge B=(q+1)(H+1)^r\) 时，\(D=q+1\)，状态数进入 \(H+q+1\)。

唯一的 \(H=0\) 情形是 \(r=n=1\)。此时 \(q=0\)、\(A=0\)、\(B=1\)、\(\tau=2\)，同一公式给出 \(N_1(1)=1\)。

## 5. 单一整数根决定的三点基数带

因为 \(\tau\in\{0,1,2\}\)，有

\[
\boxed{
N_r(n)\in
\left\{
H+\left\lfloor\frac Hr\right\rfloor-1,
H+\left\lfloor\frac Hr\right\rfloor,
H+\left\lfloor\frac Hr\right\rfloor+1
\right\}.
}
\]

也就是说，只计算一个 \((r+1)\) 次整数根，就已经把精确状态数压进三个连续整数；剩余只需一个三值边界决策。

对固定 \(r\)，因为

\[
H=(rn)^{1/(r+1)}+O(1),
\]

得到更强的渐近式

\[
\boxed{
N_r(n)
=(r+1)r^{-r/(r+1)}n^{1/(r+1)}+O(1).
}
\]

这把此前仅有的 \(\Theta(n^{1/(r+1)})\) 提升为围绕精确主项的有界加性误差。

当 \(r=1\) 时，它退化为熟悉的平方根尺度 floor quotient 分解。当前 P018 真正值得保留的候选贡献，是 all-\(r\) 的整数根压缩组织、合流解释以及有限精度状态基数接口；其历史新颖性仍未核验。

## 6. 可执行验证

`src/enterprise_math/p018_root_state_carry.py` 同时实现：

- 旧的二值 horizon carry \(\kappa\)；
- 新的精确三值状态数 carry \(\tau\)。

`tests/test_p018_root_state_carry.py` 在稠密有限网格上把三值公式与精确 two-chart count 逐项比较，并检查同一 horizon shell 内 carry 的单调性，以及 0/1/2 三种 carry 的显式样本。

## 7. 下一步形式化顺序

最经济的 Lean 路线不是一开始就处理完整有限集合基数，而是：

1. 先证三点带 \(\max(0,q-1)\le D\le q+1\)；
2. 再证 `D=q-1 -> horizon fiber present`；
3. 再证 \(\tau\) 的两个阈值；
4. 最后在选定有限集合/cardinality owner 接口后补精确基数恒等式。

这样可以把纯整数算术与有限枚举基础设施分离，也不会与 `Precision/Carry.lean` 中的一般加法进位 cocycle 重复造理论。