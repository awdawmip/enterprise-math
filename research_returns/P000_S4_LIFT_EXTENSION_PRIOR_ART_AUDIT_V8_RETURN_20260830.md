# P000 `S4` lift / group-extension / canonical-section 外部先例审计 V8 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P0006DPA8-71C4E2`  
Task-ID: `RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-2F8C6A1D9E7043B5C812`  
Claim-ID: `chatgpt-p0006dpa8-20260830-2134-71c4e2`  
Execution branch: `research/p000-s4-lift-extension-prior-art-v8-em-p0006dpa8-71c4e2`  
Execution base: `cdfb6abd2c9ab15e6295a0c07125443c1d619f59`

Hard target:

`P000_S4_LIFT_EXTENSION_SPLITTING_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

Terminal class:

`CLASSICAL_S4_EXTENSION_SPLITTING_CORE_CLASSIFIED_P000_COMPOUND_LIFT_SEMANTICS_BOUNDARY_FROZEN`

## 1. Executive result

本轮外部先例审计已经把 Gen12/Gen13 一带的 `S4` lift 语言切成了两层，而且边界是可检查的。

第一层是**经典且必须冻结为先例**的抽象数学核心：

- short exact sequence / group extension；
- split extension、homomorphic section、semidirect product、complement；
- quotient presentation 的 relator 在任意 lifts 下落入 kernel；
- abelian-kernel extension 的 `H^2` 分类；
- nonabelian-kernel 的 Schreier / Eilenberg–Mac Lane extension theory；
- section/lift 改变与 factor-set/coboundary；
- `S4` 在四点上的自然忠实作用及其在六个 2-subsets/edges 上的诱导作用；
- 一个 24 元忠实置换像至少需要 4 个点；
- definability/canonical choice 的 automorphism-invariance obstruction；
- “某一个模型存在”与“所有模型都存在”的逻辑强度差异。

这些都不能再被表述成 P000 新数学。对应 12 个 mandatory claims 的分类为：

`EXACT_DUPLICATE = 9`

`PARTIAL_ANTECEDENT = 1`

`ADJACENT_METHOD = 1`

`NO_MATERIAL_MATCH = 1`

第二层是**本轮仍未找到外部 material exact match 的 P000 compound semantics**：

`opaque native Cell identity`
`+ no carrier quotient`
`+ native-axis typing`
`+ carrier/readout non-identification`
`+ downstream frame/PF10 decorations`
`+ project-local no-quotient operational guard`.

这里的结论只能写成：

`P000_COMPOUND_SEMANTICS = NO_MATERIAL_MATCH_ONLY`

并且必须同时冻结：

`NO_MATERIAL_MATCH != NOVELTY`

本轮不是 novelty、priority、originality、patentability 或 Foundation 审查。

另外，本轮给出三个会直接约束后续 Gen13+ 文本的 exact finite guards：

1. `RELATION_RESIDUE != NONSPLITTING_CERTIFICATE`；
2. `SPLIT != CANONICAL_SECTION`；
3. `UNIVERSAL_EXISTENCE != ONE_MODEL_EXISTENCE`。

这三个 guard 都不是纯文字提醒，而是由 deterministic checker 中的两个 48 元有限扩张精确验证：

- split comparator: `C2 × S4 -> S4`；
- nonsplit comparator: `GL(2,3) -> PGL(2,3) ~= S4`。

## 2. Frozen internal dependencies

本研究只消费已冻结/已接受的上游结论，不重做 Gen12 或 V7。

### 2.1 Gen12 Driver-accepted strength

Gen12 的 Driver review 已明确接受：

`FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED`

但接受强度严格为 **existential common-model**。

同一个 declared framed/PF-10 Full-Cell 模型中存在四个 distinct opaque Cells，两个 exact lifts `R_a,R_b`，并且：

- `<R_a,R_b>` order `24`；
- bare-Cell image order `24`；
- six-axis image order `24`；
- 两个 forgetful kernels 都是 trivial；
- `R_a^3=R_b^2=(R_aR_b)^4=id`；
- 四个 K4-star derived objects 被同一组作用输运。

Driver 同时明确没有接受：

- bare P000 自动提供这四个 Cells；
- bare P000 canonically selects `R_a,R_b`；
- every admitted model admits a lift；
- complete native P000 rotation group is `S4`。

因此本轮冻结：

`GEN12_REPRESENTATION_CORE = CLASSICAL`

以及：

`GEN12_TYPED_FULL_CELL_REALIZATION = PROJECT_SPECIFIC_EXISTENTIAL_ASSEMBLY`

而不能把自然 `S4` representation 本身当作 project novelty。

### 2.2 V7 carry-forward

V7 已把 frame/torsor/connection/gauge/holonomy 的抽象数学大部分类成 classical antecedents，并把真正残留的 P000 边界限定为 compound native-identity/no-quotient semantics。

本轮继续冻结它的术语警戒：

`STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY`

若后续需要 globally parallel frame，应写：

`TRIVIAL_HOLONOMY / SYNCHRONIZABLE / PURE_GAUGE`

而不是把 standard flatness 自动等同为 trivial monodromy。

## 3. Mandatory 12-claim audit map

| # | Claim | Classification | Frozen boundary |
|---:|---|---|---|
| 1 | `1 -> K -> G~ -> S4 -> 1` group-extension language | `EXACT_DUPLICATE` | 标准 group extension exact-sequence 语言；不因此授权 P000 quotient。 |
| 2 | split / semidirect / complement / homomorphic section | `EXACT_DUPLICATE` | split iff admits homomorphic section；split 不推出 canonical section。 |
| 3 | lifted presentation relations land in `K` | `EXACT_DUPLICATE` | quotient relator 的任意 lift-word 必落 kernel；具体 residue 依赖 lift。 |
| 4 | abelian/central extensions and `H^2` | `EXACT_DUPLICATE` | 只在 abelian kernel + fixed module action 下直接使用 ordinary `H^2` classification。 |
| 5 | nonabelian extension / Schreier theory | `EXACT_DUPLICATE` | fixed outer action + `H^3(G,Z(K))` realizability obstruction + `H^2(G,Z(K))` torsor。 |
| 6 | section/lift change; complement conjugacy/nonuniqueness | `PARTIAL_ANTECEDENT` | coboundary machinery标准；complement conjugacy/uniqueness 需要额外假设，不能一般化为 canonicality。 |
| 7 | faithful degree-4 `S4` and six-edge action | `EXACT_DUPLICATE` | natural four-point action 与 2-subset action 都是 classical。 |
| 8 | 24-element faithful image needs >=4 points | `EXACT_DUPLICATE` | faithful action embeds into `S_n`; `|S_3|=6<24`; degree 4 attained。 |
| 9 | projective / covering-group analogy | `ADJACENT_METHOD` | Schur covers/double covers classical，但只在 central/projective hypotheses 匹配时可迁移。 |
| 10 | automorphism/definability obstruction to canonical section | `EXACT_DUPLICATE` | definable over fixed parameters => fixed by parameter-fixing automorphisms。 |
| 11 | universal existence vs one-model existence | `EXACT_DUPLICATE` | existential witness 与 universal model-class theorem 是不同逻辑强度。 |
| 12 | exact P000 compound semantics | `NO_MATERIAL_MATCH` | audited sources 未发现 exact compound match；不等于 novelty。 |

Machine-readable claim map:

`research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8/claim_map.json`

## 4. Claims 1–3 — extension, splitting and relation residues are standard

设有 short exact sequence

`1 -> K -> E ->^q S4 -> 1`.

这是标准 group extension 数据。Kernel `K`、quotient `S4`、extension equivalence 等语言均属于经典群论/群上同调框架。

若存在 group homomorphism

`s:S4 -> E`

满足

`q o s = id_S4`，

则 extension split；在 abelian-module setting 下，标准结论把它等价地写成 semidirect product。反之 semidirect product 给出显式 splitting section。

因此：

`SPLIT_EXTENSION = HOMOMORPHIC_SECTION_EXISTS`

是 classical exact antecedent。

### 4.1 Why lifted relators land in the kernel

取 `S4` 中 generator words `a,b`，任取 lifts `A~,B~ in E` 满足

`q(A~)=a`, `q(B~)=b`.

只要 quotient 中某个 word `r(a,b)=1`，则

`q(r(A~,B~)) = r(q(A~),q(B~)) = 1`.

因此

`r(A~,B~) in ker(q)=K`.

这不需要 P000 特殊公理；它只是 quotient + presentation 的基本事实。

在 Gen12 convention 下，目标 generators 满足：

`a^3=b^2=(ab)^4=1`.

于是任何 lifts 都必有：

`A~^3 in K`,
`B~^2 in K`,
`(A~B~)^4 in K`.

但**落入 kernel 不是 nonsplitting 的充分证据**。下一节的 exact split comparator 会直接证明这一点。

## 5. Exact finite comparator A — split extension can still show nontrivial chosen-lift residue

取最简单的 central split extension：

`E_split = C2 × S4`

with quotient

`q(c,g)=g`.

显然有 untwisted homomorphic section：

`s0(g)=(0,g)`.

同时因为 `S4` 有 sign homomorphism

`sgn:S4 -> C2`，

还有第二个 homomorphic section：

`s_sign(g)=(sgn(g),g)`.

所以一个 split extension 已经至少可以有两个不同 sections。

### 5.1 Nontrivial residue without nonsplitting

令 `z` 是 `C2` 的非平凡元素。选取并非 homomorphic 的 generator lifts：

`A~=(z,a)`,
`B~=(1,b)`.

Exact checker 计算：

`A~^3 = (z,1)`,

`B~^2 = (1,1)`,

`(A~B~)^4 = (1,1)`.

于是 chosen-lift relation residue 非平凡：

`A~^3=z != 1`.

但整个 extension 明明 split，因为 `s0` 已经是 homomorphic section。

因此必须冻结：

`RELATION_RESIDUE != NONSPLITTING_CERTIFICATE`

后续若看到某组 arbitrary lifts 的 presentation residue 非零，只能说明**这组 lifts 不是一个 homomorphic section**；不能单靠这一点断言 extension class nonsplit。

### 5.2 Split still does not produce a canonical section

定义 extension automorphism：

`F(c,g)=(c+sgn(g),g)`.

Checker 穷举 `48^2` 个乘法 pairs，验证 `F` 是 group automorphism；它：

- fixes quotient `S4` pointwise；
- fixes kernel `C2` pointwise；
- sends `s0` to `s_sign`.

所以仅从 bare extension data 不能 automorphism-invariant 地选出 `s0` 而排除 `s_sign`。

并且 `{0}×S4` 是 direct factor，因而 normal；`graph(sgn)` 是另一个 distinct complement，二者并不通过 conjugating `{0}×S4` 得到同一 complement。

因此：

`SPLIT != CANONICAL_SECTION`

也是 exact finite fact，而不是哲学性提醒。

这也解释了为什么 claim 6 整体只能记作 `PARTIAL_ANTECEDENT`：section-change/factor-set/coboundary 是标准 exact theory，但“所有 complements 自动 conjugate / unique / canonical”并没有无条件的一般定理。Schur–Zassenhaus 类 conjugacy 结论需要 Hall/coprime 等额外假设，不能静默搬到当前 `|K|` 与 `|S4|` 共享素因子的情形。

## 6. Claim 4 — the exact `H^2` applicability guard

这是本轮最重要的术语/适用性冻结之一。

标准 theorem 不是：

`all extensions by arbitrary K are H^2(S4,K)`.

正确形式是：

给定一个 **abelian group** `A`，以及已经固定的 `G`-module action

`G -> Aut(A)`，

与该作用兼容的 extension equivalence classes 由

`H^2(G,A)`

分类。

对于 central extension，conjugation action 是 trivial，所以 central extension 是这个 abelian-module theorem 的 trivial-action special case。

对本项目必须写成：

`PLAIN_H2_CLASSIFIER_APPLIES`
`=> K ABELIAN`
`+ S4-MODULE ACTION FIXED`.

因此：

`H^2(S4,K)`

只有在这些假设被明确满足时才是合法的 ordinary cohomology classifier。

若 downstream model 里的 hidden kernel 只是一个 arbitrary nonabelian automorphism kernel，就不能把它直接塞进 ordinary `H^2(S4,K)`。

Sources `SRC-WILKES-2020`, `SRC-WEIBEL-CH6`, `SRC-CONRAD-H2` 在 source ledger 中分别固定了 split/factor-set/module-action/H^2 边界。

## 7. Claim 5 — nonabelian kernels require the Schreier/Eilenberg–Mac Lane lane

若 `K` 非阿贝尔，extension 中 conjugation by a lift of `g in S4` 只在 modulo inner automorphisms 后与 lift choice 无关。

因此 quotient natural data 是 outer action：

`alpha:S4 -> Out(K)=Aut(K)/Inn(K)`,

而不是一个自动给定的 honest action：

`S4 -> Aut(K)`.

经典 Eilenberg–Mac Lane / Schreier extension theory 给出的正确结构是：

1. 先固定 outer action `alpha`；
2. 存在一个 obstruction class in

   `H^3(S4,Z(K))`;

3. obstruction 非零时，与该 outer action 相容的 extension 根本不存在；
4. obstruction 消失且 extension class set 非空后，`H^2(S4,Z(K))` 对这些 classes 作 simply transitive/torsor 型作用；
5. 这里没有普通 abelian-extension 情形那种天然 distinguished zero extension。

因此冻结：

`NONABELIAN_KERNEL`
`=> OUTER_ACTION FIRST`
`=> H^3(S4,Z(K)) REALIZABILITY GATE`
`=> H^2(S4,Z(K)) TORSOR AFTER EXISTENCE`.

尤其：

`ORDINARY_H2(S4,K) FOR ARBITRARY NONABELIAN K = INVALID_GENERALIZATION`.

这一整个 abstract framework 是 classical exact antecedent；P000 后续若真的产生 nonabelian hidden kernel，研究新意（若有）只能来自**如何从 native typed model 导出该 kernel/outer action/residue**，不能来自“非阿贝尔扩张需要 outer action 与 obstruction”本身。

## 8. Exact finite comparator B — `GL(2,3) -> PGL(2,3) ~= S4` is nonsplit

Checker 独立构造：

`GL(2,F3)`,

穷举所有 `3^4=81` 个 `2x2` matrices，保留 determinant nonzero 的 `48` 个元素。

其 scalar center kernel 为：

`{I,-I} ~= C2`.

然后让 `GL(2,3)` 作用在 projective line：

`P^1(F3) = {[1:0],[0:1],[1:1],[1:2]}`.

Exact enumeration 得到：

- projective permutation image order `24`;
- projective kernel exactly `{I,-I}`;
- hence quotient is the full permutation group on four projective points:

  `PGL(2,3) ~= S4`.

### 8.1 Direct no-section test

选择与 Gen12 相同 cycle types 的 quotient generators：

`a=(BCD)`,
`b=(AB)`.

在 `GL(2,3)` 中：

- `a` exactly has 2 lifts；
- `b` exactly has 2 lifts；
- 共 `4` 个 possible `(A~,B~)` lift pairs。

Checker 穷举四对，发现共同的 decisive residue：

`(A~B~)^4 = -I != I`

for **all four** pairs.

若 homomorphic section `s:S4->GL(2,3)` 存在，则必须把 actual quotient elements `a,b` 送到这四对中的某一对，而且必须 preserve quotient relation：

`(ab)^4=1`.

四对全失败，所以无 homomorphic section。

因此 exact：

`GL(2,3) -> PGL(2,3) ~= S4`

是 `C2`-kernel nonsplit comparator。

这与前面的 split `C2×S4` comparator 并列，给出一个非常干净的 model-class guard：

`SAME_QUOTIENT_S4 + SAME_KERNEL_ORDER_2`
`DOES_NOT_FORCE SPLITTING`.

也就是：

`UNIVERSAL_EXISTENCE != ONE_MODEL_EXISTENCE`.

Gen12 一个成功 common model 不能逻辑上排除另一个 admitted model 出现 nonsplit extension 或 no-lift。

## 9. Claims 7–8 — Gen12's abstract `S4` representation is entirely classical

`S4` 本来就是 four-letter symmetric group。其 natural action on four objects 是 definition-level classical object。

在 Gen12 的 labels 下：

`a=(BCD)`,
`b=(AB)`,

checker verifies：

`a^3=b^2=(ab)^4=id`

and:

`|<a,b>|=24`.

对四个 objects 的六个 unordered pairs：

`AB, AC, AD, BC, BD, CD`

自然诱导一个 6-point action。Checker 枚举全部 24 个 group elements 后得到：

`induced_two_subset_image_order=24`.

所以 six-edge action 也是 faithful。

这正是 Gen12 的 carrier-vertex / K4-edge representation core。它是 classical `S4` combinatorics，不是 P000 新 representation theorem。

### 9.1 Minimum faithful permutation degree

任意 faithful action of a 24-element group on `n` points gives an injection into `S_n`.

For `n<4`：

`|S1|=1`,
`|S2|=2`,
`|S3|=6`.

全部小于 `24`，不可能容纳 faithful 24-element subgroup。

而 degree `4` 的 natural `S4` action 已经实现 faithful action。

Hence exact：

`mu_perm(S4)=4`.

这解释了 Gen12 “四个 Cells 对 24 元 bare-Cell image 是 cardinality-minimal”为什么是 classical finite representation fact。

它绝不能被转述成：

`P000 reality has exactly four Cells`.

## 10. Claim 9 — Schur covers/projective representations are adjacent, not automatic identity

Schur 的 projective representation theory、Schur multiplier 与 covering groups 对 `S4` 已经是经典文献对象。

Audited authoritative references record that：

`M(S4) ~= C2`

and classical double/Schur covers of `S4` exist；文献中包括 binary-octahedral 与 `GL(2,3)` 等 representation-group realizations。

因此如果 future P000 model 真正满足：

- central `C2` kernel；
- projective representation cocycle hypotheses；
- appropriate equivalence notion；
- quotient action exactly corresponding to the projective setup，

那么 Schur-cover language 是一个 legitimate comparison tool。

但这仍然只能分类为：

`ADJACENT_METHOD`.

原因是 current P000 hidden residue 在 abstract extension language 出现，并不自动证明：

`P000_EXTENSION = SCHUR_COVER`,
`P000_EXTENSION = BINARY_OCTAHEDRAL`,
或
`P000_EXTENSION = GL(2,3)`.

必须先从 native model 导出那些 exact hypotheses。

因此 projective/covering analogies 是**防止重复发明**的 prior art，也是**防止过度类比**的 applicability guard。

## 11. Claim 10 — canonical section obstruction is standard automorphism logic

Model theory 的必要方向非常简单而强：

若 element/object `x` 可由 parameters `A` 定义，则任何 fixing `A` 的 automorphism 都必须 fix `x`.

写成：

`A-definable => Aut(M/A)-fixed`.

因此，若 primitive-preserving automorphism group 在 candidate sections 上没有 fixed point，那么不能从这些 primitives/parameters definably choose a unique section。

这不是 P000 独有原则。

本轮 split comparator `C2×S4` 给了更强的 finite group-level witness：

`F(c,g)=(c+sgn(g),g)`

是一个：

- kernel-fixing；
- quotient-fixing；
- extension automorphism，

但它交换两个 homomorphic sections `s0` 与 `s_sign`.

所以如果 signature 只记 bare extension data，没有额外 symmetry-breaking primitive，那么任何宣称“这个 section 是 canonical”的规则都必须解释为什么 `F` 不再是允许的 primitive-preserving automorphism。

冻结：

`CANONICAL_SECTION`
`=> AUT_PRIM_FIXED_POINT REQUIREMENT`.

并且保持 V7 已有 guard：本研究只使用 necessary direction

`definable => automorphism-fixed`

不在未声明 saturation/homogeneity 等额外条件时滥用 converse。

## 12. Claim 11 — existential and universal lift statements are not interchangeable

Gen12 Driver review 已经给出最明确的 internal boundary：

`there exists one declared common model with faithful S4 lift`

被接受；

但：

`every allowed model admits a faithful S4 lift`

仍然 open。

这不是措辞区别，而是不同逻辑强度。

本轮两个 exact comparator 进一步说明为什么必须严格区分：

- `C2 × S4`：split；
- `GL(2,3)`：nonsplit；

两者 quotient 都是 `S4`，kernel order 都是 `2`。

所以即使某个 model class 中已经有一个 positive witness，也不可能只靠那个 witness 得到 universal splitting theorem。

冻结：

`ONE_MODEL_POSITIVE_WITNESS`
`!=`
`UNIVERSAL_MODEL_CLASS_SUFFICIENCY`.

后续任何 universal result 必须：

- 声明 model class；
- 对每个 admitted model 证明 section exists；
- 或给出 exact countermodels / classification partition。

## 13. Claim 12 — what remains P000-specific after duplication audit?

把所有 classical layers 剥离后，本轮没有发现 material exact external duplicate 的是**组合后的 project operational semantics**，而不是其中任何单个数学构件：

1. native `Cell` identity 是 opaque project-level identity；
2. Cell identity 不能被 FCC/carrier coordinate equality 定义；
3. carrier/readout 可以组织计算但不得 quotient native identity；
4. native-axis sort 与 local presentation-channel sort 必须 typed separation；
5. frame/PF10 data 是 downstream decoration，而不是 root identity；
6. local channel permutation gauge 不自动成为 native spatial rotation；
7. hidden residue 不得通过 kernel quotient 被静默删掉以制造 `S4`；
8. time remains fixed；
9. canonical/Working Truth/Foundation promotion 不是 Researcher 输出权限。

Audited sources 分别有：

- group extensions；
- cohomology；
- permutation groups；
- projective representations；
- definability/automorphisms；
- V7 已查过的 torsor/connection/gauge；

但本轮 source set 中没有一个 authoritative source material-exactly reproduces 上述整包 operational semantics。

所以只冻结：

`P000_COMPOUND_SEMANTICS = NO_MATERIAL_MATCH_ONLY`.

并再次明确：

`NO_MATERIAL_MATCH != NOVELTY`.

“没在本轮 authoritative audit 里找到 exact material match”不能推出：

- 世界上不存在；
- 学术首次；
- inventive step；
- patentability；
- canonical truth；
- Foundation promotion。

## 14. `H^2` / nonabelian applicability matrix

| Kernel situation | Correct classical lane | What may be concluded | What is forbidden |
|---|---|---|---|
| `A` abelian, fixed `S4`-module action | ordinary `H^2(S4,A)` | extension equivalence classes for that fixed action | silently changing module action |
| `A` abelian, trivial action / central extension | `H^2(S4,A)` with trivial action | central extension classes | treating every abelian extension as central |
| `K` nonabelian, fixed outer action | Schreier / Eilenberg–Mac Lane | `H^3(S4,Z(K))` realizability obstruction; after existence, `H^2(S4,Z(K))` torsor | writing ordinary `H^2(S4,K)` as general classifier |
| arbitrary P000 hidden residue not yet typed as a group extension kernel | none yet | only derive the group/outer-action structure first | jumping directly to cohomology label |

这是本轮最建议 Driver 直接复用的 future-text gate。

## 15. Source ledger

Authoritative/expository sources are frozen machine-readably at:

`research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8/source_ledger.json`

主要 source families：

- Cambridge / Weibel / Conrad: split extensions, factor sets, abelian `H^2` classification；
- Eilenberg–Mac Lane 1947 + Brown GTM 87: nonabelian kernel extension theory；
- Encyclopedia of Mathematics: group presentation, symmetric/permutation groups, projective representations；
- modern Springer double-cover paper: classical `S_n` double-cover context；
- Berkeley model-theory notes: definability and automorphism invariance；
- internal Gen12 Driver review + V7 prior-art return: exact project boundary。

Source quality policy：

- primary/standard graduate-text references control theorem scope；
- secondary sources only explain or cross-check；
- internal project files control **what P000 currently claims**, not external priority。

## 16. Deterministic evidence

Checker:

`research_checks/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8_CHECK_20260830.py`

Claim map:

`research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8/claim_map.json`

Source ledger:

`research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8/source_ledger.json`

Finite certificate:

`research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8/finite_s4_certificate.json`

The checker independently verifies:

1. exactly 12 mandatory claims；
2. classification count `9/1/1/1`；
3. every claim has source IDs + scope guard；
4. H2/nonabelian/novelty/flatness hard guards；
5. Gen12 `a,b` generate exact order `24`；
6. six 2-subset action has image order `24`；
7. minimum faithful permutation degree is `4`；
8. split `C2×S4` has at least two homomorphic sections；
9. an extension automorphism over the identity quotient swaps those sections；
10. a chosen lift in the split extension can have nontrivial relator residue；
11. `|GL(2,3)|=48`；
12. its projective action on `P^1(F3)` has image order `24` and kernel `{I,-I}`；
13. all four lift pairs of the chosen quotient generators fail `(A~B~)^4=I`；
14. therefore the `GL(2,3)` central extension is nonsplit；
15. all required static boundary phrases remain present in the frozen return。

Expected checker terminal line:

`PASS P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8_CHECK`

## 17. Exact terminal theorem

### Theorem — external duplication boundary

Relative to the declared V8 audit map and frozen Gen12/V7 dependencies:

1. Claims 1,2,3,4,5,7,8,10,11 are `EXACT_DUPLICATE` at the abstract mathematical level.
2. Claim 6 is `PARTIAL_ANTECEDENT`: section/factor-set change is standard, but general complement conjugacy/uniqueness/canonicality requires additional hypotheses and is false without them.
3. Claim 9 is `ADJACENT_METHOD`: projective/Schur-cover theory is classical and relevant only once its hypotheses are actually derived.
4. Claim 12 is `NO_MATERIAL_MATCH` within the audited authoritative source set, solely for the exact compound P000 native-identity/no-quotient typed semantic package.
5. `H^2(S4,K)` is not a general classifier for arbitrary nonabelian `K`.
6. `GL(2,3)->PGL(2,3)~=S4` supplies an exact nonsplit `C2`-kernel comparator.
7. `C2×S4->S4` supplies an exact split comparator with noncanonical sections and a chosen-lift nonzero relation residue.
8. Therefore relation residue, splitting, and canonicality are three distinct predicates.
9. Gen12's natural four-point/six-edge `S4` representation is classical; only its declared P000 typed realization can remain project-specific.
10. A one-model positive witness does not imply a universal model-class theorem.
11. `STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY` remains frozen.
12. `NO_MATERIAL_MATCH != NOVELTY` remains mandatory.

Hence the valid terminal class is:

`CLASSICAL_S4_EXTENSION_SPLITTING_CORE_CLASSIFIED_P000_COMPOUND_LIFT_SEMANTICS_BOUNDARY_FROZEN`.

## 18. Non-theorems / frozen boundary

This return does **not** prove:

- bare P000 has a canonical `S4` section；
- bare P000 universally splits every enriched automorphism extension；
- current hidden kernel is central, abelian or `C2`；
- current hidden kernel is `GL(2,3)`, binary octahedral or another Schur cover；
- a nonzero relation residue forces nonsplitting；
- a split extension has a unique/canonical complement；
- the four-point natural `S4` action is project novelty；
- no external work anywhere duplicates the P000 compound package；
- novelty, priority, patentability, Working Truth or Foundation status。

## 19. Driver-facing next action

Driver review should freeze the following reusable rules before any further lift classification:

`PLAIN_H2_REQUIRES_ABELIAN_KERNEL_AND_FIXED_MODULE_ACTION`

`NONABELIAN_EXTENSION_REQUIRES_OUTER_ACTION_AND_H3_REALIZABILITY_GATE`

`RELATION_RESIDUE != NONSPLITTING_CERTIFICATE`

`SPLIT != CANONICAL_SECTION`

`UNIVERSAL_EXISTENCE != ONE_MODEL_EXISTENCE`

`GEN12_REPRESENTATION_CORE = CLASSICAL`

`P000_COMPOUND_SEMANTICS = NO_MATERIAL_MATCH_ONLY`

`NO_MATERIAL_MATCH != NOVELTY`

If accepted, future mathematical work should no longer spend cycles re-proving generic `S4` extension/splitting/cohomology/permutation facts. It should focus on the genuinely project-specific question:

> From the frozen P000 native typed semantics, what enriched automorphism group, kernel, outer action, relation residue and primitive-preserving automorphism action on sections are **actually derived**, and under which exact model-class hypotheses do they split or admit an `Aut_prim`-fixed section?

No kernel quotient or canonical promotion is authorized by this Researcher return.
