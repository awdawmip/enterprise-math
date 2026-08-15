# R059D Stage B — Controller-Scale Robustness / Crossover Identifiability

Researcher-ID: `EM-R059D-4C7E21`  
Taskbook source: `0dd9f78b047191535f4b05f80aafc613bbbac105`  
Frozen parent head: `0f634efbd4cf506f5ccbbbe63cfa524a065c7d72`  
Owner branch: `research/r059d-stage-b-crossover-identifiability`

## 1. Driver correction honored

All first-round R059D artifacts remain byte-immutable.

The accepted parent result is retained:

`ALIGNED_TO_ALIGNED_COUNT_CLOUD_RECURRENCE_ESTABLISHED_WITHIN_FROZEN_CONTROLLER_FAMILY`.

The first-round `N_c=3` interpretation is not promoted. It is retyped only as:

`R3_CONTROLLER_SPECIFIC_ALIAS_CANDIDATE`.

The Stage-B question is therefore identifiability: whether the intermediate count-cloud class change is a function of the macro count scale `N` itself or can be created, moved, or removed by the finite controller excursion parameter `R`.

No physical scale, metric, continuum, or probability interpretation is used.

## 2. General controller family

For every positive integer `R`, freeze

\[
G_R(+)=H^R V H^{-R},
\qquad
G_R(-)=H^{-R} V H^R.
\]

Equivalently, for branch bit \(s\in\{+1,-1\}\),

\[
G_R(s)=H^{Rs} V H^{-Rs}.
\]

The macrostep has

\[
m(R)=2R+1
\]

finite phases and control event count

\[
L_R(N)=(2R+1)N.
\]

`L_R(N)` is retained only as a control quantity.

At a phase boundary the branch excursion offset is

\[
a_R=0,1,\ldots,R,R,R-1,\ldots,1,0.
\]

Using the frozen I0 implementation labels only, the tagged position is

\[
\operatorname{pos}_R(i,s,p)
=
(3i+s\,a_R(p)\bmod 3N,\;k+b_R(p)\bmod 7),
\]

where \(b_R=0\) before the common `V` event and \(b_R=1\) afterward.

## 3. General-R endpoint theorem

The frozen carrier declares `H` and `V` to be commuting permutations. Hence, for every integer \(N\ge1\), \(R\ge1\), and \(s=\pm1\),

\[
H^{Rs}VH^{-Rs}
=
VH^{Rs}H^{-Rs}
=
V.
\]

Therefore every complete branch history has the same aligned endpoint:

\[
\operatorname{support} H_{N,L_R(N)}
=
\{A_{N,k+1}\}.
\]

The endpoint class is D0 for every positive integer `(N,R)`.

The exact full-history multiplicity is

\[
H_{\rm full}(N,R)
=
2^N (N!)^{2R+1}.
\]

This proves that exact aligned recurrence is shared by an infinite controller family, not just R2 and R3.

Freeze:

`ALIGNED_ENDPOINT_RECURRENCE_CONTROLLER_NONIDENTIFIABILITY = ESTABLISHED`.

This is a controller-identifiability statement only.

## 4. Exact alias theorem

At any corresponding intermediate offset \(a\), the same tagged constituent has branch positions

\[
3i+a
\quad\text{and}\quad
3i-a
\pmod {3N}.
\]

They coincide exactly when

\[
3N\mid 2a.
\]

Therefore

\[
\operatorname{ALIAS}(N,R)
\iff
\exists a,\ 1\le a\le R,\ 3N\mid2a.
\]

Let \(m=3N\). The positive solutions of \(m\mid2a\) are the multiples of

\[
a_0(N)=\frac{3N}{\gcd(2,3N)}.
\]

Since the excursion contains every integer offset from 1 through R,

\[
\boxed{
\operatorname{ALIAS}(N,R)
\iff
R\ge\frac{3N}{\gcd(2,3N)}
}.
\]

Thus:

- if `N` is odd, `ALIAS(N,R)` iff \(R\ge3N\);
- if `N` is even, `ALIAS(N,R)` iff \(R\ge3N/2\).

The target formula in the taskbook is therefore correct.

## 5. Exact `(N,R)` surface

For fixed `R`, the complete positive-integer alias set is

\[
\{N\text{ odd}:N\le\lfloor R/3\rfloor\}
\;\cup\;
\{N\text{ even}:N\le\lfloor2R/3\rfloor\}.
\]

This is not generally a sharp `N` threshold.

Mandatory controls:

- `R=1`: no aliased `N`;
- `R=2`: no aliased `N`;
- `R=3`: exactly `{1,2}`;
- `R=6`: exactly `{1,2,4}`;
- `R=12`: exactly `{1,2,3,4,6,8}`.

`R=6` is already non-monotone in `N`: `N=3` is non-aliased while `N=4` is aliased. Consequently a parity/residue surface cannot be compressed into a single critical `N`.

When `R>=3`, the largest aliased `N` encountered while descending from large `N` is

\[
N_{\rm first}(R)=2\lfloor R/3\rfloor.
\]

This quantity moves with the controller and is not a crossover threshold because smaller `N` can return to the non-aliased class.

For every fixed `N`, alias can be created by choosing

\[
R=a_0(N)
\]

and removed by choosing any \(1\le R<a_0(N)\), in particular `R=1`.

Therefore the observed R3 change is controller-scale movable.

Freeze:

`CONTROLLER_SCALE_ALIASING = ESTABLISHED`.

## 6. Tagged alias is not cell-coset merge

Two exact intermediate phenomena must remain distinct.

### 6.1 Same-tag branch alias

Same-tag `+/-` positions coincide iff

\[
3N\mid2a.
\]

The tagged configuration support at an offset \(a>0\) is therefore

\[
1
\quad\text{if }3N\mid2a,
\]

and otherwise

\[
2^N.
\]

### 6.2 Untagged cell support

Ignoring tag identity, the two cell cosets are

\[
3\mathbb Z_N+a
\quad\text{and}\quad
3\mathbb Z_N-a.
\]

They coincide iff \(3\mid a\). Hence phase-boundary cell support is

\[
N \quad (3\mid a),
\qquad
2N \quad (3\nmid a).
\]

This depends on the controller offset class modulo 3, not on the same-tag condition \(3N\mid2a\).

The first-round R3 phase at `a=3` therefore had an `N`-independent N-cell coset merge at the same time that the tagged configuration happened to alias only for `N=1,2`. These are different count readouts.

## 7. General-R T1 theorem

For a complete branch assignment \(s\in\{\pm1\}^N\), both used `V`-related carrier rows have the same x-support. Every base packet `3i` is visited.

### R=1

At every inter-base gap exactly one of the two interior x-cells is absent from an individual branch history. Hence every complete branch assignment has x-support `2N`, or total two-row support

\[
4N.
\]

Thus

\[
U_{N,1}(4N)
=
2^N(N!)^3.
\]

### R>=2

Only a cyclic `-` to `+` sign boundary can leave interior gap cells uncovered.

Let:

- `L` = length of the minus run ending at that boundary;
- `P` = length of the plus run starting at that boundary.

The two interior cells are uncovered according to

\[
e_R(L,P)
=
\mathbf 1[R<3L+1\ \&\ R<3P+2]
+
\mathbf 1[R<3L+2\ \&\ R<3P+1].
\]

Define

\[
A_R(x,z)
=
\sum_{L\ge1,P\ge1}
x^{L+P}z^{e_R(L,P)}.
\]

If a cyclic sign word has `t` minus-runs and `t` plus-runs, its ordered run lengths form `t` `(L,P)` pairs. A labeled cyclic word is represented `t` times by choosing the distinguished `-` to `+` boundary, giving the exact branch-assignment generating polynomial

\[
F_{N,R}(z)
=
2
+
\sum_{t=1}^{\lfloor N/2\rfloor}
\frac Nt
[x^N]A_R(x,z)^t.
\]

The leading `2` is the two constant-sign words.

If `e` x-cells are uncovered, the two-row unique support is

\[
u=6N-2e.
\]

Therefore

\[
\boxed{
U_{N,R}(6N-2e)
=
(N!)^{2R+1}
[z^e]F_{N,R}(z)
}
\qquad(R\ge2).
\]

The exact closed forms of \(A_R\), with \(q=\lfloor R/3\rfloor\), are:

For \(R=3q\), \(q\ge1\),

\[
A_R=
\frac{x^2}{(1-x)^2}
+
(z^2-1)\frac{x^{2q}}{(1-x)^2}.
\]

For \(R=3q+1\), \(q\ge1\),

\[
A_R=
\frac{x^2}{(1-x)^2}
+
2(z-1)\frac{x^{2q+1}}{1-x}
+
(z^2-1)\frac{x^{2q+2}}{(1-x)^2}.
\]

For \(R=3q+2\), \(q\ge0\),

\[
A_R=
\frac{x^2}{(1-x)^2}
+
(z^2-1)\frac{x^{2q+2}}{(1-x)^2}.
\]

The checksum is

\[
\sum_u U_{N,R}(u)
=
2^N(N!)^{2R+1}.
\]

The first-round R2/R3 expression is recovered as the special case in which every `-` to `+` boundary contributes exactly two uncovered x-cells.

## 8. General-R T2

Across all branch histories, offset `a=0` supplies the base residue class and offset `a=1` supplies both other residue classes. This occurs on both carrier rows used before and after the common `V` action.

Therefore, for every `R>=1`,

\[
\boxed{
\operatorname{CLOUD\_UNION\_SUPPORT\_COUNT}(N,R)=6N
}.
\]

This does not identify the controller because it is shared by the entire G_R family.

## 9. General-R T3

Let

\[
q=\lfloor R/3\rfloor,
\qquad
H_{\rm full}=2^N(N!)^{2R+1}.
\]

At a nonzero offset `a`, each branch sign occurs in exactly half of branch assignments. If `a` is divisible by 3 the two untagged cosets merge; otherwise they occupy the two non-base residue classes.

Summing exact occurrences over all offsets gives:

- `2N` carrier packets with multiplicity
  \[
  (q+1)H_{\rm full};
  \]
- `4N` carrier packets with multiplicity
  \[
  \frac{R-q}{2}H_{\rm full};
  \]
- the remaining `15N` carrier packets with multiplicity `0`.

`H_full` is even for every `N>=1`, so the displayed half coefficient always corresponds to an integer count.

If `R mod 3 = 2`, the two nonzero coefficients coincide and the spectrum merges to one `6N` nonzero class. This recovers the R2 special case.

Thus the intermediate multiplicity spectrum itself depends on controller scale and controller residue class even though the aligned endpoint does not.

## 10. General-R T4

The next aligned macrostep is obtained by the frozen successor relabeling `V`.

Because `V` commutes with all `H` actions used by G_R, pulling the next macrostep back by `V^-1` reproduces the same branch-offset sequence, T1 generating carrier, T2 support, T3 multiplicity spectrum, and exact phase count cloud.

Therefore

`ALIGNED_STEP_TRAVERSAL_SIGNATURE_RECURRENCE`

holds for every positive integer `R`, not only R2/R3.

## 11. Minimal controller

`R=1` is the smallest allowed excursion parameter and it already passes the complete nontrivial recurrence gate:

- two genuine branch alternatives at the intermediate excursion;
- tagged configuration support `2^N` at `a=1`;
- exact D0 endpoint recoalescence;
- full history count \(2^N(N!)^3\);
- T1 `4N` for each full history;
- T2 `6N` for the whole cloud;
- nonuniform T3 with `2N` packets at `Hfull`, `4N` packets at `Hfull/2`, and `15N` at zero;
- exact T4 recurrence.

Freeze:

`MINIMAL_NONTRIVIAL_ALIGNED_RECURRENCE_CONTROLLER_R1`.

Minimality does not establish physical naturalness.

## 12. Decorated-successor diagnostic

The frozen channel algebra is stronger than the R-only example. Every declared channel action `H`, `V`, `D=HV` is an invertible commuting permutation. Consequently, for every channel word `W` built from these actions,

\[
WVW^{-1}=V.
\]

A bounded registry was frozen before scale-down containing, in addition to the complete G_R family:

- \(W_s=D^s\);
- \(W_s=V^s\);
- \(W_s=H^sD^s\).

All survive huge-N endpoint recurrence and all were carried into scale-down. Their paired nonaligned prefixes have no same-tag alias for any `N>=1`.

Broken-return controls

\[
H^s V H^s
\quad\text{and}\quad
D^s V D^s
\]

do not have inverse returns and fail the common endpoint.

Thus the endpoint mechanism in the frozen positive grammar is classified as

`ENDPOINT_RECURRENCE_BY_REVERSIBLE_EXCURSION`.

No stronger non-reversible endpoint-recoalescence mechanism is claimed in this stage.

## 13. Controller nonidentifiability

The same aligned endpoint corresponds to many different intermediate count clouds.

Examples:

1. R1 has a single T1 support-size class `4N`; R2 has the `6N-4t` histogram.
2. R2 has no same-tag alias for any N; R3 aliases at N=1,2.
3. T3 changes with `floor(R/3)` and with `R mod 3`.
4. The bounded decorated `D1`, `V1`, and `HD1` reversible words have the same aligned endpoint while visiting different channel-labeled intermediate states.

Freeze:

`INTERMEDIATE_COUNT_CLOUD_CONTROLLER_NONIDENTIFIABILITY = ESTABLISHED`.

This is mathematically distinct from endpoint determinism: endpoint exactness survives even while the intermediate count-cloud representation is not identifiable from the endpoint.

## 14. Large-N discipline and postselection audit

The Stage-B controller registry was frozen before scale-down evaluation.

The symbolic endpoint theorem holds for all positive `(N,R)`, so every G_R controller is a huge-N endpoint survivor. No R value was discarded because its scale-down alias set was absent or unattractive.

The large-N registry also includes alias-edge probes around

\[
R_{\min}(N)=\frac{3N}{\gcd(2,3N)}.
\]

For `N=10^36` (even),

\[
R_{\min}
=
1.5\times10^{36}
\]

as an exact integer

`1500000000000000000000000000000000000`.

For the neighboring odd `N=10^36+1`,

\[
R_{\min}=3(10^{36}+1)
\]

=`3000000000000000000000000000000000003`.

These are controller-count relations only.

The explicit exact regression atlas covers all `8192` pairs

`1<=N<=128`, `1<=R<=64`.

No controller was selected after observing a preferred small-N crossover.

## 15. Deterministic checker

The deterministic checker passed:

`43303 / 43303`

with zero failures.

It includes:

- arbitrary-R endpoint regression on the full `N=1..128`, `R=1..64` box and both branch signs;
- direct existence-vs-closed-form alias verification on all 8192 `(N,R)` pairs;
- parity split and full atlas verification;
- phase tagged-alias and cell-support checks;
- direct all-branch T1 regression against the run generating theorem for `N=1..8`, `R=1..8`;
- T2 regression for `N=1..32`, `R=1..16`;
- direct all-branch T3 regression for `N=1..8`, `R=1..8`;
- R1 minimal-controller gates;
- decorated reversible-survivor and broken-return controls;
- probability/rigidity/quantum firewalls;
- postselection kill gates.

Checker digest:

`0c404cd7c7e094545d50fd7fa45bf0c373aef2f1b76dd26b0614425210976312`.

## 16. Stage-B disposition

Primary disposition:

`CONTROLLER_SCALE_ALIASING_EXPLAINS_OBSERVED_CROSSOVER`

because:

1. exact aligned recurrence holds for every positive `(N,R)`;
2. the Stage-A R3 class change is exactly one slice of
   \[
   R\ge 3N/\gcd(2,3N);
   \]
3. R1 and R2 remove the alias for every `N`;
4. increasing R can move and create alias at any fixed N;
5. fixed-R alias sets become parity-interleaved and non-monotone, so they are not a universal sharp scale;
6. decorated endpoint-surviving controllers can have no same-tag alias at any N.

Independent statuses:

`ALIGNED_ENDPOINT_RECURRENCE_CONTROLLER_NONIDENTIFIABILITY = ESTABLISHED`

`INTERMEDIATE_COUNT_CLOUD_CONTROLLER_NONIDENTIFIABILITY = ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

No intrinsic macro-micro boundary is identified in the frozen Stage-B controller grammar.

## 17. Stop

`STOP_FOR_DRIVER_REVIEW`
