# R004 无分数 count / defect / exponent 演算 —— prior art 边界

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

本说明用于把成熟数学与 R004 的项目级组合方式分开。一个构造即使全程只使用整数，也不能因此把已有数学当成新发明。

## 1. Prime-exponent 与 valuation 坐标属于成熟数学

唯一分解把每个正整数规范地对应到一个有限 prime-exponent word。等价地说，正整数乘法幺半群是由 primes 生成的自由交换幺半群；正有理数乘法群则可表示为有限支持的整数 exponent word。在这些坐标下，乘法变成指数加法，整除变成逐坐标偏序，gcd/lcm 分别变成逐坐标 minimum/maximum。

p-adic valuation 也是经典数论对象，满足

`v_p(xy)=v_p(x)+v_p(y)`

以及

`v_p(x+y)>=min(v_p(x),v_p(y))`，

且当两个输入 valuation 不同时取等号 [SRC-EOM-PADIC-VALUATION]。因此 R004 不主张 valuation arithmetic、p-adic order、non-Archimedean norm 或 ultrametric 是 Enterprise Math 的发明。

## 2. Tropical / min-plus algebra 属于成熟数学

Tropical geometry 已长期使用 min-plus / max-plus semiring，并形成完整研究传统 [SRC-RICHTERGEbert-STURMFELS-THEOBALD-2003-TROPICAL]。因此 R004 不能把

`v_p(x+y)=min(v_p(x),v_p(y))`

在非等 level 情况下的性质重新命名成“新 tropical arithmetic”。

R004 真正使用的是一个更窄的**负边界**：valuation-only addition 在两个输入 level 不同时确实服从 min 规则，但在相同 level 上，额外 divisibility/cancellation depth 可以任意大。随后把这个 carry 边界接回已经 canonical 的 P023/P024 问题：某个 coarse quotient 到底允许哪些 future operations 真正下降。

## 3. Denominator clearing 与 projective count ray 是初等先行数学

任意有限 rational probability vector 都可以乘一个公共 denominator，得到非负整数 count vector。再把所有 count 同除 gcd，就得到同一 rational ray 的唯一 primitive count representative。反过来，任意非零 count vector 都定义一个 rational normalized distribution。

因此 R004 不主张 denominator clearing、homogeneous/projective count coordinates、cross multiplication 或 determinant-style ratio comparison 是新数学。

项目级新增只是一条架构选择：把 rational normalization 降级为**外部显示层**，而把 integer counts 与 signed cross defects 提升为当前有限 toy 的原生状态。

## 4. Bell/CHSH 与凸分离属于 prior art

Bell 与 CHSH 理论、local deterministic response tables 以及线性 inequality certificates 都是成熟先行工作，并已经在 R004 主 source corpus 中登记。把同一个 Bell target 改写成 integer cone，不会自动产生“新 Bell theorem”。

R004 使用的只是一个初等线性事实：如果某个 integer linear functional 在每个 deterministic generator 上都不为正，那么它在这些 generators 的任意 non-negative integer combination 上仍然不为正。当前选定 target 在一个 CHSH functional 上得到正的 integer defect，从而形成一个完全不需要 denominator 的 impossibility certificate。它是 representation choice 与 application-specific certificate，不是对 convex duality 或 Bell polytope 的原创声明。

## 5. Fraction-free exact linear algebra 已经存在

Bareiss 早已发展 integer-preserving Gaussian elimination，用于避免 exact linear algebra 中不必要的 fraction growth [SRC-BAREISS-1968-FRACTION-FREE]。因此如果 Enterprise Math 以后需要更大的 exact linear constraint solver，Bareiss/fraction-free 路线应被视为优先复用的**先行工具**，而不是项目的新算法。

当前 R004 定理并不依赖 Bareiss elimination；目前 Bell certificate 只有十六个 generators，可以直接做有限整数验证。

## 6. Integer-valued polynomial / binomial coordinates 也属于成熟数学

Integer-valued polynomial theory 与 binomial-coordinate methods 已经有成熟理论 [SRC-CHABERT-2025-INTEGER-VALUED-POLYNOMIALS]。因此使用 binomial coefficients 与 finite differences 表达 finite combinatorial counts 也不是 Enterprise Math 的新发明。

例如 R004 的 path crossover count

`Z(N,d)=binom(N-d+1,2)`

只应被视作初等组合计数。它的项目级价值仅在于：一个看起来需要“宏观比例”的量，其实可以始终保存为两个整数 counts，再通过 cross multiplication 比较，无需把 fraction 提升为 primitive。

## 7. R004 当前正在检验的项目级组合

本轮提出的 research-local 分层接口是：

`count ray -> integer defect functional -> exponent word -> operation-conditioned residue repair`。

其语义分别是：

- **count rays**：承载 finite normalized / rational phenomena；
- **integer defects**：承载比较、Bell certificate、kill-test margin 与 monotonicity check；
- **prime-exponent words**：承载 multiplicative precision scales；
- **residue repair**：只在 declared additive future language 无法通过 valuation-only quotient 下降时补回。

当前最强的项目级新边界，并不是某个新的 p-adic theorem，而是这一条 cross-surface 结论：valuation quotient 对 multiplicative operations 可以极度压缩，但一旦 future language 包含 universal additive translations，所有压缩都会被迫恢复；在 cap `K` 下，future-safe closure 精确需要 `p^K` 个 classes，与完整 residue space modulo `p^K` 一样大。

该结论应理解为 established valuation + quotient mathematics 在 R004/P023/P024 语境下的 specialization。整套 Enterprise Math packaging 的历史 novelty 仍保持 `NOVELTY_UNVERIFIED`。
