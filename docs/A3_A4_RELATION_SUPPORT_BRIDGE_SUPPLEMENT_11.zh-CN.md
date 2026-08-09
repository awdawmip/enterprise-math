# A3 ↔ A4 ↔ P021 ↔ A2/P023 Bridge — Supplement 11

状态：`ACTIVE RESEARCH NOTE`  
范围：one-step composition count 中 witness identity 擦除的精确整数 coupling defect

## 1. 动机

P021 direction transport 已证明 cardinality shadow 一般不 composition-complete。对含 `m` 条 exact middle incidences 的一个 middle direction class，引入 predecessor/successor witness profiles

\[
l=(l_1,\ldots,l_m),
\qquad
r=(r_1,\ldots,r_m),
\]

并定义

\[
L=\sum_i l_i,
\qquad
R=\sum_i r_i,
\qquad
N=\sum_i l_i r_i,
\]

其中 `N` 是 exact matched three-edge-chain count。

P021 Stage 12 已证明充分条件

\[
\text{若 }l,r\text{ 任一侧 uniform}
\Longrightarrow
mN=LR.
\]

本文件识别出精确 obstruction，因此严格推广该 safe-reduction regime。

## 2. B41 — integer coupling defect

定义

\[
\boxed{
\Delta(l,r)
=
m\sum_i l_i r_i
-
\left(\sum_i l_i\right)
\left(\sum_i r_i\right).
}
\]

等价地，

\[
\boxed{
\Delta(l,r)
=
\sum_{1\le i<j\le m}
(l_i-l_j)(r_i-r_j).
}
\]

### pair-difference 恒等式证明

展开右侧：

\[
\sum_{i<j}
(l_ir_i+l_jr_j-l_ir_j-l_jr_i).
\]

每个 diagonal term `l_i r_i` 恰好出现 `m-1` 次，而全部 off-diagonal terms 为

\[
\sum_{i\ne j}l_i r_j
=LR-\sum_i l_i r_i.
\]

所以总和为

\[
(m-1)N-(LR-N)=mN-LR.
\]

该 defect 是 signed integer，不需要 average、probability 或 rational arithmetic。

## 3. B42 — exact cardinality-sufficiency criterion

精确 matched count 满足

\[
\boxed{
N=\frac{LR+\Delta}{m}.
}
\]

分子自动被 `m` 整除，因为它就是 `mN`。

因此

\[
\boxed{
\Delta=0
\iff
mN=LR.
}
\]

所以，只使用 `(m,L,R)` 做 cardinality-only composition 精确，**当且仅当** coupling defect 为零。

这是该 declared one-step count observable 的 exact safe-erasure criterion。

## 4. B43 — P021 uniform-fiber theorem 是严格充分子情形

若对所有 `i` 都有 `l_i=c`，则

\[
N=cR,
\qquad
L=mc,
\]

所以 `mN=LR`、`Delta=0`。`r` uniform 时同理。

因此 P021 Stage 12 被直接恢复。

但 uniformity 不是必要条件。

例如

\[
l=(0,0,1),
\qquad
r=(0,2,1).
\]

两侧都非 uniform，但

\[
m=3,
\quad
L=1,
\quad
R=3,
\quad
N=1,
\]

于是

\[
\Delta=3\cdot1-1\cdot3=0.
\]

所以真正 structural condition 是 zero coupling defect；uniformity 只是一个易检查的充分 regime。

## 5. aligned 与 anti-aligned 最小例子

取 `m=2`，令

\[
l=(1,0).
\]

### Aligned

\[
r=(1,0)
\]

得到

\[
L=R=1,
\quad
N=1,
\quad
\Delta=1.
\]

### Anti-aligned

\[
r=(0,1)
\]

marginal cardinalities 仍为

\[
L=R=1,
\]

但

\[
N=0,
\quad
\Delta=-1.
\]

所以 `Delta` 的符号和大小精确记录了 marginals 完全看不到的 middle-incidence coupling 信息。

## 6. B44 — `Delta` 在重新编码意义下是 P023 coarsest one-step repair

取 coarse state

\[
q=(m,L,R)
\]

以及 declared future observable

\[
h=N.
\]

P023-T02 已证明 `(q,N)` 是 `q` 面向 exact composition count 的 coarsest one-step repair。

在给定 `q` 后，

\[
N\mapsto\Delta=mN-LR
\]

与

\[
\Delta\mapsto N=(LR+\Delta)/m
\]

在 realizable states 上互为逆映射。

所以 `(q,Delta)` 与 `(q,N)` 对 fine witness profiles 诱导同一个 partition。因此

\[
\boxed{
(m,L,R,\Delta)
}
\]

是该 one-step count language 的 P023 coarsest repair 的一个规范整数重新编码。

这里不主张最少 machine bits，只讨论 exact quotient information。

## 7. B45 — matrix coupling defect

令 `A_{\alpha i}` 统计 coarse source class `alpha` 到 exact middle incidence `i` 的 left witnesses；令 `B_{i\beta}` 统计 `i` 到 coarse target class `beta` 的 right witnesses。

定义 marginals

\[
L_\alpha=\sum_i A_{\alpha i},
\qquad
R_\beta=\sum_i B_{i\beta},
\]

以及 exact composite count matrix

\[
C_{\alpha\beta}
=\sum_i A_{\alpha i}B_{i\beta}.
\]

定义 coupling-defect matrix

\[
\boxed{
D_{\alpha\beta}
=
mC_{\alpha\beta}-L_\alpha R_\beta.
}
\]

则逐 entry 有

\[
\boxed{
D_{\alpha\beta}
=
\sum_{i<j}
(A_{\alpha i}-A_{\alpha j})
(B_{i\beta}-B_{j\beta}).
}
\]

并且

\[
\boxed{
C_{\alpha\beta}
=
\frac{L_\alpha R_\beta+D_{\alpha\beta}}{m}.
}
\]

所以，在给定 `m` 与 left/right marginal count vectors 后，`D` 与 exact current composite count matrix `C` information-equivalent。

整个 cardinality-shadow matrix multiplication rule 精确，当且仅当

\[
\boxed{D\equiv0.}
\]

每个 relevant left row 或 right column uniform 足以使相应 defect entries 为零，但仍不是必要条件。

## 8. B46 — repair scope boundary

`Delta` 或 `D` 修复的是**当前声明的 composition-count observable**，并没有恢复 exact middle witness labels。

所以它并不会自动对以下 future language 完整：

- 后续还需要按 exact witness identity 再次 join 的 composition；
- labeled witness transport；
- 能区分“marginals 与当前 composite count 相同、但 fine profiles 不同”的 operation；
- 任何不能 factor through repaired count state 的更丰富 P021/A4 future language。

这正对应 P023 one-step repair 与 whole future operation algebra closure 的区别。

正确 hierarchy 是：

\[
\text{marginals}
\xrightarrow{+\Delta}
\text{exact current count}
\quad\text{（one-step safe）}
\]

而

\[
\text{witness-sensitive future algebra}
\Rightarrow
\text{继续保留/细化额外 witness structure}.
\]

## 9. 与 Stage 09–10 count tensor 的关系

Stage 09–10 保留按 staged cost vectors 索引的 exact counts。B41–B45 研究的是另一个 compression axis：当 witness identity 首先被聚合成 marginals 后，为 exact middle-incidence coupling 最少还要修回什么。

当 declared future language 同时需要：

- cost-sensitive multiplicity；
- 通过 aggregated middle class 的 exact composition；

两种 structure 可以组合，但不能静默合并成一个 universal state。

## 10. 与 P011 的关系

pair-difference 公式类似于整数 covariance/correlation numerator，这类代数已有成熟 prior art。P011 同样坚持先使用 integer multiplicity summaries，再做可选 normalization。

这里的 project-specific point 不是“发现 covariance”，而是把 `Delta` 精确放成 witness-identity 擦除的 P023 repair coordinate，并严格推广 P021 uniform-fiber safe-reduction condition。

## 11. Prior-art discipline

Dot-product/marginal identities、covariance numerator、contingency-table coupling 与 matrix multiplication 都是标准数学。本项目不主张这些 primitive 本身的新颖性。

当前待验证的贡献，是它们在进取数论 state hierarchy 中的精确位置：

`witness identity -> marginals + coupling defect -> exact current composition count`，

并明确给出 future-language boundary，以及 P021 与 P023 之间的 theorem-level 连接。

## 12. Executable reference

Bridge reference layer 新增：

- scalar coupling defect 与 pair-difference identity；
- 从 marginals + defect 精确恢复 composition count；
- matrix coupling-defect calculation；
- uniform 与 non-uniform zero-defect examples；
- aligned/anti-aligned same-marginal counterexamples。
