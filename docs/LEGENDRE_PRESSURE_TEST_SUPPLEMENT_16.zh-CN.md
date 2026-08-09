# Legendre 压力测试 — 补充 16

状态：`ACTIVE RESEARCH NOTE`  
范围：lower-band quotient-root channels 在稳定区间中的严格不重叠  
依赖：P017 L051 与规范 P018-T110–T113  
纪律：本文**不**证明 Legendre 猜想。本文只用初等整数不等式加强 L051，不调用任何渐近素数分布定理。

## 1. L051 是统一上界，但并非稳定区间中的最强形式

对 lower-band prime

\[
p^2<2k,
\]

定义

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad
C_p(k)=\{j_p,j_p+1\}.
\]

L051 已证明任意 target root 至多属于两个 candidate pairs `C_p(k)`。

有限压力测试进一步显示，双重重叠只发生在很小的根。最后一次发生在

\[
k=14,
\qquad p=2,\ q=3,
\]

其中

\[
C_2(14)=\{9,10\},
\qquad
C_3(14)=\{8,9\}.
\]

从 `k=15` 开始，所有 candidate pairs 两两不交。

下面给出精确证明。

---

## 2. L052 — 稳定 lower-band root channels 两两不交

状态：`PROVED`。

对任意

\[
\boxed{k\ge15}
\]

以及任意不同 lower-band primes

\[
p<q,
\qquad p^2<2k,\ q^2<2k,
\]

都有

\[
\boxed{j_p\ge j_q+2.}
\]

因此

\[
\boxed{C_p(k)\cap C_q(k)=\varnothing.}
\]

等价地，从 `k>=15` 开始，每个下降后的 root index 至多只接收**一条** lower-band least-prime shell channel。

这个统一阈值是 sharp 的，因为 `k=14` 存在上面的重叠例子。

---

## 3. 设置

固定

\[
p<q
\]

并记

\[
u=j_q.
\]

由定义，

\[
\boxed{qu^2\le k^2.}
\]

只需证明

\[
\boxed{p(u+2)^2\le k^2,}
\]

因为这样就有

\[
(u+2)^2
\le
\left\lfloor\frac{k^2}{p}\right\rfloor,
\]

从而

\[
j_p\ge u+2=j_q+2.
\]

证明分成一个统一的 `q>=13` 情形和四个小值 `q=3,5,7,11`。

---

## 4. 统一情形 q >= 13

假设

\[
q\ge13.
\]

lower-band 条件给出

\[
q^2<2k,
\]

因此

\[
q^4<4k^2.
\]

对 `q>=13`，有

\[
\boxed{q^3>4(2q-3)^2.}
\]

令 `q=13+h`、`h>=0`，则完全整数化地

\[
q^3-4(2q-3)^2
=h^3+23h^2+139h+81>0.
\]

乘以 `q` 并结合 `q^4<4k^2`，得到

\[
4q(2q-3)^2<4k^2,
\]

从而

\[
q(2q-3)^2<k^2.
\]

于是

\[
(2q-3)^2
\le
\left\lfloor\frac{k^2}{q}\right\rfloor,
\]

所以

\[
\boxed{u=j_q\ge2q-3.}
\]

由于 `q>=13` 是奇素数而 `p<q` 也是素数，必有

\[
p\le q-2,
\]

因此

\[
\boxed{u\ge2p+1.}
\]

同时 `q-p>=2`。于是

\[
\begin{aligned}
qu^2-p(u+2)^2
&=(q-p)u^2-4pu-4p\\
&\ge2u^2-4pu-4p\\
&=2(u^2-2pu-2p).
\end{aligned}
\]

由 `u>=2p+1`，

\[
u^2-2pu
=u(u-2p)
\ge u,
\]

故

\[
u^2-2pu-2p
\ge u-2p
\ge1.
\]

所以

\[
\boxed{p(u+2)^2<qu^2\le k^2.}
\]

这就完成了所有 `q>=13` 的情形。

---

## 5. 小值 q=11

此时

\[
p\in\{2,3,5,7\}.
\]

由 `q^2<2k` 得

\[
k\ge61.
\]

所以

\[
11\cdot18^2=3564<61^2\le k^2,
\]

从而

\[
u=j_{11}\ge18.
\]

对最大的 `p=7`，

\[
11u^2-7(u+2)^2
=4u^2-28u-28.
\]

当 `u>=18` 时，

\[
4u^2\ge72u,
\]

故上式至少为

\[
44u-28>0.
\]

更小的 `p` 自然也成立。

---

## 6. 小值 q=7

此时

\[
p\in\{2,3,5\},
\qquad k\ge25.
\]

最坏情况是 `p=5`。

由于

\[
7\cdot9^2=567<25^2,
\]

有

\[
u=j_7\ge9.
\]

若 `u>=11`，则

\[
7u^2-5(u+2)^2
=2u^2-20u-20>0.
\]

只剩两个较小可能：

- 若 `u=9`，则 `k>=25`，所以
  \[
  5(9+2)^2=605<625\le k^2;
  \]
- 若 `u=10`，则 `u` 的定义给出
  \[
  k^2\ge7\cdot10^2=700,
  \]
  因而 `k>=27`，且
  \[
  5(10+2)^2=720<729\le k^2.
  \]

所以 `q=7` 成立。

---

## 7. 小值 q=5

此时

\[
p\in\{2,3\}.
\]

定理假设 `k>=15`，因此

\[
5\cdot6^2=180<225\le k^2,
\]

从而

\[
u=j_5\ge6.
\]

对最坏的 `p=3`：

- 若 `u>=7`，
  \[
  5u^2-3(u+2)^2
  =2u^2-12u-12>0;
  \]
- 若 `u=6`，直接有
  \[
  3(6+2)^2=192<225\le k^2.
  \]

所以 `q=5` 成立。

---

## 8. 小值 q=3

唯一比 `3` 小的素数是

\[
p=2.
\]

仍有 `k>=15`。由于

\[
3\cdot8^2=192<225\le k^2,
\]

得到

\[
u=j_3\ge8.
\]

若 `u>=9`，

\[
3u^2-2(u+2)^2
=u^2-8u-8>0.
\]

若 `u=8`，则

\[
k^2<3\cdot9^2=243.
\]

结合 `k>=15`，只能是

\[
k=15.
\]

此时

\[
2(8+2)^2=200<225=k^2.
\]

所以 `q=3` 也成立。

L052 证毕。∎

---

## 9. k=14 的 sharp 反例

取

\[
k=14.
\]

`2` 和 `3` 都属于 lower band，并且

\[
j_2
=R_2(98)=9,
\qquad
j_3
=R_2(65)=8.
\]

因此

\[
C_2(14)=\{9,10\},
\qquad
C_3(14)=\{8,9\},
\]

root `9` 同时属于两者。

所以统一阈值不可能从 `k>=15` 降为 `k>=14`。

---

## 10. 结构后果

L051 已经给出常数跨 shell 重数；L052 在稳定区间连这个系数也消掉：

\[
\boxed{
\text{当 }k\ge15,
\quad
\text{一个下降 root scale}
\longleftarrow
\text{至多一条 lower-band least-prime shell}.
}
\]

因此在 T113 选择实际 upper/lower branch 之前，lower-band quotient windows 就已经处于相互分离的 root-scale channels 中。

这比一般“递归是良基的”更强：root coordinate 从足够大的 `k` 开始可以直接作为**无重叠的 shell label**。

---

## 11. 与精确 cofactor windows 的关系

每枚 least prime `p` 都有精确 open cofactor window

\[
W_p(k)
=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

T110 把该 window 限制在至多两个相邻 square-root basins 中。L052 说明，当 `k>=15` 时，不会有另一枚 lower-band prime 拥有其中任一 candidate root index。

所以每个 lower target root basin 至多只接收一条 lower-band least-prime shell 的 candidate cofactor-window material。

但 exact window 只占 lower basin 的一个 subinterval；把 subinterval 替换成整个 basin 仍然过粗。L052 的收益是消除跨 shell 重数，而不是允许丢掉 subwindow geometry。

---

## 12. 与 T113 和 mirror gating 的关系

T113 在唯一 L052 channel 内给出逐状态 switch：

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

所以在稳定区间，lower-band 路线现在具有：

1. 每个 target root 只有一条可能 shell channel（L052）；
2. 一个精确 offset threshold 选择该 channel 内的实际 root（T113）；
3. 实际 root 严格下降（T112）。

对 mirror states，`s=k\pm r`，因此 branch selector 变成 radius half-interval，可与现有 mirror CRT progression 求交，而且不再需要处理同一个 root scale 上多个 lower-band shell channel 的竞争。

---

## 13. 可执行核验

`lower_band_root_disjoint_bound(k)` 检查 L052 的稳定区间结论。

回归测试覆盖：

- 所有 `15<=k<1000`；
- 更大根直到 `k=200000`；
- pairwise endpoint separation `j_p>=j_q+2`；
- sharp 的 `k=14,p=2,q=3` overlap witness。

有限测试只用于审计实现；证明是上面的整数论证。

---

## 14. 下一目标

从 `k>=15` 开始，lower-band cross-shell root collision 已经消失。

下一问题不应再继续研究 root channel 本身，而应问：**每条唯一下降 root channel 内的精确 p-rough subwindow，其递归 composite capacity 是否真正小于普通 least-factor/Buchstab bookkeeping？**

预计最难分支仍是 singleton small-prime support 加一个大素数 tail；这是 parity-sensitive hard core，后续应显式隔离，而不是藏在一般递归符号中。
