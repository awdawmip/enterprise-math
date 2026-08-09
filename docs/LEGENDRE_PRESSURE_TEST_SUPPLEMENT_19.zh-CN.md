# Legendre 压力测试 — 补充 19

状态：`PROVED RESEARCH NOTE`  
范围：保留 exact cofactor windows 后的实际 lower-band root-image separation  
依赖：P017 L051–L054、P007 quotient-window transport 补充 01、P023 image-separation 补充 08、P018 T113  
纪律：只使用有限整数不等式；不使用素数分布估计，也不声称证明 Legendre 猜想。

## 1. 为什么重新检查 L052

L052 对 lower-band prime `p` 定义

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right)
\]

并使用扩大后的候选 root pair

\[
C_p(k)=\{j_p,j_p+1\}.
\]

它证明从 `k>=15` 起这些 candidate pairs 两两不交，而且 `k=14` 时 `C_2(14)` 与 `C_3(14)` 都含 root 9。

但 L054 随后证明真实 cofactor windows 本身已经严格分离。于是必须重新问：

> `k=14` 的候选 root 9 是否真的同时被两个 exact windows 实现？

答案是否定的：

\[
W_2(14)=[99,112]
\quad\Longrightarrow\quad
R_2(W_2)=\{9,10\},
\]

而

\[
W_3(14)=[66,74]
\quad\Longrightarrow\quad
R_2(W_3)=\{8\}.
\]

候选对发生了重叠，但实际 image 没有。

这提示我们使用 P023-S8 的 actual-image separation，而不是继续对放大的 candidate superset 做碰撞计数。

## 2. 实际 root image

对 prime `p<=k`，仍定义 exact cofactor window

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

定义其**实际平方根像**

\[
\boxed{
G_p(k)=\{R_2(q):q\in W_p(k)\}.
}
\]

由于 `R_2` 单调，`G_p(k)` 是一个连续整数 root 区间；由 T113，在当前 square-basin geometry 下它至多包含两个相邻 roots。

## 3. L055 —— actual lower-band root images 从 k=9 起两两不交

状态：`PROVED`。

设

\[
k\ge9,
\]

并令 `p<r` 为不同 lower-band primes：

\[
p^2<2k,
\qquad
r^2<2k.
\]

则

\[
\boxed{
G_p(k)\cap G_r(k)=\varnothing.
}
\]

因此从 `k>=9` 起，一个实际下降 root index 至多来自一条 lower-band least-prime shell。

这把“实际 shell channel”的统一稳定阈值从 L052 candidate-pair 层的 `15` 降到 exact-window 层的

\[
\boxed{9}.
\]

## 4. 共同 root 的三个必要整数条件

反设存在共同 root `s`。则存在

\[
q_p\in W_p(k),
\qquad
q_r\in W_r(k)
\]

满足

\[
R_2(q_p)=R_2(q_r)=s.
\]

由 root basin

\[
s^2\le q\le(s+1)^2-1=s^2+2s
\]

得到以下三个必要条件。

### 4.1 来自 p-shell 左边界

因为 `q_p in W_p(k)`，

\[
pq_p>k^2.
\]

又 `q_p<=s^2+2s`，所以

\[
\boxed{
k^2<p\,s(s+2).}
\tag{A}
\]

### 4.2 来自 r-shell 右边界

因为 `q_r>=s^2` 且

\[
rq_r\le k(k+2),
\]

所以

\[
\boxed{rs^2\le k^2+2k.}
\tag{B}
\]

### 4.3 来自 r-shell 左边界

同时 `rq_r>k^2`，而 `q_r<(s+1)^2`，故

\[
\boxed{k^2<r(s+1)^2.}
\tag{C}
\]

由 (A)、(B) 相减：

\[
\boxed{(r-p)s^2<2ps+2k.}
\tag{D}
\]

这四个整数不等式就是 actual collision 的完整压力入口。

## 5. 所有 r>=5 的统一压缩

若 `r>=5`，则 `r` 为奇素数，且任意更小 prime `p` 都满足

\[
p\le r-2.
\]

又有初等平方恒等式

\[
(r+1)^2-4r=(r-1)^2\ge0.
\]

由 (C)，

\[
4k^2<4r(s+1)^2\le(r+1)^2(s+1)^2,
\]

所以正整数比较给出

\[
\boxed{2k<(r+1)(s+1).}
\tag{E}
\]

将 `r-p>=2`、`p<=r-2` 与 (D)、(E) 合并：

\[
\begin{aligned}
2s^2
&\le(r-p)s^2\\
&<2ps+2k\\
&\le2(r-2)s+2k\\
&<(3r-3)s+r+1.
\end{aligned}
\]

因此任何共同 root 都必须满足

\[
\boxed{2s^2<(3r-3)s+r+1.}
\tag{F}
\]

## 6. r>=11：lower-band 强迫 s 太大

lower-band 条件给出

\[
r^2<2k
\quad\Longrightarrow\quad
r^4<4k^2.
\]

结合 (C)：

\[
r^4<4r(s+1)^2,
\]

即

\[
\boxed{r^3<4(s+1)^2.}
\tag{G}
\]

对 `r>=11`，若有

\[
2(s+1)\le3r,
\]

则

\[
4(s+1)^2\le9r^2<r^3,
\]

与 (G) 矛盾。因此

\[
2(s+1)>3r,
\]

从而整数性给出

\[
\boxed{2s\ge3r-1.}
\tag{H}
\]

现在

\[
\begin{aligned}
&2s^2-(3r-3)s-(r+1)\\
&=s(2s-3r+3)-(r+1)\\
&\ge2s-r-1\\
&\ge2r-2>0,
\end{aligned}
\]

这与 (F) 直接矛盾。

所以 `r>=11` 不可能存在实际共同 root。

## 7. r=7

(F) 变为

\[
2s^2<18s+8.
\]

当 `s=10` 时左减右已经为 `12>0`，且之后差值严格增加，因此必须

\[
s\le9.
\]

又 `p<=5`，由 (A)

\[
k^2<5\cdot9\cdot11=495,
\]

所以 `k<=22`。

但 `r=7` 为 lower-band prime 要求

\[
49<2k,
\]

即 `k>=25`，矛盾。

## 8. r=5

(F) 变为

\[
2s^2<12s+6.
\]

`s=7` 时左减右已经为 `8>0`，以后继续增加，因此

\[
s\le6.
\]

又 `p<=3`，由 (A)

\[
k^2<3\cdot6\cdot8=144,
\]

故 `k<=11`。

但 `r=5` lower-band 要求

\[
25<2k,
\]

即 `k>=13`，矛盾。

## 9. 最后的小素数对 r=3, p=2

只剩

\[
(p,r)=(2,3).
\]

(A)、(B) 分别成为

\[
\boxed{k^2<2s(s+2),}
\tag{I}
\]

\[
\boxed{3s^2\le k^2+2k.}
\tag{J}
\]

### 9.1 先排除 s>=8

由 (I)，

\[
k^2<2(s+1)^2.
\]

因为

\[
49\cdot2=98<100,
\]

所以

\[
49k^2<100(s+1)^2,
\]

即

\[
7k<10(s+1).
\]

于是

\[
49(k^2+2k)
<100(s+1)^2+140(s+1).
\]

结合 (J)：

\[
147s^2
<100(s+1)^2+140(s+1),
\]

整理为

\[
47s^2<340s+240.
\]

但 `s=8` 时

\[
47s^2-(340s+240)=48>0,
\]

且该差值对 `s>=8` 严格增加，矛盾。

因此

\[
s\le7.
\]

### 9.2 剩余 k 只能是 9,10,11

由 (I) 与 `s<=7`，

\[
k^2<2\cdot7\cdot9=126,
\]

所以在定理假设 `k>=9` 下，只可能

\[
k=9,10,11.
\]

- `k=9`：由 (J)，`3s^2<=99`，故 `s<=5`；但 (I) 右侧至多 `70<81`；
- `k=10`：由 (J)，`s<=6`；但 (I) 右侧至多 `96<100`；
- `k=11`：由 (J)，仍有 `s<=6`；但 `96<121`。

全部矛盾。

所以 `(2,3)` 在 `k>=9` 也不可能产生实际 root collision。L055 证毕。∎

## 10. Sharpness：k=8 仍有真实 collision

`k=8` 时 `2`、`3` 都属于 lower band，且

\[
W_2(8)=[33,40],
\qquad
R_2(W_2)=\{5,6\},
\]

\[
W_3(8)=[22,26],
\qquad
R_2(W_3)=\{4,5\}.
\]

所以

\[
5\in G_2(8)\cap G_3(8).
\]

因此统一 eventual threshold `k>=9` 是 sharp 的。

有界枚举进一步显示实际 lower-band cross-shell root collisions 只出现在

\[
k=5,6,8,
\]

并且全部来自 `(p,r)=(2,3)`；这一枚举只是审计，不参与证明。

## 11. 与 L052 的精确关系

L052 没有被废弃。

它证明的是更粗的 candidate-pair statement：即使不知道 exact window 内哪一支真正被实现，从 `k>=15` 起 `{j_p,j_p+1}` 本身就已经跨 shell 不交。

L055 使用更多已知信息——L054 的 exact windows——因此能把**实际 realized image**的分离阈值提前到 `9`。

两者形成一个非常清楚的 precision hierarchy：

\[
\boxed{
\text{candidate superset precision}:15
\quad\longrightarrow\quad
\text{actual-window precision}:9.
}
\]

这是“提高结构精度减少假 collision”的严格数论实例。

## 12. A2 含义：root coordinate 已足以恢复 shell label

由 P023-S8-T02，L055 等价于：

> 对 `k>=9` 的 lower band，经过 exact factor stripping 再取平方根以后，least-prime shell label `p` 仍然是 retained root coordinate 的函数。

但 `R_2` 在单个窗口内部仍可能 many-to-one，所以这**不**意味着原始 cofactor 或 composite state 都可恢复。

因此：

\[
\boxed{
\text{shell identity retained}
\neq
\text{full state retained}.
}
\]

## 13. 对 P017 下一步的影响

从 `k>=9` 起，真实 lower-band root scale 上已经不存在跨 least-prime shell 的竞争。

后续递归不应再为这种假竞争支付一个统一 multiplicity 2；真正剩余的困难转为：

1. 每条唯一 shell 内 exact p-rough subwindow 的 composite capacity；
2. 同 shell 内 root many-to-one 造成的局部状态合并；
3. L053 multiplicity-sensitive mirror CRT 对这些实际 subwindows 的进一步压缩；
4. singleton small-prime support 加大素数 tail 的 hard core。

尤其禁止把 exact windows 再扩大成完整 target root basins，否则会重新制造 L055 已经消掉的假 collision。

## 14. 可执行审计

- `src/enterprise_math/p017_actual_root_separation.py`
- `tests/test_p017_actual_root_separation.py`
- `experiments/p017_actual_root_separation_probe.py`

回归固定 `k=8,p=2,r=3,root=5` 的 sharp witness，并检查 `9<=k<2000` 全部 actual lower-band images 两两不交；独立 probe 扩展到 `k<5000` 并记录所有小值碰撞。

历史创新性继续标记为 `NOVELTY_UNVERIFIED`。这里的证明主要由初等整数不等式组成；项目新增价值首先是 exact-window / image-separation 工具促成的更强 P017 结构结论。
