# Legendre 压力测试 — 补充 17

状态：`ACTIVE RESEARCH NOTE`  
范围：保留重数的 mirror CRT 容量细化  
依赖：规范 P017-L020、L046–L048、L052  
纪律：本文**不**证明 Legendre 猜想。CRT 代数属于经典数学；这一 square-basin 特化的历史创新性尚未核实。

## 1. 先做语义吸收

规范 P017-L020 已经证明 square-basin smooth-tail dichotomy。对

\[
k^2<n<(k+1)^2,
\]

把所有 `p<=k` 的素因子连同重数全部保留，定义 full `k`-smooth core

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)},
\qquad Q_k(n)=\frac{n}{S_k(n)}.
\]

则 `Q_k(n)=1`，或者 `Q_k(n)` 是唯一一枚 `>k` 的素数；并且该状态为素数当且仅当 `S_k(n)=1`。

因此本文**不重新引入**这一分类。本文唯一新增的项目层结果，是把已经规范化的 full smooth cores 直接送入 mirror CRT cell，而不是丢掉 prime-power multiplicity 后只保留 squarefree support。

## 2. L053 — Full-core mirror CRT 容量细化

固定 `k>=2`，记

\[
M=k(k+1),
\]

并令 `1<=r<k` 是一枚 anchor-surviving radius，且两个 mirror states

\[
n_-=M-r,
\qquad
n_+=M+r
\]

都为复合数。定义它们在规范 L020 中的 full smooth cores

\[
S_-=S_k(n_-),
\qquad
S_+=S_k(n_+),
\qquad
S=S_-S_+.
\]

则：

1. `S_->1`、`S_+>1`；
2. `gcd(S_-,S_+)=1`；
3. `S` 为奇数且 `gcd(S,M)=1`；
4. 定义
   \[
   w\equiv rM^{-1}\pmod S,
   \]
   则
   \[
   w\equiv1\pmod{S_-},
   \qquad
   w\equiv-1\pmod{S_+},
   \qquad
   w^2\equiv1\pmod S;
   \]
5. 定义
   \[
   e\equiv\frac{1+w}{2}\pmod S,
   \]
   则
   \[
   e^2\equiv e\pmod S,
   \qquad
   \boxed{\gcd(e-1,S)=S_-},
   \qquad
   \boxed{\gcd(e,S)=S_+};
   \]
6. 实际 radius 落在唯一 residue class
   \[
   r\equiv M(2e-1)\pmod S.
   \]

因此，idempotent 精确恢复的是两侧完整 prime-power cores，而不仅是它们的 squarefree supports。

## 3. 证明

anchor survival 表示：任何 `p<=k` 且 `p|M` 的素数都不能整除任一 mirror state。因此所有出现在 `S_-S_+` 中的素数都与 `M` transverse，故 `gcd(S,M)=1`。由于 `2|M`，同一条件还说明 `S` 为奇数。

两个 mirror states 满足

\[
M-r\equiv0\pmod{S_-},
\qquad
M+r\equiv0\pmod{S_+}.
\]

由于 `M` 在两个 core 模数下均可逆，

\[
rM^{-1}\equiv1\pmod{S_-},
\qquad
rM^{-1}\equiv-1\pmod{S_+}.
\]

同时，anchor survival 后两侧 transverse small-prime support 互素，因此两侧所有对应 prime powers 也互素。中国剩余定理于是把两种符号组合成唯一的 `w mod S`，并立即得到 `w^2=1 mod S`。

因为 `S` 为奇数，`2` 在 `mod S` 下可逆，所以 `e=(1+w)/2` 为 idempotent。在 lower core 上 `e=1`，在 upper core 上 `e=0`；再利用两个因子互素，即得到上面的两个精确 gcd 恢复公式。最后乘回 `M`，得到 radius 在 `mod S` 下的唯一 residue class。

## 4. 对 squarefree CRT cell 的容量细化

令

\[
D=\operatorname{rad}(S)
\]

为规范 L046–L048 所使用的 squarefree transverse-support modulus。由于 `D|S`，任何满足 full-core `mod S` radius congruence 的解，必然也满足对应的 squarefree `mod D` sign-pattern congruence。

因此在 bounded radius window `1<=r<k` 内，

\[
\boxed{
\mathcal R_{\rm full}(k;S,e)
\subseteq
\mathcal R_{\rm sf}(k;D,e_D)
}
\]

从而

\[
\boxed{
\operatorname{cap}_{\rm full}
\le
\operatorname{cap}_{\rm sf}.
}
\]

特别地，

\[
\boxed{S\ge k\quad\Longrightarrow\quad
\operatorname{cap}_{\rm full}\le1.}
\]

也就是说，不引入任何新的筛法表示，仅保留原状态里本来就存在的 prime-power multiplicity，就可能把一个含多个 bounded radii 的 squarefree CRT cell 压缩到唯一 radius。

## 5. 严格改进 witness

取

\[
k=31,
\qquad M=31\cdot32=992,
\qquad r=7.
\]

则

\[
n_-=985=5\cdot197,
\qquad
n_+=999=3^3\cdot37.
\]

所以

\[
S_-=5,
\qquad
S_+=27,
\qquad
S=135,
\qquad
D=15.
\]

规范 squarefree sign-pattern progression 在 bounded radius window 中给出

\[
\mathcal R_{\rm sf}=\{7,22\},
\]

而 full-core progression 只有

\[
\boxed{\mathcal R_{\rm full}=\{7\}}.
\]

因此该 refinement 可以严格变强。

## 6. 来自 L020 的 bounded-core 支撑推论

当 L020 的 residual tail 非平凡时，`Q_k(n)>k`。又因 `n<(k+1)^2`，

\[
S_k(n)=\frac{n}{Q_k(n)}<\frac{(k+1)^2}{k+1}=k+1.
\]

所以

\[
\boxed{Q_k(n)>1\quad\Longrightarrow\quad S_k(n)\le k.}
\]

这里只把它登记为规范 L020 的直接支撑推论，而不是再次包装成新的 smooth-tail classification theorem。

## 7. 对 parity hard core 的结构后果

此前的 squarefree mirror CRT 只记录“哪些小素数选择 `+` 侧，哪些选择 `-` 侧”。L053 进一步记录状态中已经存在的完整指数。因此 hard branch 已经比“两个复合 mirror states 具有同一 squarefree support pattern”更窄：

\[
\boxed{
\text{surviving hard core}
\subseteq
\{S_-S_+<k\}
}
\]

除非 full-core congruence 已经把 bounded radius cell 压成至多一个候选。

这一结果本身还不能消灭剩余的 singleton-small-core + large-prime-tail 阻碍，但它把该阻碍压进了一个严格更小、保留 multiplicity 的状态空间。

## 8. 可执行核验

`observed_mirror_full_core_idempotent(k,r)` 直接复用规范 L020 的 `square_basin_smooth_tail` 实现 L053。回归测试核验：

- 完整 prime-power cores 的精确恢复；
- `D|S`；
- full-core lifts 包含于 squarefree sign-pattern lifts；
- `cap_full<=cap_sf`；
- `S>=k` 时至多一个 bounded lift；
- 严格 witness `k=31,r=7`。

有限测试只审计实现；定理证明是上面的 CRT 整数论证。

## 9. 下一目标

把 L052 root-channel disjointness、L053 multiplicity-preserving CRT capacity、T113 exact quotient-branch threshold 和 exact first-factor cofactor windows 组合起来。剩余压力应集中到

\[
S_-S_+<k
\]

且至少一侧携带 large prime tail 的区域。下一阶段就在这里检验 lower-band recursion 是否能够给出真正小于普通 Buchstab bookkeeping 的容量界。
