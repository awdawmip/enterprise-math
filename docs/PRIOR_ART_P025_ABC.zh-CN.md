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

因此 P025 补充 04 中写作 `M | W` 的命题应明确降格为 **ADOPTED PRIOR ART / REINTERPRETATION**，不能作为新的 P025 定理主张。项目定义的 normalized coordinate `eta=|W|/M` 仍可作为 precision diagnostic，但其整数性直接依赖 Pasten 已有整除证明。

### 2.2 Valuation-exponent arithmetic 同样属于明确前人工作

Pasten 的 lattice argument 已显式使用 `v_p(abc)` 对 derivative coordinates 的整除/大小约束。因此 P025 不能把“valuation exponents 的素因子或大小会影响 arithmetic-derivative witness”这一一般观察主张为新发现。

当前仍值得研究、并保持 `NOVELTY_UNVERIFIED` 的范围更窄：把这些数据精确正规化为 cross-minor gcd `eta_min`，进一步形成 prime-local obstruction spectrum，并把它们纳入 task-relative certificate precision。

### 2.3 定向全文审计没有发现的表述

本轮对 Pasten 原文的定向检索没有发现以下明确形式：

- `eta_min` 作为 Wronskian image 的 normalized positive generator；
- `eta_min = content(alpha_hat ∧ beta_raw)/M`；
- closed cross-support formula `gcd R e_p e_q/(g p q)`；
- prime-local absorption-obstruction spectrum；
- `mu / eta_min / nu / Pareto frontier` 的 certificate-precision decomposition。

**没有检索到绝不等于原创证据。**这些对象仍维持 `NOVELTY_UNVERIFIED`，直到完成更广泛文献审计。

## 3. Exceptional-set 路线

Bernert、Browning、Lichtman、Teräväinen 对满足 `rad(abc)<c^(1-epsilon)` 的异常三元组给出 power-saving 型计数界 [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]。Runbo Li 随后给出 `O(X^(56/85+epsilon))` 的更强指数界 [SRC-LI-2025-ABC-EXCEPTIONAL]。

因此“坏状态可以很稀薄”属于已有数论结果。P025 的潜在新增仅是把这一思想放入 quotient/collapse 语言，研究是否应在 exact-safe 与 unsafe 之外增加可复用的 scale-dependent exceptional-incidence 语义。

## 4. Derivation、lattice 与 optimization generalization 已有广泛前人工作

Kikteva 已研究 locally nilpotent derivations 上的 ABC-type generalization [SRC-KIKTEVA-2023-ABC-DERIVATION]。因此仅仅把 Mason–Stothers 从普通导数推广到更抽象 derivation，并不能作为 P025 的创新边界。

同样，Smith normal form、determinantal divisors、exterior/Pluecker coordinates、Bezout 与整数 syzygies、Dickson/Pareto antichains、affine lattice optimization、closest-vector language、linear Diophantine optimization 都属于成熟数学。它们在 P025 中是工具，不是优先权主张。

## 5. Numerical-semigroup / Apéry / factorization-length 边界

补充 16–17 把 signed block access 运输成 numerical-semigroup defect problem。周围的一般数学已经有大量前人工作，因此必须进一步收窄 P025 的创新边界。

Chapman、Dugan、Gaskari、Lycan、Mendoza De La Cruz、O'Neill、Ponomarenko 已系统研究 numerical semigroup 中的 generalized `p`-length，明确包含 `p=infinity`，并使用 Apéry-set 方法研究 asymptotic/eventual structure [SRC-CHAPMAN-ETAL-2024-P-LENGTHS]。因此 P025 不把以下内容据为新发现：

- `L_infinity` factorization length；
- Apéry-set residue compression；
- extremal numerical-semigroup factorization invariants 的 eventual quasipolynomial / affine-periodic behavior。

Garcia、Omar、O'Neill、Yih 还研究了**指定且不要求最小的 generator list** 上的 factorization statistics [SRC-GARCIA-OMAR-ONEILL-YIH-2019-FACTOR-LENGTH-II]。这与 P025 特别相关，因为不同 prime-labelled certificate coordinates 可能拥有相同或 semigroup-redundant 的 coefficient values。因此，“factorization geometry/statistics 会依赖 chosen labelled/nonminimal generator list，而不仅取决于生成出的 monoid”这一一般原则，也不能作为 P025 原创主张。

补充 16–17 当前仅把更窄的内容保留为 `NOVELTY_UNVERIFIED`：

- `y=r*1-x` 把 signed `L_infinity` certificate access 精确变成 bounded nonnegative semigroup-defect problem；
- 由该 signed transform 强制出现的 `ceil(L_j/2)` task-complete tail-certification coordinate；
- `finite tail signature + finite exception table` 作为整个 nonnegative certificate-access response 的 exact representation；
- 这些对象与 P023 task-relative precision 的整合，而不是对 numerical-semigroup general theory 的原创主张。

定向检索没有看到同样的整体接口，不等于获得优先性证据。

## 6. 当前项目新增候选

经过更严格的 prior-art 审计后，P025 暂时只保留以下**组合接口 / normalized diagnostics** 为 `NOVELTY_UNVERIFIED`：

1. 把 radical 遗忘的 multiplicity 写成显式 finite/integer residual，并保持它与未来 certificate language 的关系；
2. 把 Pasten 已有的 Wronskian residual divisibility 正规化为 `eta=|W|/M`，进一步研究 exact image floor `eta_min`；
3. 用带尺度 exterior/determinantal signature 编码该 floor，再压成 closed support/valuation 与 block-content formulas；
4. 把 `eta_min` 分解成 prime-local obstruction coordinates，同时明确 valuation-exponent arithmetic 本身属于 Pasten prior art；
5. 区分 certificate existence radius `mu`、arithmetic floor `eta_min`、floor-access radius `nu` 与完整 norm/absorption Pareto frontier；
6. 精确量化合法 constructive Bezout certificate 与 minimum task-relative access precision 之间的差距；
7. 利用 abc rows 特殊结构，把 access 化为 affine/Diophantine/blockwise preimage problems；
8. 把 high-dimensional block access 运输为 Apéry-controlled signed defect problem，同时明确 Apéry 与 `L_infinity` factorization mathematics 属于 prior art；
9. 按 future language 继续压缩 access state：image content、candidate Apéry branches、certified tail 或 finite exact response；
10. 复用 P023 query-generated precision 与 A3/A4 antichain semantics，而不重复 generic mother theorem；
11. 把 scale-dependent exceptional incidence 保留为独立可能 semantic axis，而不混入 exact witness control。

这套组合是否已有等价的一般架构理论，仍未完成广泛优先性检索；不得使用“首次”“原创”等表述。
