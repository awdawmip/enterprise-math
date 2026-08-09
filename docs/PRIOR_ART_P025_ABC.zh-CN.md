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

P025 当前只研究项目架构层的重解释：把一组针对关系生成的导数看成 `relation-conditioned witness family`，并比较 witness cost/precision 与 P023 future-safe refinement 的成本。

## 3. Exceptional-set 路线

Bernert、Browning、Lichtman、Teräväinen 对满足 `rad(abc)<c^(1-epsilon)` 的异常三元组给出 power-saving 型计数界 [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]。Runbo Li 随后给出 `O(X^(56/85+epsilon))` 的更强指数界 [SRC-LI-2025-ABC-EXCEPTIONAL]。

因此“坏状态可以很稀薄”属于已有数论结果。P025 的潜在新增仅是把这一思想放入 quotient/collapse 语言，研究是否应在 exact-safe 与 unsafe 之外增加可复用的 scale-dependent exceptional-incidence 语义。

## 4. Derivation generalization 已有广泛邻域

Kikteva 已研究 locally nilpotent derivations 上的 ABC-type generalization [SRC-KIKTEVA-2023-ABC-DERIVATION]。因此仅仅把 Mason–Stothers 从普通导数推广到更抽象 derivation，并不能作为 P025 的创新边界。

## 5. Restricted successive minima 已经覆盖 forbidden-sublattice minimum

Henk 与 Thiel 研究 **restricted successive minima**：在 symmetric convex body 中寻找最短 lattice points，同时要求这些 realizing points 避开一个或多个 forbidden sublattices [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA]。他们的框架明确包含“避开 proper sublattice 的 shortest-vector”问题，属于 Geometry-of-Numbers / Siegel-lemma avoidance 的既有研究邻域。

对 P025 witness flag，取

- real prime-coordinate witness space 中的 `K=[-1,1]^S`；
- `Lambda=T=ker_Z(alpha)`；
- forbidden sublattice `Lambda_1=T^circ=T intersect ker_Z(beta)`。

则 P025 定义的精确 witness precision 正好就是对应的 restricted first minimum：

`mu = lambda_1(K, T \ T^circ)`。

普通 additive radius `rho` 则是 unrestricted first minimum `lambda_1(K,T)`。

因此以下内容不能作为 P025 新发明：

- “避开 forbidden sublattice 的最短 witness”这个 invariant；
- 该 invariant 的一般 Geometry-of-Numbers bounds；
- 用 avoidance/Siegel-lemma 方法寻找小 non-degenerate lattice points。

项目真正剩下的问题更窄：`abc` relation 自身生成 `T^circ subset T`，arithmetic multiplicity demand 又给出独立 lower certificate，然后把同一个 restricted minimum 接入 exact proof-budget / future-precision semantics。

## 6. 当前项目新增候选

在当前检索范围内，P025 暂时只把以下**组合性架构**列为 `NOVELTY_UNVERIFIED`：

1. 把 quotient 遗忘信息写成显式 finite/integer residual；
2. 让 arithmetic task 自身生成 relation-conditioned witness / forbidden-sublattice flag；
3. 把 arithmetic demand、restricted first minimum、compact generator certificate 与 exact proof-loss shells 接成同一条有限结构链；
4. 比较两种恢复方式：`refine state until exact descent` 与 `keep coarse state + attach bounded witness`；
5. 再增加 scale-dependent exceptional incidence，形成 exact / bounded-witness / sparse-exception 分层。

这套组合是否已有等价的一般理论，尚未完成专门优先性检索；不得使用“首次”“原创”等表述。
