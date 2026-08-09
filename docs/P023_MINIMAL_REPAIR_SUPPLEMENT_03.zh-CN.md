# P023 —— 最小算术修复补充 03

状态：`ACTIVE RESEARCH NOTE`  
范围：当 `Q_r` 精度商对同空间 multiple-collapse `D_d` 不安全时的规范一比特修复

## 1. 设置

固定正整数 `r,d`。

粗精度状态为

\[
q=Q_r(n)=n//r,
\qquad
n=qr+t,
\qquad
0\le t<r.
\]

未来粗观测为

\[
h(n)=Q_r(D_d(n)).
\]

P023-T09 已分类什么时候 `h` 可以直接通过 `q` 下沉。本补充研究不安全时的**最粗修复**。

## 2. 精度 fiber 的边界相位

定义

\[
\boxed{
b_q=(qr)\bmod d.
}
\]

若 `b_q=0`，第 `q` 个 `r`-fiber 的左端点本身就是 `d` 的倍数。

若 `b_q>0`，`qr` 之后下一个 `d`-multiple 出现在偏移

\[
\boxed{
\tau_q=d-b_q
}
\]

处。

fiber 恰好在

\[
0<\tau_q<r
\]

时发生 split。

## 3. P023-T15 —— 一比特最粗修复

定义边界跨越 bit：

\[
\beta_{r,d}(n)=
\begin{cases}
1,&0<\tau_q<r\text{ 且 }t\ge\tau_q,\\
0,&\text{其他情形},
\end{cases}
\]

其中 `q=n//r`，`t=n-qr`。

则

\[
\boxed{
\widetilde q(n)=\bigl(q,\beta_{r,d}(n)\bigr)
}
\]

恰好是 `Q_r` 针对观测 `Q_rD_d` 的最粗一步修复。

等价地，对同一个 `Q_r` fiber 内任意 `x,y`，

\[
\boxed{
\beta_{r,d}(x)=\beta_{r,d}(y)
\iff
Q_r(D_d(x))=Q_r(D_d(y)).
}
\]

### 证明

在区间

\[
[qr,(q+1)r-1]
\]

内，`D_d(n)` 只会在跨过 `d` 的倍数时改变。

若 `d<r`，一个 `r`-fiber 内可能含有多个 `d`-multiple，但 `D_d(n)` 与 `n` 的差严格小于 `d<r`，所以投影到 `Q_r` 后只能得到 `q-1` 或 `q` 两种粗结果；第一个位于 `qr` 之上或等于 `qr` 的 `d`-multiple 正是粗结果从 `q-1` 切换到 `q` 的唯一阈值。

若 `d>r`，一个 `r`-fiber 内至多含有一个内部 `d`-multiple，因此粗结果同样最多两种，并由同一个 `\tau_q` 阈值分隔。

若 `d=r`，或者更一般地该 fiber 内没有内部边界，则粗结果恒定，规范 bit 取 0。

因此 `(q,\beta)` 与 `(q,h)` 诱导完全相同的分区。再由 P023-T02 得到最粗性。

### 推论

完整 Euclidean remainder

\[
t\in\{0,\ldots,r-1\}
\]

通常比本次一步修复真正需要的信息更多。对每个 splitting fiber，一个 bounded bit 已经充分且最小。

## 4. P023-T16 —— 周期与 split fiber 精确计数

令

\[
g=\gcd(r,d).
\]

相位序列

\[
b_q=(qr)\bmod d
\]

的周期为

\[
\boxed{
P=\frac d g.
}
\]

在一个周期内，它恰好遍历

\[
\{0,g,2g,\ldots,d-g\}
\]

中的每个 `g` 的倍数一次。

粗 fiber split 当且仅当

\[
0<d-b_q<r.
\]

因此一个周期内 split fiber 数量为

\[
\boxed{
S(r,d)
=
\frac{\min(r,d)}{\gcd(r,d)}-1.
}
\]

于是

\[
S(r,d)=0
\iff
\min(r,d)=\gcd(r,d)
\iff
r\mid d\text{ 或 }d\mid r.
\]

所以 P023-T09 成为这个更强周期 repair 定理的零 split 特例。

## 5. 计数证明

映射

\[
q\mapsto qr\pmod d
\]

在 `q mod d/g` 上恰好遍历每个 `g` 的倍数，因为 `r/g` 在模 `d/g` 意义下可逆。

### 若 `d<r`

所有非零相位都会 split，因此数量为

\[
\frac d g-1.
\]

### 若 `d>r`

写 `r=gR`、`d=gD`。相位 `kg` split 当且仅当

\[
kg>d-r=g(D-R),
\]

其中 `1<=k<=D-1`。所以

\[
k=D-R+1,\ldots,D-1,
\]

总数恰好

\[
R-1=\frac r g-1.
\]

两种情形统一为 `min(r,d)/g-1`。

## 6. 精度演算解释

这是 P023 第一个“最小修复 detail 不是任意分区标签，而是从既有 P018-style remainder geometry 中规范导出的 bounded integer coordinate”的实例。

所需结构是

\[
\text{粗 quotient }q
\quad+\quad
\text{一个边界 bit }\beta,
\]

而不是

\[
\text{粗 quotient }q
\quad+\quad
\text{完整 remainder }t.
\]

因此 P023 开始能够精确量化：一个未来运算真正要求补回多少精度信息。

## 7. 可执行审计

- `src/enterprise_math/p023_minimal_repair.py`
- `tests/test_p023_minimal_repair.py`

另做独立穷举：对所有正整数 `r,d<50`，split-count 闭式以及 repair-bit 分区与 projected `D_d` 输出分区的精确等价均未发现反例。该有界检查只是证明支持证据，不替代正文证明。
