# Enterprise Math — BRC Weighted / Log Global Research Foundation

Status: `CANONICAL ALL-RESEARCH FOUNDATION / MAIN-BACKED / R023-BOOLEAN-BASE-PRESERVED`  
Effective: `2026-09-02`  
Promotion authority: explicit current user instruction after main-backed extraction/regression  
Minimal universal substrate: `ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`  
Theorem ledger: `ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json`  
Reusable tool: `src/enterprise_math/brc_weighted.py` / `t0.weighted_brc_cwm`

## 1. Foundation role

Weighted/Log BRC is now part of the mathematical background available to **all Enterprise Math research modes**. It is a typed branch foundation, not a compulsory interpretation of every problem.

The universal rule is:

```text
PROBLEM_DECLARES_BRANCHING_OR_POSITIVE_WEIGHT
-> PRESERVE_THE_DECLARED_BRANCH_TYPE
-> BOOLEAN_SUPPORT_MAY_BE_TOO_COARSE
-> CWM_WEIGHTED_LAYER_IS_AVAILABLE
```

while

```text
DETERMINISTIC_SINGLE_PATH -> E=1 -> DELTA=0 -> NO_FORCED_WEIGHTED_REINTERPRETATION
SIGNED_OR_AMPLITUDE_DATA -> POSITIVE_CWM_IS_NOT_A_REPLACEMENT
```

Canonical R023 remains the Boolean result-support base. The weighted layer is a separately typed enrichment.

For FREE Phase A, only the minimal commitments in `ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` are a discovery prior. The detailed theorem ledger, examples, successful prior applications and tool catalog remain lazy: they may be opened only after the self-generated problem actually presents the corresponding branch structure. Thus global-foundation status does not create a default BRC research agenda.

## 2. Positive weighted branch carrier

For a finite family of positive rational weighted paths, use

\[
(C,W,M),
\]

where

- \(C\in\mathbb N_0\) is supported path count;
- \(W\in\mathbb Q_{\ge0}\) is total path mass;
- \(M\in\mathbb Q_{\ge0}\) is dominant single-path mass.

The algebraic carrier

\[
\mathcal S_{CWM}=\mathbb N_0\times\mathbb Q_{\ge0}\times\mathbb Q_{\ge0}
\]

uses

\[
(c,w,m)\boxplus(c',w',m')=(c+c',w+w',\max(m,m')),
\]

\[
(c,w,m)\boxtimes(c',w',m')=(cc',ww',mm').
\]

A positive edge/path weight \(a\) lifts as

\[
a\mapsto(1,a,a).
\]

Hence one path evaluation can carry count, total positive mass and dominant mass simultaneously.

Canonical theorem ID: `WBRC-T01-CWM-SEMIRING`.

## 3. Exact positive-path realizability

The weak closed envelope

\[
c\ge1,\qquad 0<m\le w\le cm
\]

is not the exact finite positive-path image.

The exact realizability locus is:

\[
(C,W,M)=(0,0,0),
\]

or

\[
C=1,\quad W=M>0,
\]

or

\[
C\ge2,\quad 0<M<W\le CM.
\]

These conditions are necessary and sufficient for a finite positive rational branch family.

Canonical theorem ID: `WBRC-T02-POSITIVE-REALIZABILITY`.

## 4. Boolean support projection

For a weighted semiring-like carrier \((S,\oplus,\otimes,0,1)\), define

\[
\beta(a)=0\iff a=0,
\qquad
\beta(a)=1\iff a\ne0.
\]

Then \(\beta\) is a semiring homomorphism to Boolean support exactly when the carrier is:

1. zerosumfree;
2. without zero divisors.

Thus positive/counting mass can forget to Boolean BRC under explicit admissibility hypotheses, while signed cancellation and zero-divisor carriers cannot.

Canonical theorem ID: `WBRC-T03-BOOLEAN-SUPPORT-HOMOMORPHISM`.

Hard witnesses:

\[
1+(-1)=0,
\qquad
2\cdot3=0\pmod 6.
\]

## 5. Effective multiplicity and logarithmic surplus

For a live CWM state with \(M>0\), define

\[
E=\frac WM,
\qquad
\Delta=\ln E=\ln\frac WM.
\]

Then

\[
1\le E\le C,
\qquad
0\le\Delta\le\ln C,
\]

and

\[
\boxed{\ln W=\ln M+\Delta.}
\]

For \(k\) equal branches,

\[
\boxed{E=k,\qquad \Delta=\ln k.}
\]

This is the canonical BRC meaning of \(\ln k\): recoalescence multiplicity after dominant-path scale has been factored out.

No logarithm is needed during exact path accumulation. When the ratio is rational, `Delta` is materialized only at readout time through the existing exact BRC `LN` runtime.

Canonical theorem IDs: `WBRC-T04-MULTIPLICITY-SURPLUS`, `WBRC-T05-MAX-TOTAL-DECOMPOSITION`.

## 6. Deterministic degeneration

For exactly one deterministic positive path,

\[
C=1,\qquad W=M,
\]

hence

\[
E=1,
\qquad
\Delta=0.
\]

Therefore this foundation does not add artificial multiplicity information to a deterministic problem.

Canonical theorem ID: `WBRC-T11-DETERMINISTIC-DEGENERATION`.

## 7. All-prefix safe weighted quotient

For declared terminal targets \(t\), define the complete future transfer

\[
F_t(x)=\bigl(C_{x\to t},W_{x\to t},M_{x\to t}\bigr).
\]

If arbitrary admissible incoming prefixes must remain valid without changing their weights, then

\[
\boxed{x\sim y\iff F_t(x)=F_t(y)\ \text{for every declared target }t.}
\]

The kernel of the full future CWM vector is the coarsest all-prefix safe weighted quotient.

Boolean future equivalence is generally strictly coarser. One-step local weighted bisimulation is sufficient but not necessary because a positive factor may be moved between an edge and downstream future without changing complete transfer.

Canonical theorem ID: `WBRC-T06-ALL-PREFIX-SAFE-QUOTIENT`.

## 8. Projective / gauge-compensated quotient

For \(\lambda>0\),

\[
G_\lambda(c,w,m)=(c,\lambda w,\lambda m).
\]

Two future signatures are projectively equivalent when count coordinates agree and one common \(\lambda\) scales both \(W\) and \(M\) for every declared target.

This is not an ordinary quotient. Exact merging requires coherent compensation of every redirected incoming weight by the same scale factor so complete path weights are preserved.

In log coordinates

\[
g=\ln\lambda
\]

is an additive absolute-scale coordinate, while

\[
\Delta'=\ln\frac{\lambda W}{\lambda M}=\Delta
\]

is gauge invariant.

Canonical theorem ID: `WBRC-T07-PROJECTIVE-GAUGE-QUOTIENT`.

## 9. One-state recurrent positive branches

For one recurrent state with positive rational loop weights

\[
q_1,\ldots,q_k,
\]

write

\[
S=\sum_iq_i,
\qquad
Q=\max_iq_i.
\]

After exactly \(n\) traversals,

\[
(C_n,W_n,M_n)=(k^n,S^n,Q^n).
\]

All-depth path count is infinite whenever a loop exists, so finite-DAG `C` does not remain finite under recurrent closure.

Total sum-product mass is finite exactly when

\[
\boxed{S<1,}
\]

and then

\[
\sum_{n\ge0}S^n=\frac1{1-S}.
\]

Dominant-path mass is bounded under the weaker condition

\[
Q\le1.
\]

If

\[
T=\ln Q,
\quad
L=\ln S,
\quad
\Delta_{\rm loop}=\ln(S/Q),
\]

then

\[
L=T+\Delta_{\rm loop}.
\]

Thus multiplicity can destabilize a system even when every individual loop contracts.

For \(k\) equal loops of weight \(q\),

\[
\boxed{kq<1\iff\ln q<-\ln k.}
\]

Canonical theorem IDs: `WBRC-T08-ONE-STATE-RECURRENT-POWER`, `WBRC-T09-ONE-STATE-TOTAL-MASS-STABILITY`, `WBRC-T10-EQUAL-LOOP-LOG-THRESHOLD`.

## 10. Global hard boundaries

All research modes must preserve these type guards:

```text
WEIGHTED_BRC != BOOLEAN_R023_MUTATION
POSITIVE_WEIGHTED_BRC != SIGNED_AMPLITUDE_CANCELLATION
BOOLEAN_SUPPORT != RECOVERED_MULTIPLICITY
LN_LOG = DERIVED_EXACT_READOUT, NOT PRIMITIVE_NATIVE_STATE
FINITE_DAG_CWM_COUNT != FINITE_COUNT_ON_RECURRENT_CLOSURE
ONE_STATE_CYCLIC_RESULT != GENERAL_SCC_SPECTRAL_THEOREM
DETERMINISTIC_SINGLE_PATH -> DELTA=0
```

Detailed negative-boundary IDs are `WBRC-N01` through `WBRC-N05` in the theorem ledger.

## 11. All-research consumption rule

This foundation is available in every research mode.

- **FREE Phase A:** inherit only `ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`. It supplies type discipline, not a suggested question. If the independently generated problem actually contains relevant branching, the exact CWM definitions may then be used; do not preload successful examples or theorem menus to steer discovery.
- **FREE Phase B / TASK research:** theorem IDs and the reusable T0 subtool may be loaded normally when relevant.
- **Driver / Steward:** use the theorem ledger and method inventory for routing, deduplication, review and backflow.

The foundation is therefore universal but lazy:

```text
ALL_RESEARCH_HAS_THE_TYPED_CAPABILITY
!=
ALL_RESEARCH_MUST_USE_THE_CAPABILITY
```

## 12. Canonical evidence and executable surfaces

Main-backed evidence chain:

- PR #1102 — exact BRC `LN/LOG` materialization;
- PR #1103 — support projection and multiplicity tower;
- PR #1104 — CWM semiring and safe quotient;
- PR #1105 — realizability and projective/gauge quotient;
- PR #1106 — one-state cyclic multiplicity closure;
- PR #1107 — first Foundation integration;
- PR #1108 — old-research regression and boundary pressure test.

Reusable current surfaces:

- `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`;
- `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json`;
- `src/enterprise_math/brc_weighted.py`;
- `tests/test_brc_weighted_foundation_tool.py`;
- `src/enterprise_math/brc_logarithm.py`;
- `research_method_inventory_addenda/20260902_brc_weighted_foundation.json`.
