# EC49CR — Five-operation native signed-X6 BRC observability and lossless joint one-step readout

2026-10-31 | Author-side portable research | EXACT_Q_RANK / EXACT_INTEGER_CERTIFICATE_PASS / NATIVE_BRC_TOTAL_PASS / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED

## Scientific input, inherited and frozen

GLOBAL_KNOWLEDGE_V1 canonical main `345b0d55546066c35f1d51bd4037db330507309c`; Enterprise Math main `c68fd26c8e605f2434a38f17f786a3bc2b26b6f7`. Inherits the *author-side*, not independently admitted, EC49CQ result at `919d85c5339e937ca03577feb1d006d8e301e044`, PR #1730. The unchanged native positive signed-X6 BRC source has Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

P000 and ACTIVE worldview remain unchanged: six native spatial axes with signed primitive steps, independent time, research three-dimensional slice of six-dimensional space, and typed structural residuals. This is a combinatorial BRC path/observer theorem, not physical time evolution, geometric slice dynamics, or a physical stability theorem.

Each ordered primitive letter is one of ±E1,...,±E6. Two **positive** BRC weight instruments on positive steps are w0=(2,3,3,2,1,1), w1=(3,2,3,2,1,1), negative-step weights all 1; third instrument counts literal paths. The DFA records ordered subwords A=(+E1,+E2), B=(+E2,+E1): each progress coordinate is 0 missing, 1 waiting, 2 seen, with four final Boolean-completion tags. Ordered operations and signed displacements are:

```
a = (-E1,-E1)                 Δ=-2E1
b = (-E2,-E2)                 Δ=-2E2
c = (+E1,+E2,-E1,-E2)        Δ=0
d = (+E2,+E1,-E2,-E1)        Δ=0
e = (+E3,+E1,+E1,-E3)        Δ=+2E1
S' = {a,b,c,d,e}
```

For any word u in complete operations, the observer R_u(tag, channel) sums the exact positive weight of every original prefix path whose displacement equals -Δ(u), times the suffix channel weight and the final tag indicator. It is linear in path multiplicity. The minimum dimensions below are over **rational-linear additive** states with these expressly chosen observations, not arbitrary nonlinear codes or finite-bit lower bounds.

## Exact theorem A: finite language rational ranks

On the formal six-axis-displacement × 9-state-DFA × 3-independent-channel space, the exact rational ranks are:

| Observable complete suffixes | Words | Target displacement fibers | Per-channel rank | Three-channel rank |
|---|---:|---:|---:|---:|
| S'^1 | 5 | 4 | 15 | **45** |
| S'^2 | 25 | 9 | 41 | **123** |
| S'^1 ∪ S'^2 | 30 | 9 | 44 | **132** |
| {ε} ∪ S'^1 | 6 | 4 | 18 | **54** |
| {ε} ∪ S'^1 ∪ S'^2 | 31 | 9 | 44 | **132** |

The per-channel ranks for S'^1∪S'^2, grouped by signed prefix target (d1,d2; other four coordinates zero), are:

```
(-4,0):4   (-2,0):6   (-2,2):4
( 0,0):6   ( 0,2):6   ( 0,4):4
( 2,0):6   ( 2,2):4   ( 4,0):4
```

**Finite exhaustive proof.** Enumerate all five operation words of length one and 25 ordered operation words of length two. For each compute its six-integer displacement and for each of nine formal DFA starting states run every primitive letter, recording the four final tag indicator rows. Disjoint prefix displacement fibers contribute a direct sum. Exact `Q` Gaussian elimination of the 0/1 matrices produces the nine ranks displayed above, with total 44. Three formally independent positive BRC channels contribute three copies because suffix weights are strictly nonzero. The executed checker uses `sympy.Matrix.rank()` for the exact upper and lower ranks and separately computes modular row bases, checking both agree. These exhaustive finite matrices, their pivot word/tag row names and their verification code are contained in the accompanying source evidence package. No general-h closed form is asserted.

## Exact theorem B: the enlarged language removes the nine-dimensional joint one-step rolling kernel

The word `ea=(+E3,+E1,+E1,-E3,-E1,-E1)` has zero displacement and cannot create a new completed A or B: no +E2 occurs and +E3 breaks an unfinished cross-boundary match. Previously completed tags are preserved. Its three channel multipliers are exactly 12, 27 and 1. Thus **for every literal prefix, every tag, and every prefix multiset**, independently of its length,

```
R_ea(tag, w0)    = 12 * R_ε(tag, w0)
R_ea(tag, w1)    = 27 * R_ε(tag, w1)
R_ea(tag, count) =      R_ε(tag, count).
```

Since `ea∈S'^2`, ε is already in the linear span of all nonempty suffixes up to any horizon H>=2; this explains `rank({ε}∪S'^≤2)=rank(S'^≤2)=132`.

More generally, for any h>=1 let V_(h+1) denote the exact rational-linear quotient under readouts `{ε}∪S'^1∪...∪S'^(h+1)`. Append each of the five possible first complete operations s, then read `{ε}∪S'^1∪...∪S'^h`. The joint successor observation consists of all `R_(sv)` with |sv|=1,...,h+1, by exact ordered concatenation `R_v(U_s P)=R_(sv)(P)`. These are *all* nonempty observations from V_(h+1); the omitted ε is recovered by the above ea identity. Therefore the joint five-way rolling map is injective and

```
dim ker T_h = 0   for every integer h>=1.
```

This removes the EC49CP nine-dimensional transient kernel **only after expanding the permitted operation/observation language**. It does not make the current finite-window quotient recursively sufficient for unlimited future updates, nor erase residual fibers newly exposed by e.

## Exact theorem C: earliest true-prefix saturation of the two-operation cumulative readout

Let P_n be **all** genuine ordered n-letter signed-X6 primitive prefix paths, not formal independently-assigned states. Exact rational ranks of the 30-word S'^≤2 readout on P_n:

| n | 4 | 6 | 8 | 10 | 12 |
|---|---:|---:|---:|---:|---:|
| rank over Q | 43 | 97 | 124 | 131 | **132** |

At n=10 only target (-4,0,0,0,0,0) is deficient, by one rank. At n=12 all nine fiber ranks saturate (12,18,12,18,18,12,18,12,12), with the following **literal real-path integer minors** nonzero modulo 1,000,003:

```
target      minor order   determinant mod 1000003
(-4,0)         12           960163
(-2,0)         18           211087
(-2,2)         12           246451
( 0,0)         18           664747
( 0,2)         18           718325
( 0,4)         12           416896
( 2,0)         18           718325
( 2,2)         12           416896
( 4,0)         12           416896
```

The nine minors contain **132 authentic literal length-12 paths** and the exact observation rows. An independent script recomputes signed displacements, tag transitions, all positive integer BRC products, and all nine modular determinants without calling the witness generator.

**Proof that earlier n do not saturate.** A separate exact rational dynamic program keeps at most three linearly independent path-weight triples for each (six-integer displacement, DFA state). This does not sample paths: any single primitive step applies the same invertible diagonal map to every vector at a given state, so induction proves retained *true* paths span every path's rational weight vector at the new state. Exact rational final elimination yields the five ranks above (independently agreeing with modular basis DP). The neutral fresh-history prefix (+E3,-E3) leaves displacement and DFA effects unchanged and applies invertible weight diagonal (3,3,1), so true rank cannot decrease from n to n+2. Since n=10 rank is only131, none of the earlier even n saturates; n=12 nonzero minors and the same neutral prefix prove all even n>=12 saturate. Odd n cannot return on these even-parity target fibers. Hence:

```
n_sat(S'^≤2) = 12.
```

Additional exact rational audits: S'^1 gives ranks 38,44,45 for n=6,8,10 and first saturates at n=10; S'^2 gives 91,116,122,123 for n=6,8,10,12 and first saturates at n=12.

## Verification and provenance

Actually executed a formal complete 30-word DFA row-system checker, a separate rational dynamic-path basis checker, an independent literal-path modular determinant checker, and an independent all-prefix integer DP compared with the **unchanged native** `endpoint_weight` and `endpoint_multiplicity`. At n=12, all **90 BRC native aggregate integer comparisons** (30 suffixes × three channels) pass; each checked sum of four A/B labels matches its native unscreened channel total. Native API itself does not filter labels; the separately implemented DFA does. Exact rational/rank arithmetic is distinct from any unproved physical dynamics.

The full verbatim author proof, executed code, literal-path certificates, full JSON (formal, rational, native), and execution log are retained as `EC49CR_FULL_EVIDENCE.tar.xz` (SHA256 `2e15022c9ec3e9bf891490e4c25976c22c3df8f21fafc4753463f6da6bd474e0`). Run Python3+SymPy: `python VERIFY_EC49CR.py`; `python VERIFY_EC49CR_RATIONAL.py`; `python RECHECK_EC49CR_INDEPENDENT.py CERT_EC49CR_REAL_{4,6,8,10,12}_SLE2.json`; `python VERIFY_EC49CR_NATIVE.py`. Literature background only: Balle–Panangaden–Precup, *A Canonical Form for Weighted Automata and Applications to Approximate Minimization*, arXiv:1501.06841 (2015). No novel-physics, clinical, stability or broader BRC result is inferred.

## Next EC49CS

Compute exact abstract rational ranks and first real-path saturation for three complete suffix operations of S' (125 exact three-operation words), classify all new signed displacement fibers and derive a row-span recursion which avoids brute-force 5^h future enumeration. Separate zero joint one-step kernel from the unbounded future-state size.

## Authorization state

For this actual client the source-native `em_status` call returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`. Therefore the current active owner, native CLAIM, session, Research-Activity, Result or Driver review cannot be confirmed. No prior conversation's identity or role is reused, and the research remains `PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`. GitHub PR storage is not formal Source-native admission. No credentials or permission changes.
