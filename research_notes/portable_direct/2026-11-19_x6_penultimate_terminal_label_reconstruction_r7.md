# X6 observer VIII (R7): exact terminal-label reconstruction from penultimate source languages

Date: 2026-11-19 (Asia/Shanghai). Status: author-proved conditional finite named-port theorem; independent mathematical review NOT_REVIEWED. Research line RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3. Frozen P000/task science pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; current normative rules read independently.

## Previous verified frontier and question

R4 gave exact full-future Port-language classes, R5 proved two-channel penultimate stabilization, and [R6](2026-11-19_x6_multisource_port_penultimate_alias_r6.md) showed that with t channels of exact local period one, a penultimate observation class can split into at most max(1,t) full-language classes. R6 left the *exact* split count and an explicit reconstruction algorithm implicit. This R7 solves both at every fixed observed fiber, not merely with a universal upper bound.

## Typed model and observer

Fix d>=2 distinct named source types x_1,...,x_d, terminal quota vector a=(a_i) with a_i>=1, finite Port-controller modes Q, and deterministic partial source-labelled transitions (n,q) --x_j--> (n+e_j,q') with coordinatewise 0<=n<=a and no silent transitions. Terminal accepting controller modes may be specified independently. The productive reachable states at rank k=sum n_i have at least one accepted complete continuation. All their complete continuation words have the same length H=sum a_i-k. They retain named-source labels and a Parikh vector equal to a-n.

An observer O(s)=(k,(n_i mod p_i)_i), with exact local periods p_i>=1, hides exact winding and q. The finite typed Boolean BRC branch carrier keeps ordered named-source words and Q-mode provenance; its support (n,q) is a valid quotient for precisely this partial named-source append/future-language interface. It does not retain signed/phase amplitudes or certify native X6 force-event permission.

For productive s put C(s) = its nonempty set of accepted H-letter completions. Put P(s)=Pref_{<=H-1}(C(s)), including the empty word. At fixed observed fiber o, let E(o) be the partition into equal P(s) classes. Each class E contains a common prefix word u_E of length H-1 (H>=1), because every represented state is productive. Define
```
J_E(u_E) = { j in {1,...,d} :
  a - n(s) - Parikh(u_E) = e_j  for some s in E }.
```
Each difference is indeed exactly one unit vector because u_E belongs to the productive prefix language of every s.

## Theorem 1 — exact terminal-label degree and constructive decoder

For every H>=1 and each fixed observation o,

```
|{C(s): O(s)=o, s productive}| = SUM_{E in E(o)} |J_E(u_E)|.
```

The right side is independent of the chosen full-length common prefix u_E in each E. In particular, with M_h(o)=number of distinct productive prefix languages Pref_{<=h}(C(s)) on fiber o,

```
M_{H-1}(o) = |E(o)|,
M_H(o) = SUM_E |J_E(u_E)|,
b_H(k) = ceil(log_2 max_o SUM_E |J_E(u_E)|).
```

These formulas include H=1, where u_E is the empty word. No formula for H-1 is asserted when H=0.

**Proof.** Fix E and a word u=u_E of length H-1 in the common language. For any state s=(n,q) in E, its residual quota after u is the one-hot vector a-n-Parikh(u)=e_{j(s,u)}. If two states s,s' share the same last index j, they have the same exact n. For any other word v of length H-1 in the common prefix language P(E), the *only* quota-compatible last source type is the index l with a-n-Parikh(v)=e_l. Since v lies in both productive prefix languages, v x_l is an accepted completion for both states. Conversely every accepted completion has such a length-(H-1) prefix v. Hence
```
C(s) = { v x_l : v in P(E), |v|=H-1,
                 a-n-Parikh(v)=e_l },
```
and s,s' have identical complete languages when j(s,u)=j(s',u). If j differs, the exact Parikh vectors of their complete continuations differ by e_i-e_j; the nonempty full languages cannot be equal. Thus j maps E's distinct full-language classes *bijectively* to J_E(u). Different E already have different penultimate languages, hence have different full languages. Summing proves the equality, and the bijection also proves independence of the chosen u. The fixed-length optimal code for all full-language classes on a fiber uses ceil(log2 M_H(o)) bits; max over o gives b_H(k). QED.

**Constructive decoder.** Given the penultimate language-class E and a label j in J_E(u_E), compute the exact remaining pre-prefix quota n=a-Parikh(u_E)-e_j; then for each word v of length H-1 in P(E), append the unique label l with a-n-Parikh(v)=e_l. This recovers *the entire accepted complete future source language*, rather than necessarily the hidden physical/controller state. If encoding E and j jointly under original observer o, an enumerative code with SUM_E |J_E| labels is optimal; two separately padded codes can waste bits.

## Theorem 2 — exact period-one obstruction and residual test

Put T={i:p_i=1}, t=|T|. If |J_E|>=2, then J_E is a subset of T; hence every degree is 1 or at most t. More concretely, two different j,j' in J_E have exact count vectors differing by e_{j'}-e_j, and each of the two changed coordinates must have period one.

**Proof.** States in the same E and observation share n mod p. With a common u, their counts are a-Parikh(u)-e_j and a-Parikh(u)-e_{j'}. Different indices change only j and j' by ±1. Divisibility by p_j and p_{j'} requires p_j=p_{j'}=1. Any index participating in a degree>=2 class participates in such a pair. QED.

Thus the *actual*, controller-dependent last-step multiplicative loss on fiber o is
```
M_H(o)/M_{H-1}(o) = (SUM_E |J_E|)/|E(o)|,
```
the mean terminal-label degree. The exact bit increase is
```
ceil(log2 SUM_E |J_E|) - ceil(log2 |E(o)|).
```
These distinguish genuine Port/source history residual from the mere existence of t>=2 period-one channels: the controller may forbid every nontrivial degree even when t is large. R6's sharp upper bound M_H<=max(1,t)M_{H-1} follows immediately.

For the R6 free one-mode capacity-respecting witness with a=(1,...,1) and periods (1 repeated t times,2), at rank k=d-1 the observed fiber consisting of the t states missing exactly one period-one source has E(o)={one penultimate class}, and |J_E|=t. The information cost is exactly ceil(log2 t), for every t>=2. In the t=2 case n=(0,1,1), n'=(1,0,1) yield distinct final sources A and B even though their observer is identical.

## Finite exact BRC validation

Executed `x6_penultimate_terminal_label_brc_verify.py` with Python 3; emitted `x6_penultimate_terminal_label_brc_results.json`. Source SHA256: `51ce83b851f8a4bf14d9702250d31a571fad14135f8fa21b310da58956208b5d`; JSON SHA256: `65639b0d07211f7754d2fb668c0c97671ef188d42c5f9f991100dc61958a086a`.

Complete checked domain: all 3^6=729 two-mode partial deterministic Port-controller transition maps on three named source types; all four quota vectors (1,1,1),(1,1,2),(1,2,1),(2,1,1); five period vectors (1,1,1),(1,1,2),(1,2,2),(2,3,1),(2,2,2); and all three nonempty accepting-terminal-mode masks {0},{1},{0,1}. Exactly 43,740 model/quota/period/acceptance configurations, including 16,970 productive root configurations, 104,329 productive observed fibers and 5,216 nontrivial penultimate classes. In 4,912 observed fibers the full-language code requires strictly more bits than the penultimate code. Maximum observed degree is 3. Every equality in the two theorems, the full-word-to-(count,mode) Boolean support quotient, and capacity/acceptance conditions passed. Constructive sharp witnesses for t=2,...,6 were checked separately as exact one-mode combinatorial certificates. No assumption that finite tests prove the universal parameter theorem is made; the arbitrary-d proof is above.

Reproduce: `python3 x6_penultimate_terminal_label_brc_verify.py > x6_penultimate_terminal_label_brc_results.json`. Hashes identify the locally executed exact files; compare with published bytes before claiming remote reproduction.

## Interpretation, native boundary and next research

The theorem produces an *exact minimal suffix-selector certificate*: a penultimate future-language class plus its terminal source label reconstructs the full future language. It also supplies a measurable failure condition for Port-history erasure, rather than requiring all Port histories to be retained. It preserves the account's residual-fidelity and source-order requirements.

This result is about declared finite labelled support models. P000 keeps native X6 as six spatial Cell axes plus separately typed event time; native primitive stable nonzero balance requires three signed nonzero force contributions satisfying TRIADIC_CLOSURE_E, and the native three-dimensional research slice is not a two-dimensional plane. The Port controller in this note is a *conditional* event-permission object, not a verified native Cell/Link/Port permission relation. Neither finite-word support nor a one-mode Port witness supplies that missing native triadic admissibility certificate.

**Next discriminating unit:** specify one actually permitted, source-labelled triadic closure event and its Port occupancy/release/ordered-history rule from frozen native definitions, with full six-coordinate and third-slice-component provenance. Establish a future-operation-preserving map from the native admissible transition to the present (n,q) support model; then compute J_E for actual native event fibers. If two period-one native source labels can trade a final event inside a common E, the terminal-label residual is compulsory for this observer; if every actual E has degree one, the extra last-event selector is unnecessary for this native interface.

Provenance: previous R6 historical published Activity RA-545183ADD4EF71C3E4698AEE / EM-X6-214D9C, original SID MCP-d467c19ce42d4d7fa65a3901db1cf6b2. This source preservation neither replaces an actual current session authorization nor asserts a new CLAIM, native PROGRESS, independent acceptance, or native triadic mapping.
