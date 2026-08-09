# Legendre 压力测试 — 补充 21

状态：`PROVED + OPEN FRONTIER RESEARCH NOTE`  
范围：通过对偶因子窗口研究 high-band root-shell repair  
依赖：P007 对偶因子窗口补充 02、P017 high-band rough windows、P023-S9 最小 repair 计数  
纪律：素数定理属于经典前人工作。关于真实 high-band multiplicity 的陈述严格区分为已证明有限见证与“是否无界”的开放问题。

## 1. 为什么 lower-band 的一比特 repair 不能直接复用

P017 补充 20 已经把 lower-band 的真实跨 shell root ambiguity 完全局部化：只有 `k=5,8` 真正需要 binary repair。

同样结论在 high least-factor band

\[
p^2\ge2k
\]

中是错误的。

同一个保留 root fiber 内可以出现很多不同 least-prime shells。正确对象因此是**局部 shell split multiplicity**，而不是固定 shell bit。

## 2. Raw 与 realized root-label 集合

固定 square basin

\[
(k^2,k(k+2)]
\]

以及保留的 cofactor root index `s`；其 quotient bucket 为

\[
J_s=[s^2,s(s+2)].
\]

定义 raw high-band prime-label envelope：

\[
P^{\rm win}_{k,s}
=
\{p\le k:\ p\text{ prime},\ p^2\ge2k,\ W_p(k)\cap J_s\ne\varnothing\}.
\]

定义 realized label set：

\[
P^{\rm sh}_{k,s}
=
\{p\in P^{\rm win}_{k,s}:\exists q\in W_p(k)\cap J_s\text{ 为 }p\text{-rough}\}.
\]

于是

\[
\boxed{P^{\rm sh}_{k,s}\subseteq P^{\rm win}_{k,s}.}
\]

相应局部 repair burden 为

\[
R^{\rm win}_{k,s}=|P^{\rm win}_{k,s}|,
\qquad
R^{\rm sh}_{k,s}=|P^{\rm sh}_{k,s}|.
\]

只有第二个才是实际 P017 状态在 root 上恢复 shell label 所需的 task-minimal burden。

## 3. L058 —— 精确 high-band raw factor window

状态：`PROVED`。

由 P007-S2-T03，所有能够到达 root `s` 的 raw factor labels 精确落在

\[
\boxed{
D_{k,s}
=
\left[
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
\right].
}
\]

因此

\[
\boxed{
P^{\rm win}_{k,s}
=
D_{k,s}
\cap\{p\le k:p\text{ prime},\ p^2\ge2k\}.
}
\]

### 证明

`W_p(k)` 命中 root bucket，当且仅当

\[
k^2<p\,s(s+2)
\]

且

\[
p\,s^2\le k(k+2).
\]

这正是 `D_{k,s}` 的两个整数端点不等式。随后再显式施加 prime、least-factor range 与 high-band 条件即可。∎

于是一个 root-shell collision 问题被压成“一个整数区间 + admissibility predicates”。

## 4. L059 —— realized repair 的初等局部上界

状态：`PROVED`。

对任意真实 least-prime shell 状态 `n=pq`，若保留 root `s=R_2(q)`，则 `p<=q` 且 `n>k^2`，所以

\[
q>k.
\]

因此

\[
s\ge\lfloor\sqrt{k}\rfloor.
\]

记

\[
r=\lfloor\sqrt{k}\rfloor.
\]

由精确对偶窗口得到粗但统一的界

\[
\boxed{
R^{\rm sh}_{k,s}
\le
R^{\rm win}_{k,s}
\le
2r+8
\qquad(k\ge4).
}
\]

### 证明

去掉 prime/high-band filters 只会增加数量，所以 raw multiplicity 至多为整数窗口基数

\[
C_{k,s}
=
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
-
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor.
\]

对应的实数端点差为

\[
\Delta_{k,s}
=
\frac{2k(s+k+2)}{s^2(s+2)},
\]

它对正 `s` 递减。因为 `s>=r` 且 `k<(r+1)^2`，所以 `k<=r(r+2)`，从而

\[
\Delta_{k,s}
\le
\Delta_{k,r}
\le
2r+8.
\]

最后使用 `floor(x)-floor(y)<=ceil(x-y)`，得到 `C_{k,s}<=2r+8`。∎

这个界故意保持初等且并不紧。它的意义是：所需 shell repair 虽然不是常数，但仍是有限且对 `k` 次线性增长。

## 5. L060 —— square-of-square 对角 factor window

状态：`PROVED`。

取

\[
k=t^2,
\qquad
s=t,
\qquad
t\ge6.
\]

则 dual factor window 为

\[
D_{t^2,t}
=
\left[
\left\lfloor\frac{t^4}{t(t+2)}\right\rfloor+1,
\left\lfloor\frac{t^2(t^2+2)}{t^2}\right\rfloor
\right].
\]

因为

\[
\frac{t^3}{t+2}
=t^2-2t+4-\frac8{t+2},
\]

再施加 least-factor bound `p<=k=t^2` 后得到

\[
\boxed{
D_{t^2,t}\cap[1,t^2]
=[(t-1)^2+3,t^2].
}
\]

该区间内的所有 prime 都自动满足 high-band 条件。

## 6. L061 —— raw high-band root repair multiplicity 无界

状态：`PROVED`；最后的增长矛盾只使用经典素数定理。

令

\[
A_t
=
\#\{p\text{ prime}:(t-1)^2<p\le t^2\}.
\]

由 L060，

\[
R^{\rm win}_{t^2,t}
=
\#\{p\text{ prime}:(t-1)^2+3\le p\le t^2\}.
\]

两者最多相差 1，因为只删掉了 `(t-1)^2` 后面的两个整数；对 `t>=6`，两个连续整数中至多一个能为 prime。因此

\[
\boxed{
A_t-1
\le
R^{\rm win}_{t^2,t}
\le
A_t.
}
\]

### 无界性的证明

如果 `A_t` 全局被常数 `C` 控制，则把连续平方区间逐段相加得到

\[
\pi(T^2)
=
\sum_{t=2}^{T}A_t+O(1)
=O(T).
\]

但经典素数定理给出

\[
\pi(T^2)
\sim
\frac{T^2}{2\log T},
\]

它不是 `O(T)`。所以 `A_t` 无界，进而

\[
\boxed{R^{\rm win}_{t^2,t}\text{ 无界}.}
\]

由 P023-S9，如果一种 representation 把 raw exact-window 的每个 label 都当作可能任务状态，那么在 root-only 状态之上不存在全局固定有限 alphabet 的 repair。

这给出一个严格数论原因：**envelope precision 可以携带无界 label burden。**

## 7. L062 —— 固定 one-bit repair 在真实 high-band shell 上也已经失败

状态：`PROVED BY EXPLICIT FINITE WITNESS`。

在

\[
k=1737,
\qquad
s=45
\]

时，同一个真实 root fiber 同时包含以下 8 条不同 least-prime shells：

\[
\boxed{
1429,1439,1447,1451,1459,1471,1481,1489.
}
\]

每个 label 都在 root-45 bucket 内拥有真实 `p`-rough cofactor。因此

\[
\boxed{R^{\rm sh}_{1737,45}=8.}
\]

P023-S9-T03 于是给出：如果保留 root 45 并要求恢复 least-prime shell，则该 fiber 上任何 repair coordinate 的 alphabet 至少需要 8 个符号。

所以 universal one-bit、甚至 two-bit high-band shell repair 都是错误的。

## 8. Realized burden 的有界增长证据

精确 executable scan 找到以下首次出现的 multiplicity：

- `2`：`k=8`、root `3`、shells `(5,7)`；
- `3`：`k=56`、root `8`、shells `(41,43,47)`；
- `4`：`k=127`、root `12`、shells `(97,103,107,109)`；
- `5`：`k=317`、root `20`、shells `(229,233,239,241,251)`；
- `6`：`k=629`、root `25`；
- `7`：`k=1242`、root `39`；
- `8`：`k=1737`、root `45`。

在 square-of-square 对角线上，精确有限审计还得到

\[
(t,R^{\rm win},R^{\rm sh})
=(100,20,3),
(200,39,6).
\]

这些数字是**计算观察**，不是“realized multiplicity 无界”的证明。

## 9. 对角 realizability 变成 prime-pair 问题

对 `k=t^2,s=t,t>=6`，每个 raw candidate prime `p` 都远大于 root bucket 内任意 `q` 的 `sqrt(q)`。因此该 bucket 内一个 `p`-rough quotient 必须本身就是 prime。

所以对角真实 burden 精确计数满足以下条件的 prime pairs `p,q`：

\[
(t-1)^2+3\le p\le t^2,
\qquad
t^2\le q\le t^2+2t,
\]

且

\[
t^4<pq\le t^4+2t^2.
\]

这已经不是 raw interval count，而是一个很薄的 near-diagonal semiprime incidence problem。

### Centered Goldbach 子族

令 `K=t^2`，并写

\[
p=K-a,
\qquad
q=K+a+2.
\]

则

\[
p+q=2K+2
\]

且

\[
\boxed{pq=K(K+2)-a(a+2).}
\]

只要 `p,q` 都是 prime，且

\[
a(a+2)<2K,
\]

则乘积落在 square basin 中，`p` 是其 least prime factor，`q` 仍落在 root bucket `t`。因此每个这样的 near-central Goldbach representation 都贡献一条 root `t` 上的真实 high-band shell。

这给 actual repair multiplicity 与局部 prime-pair structure 建立了明确桥梁，但并不声称已经解决该 prime-pair 问题。

## 10. 开放前沿 —— realized high-band repair multiplicity 是否无界？

定义

\[
H(k)
=
\max_s R^{\rm sh}_{k,s}.
\]

目前已经知道

\[
H(1737)\ge8,
\]

而 raw envelope 的对应量已严格证明无界。

当前开放问题是

\[
\boxed{\sup_k H(k)=\infty\ ?}
\]

第 9 节的对角化解释了为什么它明显比 raw-window unboundedness 更难：admissibility filter 已经把一维 prime-counting 问题变成了很薄的 prime-pair incidence 问题。

这应作为真正的数论前沿继续攻击，而不能从有界计算增长直接假定答案。

## 11. 工具反哺

本阶段再增加两条长期研究纪律。

第一，

\[
\boxed{
\text{candidate interval count}
\to
\text{prime-label envelope}
\to
\text{p-rough realized labels}
}
\]

是三种不同 precision 层级。

第二，P023 的 local split multiplicity 不只是工程状态成本。在 P017 中它成为真正的数论 observable：其增长第一层由 prime density 控制，第二层再由 prime-pair realizability 控制。

## 12. 可执行规格

- `src/enterprise_math/quotient_window.py`
- `src/enterprise_math/p017_high_band_root_precision.py`
- `tests/test_p007_dual_factor_window.py`
- `tests/test_p017_high_band_root_precision.py`

有限计算负责精确见证和回归。L058–L061 是普通数学证明；L062 是显式有限 witness theorem；realized-shell multiplicity 的无界性仍保持开放。
