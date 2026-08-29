# 乘法原生分离几何：互素纤维、无限分离与桥操作公理化 — Research Return

Task: `RS-MULTIPLICATIVE-NATIVE-SEPARATION-GEOMETRY`  
Publication: `TP2-1D8664162DEA456852C1`  
Researcher-ID: `EM-MBGG0-7A2C91`  
Claim: `chatgpt-mbgg0-20260829-1851-7a2c91`  
Execution record: `ER-7A2C91E44F9B2D6C08A1`

## Terminal verdict

`SUCCESS / OPERATION-SENSITIVE-SEPARATION / TAGGED-CARRIER-FIBRATION / PURE-MULTIPLICATIVE-SELECTIVE-COLLAPSE-BARRIER / BRIDGE-TAXONOMY-FROZEN`

核心结论不是“互素整数天然处在无限远”，而是更精确的四层结论：

1. **乘法本身并不强迫互素断连。** 若先把两个整数放入同一个允许质因子 carrier 中，则固定 carrier 内的乘/除坐标运动可以连接完全互素的 active supports。
2. **最小 carrier lift + carrier-preserving native alphabet** 会产生真实的断连：canonical minimal lifts 的连通分量由 prime carrier 精确标记，因此 `gcd(m,n)=1`（且 `m,n>1`）推出 native separation；更强地，`supp(m) != supp(n)` 就已断连。
3. 普通整数值会忘记“允许哪些 prime channels”的 ambient carrier。于是存在 **整数投影不变、几何状态改变** 的桥：carrier authorization / restriction。这种桥在普通数轴上距离为 0，却在乘法几何里非平凡。
4. 对隐藏 squarefree CRT channels，纯乘法/求逆不能从单位元族制造“只在部分 channels 为 0”的非平凡 zero-divisor witness。要得到 factor endpoint，必须有某个 primitive input 或非纯乘法操作首次制造 **proper nonempty selective-collapse pattern**。这给后续 BRC bridge 一个可审计的硬门槛。

因此，本任务支持的“新数轴”不是一条线，而是

`prime-carrier base / support lattice + exponent-lattice fibers + explicit bridge morphisms`。

---

## 0. 输入边界与标准背景

已读取冻结依赖：

- `research_result_records/RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS/RR-C28C28A7C8EF8B9C96F6.json@b74c886f...`
- `research_returns/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_RETURN_20260829.md@b74c886f...`

依赖中已经证明 factor-edit / valuation-L1 几何与普通加法局部性双向无界失真，并证明完整 M1/M2 邻接不能忠实压成一条一维轴。本任务不重做这些结果，而是进一步取消 L1 距离作为第一性对象。

标准背景只作建模底座、不作新颖性主张：

- 正整数乘法可用 prime-exponent finitely-supported vector 表示；mathlib 的 `Nat.factorization : ℕ → ℕ →₀ ℕ` 是同一标准编码。
- pairwise-coprime 因子的 Chinese remainder theorem 把模乘积的商环分解为 factor rings 的直积；squarefree 情形为有限域直积。

本任务的新内容是：**把 ambient prime carrier 作为额外状态变量保留，并把 carrier change 与 channel-selective collapse 分离成不同桥型。**

---

# G0 — Native state model

## DEFINITION G0.1 — Prime carrier fiber

令 `P` 为所有素数集合。对每个有限 carrier `C ⊂ P` 定义

\[
X_C := \mathbb N_0^C.
\]

状态写作

\[
(C,a),\qquad a=(a_p)_{p\in C},\ a_p\ge 0.
\]

整数投影为

\[
\pi(C,a)=\prod_{p\in C}p^{a_p}.
\]

active support 为

\[
\operatorname{asupp}(C,a)=\{p\in C:a_p>0\}.
\]

carrier 与 active support 必须区分：`C` 是**被授权可使用的 prime channels**，active support 是当前真正出现的 channels。

## DEFINITION G0.2 — Canonical minimal-carrier lift

对 `n>1` 定义

\[
\lambda(n):=(\operatorname{supp}(n), (v_p(n))_{p\mid n}).
\]

并令 `λ(1)=(∅,0)`。

这是普通整数到 tagged state space 的一个 canonical section，但不是唯一 ambient realization：只要 `supp(n) ⊆ C`，都可用零填充得到 `(C,a_C)` 且 `π(C,a_C)=n`。

### EXAMPLE — integer projection forgets carrier

`6` 同时可表示为

- `({2,3}, (1,1))`,
- `({2,3,5}, (1,1,0))`,
- `({2,3,5,7}, (1,1,0,0))`。

整数 `6` 本身不记录“5、7 是否已被授权为 native channel”。

## DEFINITION G0.3 — Ambient fixed-carrier native alphabet `A_amb(C)`

对 `p∈C`，允许一步

\[
a\mapsto a+e_p,
\]

以及当 `a_p>0` 时

\[
a\mapsto a-e_p.
\]

也就是在固定 `C` 内进行 prime-exponent 的单位乘/除。active support 可以出生或消失，但 **carrier `C` 不变**。

这点很重要：我们没有通过“禁止 support change”循环定义断连。固定 carrier 内甚至允许从一个 active support 完全消失后再生成另一个 disjoint active support。

## DEFINITION G0.4 — Strict minimal-support alphabet `A_strict`

在 bare integer 上，若当前 `p` 指数至少为 1，则可 `×p`；可 `/p` 但要求除后 `p` 指数仍至少为 1。也就是任何一步都保持 exact prime support。

`A_strict` 等价于每个 fixed exact-support positive orthant

\[
\mathbb N_{\ge1}^{S}
\]

内部的坐标单位运动。

---

# G1 — Separation theorem, counterexample, and alphabet classification

## THEOREM G1.1 — Fixed-carrier fiber connectivity

对任意有限 `C`，图 `X_C` 在 `A_amb(C)` 下连通。

### Proof

任意 `a,b∈N_0^C`，逐坐标把 `a_p` 减到 `b_p` 或加到 `b_p`；每步恰为 `±e_p`，且坐标始终非负。故存在 native path `a→b`。∎

## THEOREM G1.2 — Tagged total space components are exactly carrier fibers

令

\[
X:=\bigsqcup_{C\subset P,\ |C|<\infty}X_C
\]

且 native alphabet 只含各 `A_amb(C)` 内部操作。则 connected components 精确为 `X_C`。

### Proof

每个 generator 只改变 exponent vector，不改变 type label `C`，故 path 不能跨 fiber；另一方面 G1.1 说明每个 fiber 内部连通。∎

## COROLLARY G1.3 — Minimal-carrier native separation

对正整数 `m,n`：

\[
\lambda(m)\sim_{native}\lambda(n)
\iff
\operatorname{supp}(m)=\operatorname{supp}(n).
\]

所以若 `m,n>1` 且 `gcd(m,n)=1`，则 supports 非空且 disjoint，因而 native-disconnected。

注意结论比“互素才断连”更强：即使共享质因子，只要完整 supports 不同，也断连。例如 `6=2·3` 与 `10=2·5` 的 gcd 为 2，但 canonical minimal carriers 不同。

## COUNTEREXAMPLE G1.4 — `gcd=1` 本身不产生断连

取 `m=6`, `n=35`，共同 ambient carrier

\[
C=\{2,3,5,7\}.
\]

在 `X_C` 中有 native path

\[
(1,1,0,0)
\to(0,1,0,0)
\to(0,0,0,0)
\to(0,0,1,0)
\to(0,0,1,1).
\]

整数投影即

\[
6\to 3\to 1\to 5\to 35.
\]

全程只用 `×/÷` 已授权 carrier primes，没有改变 carrier。故

\[
\boxed{\gcd(m,n)=1\not\Rightarrow \text{separation under a common ambient carrier}.}
\]

真正的 separation 来源是 **carrier commitment**，不是 gcd 这一数值关系本身。

## THEOREM G1.5 — Strict-support bare-integer components

在 `A_strict` 下，两整数连通当且仅当 prime supports 相同。

### Proof

每步禁止某 prime exponent 从 1 降到 0，也禁止引入当前 support 外的 prime，因此 support invariant。反向若 supports 相同，逐 prime 调整指数即可。∎

## MODELING_CHOICE G1.6 — Operation-sensitive classification

| Alphabet | Carrier policy | Active support change? | Connectivity consequence |
|---|---|---:|---|
| `A_global` | one global carrier containing all primes | yes | all positive integers lie in one connected multiplicative state space; coprime separation false |
| `A_amb(C)` | finite fixed ambient carrier | yes | every `X_C` connected; disjoint active supports can be native-connected |
| canonical minimal lift + `A_amb` | endpoints start in minimal carriers; native ops cannot change carrier | yes within carrier | endpoints native-connected iff exact prime supports equal |
| `A_strict` | no explicit carrier tag | no birth/death of support | components are exact-support classes |
| directed erosive alphabet | may delete support, may only multiply existing support | death yes, birth no | `m→n` iff `supp(n)⊆supp(m)`; disjoint nonempty endpoints have no directed path, but weak undirected graph can meet at `1` |

所以“乘法相邻”的第一性对象不能只写一个 distance；必须先冻结 **操作字母表 + carrier semantics + directionality**。

---

# G1b — Minimal carrier-bridge theorem

## DEFINITION G1b.1 — Elementary carrier bridges

对 `p∉C`，定义 carrier authorization bridge

\[
E_p:(C,a)\mapsto(C\cup\{p\},a\oplus0_p).
\]

它不改变整数投影：`π(E_p(C,a))=π(C,a)`。

若 `p∈C` 且当前 `a_p=0`，定义 restriction bridge

\[
R_p:(C,a)\mapsto(C\setminus\{p\},a|_{C\setminus\{p\}}).
\]

同样不改变整数投影。

这两个操作改变几何 type，却在普通整数轴上“移动距离 0”。

## THEOREM G1b.2 — Canonical endpoint bridge count

令 `C=supp(m)`, `D=supp(n)`。若允许 native fiber motion 加上单-prime `E_p/R_p`，并要求起终点都是 canonical minimal lifts，则最少 carrier-change events 数为

\[
\boxed{|C\triangle D|=|D\setminus C|+|C\setminus D|.}
\]

### Lower bound

每个 `p∈D\C` 最终必须进入 carrier，至少一次 authorization；每个 `p∈C\D` 最终必须退出 carrier，至少一次 restriction。

### Upper bound

先逐个 authorization 到 `C∪D`；在共同 fiber 内用 G1.1 的 native motion从 `m` 调到 `n`；此时 `C\D` 各坐标已为 0，再逐个 restriction 到 `D`。恰用 `|C△D|` 次 carrier bridge。∎

这个数量不是新的“整数距离”主张；它只是 bridge signature 的一个分量。指数变化量、channel coupling 与 collapse depth 仍是不同结构。

---

# G2 — Pure-operation closure boundary

本节只证明**明确语法下**的 no-go，不外推到全部 factor-blind algorithms。

## THEOREM G2.1 — Valuation-diagonal barrier for semiprime input

令 `N=pq`，`p≠q` 为隐藏素数。设 public constants `c_j` 均满足 `gcd(c_j,N)=1`。从 `N` 与这些 `c_j` 出发，只允许 multiplication、以及在有理数域中对已生成元素求 inversion。则任一生成表达式 `x` 在 hidden valuations 上满足

\[
(v_p(x),v_q(x))=(k,k)
\]

加上 public constants 的 `(0,0)` 贡献，其中 `k∈Z`。

特别地，不可能得到

\[
(t,0)\quad\text{或}\quad(0,t),\qquad t\ne0,
\]

即不能仅靠此语法隔离一个 hidden prime channel。

### Proof

`N` 的 valuation vector 是 `(1,1)`；每个 public unit constant 在 `p,q` 上 valuation 为 `(0,0)`。multiplication 对 valuation vectors 做加法，inversion 做取负，所以闭包始终位于由 `(1,1)` 生成的 rank-1 diagonal subgroup。∎

### Boundary

若允许一个 public constant 本来就与 `N` 共享非平凡因子，则 factor information 已经进入输入；若允许按 hidden factor 精确 division/projection，则 endpoint 同样已被供应。这些不属于 factor-blind pure-operation regime。

## DEFINITION G2.2 — CRT zero/nonunit pattern

先取 squarefree

\[
N=\prod_{i=1}^r p_i.
\]

定义

\[
Z_N(x):=\{i:p_i\mid x\}.
\]

在 CRT 直积 `Z/NZ ≅ ∏ F_{p_i}` 中，它正是 residue `x` 为 0 的 coordinate 集合。

## THEOREM G2.3 — Zero-pattern union law

对任意整数 `x,y`：

\[
\boxed{Z_N(xy)=Z_N(x)\cup Z_N(y).}
\]

### Proof

对每个 prime `p_i`，由 prime divisibility：`p_i | xy` 当且仅当 `p_i|x` 或 `p_i|y`。逐 coordinate 即得。∎

## COROLLARY G2.4 — Pure multiplicative selective-collapse barrier

若 primitive residues 全是 units（`Z=∅`），并可额外使用 `0 mod N`（`Z={1,...,r}`），在 multiplication 与 unit inversion 下只能得到：

- unit：`Z=∅`；或
- total zero：`Z={1,...,r}`。

不可能首次生成 proper nonempty pattern

\[
∅\subsetneq Z_N(x)\subsetneq\{1,...,r\}.
\]

因此不能生成 nontrivial zero divisor / factor witness。

对 squarefree `N`：

\[
\gcd(x,N)=\prod_{i\in Z_N(x)}p_i.
\]

所以非平凡 factor endpoint 与 proper nonempty selective-collapse pattern 是同一件事的两个表述。

## COUNTEREXAMPLE / ESCAPE G2.5 — 非纯乘法 singularization 可以跨界

取 `N=15`, public unit `a=2`。纯 powers `2^k mod 15` 始终是 units；但加入 subtraction 后

\[
2^2-1=3,
\qquad
\gcd(3,15)=3.
\]

CRT pattern 从 `∅` 变为 `{3-channel}`。真正创建 bridge witness 的不是乘法，而是 `x↦x-1` 这一 singularization step；`gcd` 只是随后把 witness 投影成 endpoint。

这不是新分解算法主张，只是最小结构例子。

---

# G3 — Bridge axioms: non-scalar complexity

下面均标为 `MODELING_CHOICE`，不是成熟标准术语。

## MODELING_CHOICE G3.1 — Carrier-change signature

对 bridge `B:(C,a)→(D,b)` 定义有向二元签名

\[
\chi_C(B)=\bigl(|D\setminus C|,\ |C\setminus D|\bigr)
=(\text{birth rank},\text{death rank}).
\]

不先压成一个数，因为 authorization 与 de-authorization 的信息不同。

- native fiber move：`(0,0)`；
- 单-prime authorization：`(1,0)`；
- 单-prime restriction：`(0,1)`。

## MODELING_CHOICE G3.2 — Carrier coupling arity `κ`

在 CRT/product-coordinate 表示下，定义 operator 的 coupling arity 为：能把输入 coordinates 分块后，使每个输出 block 只依赖一个至多 `k`-coordinate 输入 block 的最小 `k`。

- coordinatewise multiplication / exponent update：`κ=1`；
- 真正把多个 carrier channels 联合进同一个不可分解 response 的操作可有 `κ≥2`。

注意 `κ>1` 不是 factorization 的充分条件；反之 `κ=1` 的 congruence dynamics 也可能因不同 moduli 产生 selective collapse。它只是独立复杂度轴。

## MODELING_CHOICE G3.3 — First selective-collapse depth `τ`

给定 precommitted operation sequence `B_1,...,B_T`，定义

\[
\tau:=\min\{t:∅\subsetneq Z_N(x_t)\subsetneq [r]\},
\]

若永不发生则 `τ=∞`。

纯 multiplicative unit/zero closure 由 G2.4 得 `τ=∞`。

## MODELING_CHOICE G3.4 — Observability class

桥输出分为：

1. `LATENT`：只改变 carrier authorization，整数投影不变；
2. `WITNESS`：公开可观察到 selective collapse / nontrivial zero-divisor，但尚未输出 factor；
3. `ENDPOINT`：允许的 extraction map 已输出 nontrivial carrier endpoint。

这防止把“存在 bridge”“能观察 bridge”“能恢复 endpoint”混为一个结论。

---

# G4 — Minimal bridge classes

| Bridge class | 典型动作 | `χ_C` | selective collapse? | 数学地位 |
|---|---|---:|---:|---|
| carrier authorization | `C→C∪{p}`，新增零 exponent coordinate | `(1,0)` | 否 | **真实 tagged-geometry bridge**，但整数投影不变；本身不提供 hidden factor |
| carrier restriction | 零 exponent channel 从 carrier 移除 | `(0,1)` | 否 | canonical endpoint 清理；不是 factor discovery |
| known support expansion | `x→xp` 且 `p` 已公开给出 | 常伴随 `(1,0)` | 否 | 跨 support，但 factor label 已给出；不是隐藏 endpoint 恢复 |
| quotient / projection | 投影到已命名 carrier/channel | 视类型而定 | 可有 | 若投影 index 已知，属于**标签供应/记号变化**；若 projector 由 earlier witness 导出，真正 bridge 已发生在上游 |
| congruence singularization | `f(x)` 使某 CRT channels 首次变 0、另一些不变 0 | 通常 `(0,0)` | **是** | **真正 channel-selective bridge creator** |
| zero-divisor extraction | `z→gcd(z,N)` | 输出 endpoint | witness 已存在 | extractor，不是 witness generator |
| balanced coupling | 预承诺的 multi-channel mixing / survivor response | 待定 | 待证明 | 只有在 factor-blind 输入下产生 proper nonempty collapse 或等价 endpoint witness 才算真正 bridge；否则只是 classifier |

### Key separation

`carrier bridge` 与 `CRT selective-collapse bridge` 是两种不同机制：

- 前者改变“允许哪些 prime directions”，甚至可以不改变整数值；
- 后者不必改变 carrier，却改变 hidden channel singularity pattern。

因此 bridge theory 不应被一个 scalar distance 吞掉。

---

# G5 — Regression examples

## Example 1 — prime powers: native inside one carrier

`8=2^3`, `32=2^5`，supports 同为 `{2}`：

\[
8\to16\to32
\]

是 `A_strict` native path；carrier signature `(0,0)`。

## Example 2 — square-factor number with same support

`12=2^2·3`, `18=2·3^2`：

\[
12\to6\to18
\]

每步只调整已存在 prime exponent，support 始终 `{2,3}`。平方因子本身不会制造新 sector。

## Example 3 — semiprimes sharing one prime

`6=2·3`, `10=2·5`，`gcd=2`，但 minimal carriers `{2,3}` 与 `{2,5}` 不同：

- native minimal-carrier path：不存在；
- carrier-change signature from canonical endpoint to endpoint：birth 1 (`5`), death 1 (`3`)；
- 最少 carrier-change events = 2。

所以“gcd>1 即乘法相邻”同样不是正确 primitive。

## Example 4 — coprime semiprimes

`6=2·3`, `35=5·7`：

- canonical minimal lifts native-disconnected；
- 最少 carrier-change events `|{2,3}△{5,7}|=4`；
- 一旦 authorization 到 union `{2,3,5,7}`，fiber 内有 native path `6→3→1→5→35`。

这直接显示 separation 是 carrier-sensitive，而非仅 gcd-sensitive。

## Example 5 — CRT zero-divisor boundary

`N=15=3·5`：

- units 的任意纯乘积仍是 unit；
- 与 `0` 一起做纯乘法只得到 unit 或 `0`；
- `2^2-1=3` 首次生成 proper zero pattern `{3}`；
- `gcd(3,15)=3` 输出 endpoint。

---

# Exact checker

文件：

`research_checks/MULTIPLICATIVE_NATIVE_SEPARATION_GEOMETRY_CHECK_20260829.py`

标准库 exact-integer checker 已执行并通过：

`PASS: multiplicative native separation geometry exact regressions`

检查内容：

1. `A_strict` 下 same-support constructive paths；
2. shared-factor/different-support 与 coprime-semiprime 的 no-native-path regression；
3. common ambient carrier 下 `6→35` 的 exact exponent-state path；
4. carrier bridge signature examples；
5. directed erosive alphabet 的 support-inclusion reachability；
6. 多个 squarefree moduli 上全枚举验证 `Z(xy)=Z(x)∪Z(y)`；
7. 全枚举 units multiplication closure 不生成 nontrivial zero divisor；
8. semiprime valuation diagonal barrier；
9. `N=15, 2^2-1=3` selective-collapse witness。

---

# Theorem / Definition / Modeling Choice / Counterexample register

## THEOREM

- `G1.1` fixed-carrier fiber connectivity.
- `G1.2` tagged total-space components are exactly carriers.
- `G1.3` canonical minimal lifts are native-connected iff exact supports equal.
- `G1.5` strict-support bare-integer components equal exact-support classes.
- `G1b.2` minimal canonical carrier-change event count equals support symmetric difference.
- `G2.1` semiprime pure multiplication/inversion valuation-diagonal barrier under explicit public-unit assumptions.
- `G2.3` CRT zero-pattern union law.
- `G2.4` units/zero pure multiplicative closure cannot create proper nonempty selective-collapse pattern.

## DEFINITION

- carrier fiber `X_C`;
- integer projection `π`;
- active support;
- minimal-carrier lift `λ`;
- ambient native alphabet `A_amb(C)`;
- strict native alphabet `A_strict`;
- elementary authorization/restriction bridges;
- CRT zero-pattern `Z_N`.

## MODELING_CHOICE

- treating ambient carrier authorization as latent state;
- carrier-change signature `χ_C`;
- coupling arity `κ`;
- selective-collapse depth `τ`;
- observability classes `LATENT/WITNESS/ENDPOINT`.

## COUNTEREXAMPLE

- `6` and `35` are coprime yet become native-connected inside the common ambient carrier `{2,3,5,7}`. Therefore no theorem of the form `gcd=1 ⇒ native separation` is valid without carrier/alphabet hypotheses.
- `6` and `10` share gcd 2 yet canonical minimal lifts remain separated. Therefore gcd intersection alone does not characterize native connectivity.

---

# What survives as the “multiplicative number space”

The strongest surviving object is a **carrier fibration**, not a line:

\[
\bigsqcup_{C\in\mathrm{Fin}(P)} \mathbb N_0^C
\longrightarrow
\mathrm{Fin}(P),
\]

with:

- base: finite prime-carrier lattice / support lattice;
- fiber over `C`: exponent orthant/lattice `N_0^C`;
- native morphisms: coordinate multiplication/division inside a fiber;
- latent bridges: carrier authorization/restriction;
- observable algebraic bridges: operations that create selective CRT singularity patterns;
- endpoint extraction: maps such as gcd that convert a witness into a factor endpoint.

普通整数映射 `π` 把大量不同 tagged states 压到同一个整数，因此一条普通数轴天然看不见 carrier authorization geometry。

这比“定义一个新的乘法距离”更接近本任务要求：**先有 fiber 与 bridge，distance 至多是后置派生量。**

---

# BRC successor gate

**值得继续研究 BRC bridge，但必须换成下面的硬问题：**

> 在 public-input / hidden-factor verifier 模式下，某个 precommitted BRC/CBRC operator family 是否能从 factor-blind inputs 产生一个 `proper nonempty` CRT selective-collapse pattern（或等价的 nontrivial zero-divisor / projector witness），且该 witness 不是由 factor-labelled constant、hidden projection、或 prior gcd supplied information 偷带进来的？

分三层判定：

1. `bridge existence`：是否发生 selective collapse；
2. `bridge observability`：public response 是否能识别它；
3. `endpoint recovery`：允许 extraction 后是否得到 nontrivial factor。

若 BRC 只能给 coefficient-support survivor classifier，而不能越过 G2.4 的 selective-collapse barrier，则它不是 endpoint bridge。

若能越过，则下一任务才值得研究其成功率、总成本与 prior-art equivalence。

---

# Novelty / prior-art boundary

本 return **不宣称**以下标准对象为新：

- prime factorization / valuation vector；
- free commutative monoid interpretation of positive integers;
- support lattice / divisibility language；
- CRT product decomposition；
- zero divisors 与 gcd factor extraction 的标准关系。

本任务的研究贡献限定为：把这些标准对象组织成一个可审计的 **carrier-sensitive native/bridge semantics**，证明 `gcd` 断连命题的 operation-sensitive boundary，并冻结 pure-multiplicative selective-collapse no-go 作为后续 BRC bridge 的门槛。

## Final disposition

`SUCCESS`。

- G0：完成；
- G1：完成，含 theorem + counterexample + operation-sensitive classification；
- G2：完成，明确窄语法 no-go 边界；
- G3：完成，给出至少三种非标量/非单一 metric bridge descriptors；
- G4：完成 minimal bridge classes；
- G5：完成 exact regressions + checker。

Next research recommendation:

`PROCEED_TO_BRC_BRIDGE_CLASSIFICATION_OR_FACTOR_BLIND_ENDPOINT_RECOVERY`, but enforce `SELECTIVE_COLLAPSE_WITNESS_REQUIRED` before any factorization claim.
