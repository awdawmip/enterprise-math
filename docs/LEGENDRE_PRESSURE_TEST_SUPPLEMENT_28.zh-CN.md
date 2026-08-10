# Legendre 压力测试 — 补充 28

状态：`PROVED RESEARCH NOTE`  
范围：split-shell statistic 的精确 Möbius 表示与 Jacobsthal 型 occupancy certificate  
依赖：P017 L068–L069 输入、canonical P017 Möbius tools、p-rough cofactor semantics  
纪律：有限 inclusion–exclusion、primorial coprimality 与 Jacobsthal function 都属于经典数论。本补充只是把它们特化到 P017 的精确 root-split intervals。

## 1. Realizability 就是对有限 primorial 的互素性

固定 prime `p`，定义

\[
\boxed{
P_{<p}
=
\prod_{r<p\atop r\text{ prime}} r.
}
\]

对任意正整数 `q`，

\[
\boxed{
q\text{ 是 }p\text{-rough}
\iff
\gcd(q,P_{<p})=1.
}
\]

因为 `q` 不是 `p`-rough，当且仅当它存在一个小于 `p` 的素因子；这又等价于它与 `P_{<p}` 共享素因子。

所以 L068 的 realizability filter 本质上是一个精确有限 reduced-residue 条件。

## 2. P017-L069-A —— 任意 p-rough interval 的精确 Möbius count

状态：`PROVED`。

对正整数区间

\[
[a,b],
\qquad
1\le a\le b,
\]

定义

\[
R_p[a,b]
=
\#\{q\in[a,b]:q\text{ 是 }p\text{-rough}\}.
\]

则 inclusion–exclusion 给出

\[
\boxed{
R_p[a,b]
=
\sum_{d\mid P_{<p}}
\mu(d)
\left(
\left\lfloor\frac bd\right\rfloor
-
\left\lfloor\frac{a-1}{d}\right\rfloor
\right).
}
\]

### 证明

因为 `P_{<p}` square-free，

\[
\mathbf1_{\gcd(q,P_{<p})=1}
=
\sum_{d\mid\gcd(q,P_{<p})}\mu(d).
\]

对 `q in [a,b]` 求和并交换有限求和顺序。区间中被 `d` 整除的整数数量精确为

\[
\left\lfloor\frac bd\right\rfloor
-
\left\lfloor\frac{a-1}{d}\right\rfloor.
\]

即得。∎

整个公式不使用 asymptotic sieve approximation。

## 3. 应用于 L068 的两个 root branches

对每个 prime `p<=k`，令

\[
W_p^-
\]

和

\[
W_p^+
\]

为 L068 中被 boundary quotient `m_p^2` 分开的 lower / upper root subwindows。

定义

\[
\boxed{
R_p^-(k)=R_p[W_p^-],
\qquad
R_p^+(k)=R_p[W_p^+],
}
\]

空 interval 的 count 规定为 0。

它们都是只由 `k,p` 决定的显式 finite Möbius sums。

## 4. P017-L069-B —— Split shell 的 exact Möbius positivity criterion

状态：`PROVED`。

由 L068，真实 least-prime shell 实现两个 cofactor-root branches，当且仅当每个 branch 都至少含有一个 `p`-rough quotient。

所以

\[
\boxed{
r_p=2
\iff
R_p^-(k)>0
\text{ 且 }
R_p^+(k)>0.
}
\]

等价地，split bit 为

\[
\boxed{
\beta_p^{\rm split}(k)
=
\mathbf1[R_p^-(k)>0]\,
\mathbf1[R_p^+(k)>0].
}
\]

这把 root-split theorem 的 realizability 部分变成两个精确 local inclusion–exclusion signs。

## 5. P017-L069-C —— 第二 repair-spectrum coordinate 的 exact Möbius formula

状态：`PROVED`。

L067 已给出

\[
S(k)=\sum_{p\le k}\mathbf1[r_p=2].
\]

代入 L069-B，得到

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\mathbf1[R_p^-(k)>0]\,
\mathbf1[R_p^+(k)>0].
}
\]

其中每个 `R_p^±` 都是 L069-A 的显式 finite Möbius sum。

因此 P011/P023 的第二 relative repair-spectrum coordinate 已经被完整写成经典有限 sieve arithmetic。

困难不再是定义这个量，而是控制这些短 moving rough intervals 的 simultaneous positivity。

## 6. 与 overshoot criterion 的关系

若 L068 raw overshoot gate

\[
p<\tau_p\le2k
\]

不成立，则两个 subwindows 至少有一个为空，相应 Möbius count 自动为 0。

因此也可以写成

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\mathbf1[p<\tau_p\le2k]
\mathbf1[R_p^-(k)>0]
\mathbf1[R_p^+(k)>0].
}
\]

这把两层结构完全显式化：

1. exact quotient/root geometry 决定是否存在两个 raw branches；
2. exact sieve arithmetic 决定每个 branch 是否存在真实 least-prime state。

## 7. k=6,p=3 的纠偏变成一个零 Möbius count

`k=6,p=3` 时，L068 说明 raw window 的确跨 root boundary。

upper raw branch 只有一个 quotient：

\[
q=16.
\]

又

\[
P_{<3}=2
\]

且 `gcd(16,2)>1`，因此

\[
\boxed{R_3^+(6)=0.}
\]

lower branch rough count 为正，但两个 positivity bits 的乘积仍为 0。

所以这个 false raw collision 被一个精确 local Möbius cancellation 删除。

## 8. Jacobsthal 型 sufficient occupancy certificate

令 `j(n)` 表示经典 Jacobsthal function，采用如下约定：

> `j(n)` 是最小正整数 `m`，使任意 `m` 个连续整数中都至少有一个与 `n` 互素。

那么任何长度至少为

\[
j(P_{<p})
\]

的 interval 都必然含有一个 `p`-rough integer。

所以 L068 raw slot counts 给出一个 sufficient split certificate：

\[
\boxed{
L_p\ge j(P_{<p})
\quad\text{且}\quad
U_p\ge j(P_{<p})
\Longrightarrow
r_p=2.
}
\]

等价地，如果某个 raw split 在 realizability filter 后失败，则至少一侧的 rough-empty branch 长度严格小于对应 Jacobsthal guarantee。

这只是充分证书。更短 interval 当然仍可能含有 p-rough integers。

## 9. 为什么 Jacobsthal bridge 有用

L068 把问题拆成 moving boundary 与 rough occupancy。L069 现在给 occupancy 两种攻击模式：

- **exact mode**：直接求 finite Möbius count；
- **guarantee mode**：用 Jacobsthal upper bound，仅凭 interval length 证明 positivity。

这样可以直接消费成熟 covering/gap 结果，而不改变 P017 state semantics。

同时要避免一个常见误读：Jacobsthal bound 是 worst-case interval guarantee，不是当前 moving subwindow 的 exact rough count。

## 10. Complexity boundary

若直接展开 Möbius formula，会对 `P_{<p}` 的所有 square-free divisors 求和；项数随小于 `p` 的 primes 数量呈指数增长。

这不影响 theorem 正确性，只表示 exact closed formula 并不自动等于最优 executable algorithm。

已有 P017 rough/Buchstab recursion、CRT compression、Bonferroni truncation 或 Jacobsthal bounds，都可能针对不同 task 给出更便宜的 proof certificate。

因此仍需坚持：

\[
\boxed{
\text{exact semantic formula}
\neq
\text{optimal proof algorithm}.
}
\]

## 11. 可执行规范

- `src/enterprise_math/rough_interval_mobius.py`
- `src/enterprise_math/p017_root_split_mobius.py`
- `tests/test_p017_root_split_mobius.py`

可执行层把 Möbius count 与 direct gcd oracle 在 bounded intervals 上逐一对照，仅用 Möbius positivity 重建 L067 split-shell set，并固定 `k=6,p=3` 的 upper-count-zero correction。

## 12. 前人工作边界

Primorial coprimality、Möbius inclusion–exclusion 与 Jacobsthal function 都是 established number theory，不属于 Enterprise Math 发明。

项目新增的接口，是把 L067 repair-spectrum coefficient 精确识别成由 quotient-root overshoot calculus 生成的**两个特定 moving primorial-coprime interval counts 的 positivity coupling**。
