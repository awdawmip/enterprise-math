# P025 补充 17 —— Task-Minimal Apéry Tail Precision 与有限 Exact Access Signature

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 16；P023 task-relative quotient/minimal repair  
Hard block：`NONE`

## 1. 问题

补充 16 给 primitive 正系数行 `b` 附加了有限 Apéry access profile

\[
\Sigma_{\rm Ap}
=
\bigl(P,(a_j,L_j)_{j\bmod P}\bigr),
\qquad
P=\sum_i b_i,
\]

其中 `a_j` 是剩余类 `j` 中最小的 semigroup defect，`L_j` 是实现 `a_j` 的最小非负 `L_infinity` 分解半径。

这份状态足以恢复最终 access law，但 P023 要求继续问：

> 对当前声明的 future language，里面究竟哪些信息真的可见？

如果未来只问“某个 target 是否已经进入精确 affine-periodic tail，以及进入后 `kappa_b(N)` 是多少”，那么完整 `L_j` 仍然过细。

## 2. P025-D08 —— certified-tail coordinate

定义

\[
\boxed{
q_j
=
\left\lceil\frac{L_j}{2}\right\rceil.
}
\]

补充 16 已证明，Apéry 下界

\[
r_0(N)=\frac{N+a_j}{P},
\qquad j\equiv-N\pmod P,
\]

精确可达当且仅当

\[
L_j\le2r_0(N).
\]

因为 `r_0(N)` 为整数，这等价于

\[
\boxed{q_j\le r_0(N).}
\]

所以 `L_j` 内部超出 `ceil(L_j/2)` 的奇偶/细节，对 tail-certification language 完全不可见。

定义 **certified-tail signature**：

\[
\boxed{
\Sigma_{\rm tail}(b)
=
\bigl(P,(a_j,q_j)_{j\bmod P}\bigr).
}
\]

## 3. P025-T50 —— `Sigma_tail` 精确决定 tail entry 与 stable access

对 target `N>=0`，令 `j congruent -N mod P`。`Sigma_tail` 直接决定该剩余类的第一稳定目标

\[
\boxed{
N_j^*
=
\min\{N\ge0:
N\equiv-j\pmod P,
\ N\ge Pq_j-a_j\}.
}
\]

于是精确有

\[
\boxed{
\text{stable}(N)
\iff
N\ge N_j^*.
}
\]

一旦 stable，

\[
\boxed{
\kappa_b(N)
=
\frac{N+a_j}{P}.
}
\]

所以这一 future language 完全不需要 raw `L_j`。∎

## 4. P025-N07 —— 单独 Apéry values 仍然不够

比较两个 primitive 四坐标行

\[
\boxed{b=(2,4,5,11),
\qquad
b'=(2,5,7,8).}
\]

二者都有

\[
P=22.
\]

它们生成相同的 numerical semigroup `S=<2,5>`，而且相对于 `22` 的完整 Apéry value 表也完全相同：

\[
\boxed{
(0,23,2,25,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21).
}
\]

但是 defect residue `6` 上的 factorization geometry 不同。

第一条 row 有

\[
6=2+4,
\]

每个坐标最多用一次，所以

\[
L_6=1,
\qquad q_6=1.
\]

第二条 row 的现有 coefficient coordinates 只能用

\[
6=2+2+2,
\]

因此

\[
L_6=3,
\qquad q_6=2.
\]

对应 target residue 为

\[
N\equiv-6\equiv16\pmod{22}.
\]

在最早 target `N=16` 时，Apéry lower radius 为 `1`。第一条 row 已可实现，第二条尚不可实现：

\[
\boxed{
\kappa_b(16)=1,
\qquad
\kappa_{b'}(16)=2.
}
\]

第二条 row 要到 `N=38` 才进入该剩余类的 Apéry tail。

所以

\[
\boxed{
\text{相同 numerical semigroup + 相同 Apéry values}
\not\Rightarrow
\text{相同 access precision}.
}
\]

这对项目尤其重要，因为 prime-labelled witness coordinates 保留的 factorization multiplicity/geometry 会被普通 semigroup membership 忘掉。

## 5. P025-T51 —— raw `L_j` 对 tail certification 又过细

再比较

\[
\boxed{b=(2,4,5,11),
\qquad
c=(2,5,6,9).}
\]

二者同样有 period `22` 和完全相同的 Apéry value 表，但 raw minimum factorization-radius profiles 不同。

然而压缩后却满足

\[
\boxed{
\left\lceil L_j(b)/2\right\rceil
=
\left\lceil L_j(c)/2\right\rceil
=1
\quad\text{对每个非零剩余类 }j.
}
\]

因此两者的整个 `Sigma_tail` 完全一致，尽管 raw `L_j` 不一致。

由 P025-T50，它们对所有非负 target 给出的 tail-entry 判断和 stable access value 完全相同。在这个例子里甚至每个 target 都已 stable，所以完整 nonnegative access functions 相同。

于是得到一个明确的合法 quotient：

\[
\boxed{
L_j
\longmapsto
q_j=\lceil L_j/2\rceil
}
\]

它确实丢掉 factorization 细节，却完整保留当前 tail language。

## 6. P025-D09 —— finite exact access signature

Tail signature 不负责恢复有限 exceptional preperiod 内的 access 值。补充 16 已证明异常集合

\[
\mathcal E_b
\]

有限且可精确计算。

附加有限响应表

\[
\boxed{
\mathcal X_b
=
\{(N,\kappa_b(N)):N\in\mathcal E_b\}.
}
\]

定义

\[
\boxed{
\Sigma_{\rm exact}(b)
=
\bigl(\Sigma_{\rm tail}(b),\mathcal X_b\bigr).
}
\]

## 7. P025-T52 —— 一个有限状态重建整个无限 access function

对每个 `N>=0`：

1. 若 `N in E_b`，直接从有限 exception table 读取 `kappa_b(N)`；
2. 否则 `N` 已处在自己的 certified tail，利用
   \[
   \kappa_b(N)=\frac{N+a_{-N}}P.
   \]

因此

\[
\boxed{
\Sigma_{\rm exact}(b)
\text{ 可重建全部 }N\in\mathbb N_0
\text{ 上的 }N\mapsto\kappa_b(N).
}
\]

这是有限精确信息，不是 asymptotic approximation，更不是偷偷保存一张无限表。∎

工作样本：

- `(5,2)` 的 exception table 为 `{(1,2)}`；
- `(2,5,7,8)` 为 `{(16,2)}`；
- `(2,4,5,11)` 为空表。

## 8. P023 解释

Stage 16–17 现在为同一 coefficient row 给出至少三种不同精度状态：

\[
\boxed{
\begin{array}{ll}
(P,a_j) & \text{只恢复候选 affine branches},\\
(P,a_j,q_j) & \text{恢复 certified tail + stable exact values},\\
(P,a_j,q_j)+\mathcal X_b & \text{恢复整个 exact nonnegative access function}.
\end{array}
}
\]

完整 factorization geometry 仍然更丰富，因为它还可以回答 witness identity/decomposition 等当前 language 没有声明的问题。

因此“全部保留”和“只留 semigroup membership”都不是普适最小答案，正确 representation 必须由 future language 决定。

## 9. Prior-art 纪律

Apéry sets、numerical-semigroup factorization theory、`L_infinity` factorization length 与 eventual quasipolynomial behavior 都属于前人工作，Stage 16 已登记相关现代 `p`-length 文献。

P025 不主张这些一般结构的历史原创性。项目侧继续检验的，是 signed certificate access 被运输到 semigroup-defect 语言以后形成的 task-relative compression ladder，尤其：

\[
\text{Apéry membership state}
<
\text{tail-certification state}
<
\text{full exact-access state}.
\]

历史优先性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_apery_tail_precision.py`
  - `(a_j,ceil(L_j/2))` certified-tail signature；
  - exact tail query；
  - finite exact access signature；
  - full response reconstruction；
  - equal-Apéry/different-onset 反例；
  - equal-tail/different-raw-factorization 样本。
- `tests/test_abc_apery_tail_precision.py`
  - 上述精确反例；
  - 完整 access function 重建；
  - finite exception tables；
  - tail-only state 在 exceptional target 上的显式 partiality。

## 11. 下一前沿

没有 hard block。继续：

1. 判断 `Sigma_exact` 中 exception table 是否还能规范压缩；
2. 与 P024 numerical-semigroup boundary precision 做母层归属审计；
3. 研究 profile 在原始整数 block 的 multiplication/exponentiation 下如何变换；
4. 从 scalar target access 扩展到多个 simultaneous derivative/certificate targets；
5. 在非 ABC relation-conditioned witness system 中寻找同样的 finite-tail + exception-table 结构。
