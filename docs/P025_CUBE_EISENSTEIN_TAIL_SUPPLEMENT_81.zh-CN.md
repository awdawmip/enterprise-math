# P025 补充 81 —— Prime-Cube Shell 的全局 Eisenstein Tail

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 75–80  
硬阻断：`NONE`

## 1. Stage 80 的 hard boundary 在指数三上可以闭合

Stage 80 隔离了 supermodular region

\[
M>P
\Longrightarrow
m(F)>\sqrt P,
\]

但对一般奇素数指数，仍没有完成该区域的全局计数。

指数三有额外代数结构：两个非线性 cyclotomic factors 都是正定 Eisenstein norm forms。这提供了足够强的 value-side representation bound；再保留 Stage 79 中被 universal `m(F)>=2T` 丢掉的 linear-factor radical，就可以闭合 supermodular region，并进一步对整个 prime-cube shell 证明全局 power saving。

## 2. 设置

设

\[
3\le q<p\le P
\]

为不同奇素数。定义

\[
F_+(p,q)=p^2-pq+q^2,
\]

以及

\[
F_-(p,q)=p^2+pq+q^2.
\]

则

\[
p^3+q^3=(p+q)F_+(p,q),
\]

并且

\[
p^3-q^3=(p-q)F_-(p,q).
\]

精确 projective atoms 为

\[
\rho_{3,+}=\frac{m(p^3+q^3)}{3(p+q)},
\qquad
\rho_{3,-}=\frac{m(p^3-q^3)}{3(p+q)}.
\]

固定

\[
0\le\tau\le1,
\]

我们计数满足

\[
\boxed{\rho_{3,\pm}\ge P^\tau}
\]

的 prime pairs。

## 3. P025-T164 —— activation 保留 linear-factor radical

记

\[
L_+=p+q,
\qquad
L_-=p-q.
\]

Stage 79 给出

\[
m(F_+)\ge\frac{3P^\tau(p+q)}{\gcd(L_+,3)m(L_+)}.
\]

因为 `gcd(L_+,3)<=3` 且

\[
\frac{L_+}{m(L_+)}=\operatorname{rad}(L_+),
\]

得到

\[
\boxed{m(F_+)\ge P^\tau\operatorname{rad}(p+q).}
\]

对 difference branch，

\[
m(F_-)\ge\frac{3P^\tau(p+q)}{\gcd(L_-,3)m(L_-)}
\]

从而因为 `p+q>p-q`，

\[
\boxed{m(F_-)>P^\tau\operatorname{rad}(p-q).}
\]

因此两个 branch 中，nonlinear cyclotomic residual 都至少是 projective threshold 乘以对应 linear factor 的 radical。

这份被保留下来的 radical 信息，是 Stage 79 universal `m(F)>=2T` 所主动擦掉、但 Stage 81 重新需要的关键坐标。

## 4. P025-T165 —— nonlinear factors 是 Eisenstein norms

令

\[
Q(x,y)=x^2-xy+y^2.
\]

这是 Eisenstein integers `Z[omega]` 的 norm form。

有

\[
\boxed{F_+(p,q)=Q(p,q),}
\]

以及

\[
\boxed{F_-(p,q)=Q(p,-q).}
\]

所以两个 cube branches 都由同一个正定 binary quadratic norm form 表示。

经典表示公式为

\[
r_Q(n)=6\sum_{d\mid n}\chi_{-3}(d),
\]

从而特别得到

\[
\boxed{r_Q(n)\le6\tau(n).}
\]

等价地，从 Eisenstein integers 的唯一分解看，一个 norm value 的表示数至多是 divisor-function 级别，再乘六个 units。

利用标准 divisor bound，

\[
\boxed{r_Q(n)\ll_\varepsilon n^\varepsilon.}
\]

这里不主张任何表示论新颖性。

## 5. 外部 radical-count 输入

使用经典 de Bruijn estimate；其当前形式可见 Bernert–Browning–Lichtman–Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2 的 equation (1.1)：

对固定

\[
\lambda>0
\]

及任意

\[
\varepsilon>0,
\]

\[
\boxed{\#\{n\le x:\operatorname{rad}(n)\le x^\lambda\}=O_\varepsilon(x^{\lambda+\varepsilon}).}
\]

这是外部 prior art。

## 6. 平衡 radical split

令

\[
\boxed{H=P^{(1-\tau)/2}.}
\]

按照对应 linear factor 的 radical 是否不超过 `H`，把 activated pairs 分成两支。

`H` 的选择不是 heuristic，而是恰好平衡下面两个独立计数。

## 7. P025-T166 —— small-linear-radical branch

假设

\[
\operatorname{rad}(L_\pm)\le H.
\]

当 `tau<1` 时，对

\[
\lambda=\frac{1-\tau}{2}
\]

应用 de Bruijn estimate，可知不超过

\[
L_\pm\le2P
\]

的这类 linear factors 数量为

\[
O_{\tau,\varepsilon}\left(P^{(1-\tau)/2+\varepsilon}\right).
\]

固定一个 sum `L_+=p+q` 或 difference `L_-=p-q` 后，height-`P` box 中 ordered integer pairs 至多有 `O(P)` 个；加上 primality 只会减少数量。

因此 small-radical branch 的贡献为

\[
\boxed{O_{\tau,\varepsilon}\left(P^{3/2-\tau/2+\varepsilon}\right).}
\]

当 `tau=1` 时，`H=1`，而 `L_±` 是至少为 2 的偶整数，因此该 branch 为空。

## 8. P025-T167 —— large-linear-radical branch

现在设

\[
\operatorname{rad}(L_\pm)>H.
\]

由 P025-T164，

\[
m(F_\pm)>P^\tau H=P^{(1+\tau)/2}
\]

（sum branch 的边界非严格性无关紧要）。

并且

\[
F_+(p,q)\le P^2,
\]

而

\[
F_-(p,q)<3P^2.
\]

因此所有该 branch 的 values 都不超过

\[
X:=3P^2
\]

并具有至少

\[
Y:=P^{(1+\tau)/2}
\]

的 multiplicity residual。

所以

\[
\operatorname{rad}(F_\pm)=\frac{F_\pm}{m(F_\pm)}\ll P^{(3-\tau)/2}.
\]

相对于 value height `X asymp P^2`，这对应 radical exponent

\[
\frac{3-\tau}{4}.
\]

应用 de Bruijn，并把固定常数吸收到 `epsilon`，possible norm values 数量为

\[
O_{\tau,\varepsilon}\left(P^{(3-\tau)/2+\varepsilon}\right).
\]

每个这样的 value 至多有

\[
O_\varepsilon(P^\varepsilon)
\]

个 Eisenstein representations，所以 large-radical branch 同样贡献

\[
\boxed{O_{\tau,\varepsilon}\left(P^{3/2-\tau/2+\varepsilon}\right).}
\]

## 9. P025-T168 —— 全局 prime-cube projective tail

合并 P025-T166 与 P025-T167，可得对任一 sign 及每个固定

\[
0\le\tau\le1,
\]

都有

\[
\boxed{N_{3,\pm}(P;\rho_{3,\pm}\ge P^\tau)\ll_{\tau,\varepsilon}P^{3/2-\tau/2+\varepsilon}.}
\]

其中 `N_{3,+}`、`N_{3,-}` 分别计数 cube-sum 与 cube-difference shell 中的不同奇素数对

\[
3\le q<p\le P.
\]

特别地 threshold one 时，

\[
\boxed{N_{3,\pm}(P;\rho_{3,\pm}\ge1)\ll_\varepsilon P^{3/2+\varepsilon}.}
\]

ambient prime-base pair universe 至多是 `P^2` 量级，因此这是 prime-cube shell 中的无条件 power saving。

该特殊 shell theorem 不推出 full abc problem 的结论。

## 10. 为什么指数正好是平衡点

两支在 exponent level 上的成本分别是

\[
P\cdot H
\]

和近似

\[
\frac{P^2}{P^\tau H}.
\]

令其平衡得到

\[
H^2=P^{1-\tau},
\]

即

\[
H=P^{(1-\tau)/2},
\]

共同 exponent 为

\[
\boxed{\frac32-\frac\tau2.}
\]

所以 threshold one 的 `3/2` 并不是某一支证明的偶然产物，而是两类稀疏性相遇的位置：

1. rare low-radical linear factors；
2. rare high-residual Eisenstein norm values。

## 11. 与 Stage 80 的关系

Stage 80 把 signatures 分为

\[
M\le P
\]

与

\[
M>P.
\]

Stage 81 没有越过 horizon 后继续硬算 modulus，而是主动换语言：

\[
\boxed{\text{root-of-unity congruence state}\to\text{Eisenstein norm value state}.}
\]

对于指数三，这个 value state 的 representation multiplicity 有 divisor-bound 控制，因此 supermodular region 可以在不丢失目标 power saving 的情况下被计数。

这是 theorem-native coordinate switching 的一次明确成功。

## 12. Prior-art / novelty 边界

外部 / 经典组成包括：

- Eisenstein integers 与其 norm form；
- representation formula / `6 tau(n)` envelope；
- divisor bound；
- de Bruijn radical-count estimate，以及当前 abc exceptional-set 文献对它的复述。

P025 不单独主张这些组成部分的新颖性。

项目侧候选结果是：保留 `rad(p±q)` 的 exact projective activation inequality、平衡 small-linear-radical / large-Eisenstein-residual split，以及由此得到的 prime-cube shell projective-tail theorem。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_cube_eisenstein_tail.py`；
- `tests/test_abc_cube_eisenstein_tail.py`。

executable compiler 检查：

- 两个 nonlinear cube factors 均为 Eisenstein norm values；
- 不用浮点的 exact rational power thresholds；
- activated fixtures 上保留的 `m(F)>=T rad(L)` 下界；
- balanced small / large linear-radical branch predicate；
- exact `6 tau(F)` representation envelope。

## 14. 下一前沿

不存在硬阻断。继续：

1. 把指数四作为第一个 parity counter-pressure，精确确定 P025-T155 的哪一步失败，并找出 nonlinear factor squarefree 但仍 activated 的最小状态；
2. 判断更高奇素数指数是否存在同样便宜的 norm / Thue representation bound，足以闭合其 Stage-80 supermodular region；
3. 将 `3/2-tau/2` shell exponent 与直接 square-divisor counting 比较，确认真正的增益来自 Eisenstein value coordinate 的哪一部分；
4. 在 parity boundary 固定后，把成功的 congruence-to-value coordinate switch Relay 给 A2/E002。
