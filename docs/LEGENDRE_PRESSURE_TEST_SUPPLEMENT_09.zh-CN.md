# 勒让德压力测试 — 补充 09

状态：`ACTIVE RESEARCH NOTE`  
范围：高最小因子带中的乘法素数资源容量  
依赖：P017 L021、L030–L036 与 L037–L039  
纪律：本补充不证明勒让德猜想。它只利用已经分离的素数资源的“大小”而不只是“数量”，加强一个有限高带计数上界。

## 1. 为什么 L036 还不是资源论证的终点

在高最小因子带

\[
p^2\ge 2k,
\]

P017 已经证明两个关键事实：

1. cofactor window `W_p(k)=[A,B]` 的长度至多为 `p`；
2. 该窗口中不同的 `p`-rough cofactor survivors 两两互素。

对 three-prime shell state

\[
n=p\ell s,
\qquad
p\le \ell\le s,
\]

L036 只使用可用素数资源的数量。若

\[
K_p=\left\lfloor\frac{(k+1)^2-1}{p^2}\right\rfloor
\]

且

\[
R_p=\#\{r\text{ 为素数}:p\le r\le K_p\},
\]

则

\[
T_p\le\left\lfloor\frac{R_p+1}{2}\right\rfloor,
\]

其中 `T_p` 是最小因子为 `p` 的 shell 中 three-prime states 的数量。

这个加法资源计数忽略了各素数本身的大小。本补充完全保留同一套资源分离，只把“计数资源”升级为“相乘资源”。

---

## 2. 设定

令

\[
U=(k+1)^2-1
\]

为开平方盆地的上端点，并令

\[
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\qquad
B=\left\lfloor\frac{U}{p}\right\rfloor.
\]

于是

\[
W_p(k)=[A,B].
\]

在高带 `p^2>=2k` 中，每个 three-prime state 都写成

\[
n_i=pq_i,
\qquad
q_i=\ell_i s_i,
\]

其中素数满足

\[
p\le\ell_i\le s_i\le K_p.
\]

令

\[
\mathcal R_{p,k}
=
\{r\text{ 为素数}:p\le r\le K_p\}
\]

并定义资源乘积

\[
P_{p,k}=\prod_{r\in\mathcal R_{p,k}}r.
\]

空乘积定义为 `1`。

### 素数平方额外额度

因为 `|W_p(k)|<=p`，其跨度至多为 `p-1`。而根至少为 `p` 的两个不同平方之间，最小间距为

\[
(p+1)^2-p^2=2p+1>p-1.
\]

所以 `W_p(k)` 中至多存在一个“平方根为不小于 `p` 的素数”的平方数。

定义

\[
\xi_{p,k}
=
\begin{cases}
r,&\text{若存在素数 }r\in\mathcal R_{p,k}\text{ 使 }r^2\in[A,B],\\
1,&\text{否则。}
\end{cases}
\]

这个量只由窗口和有限资源区间决定，不需要先枚举实际 three-prime states。

---

## 3. L040 — 高带乘法资源容量

状态：`PROVED`。

设最小因子为 `p` 的 shell 中所有 three-prime cofactors 为

\[
q_1,\ldots,q_{T_p}.
\]

则

\[
\boxed{
\prod_{i=1}^{T_p}q_i\mid \xi_{p,k}P_{p,k}.
}
\]

因此

\[
\boxed{
A^{T_p}
\le
\prod_{i=1}^{T_p}q_i
\le
\xi_{p,k}P_{p,k}.
}
\]

定义整数乘法容量

\[
C_\times(k,p)
=
\max\{t\in\mathbb N_0:A^t\le \xi_{p,k}P_{p,k}\}.
\]

则

\[
\boxed{T_p\le C_\times(k,p).}
\]

与 L036 合并得到

\[
\boxed{
T_p
\le
\min\left(
C_\times(k,p),
\left\lfloor\frac{R_p+1}{2}\right\rfloor
\right).
}
\]

这里不需要对数：`C_x` 只需用精确整数反复乘以 `A`，直到下一次乘法会超过有限资源乘积即可。

### 证明

由 L035，不同的高带 `p`-rough cofactor survivors 两两互素。因此，不同 three-prime cofactors 的素因子支撑互不重叠。

每个非平方 cofactor

\[
q_i=\ell_i s_i,
\qquad \ell_i<s_i,
\]

使用 `R_(p,k)` 中两个不同素数，并且在总 cofactor 乘积中各出现一次。

平方 cofactor 的形式为

\[
q_i=r^2.
\]

窗口中至多有一个这种 cofactor。它的根 `r` 已经在 `P_(p,k)` 中出现一次，因此只需再额外补一份 `r`。这个额外副本恰好就是 `xi_(p,k)`。

所以全部 three-prime cofactors 的乘积整除

\[
\xi_{p,k}P_{p,k}.
\]

又因为每个 `q_i` 都在 `[A,B]` 中，所以 `q_i>=A`，从而

\[
A^{T_p}\le\prod_i q_i.
\]

根据 `C_x(k,p)` 的定义立刻得到 `T_p<=C_x(k,p)`。最后取该界与 L036 的最小值，即得组合上界。∎

---

## 4. 为什么平方额外额度是规范确定的

若存在素数 `r>=p` 使

\[
r^2\in W_p(k),
\]

则 `r^2` 没有任何小于 `p` 的素因子，因此它自动是 `p`-rough。于是

\[
p r^2
\]

确实是最小因子为 `p` 的 shell 中一个 three-prime state。

所以这个例外的重复资源并不是为了安全而猜出的松弛项。只要它存在，平方分支就是由精确 cofactor window 强制产生的。

---

## 5. 精确核验例子

### 例 A — 乘法容量直接排除 triple

取

\[
k=12,
\qquad p=5.
\]

则

\[
W_5(12)=[29,33],
\qquad
K_5=6.
\]

区间 `[5,6]` 中唯一素数资源是 `5`，所以

\[
P_{5,12}=5,
\qquad
\xi_{5,12}=1.
\]

因为

\[
29>5,
\]

所以

\[
C_\times(12,5)=0.
\]

L036 的加法上界仍允许一个 three-prime state，而 L040 直接证明这里一个都没有。

### 例 B — 新界取等且严格强于旧界

取

\[
k=45,
\qquad p=11.
\]

则

\[
W_{11}(45)=[185,192]
\]

资源素数为

\[
11,13,17.
\]

因此 L036 给出

\[
T_{11}\le2.
\]

但

\[
185^2>11\cdot13\cdot17,
\]

所以

\[
C_\times(45,11)=1.
\]

实际唯一的 three-prime cofactor 是

\[
187=11\cdot17,
\]

因此乘法上界恰好取等。

### 例 C — 唯一平方分支

取

\[
k=11,
\qquad p=5.
\]

则

\[
W_5(11)=[25,28].
\]

唯一的素数平方是

\[
25=5^2,
\]

所以

\[
\xi_{5,11}=5.
\]

资源乘积本身也是 `5`，故资源上限为 `25`，恰好等于这个平方 cofactor。

---

## 6. L040 能解决什么、不能解决什么

L040 是对 L036 的真实加强，因为它利用有限素数资源的大小，而不只是数量。有限回归扫描中存在大量情形满足

\[
C_\times(k,p)
<
\left\lfloor\frac{R_p+1}{2}\right\rfloor.
\]

但它仍然只是一个高带 three-prime 上界。

它**不能**：

- 控制 cofactor `q` 本身为素数的 semiprime states `p*q`；
- 证明每个高带 shell 都足够小，从而强迫整个平方盆地出现素数；
- 对所有 `(k,p)` 都更强——有时 L036 的加法界更强；
- 绕过任意短区间中的经典 rough-number 或 Jacobsthal 困难。

所以正确对象是组合上界，而不是单独使用 L040。

---

## 7. 审计结论与下一目标

最近对共同中心相关性的搜索没有得到 raw hit bits 或成功 prime-tail branches 的普遍稀疏规律。没有新的确定性不等式之前，不应继续把该路线升级。

L040 能通过审计，是因为它从 L035 已经证明的结构中提取了新的不等式：**高带 cofactor survivors 之间的素数资源不能复用。**

因此下一步问题被进一步压缩为：

> 能否把乘法容量跨不同最小因子 shell 汇总，或者把它与 semiprime 部分耦合，从而严格控制整个平方盆地中的 composite states 总数？

如果仍然做不到，那么 high-band rough-window 路线应停在已经得到的精确有限约化，而不是继续增加等价描述。
