# S23/AV auxiliary likelihood-sign observer: exact capacity plateaux 20–716

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXECUTED_EXACT_FINITE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Research identity: `EM-DIRECT-B0150F`; native activity `RA-48D51C1E4EC7088AC23FDF7C`. No formal Task CLAIM or Result/Review asserted.
Predecessors: PR #1777 plateaux 1–19 (especially `research_notes/brc_s23_av_analytic_plateaux18_19_20261108_r1/PROOF.md` at `f2776cc4afd609ec10b933783a2791bea0830169`); universal scaled-cell first-entry law `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`.

## Theorem (697 new exact plateaux)

Consider the frozen two-point iid auxiliary observation laws for labels (1,3,4):
`P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)`. Preserve the joint counts `(k,ell)` of labels 1 and 4; label 3 is neutral padding. Let `r=ln(7)/ln(10/7)` and the reflected-log threshold triangle
`D_h={(v,j) in Z_nonnegative^2:v+j<=h}`, with `t(v,j)=r*v-j`.
Let `N(h)` be the minimum common padded length such that every open threshold-partition cell, bounded or exterior, contains an attainable prefix score `E(k,ell)=k-r*ell`.

Define `epsilon=79*r-431>0`, `d0=2074774-380295*r`, `a_i=floor(i*d0/epsilon)`,
`V_i=380295*i+79*a_i`, `K_i=2074774*i+431*a_i`, and
`M_i=K_i+V_i-V_(i-1)-1`.

**For every integer i with 20<=i<=716 and every integer h with V_(i-1)+511<=h<=V_i+510, the exact capacity is N(h)=M_i.**

In particular the first new plateau is `N(h)=41880515` for `7226985<=h<=7607279`; at the final proved endpoint `h=272324831`, `N(h)=1486099146`. Combined with the predecessor through plateau 19, this gives a contiguous exact capacity staircase from its earlier starting range to `h=272324831`. The new extension covers `272324831-7226984=265097847` additional integer horizons and 697 plateau indices.

## Mathematical proof: integer-gap reduction

Set `eta=11*r-60` and `gamma=eta-epsilon`. The unimodular basis `U=(79,431), W=(11,60)` has determinant `79*60-431*11=-1`. Any integer threshold displacement `(dv,dj)=A*U+B*W` has reflected-log difference `x=A*epsilon+B*eta`; moreover the exact integer `B=79*x-epsilon*dv`. For any distinct thresholds in `D_H` with `0<x<epsilon`, `|dv|<=H` yields
`|B|<epsilon*(H+79)`.

An exact rational enclosure `LO/Q<r<HI/Q` is certified by 45-term atanh series with a rigorous positive geometric remainder, where
`Q=10^26`, `LO=545569623581288298975349314`, `HI=LO+1`.
It gives `0<d0<epsilon`, `eta>4800*epsilon`, `gamma>6*epsilon`.
For each endpoint `H_i=V_i+510` (20<=i<=716), the checker computes the rigorous upper bound `Bmax=ceil(epsilon_upper*(H_i+79))` and exhausts all nonzero integers `B` between `-Bmax` and `Bmax`. The `B=0` case has no difference in `(0,epsilon)`. For each nonzero `B`, the unique possible `A` is `-floor(B*eta/epsilon)` when `B>0`, or `floor(|B|*eta/epsilon)+1` when `B<0`; interval bounds certify that all necessary floors are fixed.

For each candidate, the checker reconstructs `dv=79*A+11*B`, `dj=431*A+60*B`, validates its strict width enclosure, and applies the exact minimum triangle embedding cost `max(dv_++dj_+,(-dv)_++(-dj)_+)`. All embedded candidates in the stated finite family have `dv` and `dj` of the same sign. A positive-positive candidate can originate at a left endpoint whose first coordinate `v` lies in `[0,H-dv-dj]`; a negative-negative candidate can originate only when `-dv<=v<=H+dj`. These integer intervals are exact existential projections over the second endpoint coordinate `j`; treating every such v as potentially dangerous is conservative.

## Mathematical proof: certified translated-witness interval cover

For each `s`, the predecessor scaled-cell theorem yields `0<delta_s:=K_s-r*V_s<epsilon`. For a threshold left endpoint `(v,j)`, if `v<=V_s` and `K_s>=H`, the translated prefix
`(k,ell)=(K_s-j,V_s-v)` is nonnegative, has score `E(k,ell)-t(v,j)=delta_s`, and length at most `K_s+V_s-v`.

At endpoint `H_i`, budget `M_i` and witness `s<=i`, the raw admissible left-v interval is
`[max(0,K_s+V_s-M_i),min(V_s,V_i)]` provided `K_s>=H_i`.
Remove the v-origin intervals of **every embeddable** sub-epsilon displacement whose certified gap lower bound is at most the certified upper bound for `delta_s`. On each surviving integer interval, all outgoing threshold gaps are strictly larger than `delta_s`; hence this one witness enters the immediately following bounded cell for every legal `j`.

`VERIFY_PLATEAUX20_716.py` constructs these exact intervals for each of 697 endpoints and performs a deterministic interval-cover sweep from `v=0` through `v=V_i`. It **asserts complete cover at every endpoint**. Maximum encountered sub-epsilon classes: 220; maximum covering witness blocks: 7. This is a finite, certified integer enumeration of displacement types and witness intervals, not an enumeration of the approximately quadratic number of thresholds.

For example, at i=20 the covering blocks (inclusive) are:

| left v interval | witness s | maximal common-prefix length |
|---|---:|---:|
| 0..4564093 | 12 | 29464398 |
| 4564094..6085431 | 16 | 34721600 |
| 6085432..7226474 | 19 | 40566489 |
| 7226475..7606769 | 20 | 41880515 |

The i=20 displacement classifier checks all 40 `B` candidates and obtains precisely six embeddable sub-epsilon directions (`B=±1,±2,±3`). The interval algorithm safely handles all of them. For i=716 the six witness blocks, reproduced in `RUN_EVIDENCE.txt`, finish at `v=272324321=V_716` with capacity `M_716=1486099146`.

## Upper 510 rows and exterior intervals

At `H_i=V_i+510`, left thresholds with `v>V_i` satisfy `0<=j<=509`. The predecessor **top-510-row gamma lemma** proves every outgoing bounded gap has width at least `gamma`: writing `x=A*epsilon+B*eta`, its cases `B=0,1,>=2,<=-1` contradict the available 509 units of triangle slack whenever `0<x<gamma`. This argument has no restriction on the number of sub-epsilon direction types and therefore applies at all the new endpoints.

For each such `v`, take the least `m in {1,...,6}` such that `L=V_i+68+79*m>=v`, and put `K=K_i+371+431*m`. The offset is
`K-r*L=delta_i+gamma-m*epsilon`, lying strictly in `(0,gamma)`. The checker validates this for each m and each i, and certifies maximum length `K_i+3498<M_i`.

The two exterior cells are covered by `(k,ell)=(0,floor(H_i/r)+1)` and `(floor(r*H_i)+1,0)`; rational adverse endpoints establish strict inequalities and lengths at most `M_i`. Neutral label-3 padding therefore proves `N(H_i)<=M_i`.

## Sharpness for all intermediate horizons

For `t=V_(i-1)+1`, the existing unimodular scaled-gap first-entry theorem establishes a particular *adjacent* threshold cell first hit by a prefix of length
`K_i+V_i-t=M_i`, already present at `h=510+t=V_(i-1)+511`.
Thus `N(V_(i-1)+511)>=M_i`. Threshold nesting makes `N(h)` nondecreasing; combined with the endpoint cover above, it is equal to `M_i` throughout the specified inclusive interval. Consecutive intervals meet without a gap or overlap, as checked exactly.

## Evidence, source scope, and next unit

The verifier consists entirely of Python standard-library `Fraction`, integer arithmetic, exact interval comparisons and a deterministic integer interval-cover algorithm. Its executed stdout is `RUN_EVIDENCE.txt`, including every checkpoint and `CERTIFICATE_SHA256=4a604c8c6b33a8657646fd026eb58494a9fa69f456ae37774b9d876efcd5f4aa` for the concatenated computed covering records. This digest identifies the finite computation output, not a mathematical acceptance signature.

At i=717 the *same fully-v-uniform witness family* first fails to cover `v=42217880` under its budget. That failure is specific to this sufficient covering construction; capacity at i=717 remains open. A useful next unit is a j-localized witness to repair this uncovered v band, or a different exact upper-bound witness.

Typed BRC usage: the carrier retains the joint label-1/label-4 count, multiplicity and label-3 padding; the observer is the auxiliary likelihood-sign partition for the fixed frozen two-point experiment. No mother-model ten-label transfer or X6 spatial interpretation is asserted. Protected P000 and ACTIVE worldview are unchanged. This is author-side proof plus executed exact finite certificate, pending independent mathematical review and any formal Source Result admission.
