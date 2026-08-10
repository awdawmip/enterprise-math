# P022 — 由 zero digits 产生的 Franel 分级 p-adic 盆地

状态：`ACTIVE RESEARCH NOTE / PRIOR-ART VALUATION THEOREM + NEW P022 SPECIALIZATION`  
Owner：`program/p022-geometry-v2`  
依赖：Delaygue 的 Apéry-like valuation theorem；Franel p-Lucas zero-digit basin；half-index witness family  
跨路线相关：P011 collision precision；P018/P023 graded repair；P024 task-relative observation depth

## 1. 已确认 Delaygue 的既有定理直接覆盖 Franel

记

\[
F_N=\sum_{k=0}^{N}\binom Nk^3.
\]

对素数 `p`，定义

\[
Z_p=\{1\le d\le p-1:p\mid F_d\}
\]

并令

\[
\alpha_p(F,N)
\]

表示 `N` 的 base-`p` 展开中，落在 `Z_p` 内的 digit 数量。

Éric Delaygue 在 *Arithmetic properties of Apéry-like numbers* 的 Theorem 1 中，对满足相应 Apéry-like multisum / differential-operator 条件的序列证明了 Kummer 型 valuation lower bound。论文的应用表明确包含

\[
\sum_k\binom nk^3
\]

这个 Franel sequence，其 factorial-ratio multisum 为

\[
\frac{(n_1+n_2)!^3}{n_1!^3n_2!^3},
\]

且对应 differential operator 属于 type-I 情形。因此，对任意 prime `p` 与任意 `N`，已有定理直接给出

\[
\boxed{
v_p(F_N)\ge \alpha_p(F,N).
}
\]

这是**已有数学**，P022 不主张发明该 valuation theorem。

P022 在这里的新推进，是把它与我们已经得到的 Franel zero-digit geometry、强制 midpoint family 与 task-relative precision 结构结合起来。

参考：É. Delaygue, *Arithmetic properties of Apéry-like numbers*, Compositio Math. 154 (2018), 249--274, Theorem 1 与包含 Franel numbers 的 application table；arXiv:1310.4131v2。

---

## 2. P022-LI20 — guaranteed valuation depth 的精确分布

记

\[
z_p=|Z_p|.
\]

在完整 digit block

\[
0\le N<p^L
\]

中，共有 `L` 个独立 base-`p` digit positions；每个位置有 `z_p` 个 zero digits、`p-z_p` 个 nonzero digits。

因此满足

\[
\alpha_p(F,N)=j
\]

的指标数量精确为

\[
\boxed{
C_{p,L}(j)
=
\binom Lj z_p^j(p-z_p)^{L-j}.
}
\]

且

\[
\sum_{j=0}^{L}C_{p,L}(j)=p^L.
\]

结合 Delaygue 定理，得到有限尺度 certificate：

\[
\boxed{
\#\{0\le N<p^L:v_p(F_N)\ge r\}
\ge
\sum_{j=r}^{L}C_{p,L}(j).
}
\]

这里必须保留“不等号”：真实 Franel valuation 可能高于 digit lower bound。

---

## 3. P022-LI21 — 平均 guaranteed p-adic depth

对上述精确二项 profile 求一阶矩：

\[
\sum_{0\le N<p^L}\alpha_p(F,N)
=
Lz_pp^{L-1}.
\]

因此

\[
\boxed{
\frac1{p^L}
\sum_{0\le N<p^L}v_p(F_N)
\ge
\frac{Lz_p}{p}.
}
\]

所以只要 `Z_p` 非空，平均 `p`-adic depth 至少随 base-`p` digit horizon `L` **线性增长**。

由于 `L` 与数值尺度的对数同阶，这给出了一个非常明确的结构：有限 digit-state alphabet 会在更大 horizon 中强迫越来越深的算术精度。

---

## 4. P022-LI22 — counting-typical depth 也随 digit horizon 线性增长

在完整 `p^L` block 的均匀计数下，

\[
\alpha_p(F,N)
\]

具有精确的 binomial mean/variance：

\[
\mathbb E\alpha
=L\frac{z_p}{p},
\]

\[
\operatorname{Var}(\alpha)
=L\frac{z_p}{p}
\left(1-\frac{z_p}{p}\right).
\]

因此对任何固定

\[
0<\varepsilon<z_p/p,
\]

Chebyshev 不等式给出显式有限界：

\[
\frac{
\#\{N<p^L:\alpha_p(F,N)<(z_p/p-\varepsilon)L\}
}{p^L}
\le
\frac{z_p(p-z_p)}{\varepsilon^2p^2L}.
\]

又因

\[
v_p(F_N)\ge\alpha_p(F,N),
\]

故

\[
\boxed{
\frac{
\#\{N<p^L:v_p(F_N)\ge(z_p/p-\varepsilon)L\}
}{p^L}
\longrightarrow1.
}
\]

也就是说，之前的 density-one divisibility basin 其实是**分级的**：绝大多数 Franel indices 都至少带有与 digit depth 成正比的 `p`-adic valuation lower bound。

这里不主张真实 valuation/L 一定收敛到 `z_p/p`；我们证明的是 lower-bound language。

---

## 5. P022-LI23 — 重复 midpoint digit 形成精确 valuation tower

假设

\[
p\equiv5,7\pmod8.
\]

半指标定理已经证明

\[
m=\frac{p-1}{2}\in Z_p.
\]

对 `L>=1` 定义

\[
N_L=m(1+p+\cdots+p^{L-1}).
\]

因为

\[
m=\frac{p-1}{2},
\]

直接得到闭式

\[
\boxed{
N_L=\frac{p^L-1}{2}.
}
\]

其 base-`p` 展开恰好由 `L` 个 midpoint zero digit `m` 组成，所以

\[
\alpha_p(F,N_L)=L.
\]

Delaygue 定理因此给出无限 tower：

\[
\boxed{
v_p\!\left(F_{(p^L-1)/2}\right)\ge L
\qquad(L\ge1).}
\]

等价地，

\[
\boxed{
p^L\mid F_{(p^L-1)/2}.}
\]

这比简单重复 mod-`p` Lucas congruence 强：每重复一个 zero digit，guaranteed valuation 都再增加一层。

---

## 6. P022-LI24 — composite A-boundary 内的无限分级 tower

进一步取

\[
p>5,
\qquad
p\equiv5\ \text{或}\ 23\pmod{24}.
\]

对每个**奇数** `L>=1`，令

\[
N_L=\frac{p^L-1}{2}.
\]

对应 A-boundary 为

\[
2N_L-1=p^L-2.
\]

由于

\[
p\equiv-1\pmod3
\]

且 `L` 为奇数，

\[
p^L-2\equiv-1-2\equiv0\pmod3.
\]

`p>5` 又保证该数大于 3，所以边界为合数。于是 half-index family 被提升成一个无限**graded composite-boundary tower**：

\[
\boxed{
2N_L-1\text{ 为合数},
\qquad
v_p(F_{N_L})\ge L
\quad(L\text{ 为奇数}).}
\]

这里仍然**没有**直接得到 pure defect valuation `v_p(D_(N_L))`，因为大指标上的 canonical A-elimination 可能使用本身已被 `p` 整除的早期 Franel factors。

这正是我们在 `L=1` 已经分离出的 support-cancellation 边界。

---

## 7. 精度解释

p-Lucas 之前给出的只是一个 Boolean finite-state language：

\[
\text{base-p word 中是否出现 zero digit?}
\]

Delaygue valuation theorem 把它升级成分级语言：

\[
\boxed{
\text{base-p word 中一共出现多少次 zero digit?}
}
\]

每一个 zero digit 至少保证一个新的 `p`-adic depth 单位。

因此，对这个 lower-bound future language 来说，充分状态并不是完整巨大的 `F_N`，而只是对有限 zero-digit alphabet 的访问次数。

这与 P022 已经得到的 event-driven Barlow repair 具有高度结构相似性：

- wall encounters 累积 repair dimension；
- zero-digit encounters 累积 guaranteed p-adic valuation。

二者都是 **event-counted precision，而不是 clock-counted precision**。

若未来提炼一般母定理，应归 A2/P023/P024；P022 只保留 Franel/geometry specialization。

---

## 8. 与 half-defect 猜想的边界

这条 graded theorem **没有**证明当前更强的

\[
v_p(D_{(p-1)/2})=1.
\]

在一个 digit 的 midpoint 上，它只给出

\[
v_p(F_{(p-1)/2})\ge1.
\]

exact defect 仍然需要已经分拆出来的两个独立条件：

1. canonical A-elimination support 避开所有更早 Franel zero digits；
2. midpoint zero 在模 `p^2` 下是 simple lift。

Delaygue 的 lower bound 并不自动给出这个上界。

因此 LI20--LI24 大幅强化了无限算术侧，但没有抹掉真正的 Franel--Wieferich / support-avoidance frontier。

---

## 9. Prior-art / novelty 边界

已有输入：

- Delaygue 对 Franel sequence 的 Kummer 型 p-adic valuation lower bound；
- p-Lucas 结构与标准二项计数/概率恒等式。

P022 特定推进：

- complete base-`p` block 上 guaranteed valuation-depth 的精确分布；
- 平均与 density-one graded-depth 解释；
- repeated-half-index tower `N_L=(p^L-1)/2`；
- 其在 `p=5,23 mod24` 下的奇数层 composite-boundary specialization；
- 把 zero-digit events 解释为 graded repair depth 的 precision language。

这一组合的历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_franel_graded_basin.py`；
- `tests/test_p022_barlow_franel_graded_basin.py`。

代码以纯整数方式计算 `alpha` profile、guaranteed valuation tails、平均 lower bound、repeated midpoint indices 与 odd-level composite-boundary tower；短 horizon 测试再用 Franel 精确整数核验 Delaygue lower bound。
