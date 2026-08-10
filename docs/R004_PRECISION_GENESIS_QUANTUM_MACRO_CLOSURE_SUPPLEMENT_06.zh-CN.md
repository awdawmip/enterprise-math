# R004 精度宇宙生成 —— Supplement 06：无分数 count defect、指数坐标与 valuation repair

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_05.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

本补充针对上一轮 R004 暴露出的一个结构问题：`eta`、Bell total-variation cost、macro pair fraction 等 normalized fraction 开始像 primitive 一样进入内部语言。本轮结果表明，它们没有必要成为 primitive。

更强的结论也不是“所有计算都强行塞进一种 exponent coordinate”。不同 future language 有不同的安全 coarse state。目前浮现出的原生接口是分层的：

`integer count ray -> integer defect functional -> prime-exponent word -> operation-conditioned residue repair`。

传统 fraction 仍可以在外部科学接口中使用，但当前 R004 内部状态可以继续保持 finite、integer-first。

## 1. Rational normalization 可以降级成 count-ray view

设

`q=(q_1,...,q_m)`

是一个有限 rational probability vector。取公共 denominator `L`，则

`c_i=L q_i`

都是非负整数，并满足

`sum_i c_i=L`。

反过来，任意非零 integer count vector `c` 都给出 rational normalized view

`q_i=c_i/sum_j c_j`。

两个 count vectors 表示同一个 normalized view，当且仅当对每个 `i` 都有

`c_i sum(d) = d_i sum(c)`。

把所有 entries 同除 gcd，就得到同一 ray 的唯一 primitive integer representative。

因此 finite rational distribution 可以在内部保存成

\[
\boxed{[c_1:\cdots:c_m]}
\]

而不是 fraction tuple。

这是初等 denominator-clearing / projective count mathematics，不是 Enterprise Math 新定理。

## 2. 比较退化为 integer cross defect

对传统写法 `a/b` 与 `c/d`，定义 signed integer

\[
\boxed{\Delta=ad-cb.}
\]

则：

- `Delta=0` 当且仅当两个 normalized quantities 相等；
- `Delta>0` 当且仅当前者更大；
- `Delta<0` 当且仅当后者更大。

不需要执行 division。

如果两个 count states 分别复制任意正整数倍，`Delta` 只会乘一个正整数，所以 sign 与 zero/nonzero 状态不变。因此即便对外仍展示 fraction，cross defect 也更适合作为内部 proof object。

## 3. Integer linear defect functional 统一 kill test

更一般地，令 finite count state

`z in N_0^m`

并取

`h in Z^m`。

定义

\[
\boxed{\Delta_h(z)=h\cdot z.}
\]

把全部 counts 复制 `k>0` 次，有

`Delta_h(kz)=k Delta_h(z)`。

因此 sign、exact zero 与 half-space membership 都不依赖 normalization。

这个对象可以统一当前 R004 的：

- Bell/CHSH separating certificate；
- 实验 lower-bound margin；
- macro count word 的 cross-multiplied comparison；
- 只关心符号或 vanishing defect 的 finite linear future constraint。

### Integer-cone consequence

若 deterministic integer generators `g_1,...,g_r` 对某个 functional 都满足

`Delta_h(g_i)<=0`，

那么任意 non-negative integer combination

`z=sum_i w_i g_i`

仍满足

`Delta_h(z)<=0`。

所以只要 target `t` 有

`Delta_h(t)>0`，

就得到一个 exact integer impossibility certificate：target 不在该 generator cone/monoid 中。这只是初等 linearity / convex-semigroup mathematics，不是新的 separation theorem。

## 4. Bell 不再需要 primitive probability fraction

对一个 deterministic local response table

`lambda=(A_0,A_1,B_0,B_1)`，

定义五维 integer generator

\[
g_\lambda=(A_0B_0,A_0B_1,A_1B_0,A_1B_1,1).
\]

现有 R004 exact target 的四个 setting correlation numerators 与公共 count mass 是

\[
\boxed{t=(-12,-12,-16,16,20).}
\]

取 integer functional

\[
\boxed{h=(-1,-1,-1,+1,-2).}
\]

对全部十六个 local deterministic generators，

`h dot g_lambda`

只会等于 `0` 或 `-4`。

而 target 满足

\[
\boxed{h\cdot t=16>0.}
\]

所以 setting-independent local count cone 被一个**整数 Bell defect 16**精确分离。传统写法 `|S|=14/5>2` 只是这一个有限 obstruction 的外部表示。

Bell/CHSH 本身继续属于 prior art。R004 的变化只是 representation：primitive executable witness 可以是 integer cone certificate，而不是 rational expectation value。

## 5. Measurement dependence 变成 seed-transfer cost

给定两个 equal-total latent count rows `u,v`，定义 **seed-transfer defect**

\[
T(u,v)=\sum_i\max(u_i-v_i,0).
\]

由于总 mass 相等，positive excess 与 negative excess 必然相等，所以 `T` 正好等于把一个 row 变成另一个 row 所需重新分配的最少 count atoms 数。它等于普通 `L1` distance 的一半，但计算时完全不需要除以 2。

对四个 CHSH setting-conditioned latent rows，令

`T=max_(s,t) T(mu_s,mu_t)`。

若公共 setting mass 为 `W`，integer CHSH numerator 为 `N`，定义 Bell excess

\[
\boxed{B=|N|-2W.}
\]

上一轮 relaxed measurement-independence inequality 于是完全整数化为

\[
\boxed{B\le6T.}
\]

对 R004 已有的 denominator-60 显式 witness：

\[
W=60,\qquad N=-168,\qquad B=48,
\]

而四个 setting rows 的六个 pair 全部满足

\[
\boxed{T=8.}
\]

因此

\[
\boxed{B=6T=48.}
\]

上一轮的 `2/15` 只是外部 normalized view `T/W=8/60`；fraction 不再是 native sharp statement。

## 6. Record overlap 变成 integer two-cell state

对 threshold-record resolution `d` 与 alternative separation `delta`，定义

\[
A=\max(d-\delta,0),
\qquad
S=\min(d,\delta).
\]

于是

\[
\boxed{A+S=d.}
\]

`A` 是给出相同 record 的 environment-state 数，`S` 是给出不同 record 的 state 数。传统 overlap

`eta=A/d`

只是外部 normalized view。

若实验给出的 lower threshold 是 rational word `q/s`，内部只比较 integer margin

\[
\boxed{K=sA-qd.}
\]

`K>=0` 表示该 finite count state 可以达到 threshold；`K<0` 则在 declared multiplicative visibility model 下被排除。

对 Pedalino representative lower endpoint `9/100`，内部测试只剩

\[
\boxed{K=100A-9d.}
\]

模型内部无需 decimal/fraction。

## 7. Macro crossover 也保留为 count word

对 path `P_N` 与 record resolution `d`，直接保存两个整数：

\[
Z(N,d)=\#\{\text{zero-overlap unordered pairs}\},
\]

\[
O(N,d)=\#\{\text{positive-overlap unordered pairs}\}.
\]

当 `N>d` 时，

\[
\boxed{Z(N,d)=\binom{N-d+1}{2}},
\]

且

`Z+O=binom(N,2)`。

传统 zero-overlap fraction 只是外部 view `Z/(Z+O)`。

其单调性也不需要 division。令 `T_N=binom(N,2)`，直接计算 integer cross defect

\[
\boxed{
G_N
=Z(N+1,d)T_N-Z(N,d)T_{N+1}
\ge0.
}
\]

于是通常被说成“比例单调增长”的命题，仍然可以完全是整数定理。

Binomial-coordinate counting 属于成熟先行数学 [SRC-CHABERT-2025-INTEGER-VALUED-POLYNOMIALS]。

## 8. P005 scale multiplication 在 exponent space 中完全线性化

对正 scale factor

\[
\lambda=\prod_p p^{a_p},
\]

定义 finite-support exponent word

\[
\boxed{\nu(\lambda)=(a_p)_p.}
\]

唯一分解给出：

\[
\nu(\lambda\mu)=\nu(\lambda)+\nu(\mu),
\]

\[
\nu(\gcd(\lambda,\mu))=\min(\nu(\lambda),\nu(\mu)),
\]

\[
\nu(\operatorname{lcm}(\lambda,\mu))=\max(\nu(\lambda),\nu(\mu)),
\]

其中 min/max 都逐坐标执行。

因此 P005 positive-integer scale lattice 可以不用 logarithm，直接表示成 finite-support integer lattice / monoid。

### Rank 与 total depth 必须分开

定义

\[
\boxed{D(\lambda)=\omega(\lambda)=\#\{p:a_p>0\}}
\]

以及

\[
\boxed{H(\lambda)=\Omega(\lambda)=\sum_p a_p.}
\]

`D` 表示 active prime axes 数；`H` 表示总 prime-step depth。它们是两个不同的 finite resources。

在 global divisibility Hasse graph 中，每条 edge 只乘或除一个 prime，则

\[
\boxed{
d_H(\lambda,\mu)
=\sum_p|a_p-b_p|.
}
\]

等价地，令 `g=gcd(lambda,mu)`，

\[
d_H(\lambda,\mu)
=\Omega(\lambda/g)+\Omega(\mu/g).
\]

对 equal-exponent candidate `lambda=P^a`、squarefree rank `D`，

`H(lambda)=D a`，

恰好等于对应 exponent divisor grid 的 opposite-corner diameter。

这些都是标准 unique-factorization arithmetic；R004 的项目级价值在于把它们提升成 native precision coordinate interface。

## 9. Positive rational multiplicative quantity 也能写成 exponent word

对 positive rational `r=a/b`，定义

\[
\boxed{
\nu(r)=\nu(a)-\nu(b)\in\bigoplus_p\mathbb Z.
}
\]

于是外部 fraction `2/15` 的 exact Laurent exponent word 是

`{2:+1, 3:-1, 5:-1}`。

这说明即便某个 normalized multiplicative quantity 必须精确保留，slash 也不是 fundamental object。

但这绝不意味着 additive physics 应被强行塞进 exponent coordinates。加法会立即暴露 sharp failure boundary。

## 10. Valuation-only addition 在非对角区安全

固定 prime `p`。经典 p-adic valuation 满足 [SRC-EOM-PADIC-VALUATION]

\[
\nu_p(x+y)\ge\min(\nu_p(x),\nu_p(y)).
\]

如果两个输入 levels 不同，则必须取等号：

\[
\boxed{
\nu_p(x)\ne\nu_p(y)
\Longrightarrow
\nu_p(x+y)=\min(\nu_p(x),\nu_p(y)).
}
\]

所以**离开 equal-level diagonal 后**，valuation-only coarse state 对 addition 是 exact sufficient state。

这与成熟的 min-plus / tropical 结构相邻 [SRC-RICHTERGEbert-STURMFELS-THEOBALD-2003-TROPICAL]；R004 不主张 min rule 是新发明。

## 11. Equal-level valuation carry 无上界

对角线完全不同。

任取 prime `p`、base level `k>=0` 和想要的 extra depth `m>=1`，令

\[
x=p^k,
\qquad
y=p^k(p^m-1).
\]

则

\[
\nu_p(x)=\nu_p(y)=k,
\]

但

\[
\boxed{
\nu_p(x+y)=k+m.
}
\]

因为 `m` 任意，所以仅凭两个相同 valuation levels，不可能存在一个 bounded carry rule 决定 sum level。

这就是 exponent calculus 里的 P018 carry analogue：被丢掉的 unit/residue detail 可以沿 valuation depth 向上影响任意多层。

## 12. Finite cap K 有一个 exact residue repair

定义 capped observation

\[
q_K(x)=\min(\nu_p(x),K),
\]

并把 multiples of `p^K` 与 zero 放在 level `K`。

对 uncapped level `a<K`，写

\[
x=p^a u,
\qquad p\nmid u.
\]

保留 normalized unit residue

\[
\boxed{u\bmod p^{K-a}.}
\]

修复后的 state 是

\[
\boxed{\sigma_{p,K}(x)=(a,u\bmod p^{K-a}).}
\]

level `K` 只需要一个 terminal marker。

这个 signature 与 `x mod p^K` 等价，但把 residue 分解成 exponent level + 该 level 真正需要的 unit detail。两个 repaired signatures 可以完全通过 integer modular arithmetic 相加，并精确决定 sum 的 capped valuation。

## 13. 对 arbitrary partner，unit-residue repair 是 sharp 的

固定 level `a<K`，normalized unit residues 的数量精确是

\[
\boxed{
\varphi(p^{K-a})
=(p-1)p^{K-a-1}.
}
\]

如果 future language 包含 arbitrary additive partners，那么任意两个不同 unit residues 都不能合并。

设 `u,u'` 是 modulo

`M=p^{K-a}`

的两个不同 units。选择 unit partner

\[
v\equiv-u\pmod M.
\]

则

`u+v`

可被 `M` 整除，而

`u'+v`

不能，因为 `u'!=u mod M`。

乘回公共 factor `p^a` 后，第一个 sum 达到 capped level `K`，第二个不到。因此这两个 unit residues 拥有不同 future signatures。

所以这些 unit-residue classes 不是实现习惯，而是 declared all-partner additive language 强制要求的 distinctions。

## 14. Universal translations 会消灭全部 valuation compression

class count 会望远镜化：

\[
1+\sum_{a=0}^{K-1}\varphi(p^{K-a})
=1+\sum_{h=1}^{K}\varphi(p^h)
=\boxed{p^K}.
\]

还可以给一个更短的 future-signature 证明。

在 modulo `p^K` 的 residue space 上，若

`x != x' mod p^K`，

取 translation

\[
t\equiv-x\pmod{p^K}.
\]

则

\[
q_K(x+t)=K,
\]

而

\[
q_K(x'+t)<K.
\]

所以所有 additive translations 的 family 会区分每一个 residue。对完整 translation language，coarsest future-safe quotient 就是 exact residue equality modulo `p^K`。

于是得到本补充最强的负结果：

\[
\boxed{
\text{valuation-only }(K+1)\text{-class compression}
\xrightarrow{\text{all translations}}
p^K\text{ exact residue classes}.
}
\]

### 含义

Exponent/valuation coordinate 不是 remainder information 的 universal replacement。它们严格依赖 operation family：

- multiplication、divisibility、gcd/lcm：exponent coordinates 是天然语言；
- unequal valuation levels 的 addition：level 已经足够；
- equal levels 的 addition：carry 依赖 unit detail；
- universal additive translation language：future-safe repair 恢复完整 residue state。

这正是 P023/P024 所研究的 operation-conditioned precision boundary。

## 15. Fraction-free exact linear algebra 是可复用工具，不是 novelty

如果未来 R004 需要求解更大的 exact linear equation / inequality systems，也没有必要自动回到 ordinary rational Gaussian elimination。Bareiss integer-preserving elimination 是成熟的 fraction-free exact-linear-algebra prior art [SRC-BAREISS-1968-FRACTION-FREE]。

当前 Bell certificate 不需要该 machinery，因为十六个 generators 可以直接有限验证；但工具边界很重要：以后即便 constraint system 变大，也可以继续 integer-first，同时不能把 Bareiss 路线误报成项目原创。

## 16. 独立 executable 压力测试

在文档化之前，本轮新公式已用 exact integer enumeration 独立检查：

- **10,000** 个 scale pairs `1..100 x 1..100`：product→sum、gcd→min、lcm→max 与 Hasse-distance identities 全部成立；
- **2,970** 个 path `(N,d)` cases：normalized-growth cross defect 全部非负；
- 全部 **16** 个 local deterministic Bell generators：integer dual defect 只取 `0` 或 `-4`，target defect 精确为 `+16`；
- 显式 setting-dependent Bell witness 的六个 setting pairs，seed-transfer defect 全部精确为 `8`；
- 对 `p in {2,3,5}`、`K=1..4` 的 **414,620** 个 capped p-adic residue-pair additions，repaired `(level,unit residue)` signature 全部精确恢复；
- 同一有限 prime/cap family 共 **930** 个 residues 的 universal-translation future signatures 全部验证 injective。

这些是 bounded executable checks，不代替上面的普通证明。本轮不会因为这些独立检查就宣称 fresh full-repository CI 已通过。

## 17. 修订后的 R004 arithmetic architecture

主结论不是“禁止 fractions”，而是更严格的分层。

### Native finite layer

只要 declared operations 允许，内部优先使用

\[
\boxed{
\text{Count} + \text{Defect} + \text{Exponent} + \text{Repair}
}
\]

### External interface layer

只有当外部理论/实验本身以 fraction、percentage、real-valued expectation、visibility、TV distance 等 normalized observable 报告结果时，再把内部整数 state 转成相应传统格式。

### Operation-safety rule

不存在一个全局 privileged compressed coordinate。合法 representation 由 future operation language 决定：

- count ray 对 finite rational normalization 足够；
- integer defect functional 对 homogeneous inequality/certificate 足够；
- exponent word 对 multiplicative scale algebra 足够；
- addition/cancellation 让 valuation-only state 不安全时必须补 residue repair。

这比“用一个 universal exponent coordinate 替代 universal real-number coordinate”更符合 Enterprise Math 自己的底层逻辑。

## 18. Foundation feedback candidate

这轮真正可复用的 cross-route finding 是：

> **原生 finite coordinate 应由它能安全承载的 future-operation family 选择，而不是因为 scalar、fraction、exponent 或 residue 在形式上更漂亮。**

R004 给出一个 sharp specialization：

- valuation level 对 multiplicative/min-max operations 是合法 coarse state；
- 对 unequal-level addition，它局部合法；
- 对 universal additive translations，它不安全；
- 在 universal translation language 下，exact repair 就是 full residue modulo `p^K`。

这应以 `CONSUME/TEST` 形式回流 P018/P023/P024/Foundation。但它还不是“把 Foundation primitive state 改成 valuation vector”的理由，因为同一个 theorem 已经证明那样全局替换会失败。
