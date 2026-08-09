# Legendre 压力测试 — 补充 16

状态：`ACTIVE RESEARCH NOTE`  
范围：lower-band quotient-root channels 在稳定区间中的严格不重叠  
依赖：P017 L051 与规范 P018-T110–T113  
纪律：本文**不**证明 Legendre 猜想。本文只用初等整数不等式加强 L051，不调用渐近素数分布定理。

## 1. L051 是统一上界，但不是稳定区间最强形式

对 lower-band prime `p^2<2k`，定义

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad C_p(k)=\{j_p,j_p+1\}.
\]

L051 已证明任意 target root 至多属于两个 candidate pairs。有限压力测试显示，双重重叠只发生在小根；最后一次发生在

\[
k=14,\qquad p=2,\ q=3,
\]

其中

\[
C_2(14)=\{9,10\},\qquad C_3(14)=\{8,9\}.
\]

从 `k=15` 开始 candidate pairs 两两不交。下面给出精确证明。

## 2. L052 — 稳定 lower-band root channels 两两不交

状态：`PROVED`。

对任意 `k>=15` 以及任意不同 lower-band primes `p<q`，

\[
\boxed{j_p\ge j_q+2.}
\]

因此

\[
\boxed{C_p(k)\cap C_q(k)=\varnothing.}
\]

等价地，每个下降后的 root index 至多只接收一条 lower-band least-prime shell channel。`k=14` 的例子说明阈值 sharp。

## 3. 设置

固定 `p<q` 并记 `u=j_q`。由定义，

\[
qu^2\le k^2.
\]

只需证明

\[
p(u+2)^2\le k^2,
\]

因为这样 `(u+2)^2<=floor(k^2/p)`，从而 `j_p>=u+2=j_q+2`。

## 4. 统一情形 q>=13

lower-band 条件 `q^2<2k` 给出 `q^4<4k^2`。

对 `q>=13`，

\[
q^3>4(2q-3)^2.
\]

写 `q=13+h`、`h>=0`，则

\[
q^3-4(2q-3)^2=h^3+23h^2+139h+81>0.
\]

因此

\[
q(2q-3)^2<k^2,
\]

所以 `u=j_q>=2q-3`。由于 `p<q` 为素数且 `q` 为奇数，`p<=q-2`，故 `u>=2p+1`。同时 `q-p>=2`。于是

\[
\begin{aligned}
qu^2-p(u+2)^2
&=(q-p)u^2-4pu-4p\\
&\ge2u^2-4pu-4p\\
&=2(u^2-2pu-2p)>0,
\end{aligned}
\]

因为 `u>=2p+1`。故

\[
p(u+2)^2<qu^2\le k^2.
\]

## 5. 小值 q=3,5,7,11

### q=11

lower band 强迫 `k>=61`；由于 `11*18^2<61^2`，有 `u>=18`。最坏 `p=7` 时

\[
11u^2-7(u+2)^2=4u^2-28u-28>0.
\]

### q=7

此时 `k>=25`，且 `7*9^2<25^2`，所以 `u>=9`。最坏 `p=5`：`u>=11` 时直接为正；`u=9` 时 `5*11^2=605<625<=k^2`；`u=10` 会迫使 `k>=27`，而 `5*12^2=720<729<=k^2`。

### q=5

定理假设 `k>=15`；`5*6^2<15^2`，所以 `u>=6`。最坏 `p=3`：`u>=7` 时直接成立；`u=6` 时 `3*8^2=192<225<=k^2`。

### q=3

只有 `p=2`。`k>=15` 时 `3*8^2<15^2`，故 `u>=8`。若 `u>=9`，则 `3u^2-2(u+2)^2=u^2-8u-8>0`；若 `u=8`，由 `k^2<3*9^2=243` 与 `k>=15` 得 `k=15`，而 `2*10^2<225=k^2`。

因此 L052 全部成立。∎

## 6. Sharpness

`k=14` 时

\[
j_2=R_2(98)=9,\qquad j_3=R_2(65)=8,
\]

所以 root `9` 同时属于两条 candidate pair。统一阈值不能降低到 `14`。

## 7. 结构后果

L051 给出常数跨 shell 重数；L052 在稳定区间把这个系数也消掉：

\[
\boxed{
\text{当 }k\ge15,
\quad
\text{一个下降 root scale}
\longleftarrow
\text{至多一条 lower-band least-prime shell}.
}
\]

因此 root coordinate 可以在 T113 选择实际 branch 之前就作为无重叠 shell label。

## 8. 精确窗口仍然必须保留

每枚 least prime 的 open cofactor window 是

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L052 消除了跨 shell root multiplicity，但**不**允许把精确 subwindow 粗化为整个 target square basin；那样仍然太松。

## 9. 与 T113 和 mirror gating 的关系

T113 在唯一 L052 channel 内给出逐状态 switch：

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

对 mirror states，`s=k\pm r`，所以 branch selector 是 radius half-interval，可以直接与 mirror CRT progression 求交，而且同一 root scale 上不再有多个 lower-band shell channel 竞争。

## 10. 可执行核验

`lower_band_root_disjoint_bound(k)` 检查 L052。回归覆盖全部 `15<=k<1000`、若干大根直到 `k=200000`、pairwise endpoint separation，以及 sharp 的 `k=14,p=2,q=3` witness。

有限测试只用于审计实现；证明是上面的整数论证。

## 11. 下一目标

从 `k>=15` 开始，lower-band cross-shell root collision 已经消失。下一问题是：**每条唯一下降 root channel 内的精确 p-rough subwindow，其递归 composite capacity 是否真正小于普通 Buchstab bookkeeping？**

预计最难分支仍是 singleton small-prime support 加一个大素数 tail；后续应把这个 parity-sensitive hard core 显式隔离，而不是藏进一般递归符号。
