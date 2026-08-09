# P025 ABC Radical-Support / Witness-Space 前人工作边界

状态：`ACTIVE PRIOR-ART MAP / NONCANONICAL`  
核验日期：2026-08-09

## 1. Mason–Stothers 与 Wronskian 路线

Baek 与 Lee 的 Lean 4 形式化清楚展示了 Mason–Stothers 的经典短证明：`f/rad(f)` 整除导数；`a+b+c=0` 让三个 Wronskian 变成同一个公共 witness；三个 multiplicity residual 的乘积因而整除该 witness；最后由 Wronskian 的 degree capacity 得到 radical degree 控制 [SRC-BAEK-LEE-2024-MASON-LEAN]。

P025 可以把这条证明重新解释成

`residual -> common witness -> witness capacity -> support bound`，

但 derivative、radical、Wronskian、Mason–Stothers 定理及其形式化都不是进取数论的新发现。

## 2. Pasten：整数上的 relation-conditioned arithmetic derivatives

Pasten 已经直接研究了整数版的导数桥：构造满足 Leibniz 规则、并针对指定 `a+b=c` 加法关系施加约束的 arithmetic derivations；Geometry of Numbers 给出受控大小的导数，并建立足够小的 derivations 与 ABC 猜想之间的精确联系 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

因此以下说法不能作为 P025 创新主张：

- “ABC 应存在某种整数导数”；
- “导数应同时感知乘法与 `a+b=c`”；
- “整数 Wronskian 可以吸收 `n/rad(n)` 型 multiplicity residual”；
- “证明 ABC 可转成寻找足够小的 arithmetic derivative”。

本轮全文审计进一步收紧了这一边界。

### 2.1 P025 补充 04 使用的完整 residual-product divisibility 已由 Pasten 明确证明

Pasten 在 arithmetic Wronskian inequality 的证明中明确指出

`a/rad(a)`、`b/rad(b)`、`c/rad(c)`

都整除同一个非零 Wronskian，再利用三者两两互素推出它们的乘积整除该 Wronskian [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

因此 P025 补充 04 中写作

`M | W`，其中 `M=(a/rad(a))(b/rad(b))(c/rad(c))`，

的命题应明确降格为 **ADOPTED PRIOR ART / REINTERPRETATION**，不能作为新的 P025 定理主张。项目定义的 normalized coordinate

`eta=|W|/M`

仍可作为 precision diagnostic，但它之所以为整数，直接依赖 Pasten 已有的整除证明。

### 2.2 Valuation-exponent arithmetic 同样属于明确前人工作

Pasten 的 lattice argument 已经显式使用 prime-adic valuation exponents `v_p(abc)` 对 derivative coordinates 的整除/大小约束；证明中正是通过包含 `v_p(abc)` 的 divisibility relation 得到 norm lower bounds [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

因此 P025 不能把“valuation exponents 的素因子或大小会影响 arithmetic-derivative witness”这一一般观察主张为新发现。

当前仍值得研究、且保持 `NOVELTY_UNVERIFIED` 的范围更窄：把这些数据精确正规化成 cross-minor gcd `eta_min`，进一步形成 prime-local obstruction spectrum，并把它们纳入 task-relative certificate precision。

### 2.3 本轮定向全文审计没有发现的表述

本轮对 Pasten 原文的定向检索没有发现以下明确形式：

- 把 `eta_min` 定义成 Wronskian image 的 normalized positive generator；
- `eta_min = content(alpha_hat ∧ beta_raw)/M`；
- closed cross-support formula `gcd R e_p e_q/(g p q)`；
- prime-local absorption-obstruction spectrum；
- `mu / eta_min / nu / Pareto frontier` 的 certificate-precision decomposition。

**没有检索到绝不等于原创证据。**这些对象仍维持 `NOVELTY_UNVERIFIED`，直到完成更广泛的文献审计。

## 3. Exceptional-set 路线

Bernert、Browning、Lichtman、Teräväinen 对满足 `rad(abc)<c^(1-epsilon)` 的异常三元组给出 power-saving 型计数界 [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]。Runbo Li 随后给出 `O(X^(56/85+epsilon))` 的更强指数界 [SRC-LI-2025-ABC-EXCEPTIONAL]。

因此“坏状态可以很稀薄”属于已有数论结果。P025 的潜在新增仅是把这一思想放入 quotient/collapse 语言，研究是否应在 exact-safe 与 unsafe 之外增加可复用的 scale-dependent exceptional-incidence 语义。

## 4. Derivation、lattice 与 optimization generalization 已有广泛前人工作

Kikteva 已研究 locally nilpotent derivations 上的 ABC-type generalization [SRC-KIKTEVA-2023-ABC-DERIVATION]。因此仅仅把 Mason–Stothers 从普通导数推广到更抽象 derivation，并不能作为 P025 的创新边界。

同样，Smith normal form、determinantal divisors、exterior/Pluecker coordinates、Bezout 与整数 syzygies、Dickson/Pareto antichains、affine lattice optimization、closest-vector language、linear Diophantine optimization 都属于成熟数学。它们在 P025 中是工具，不是优先权主张。

## 5. 当前项目新增候选

经过更严格的 prior-art 审计后，P025 暂时只保留以下**组合接口 / normalized diagnostics** 为 `NOVELTY_UNVERIFIED`：

1. 把 radical 遗忘的 multiplicity 写成显式 finite/integer residual，并保持它与未来 certificate language 的关系；
2. 把 Pasten 已有的 Wronskian residual divisibility 正规化为 `eta=|W|/M`，进一步研究 exact image floor `eta_min`；
3. 用带尺度 exterior/determinantal signature 编码该 floor，再压成 closed support/valuation gcd formula；
4. 把 `eta_min` 分解成 prime-local obstruction coordinates，同时明确 valuation-exponent arithmetic 本身属于 Pasten prior art；
5. 区分 certificate existence radius `mu`、arithmetic floor `eta_min`、floor-access radius `nu` 与完整 norm/absorption Pareto frontier；
6. 精确量化一个合法 constructive Bezout certificate 与 minimum task-relative access precision 之间的差距；
7. 利用 abc rows 的特殊结构，把 three-coordinate access 化成 affine integer line，把 `1+qr=p^m` 化成 exact two-variable Diophantine problem；
8. 复用 P023 query-generated precision 与 A3/A4 antichain semantics，而不重复 generic mother theorem；
9. 把 scale-dependent exceptional incidence 保留成独立可能的 semantic axis，而不把它混入 exact witness control。

这套组合是否已有等价的一般理论，仍未完成广泛优先性检索；不得使用“首次”“原创”等表述。
