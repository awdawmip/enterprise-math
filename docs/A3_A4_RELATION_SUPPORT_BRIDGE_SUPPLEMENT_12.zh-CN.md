# A3 ↔ A4 ↔ P021 ↔ A2/P023 Bridge — Supplement 12

状态：`ACTIVE RESEARCH NOTE`  
范围：整个有限 count-composition algebra 中 witness label 擦除的精确判据

## 1. 从 one-step defect 到递归稳定的 identity erasure

Supplement 11 给出了一个 declared scalar/matrix composition count 的精确 coupling defect。即使 hidden witness profiles 非 uniform，也可能偶然出现 zero defect。

这足以保证**当前** count observable 精确，但不能保证任意后续 count composition 仍 future-complete。

要支持整个 operation language，需要更强且递归稳定的条件。

对应的成熟数学结构是 non-negative-integer transition matrices 的 equitable partition / exact lumping。

## 2. 设置

令 `X` 为有限 exact witness set，

\[
\mathcal P=\{C_1,\ldots,C_q\}
\]

为准备被 collapse 的 witness identities 的 partition。

令

\[
M:X\times X\to\mathbb N
\]

为 non-negative-integer transition/count matrix。

对 `x in C_a`，定义流向 target cell `C_b` 的 block-output count：

\[
S_M(x,b)=\sum_{y\in C_b}M_{xy}.
\]

## 3. B47 — one-step count descent 当且仅当 equitability

以下两件事等价。

### (A) Block-count observable 通过 witness partition 下沉

任意 `x,x'` 属于同一个 source cell `C_a` 时，对所有 target cell `C_b` 都有

\[
S_M(x,b)=S_M(x',b).
\]

### (B) `P` 对 `M` equitable

同一个 source cell 中所有 rows，对每个 target cell 的 block sums 都相同。

条件成立时定义 exact quotient count matrix：

\[
\boxed{
Q_M(a,b)=S_M(x,b)
\quad(x\in C_a),
}
\]

它与 representative 无关。

这正是 P023 fiber-constancy/descent 在 integer block-count observation 上的具体化。

## 4. B48 — equitable matrices 对 composition 闭合

若 `M` 与 `N` 对同一个 partition `P` 都 equitable，则 `MN` 也 equitable，并且在 non-negative integers 上

\[
\boxed{
Q_{MN}=Q_MQ_N.
}
\]

### 证明

取 `x in C_a`，对 target cell `C_c`：

\[
\sum_{z\in C_c}(MN)_{xz}
=
\sum_y M_{xy}\sum_{z\in C_c}N_{yz}.
\]

按 middle witness cells `C_b` 分组。由于 `N` equitable，对所有 `y in C_b`，inner target-block sum 都是常数 `Q_N(b,c)`，故

\[
=
\sum_b Q_N(b,c)
\sum_{y\in C_b}M_{xy}
=
\sum_b Q_M(a,b)Q_N(b,c).
\]

结果与 `x in C_a` 的具体选择无关，所以同时证明 `MN` equitable 与 quotient-product identity。

## 5. B49 — finite operation-family theorem

令

\[
\mathcal M=\{M_\alpha\}_{\alpha\in A}
\]

为同一个 exact witness set 上的有限 non-negative-integer transition/count matrix family。

若每个 generator 都对 `P` equitable，则对任意 operation word

\[
w=\alpha_1\cdots\alpha_k,
\]

其 exact fine transition

\[
M_w=M_{\alpha_1}\cdots M_{\alpha_k}
\]

都 equitable，并且

\[
\boxed{
Q_{M_w}
=
Q_{M_{\alpha_1}}\cdots Q_{M_{\alpha_k}}.
}
\]

所以，对 declared future language

> “从 source coarse cell 出发，经过任意有限 operation word，精确计算进入每个 target coarse cell 的 total weighted path count”

来说，每个 partition cell 内的 fine witness labels 可以永久删除。

这是 whole-algebra future-safety theorem，而不是 one-step repair。

## 6. B50 — 对 declared generator language 的必要性

若 future language 包含每个 generator `M_alpha` 的 one-step block-count observable，则每个 generator equitable 也是必要条件。

因为一旦某个 generator 使同一个 coarse cell 内两个 exact states `x,x'` 得到不同 target-cell count vector，一步 observable 已经能区分它们，所以 proposed witness partition 就不 future-safe。

因此对该 declared language，精确判据为

\[
\boxed{
\text{all generator matrices equitable}.
}
\]

## 7. B51 — block-total representation

令 `n_a=|C_a|`。source block `C_a` 到 target block `C_b` 的 fine total mass 为

\[
T_M(a,b)
=
\sum_{x\in C_a,y\in C_b}M_{xy}
=
 n_a Q_M(a,b).
\]

所以若 cell sizes 被保留，equitable state 下 block totals 与 quotient row-count matrix information-equivalent：

\[
\boxed{
Q_M(a,b)=T_M(a,b)/n_a.
}
\]

该除法由 equitability 保证整除。

对 operation word：

\[
T_{M_w}(a,b)
=
n_a(Q_{M_{\alpha_1}}\cdots Q_{M_{\alpha_k}})_{ab}.
\]

因此 exact block-total path counts 也能在 `(cell sizes, quotient matrices)` 上闭合。

## 8. B52 — local zero coupling defect 严格弱于 global count-lumpability

Supplement 11 已证明，即使两个 profiles 都 non-uniform，也可能有 `Delta=0`，例如

\[
l=(0,0,1),
\qquad
r=(0,2,1).
\]

这使某一个 selected cardinality composition 精确，但 hidden incidences 仍然可能被其他 target-block count observable 区分。

因此

\[
\boxed{
\Delta=0\text{ for one requested join}
\not\Rightarrow
\text{equitable future count algebra}.
}
\]

当前 hierarchy 可以精确写成：

- 一个 selected current count：zero defect，或保留 `Delta`；
- 一个 matrix 的全部 one-step block counts：equitable partition；
- finite matrix family 的 arbitrary words：每个 generator equitable；
- witness identity 本身：一般仍需 labels，或进一步证明更丰富 quotient。

## 9. P023 extraction

本 supplement 是 specialization，不是竞争性母理论。

P023 已经说明 finite operation family 精确下沉，当且仅当 chosen partition/congruence 对每个 generator 都 compatible。这里把 abstract condition 化成一个明确 integer criterion：

\[
\boxed{
\text{同一个 source block 内，对每个 target witness block 的 row sum 必须恒定。}
}
\]

所以对 non-equitable witness partition 的修复，应直接使用 P023 partition-refinement closure，按照 operation family 强迫出来的 future block-count signatures 去 split exact states。

Bridge 不应再造一套 generic refinement algorithm。

## 10. 与 P021 的关系

P021 witness-transport 的核心教训是 cardinality shadow 会丢失 composition 所需的 middle-incidence identity。Supplement 11 量化了 one-step coupling defect。B47–B52 进一步给出了对 whole count language 能递归稳定删除 witness identity 的更强条件。

P021 继续保留 direction transport 的发现/应用归属；Bridge 只承担 P023 的 general count-algebra specialization。

## 11. 与 A4/E001 的关系

A4/E001 可根据 requested semantics 选择三种不同 state：

1. 只问 existence：boolean relation support；
2. witness partition equitable 且需要 block/path counts：non-negative-integer quotient matrices；
3. equitability 失败或 diagnostic 对 identity 敏感：保留 exact witness incidence。

这样工程 state 选择就由数学条件决定，而不是经验 heuristic。

## 12. Prior-art discipline

Equitable partition、quotient matrix、lumpability 与 invariant block-constant subspace 都是成熟 graph/algebra/Markov-chain 概念。本项目不主张 abstract mathematics 本身的新颖性。

当前 project-specific value 是把该精确判据放进现有 Enterprise Math state ladder，连接 P021 witness loss、A4/E001 count semantics 与 P023 legal quotienting。

## 13. Executable reference

Bridge reference layer 新增：

- integer matrix + witness partition 的 equitability audit；
- exact quotient count matrix；
- matrix-family / operation-word quotient verification；
- block-total reconstruction；
- local zero coupling defect 不推出 global equitability 的 counterexample。
