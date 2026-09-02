# Enterprise Math — BRC Weighted / Log Foundation Extension

Status: `CANONICAL FOUNDATION EXTENSION / MAIN-BACKED / R023-BOOLEAN-BASE-PRESERVED`
Effective: `2026-09-02`
Steward integration: `DIRECT_FOUNDATION_MAINTENANCE`
Evidence baseline: `main@843d3e41d570361f77589cbf4983670f3918feac`

## 1. Purpose and authority

This definition records the verified weighted/logarithmic branch layer that now sits above the canonical R023 Boolean-result-support BRC base.

It is a **typed extension**, not a replacement of R023 and not a new primitive ontology.

Freeze:

```text
CANONICAL_BRC_BASE_LAYER = BOOLEAN_RESULT_SUPPORT_SEMANTICS
WEIGHTED_BRC = SEPARATELY_TYPED_ENRICHMENT
LN_LOG = DERIVED_EXACT_READOUT_COORDINATES, NOT PRIMITIVE STATE
SIGNED_AMPLITUDE_CANCELLATION != POSITIVE_WEIGHTED_BRC
GENERAL_SCC_SPECTRAL_THEORY = NOT_PROMOTED_BY_THIS FILE
FREE_AXIOM_DISCOVERY_PHASE_A = UNCHANGED
```

The exact source evidence is the merged BRC arithmetic/log and weighted-BRC research sequence:

- PR #1102 / `2fc50ba0823a02bd213bba4fe89d7446957dc34a` — exact BRC `LN/LOG` materialization;
- PR #1103 / `889a0c10991fa9d8a70e273535ea0d1a21039f33` — weighted support projection and multiplicity tower;
- PR #1104 / `8a05c2ad3d44d4f4aeb7040ad7213583061d669b` — CWM semiring and all-prefix safe quotient;
- PR #1105 / `ed2fdcb28e7205832ad9e507eba872e1a8f1c6f5` — CWM realizability correction and projective/gauge quotient;
- PR #1106 / `843d3e41d570361f77589cbf4983670f3918feac` — one-state cyclic log-multiplicity closure.

## 2. Positive weighted branch algebra

For finite branch families with non-negative weights, propagation along one path is multiplicative and recoalescence across alternative paths is additive.

For a finite DAG with positive rational edge weights, the exact native summary at a source/target pair is

\[
(C,W,M),
\]

where

- \(C\in\mathbb N_0\) is the number of supported paths;
- \(W\in\mathbb Q_{\ge0}\) is the sum of all path weights;
- \(M\in\mathbb Q_{\ge0}\) is the largest single path weight.

The carrier

\[
\mathcal S_{CWM}=\mathbb N_0\times\mathbb Q_{\ge0}\times\mathbb Q_{\ge0}
\]

has operations

\[
(c,w,m)\boxplus(c',w',m')=(c+c',\;w+w',\;\max(m,m')),
\]

\[
(c,w,m)\boxtimes(c',w',m')=(cc',\;ww',\;mm').
\]

A positive edge of weight \(a\) lifts as

\[
a\longmapsto(1,a,a).
\]

Thus one semiring path evaluation simultaneously carries count, total mass, and dominant-path mass.

## 3. Exact positive-path realizability locus

The algebraic envelope

\[
c\ge1,\qquad 0<m\le w\le cm
\]

is closed but is larger than the exact image of finite families of **positive** path weights.

The exact realizability conditions are:

\[
(C,W,M)=(0,0,0)
\]

for no supported path;

\[
C=1\quad\Longrightarrow\quad W=M>0;
\]

and

\[
C\ge2\quad\Longrightarrow\quad 0<M<W\le CM.
\]

These conditions are necessary and sufficient for a finite family of positive rational path weights after allowing an appropriate rational realization.

This distinction must be preserved in later theorem statements: `ALGEBRAIC_CWM_CARRIER != EXACT_POSITIVE_PATH_REALIZABILITY_LOCUS`.

## 4. Boolean support as a forgetful image

For a semiring-like weighted branch carrier \((S,\oplus,\otimes,0,1)\), define

\[
\beta(a)=\begin{cases}
0,&a=0,\\
1,&a\ne0.
\end{cases}
\]

The nonzero-support map is a semiring homomorphism to Boolean support exactly when the weighted carrier has both:

1. **zerosumfreeness**: \(a\oplus b=0\Rightarrow a=b=0\);
2. **no zero divisors**: \(a\otimes b=0\Rightarrow a=0\) or \(b=0\).

Hence positive/non-negative counting or mass semantics can forget to Boolean BRC without creating or deleting support, while signed cancellation or zero-divisor carriers generally cannot.

Canonical counter-boundaries include:

\[
1+(-1)=0
\]

for signed cancellation, and

\[
2\cdot3=0\pmod 6
\]

for a zero-divisor carrier.

Therefore the R023 Boolean base is a valid support projection only under an explicit admissible weighted carrier; Boolean BRC does not recover erased multiplicity or weight.

## 5. Logarithmic coordinates and multiplicity surplus

For a live finite weighted path family \((C,W,M)\) with \(M>0\), define the effective multiplicity

\[
E=\frac WM
\]

and the logarithmic recoalescence surplus

\[
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

For \(k\) equal-weight branches,

\[
\boxed{\Delta=\ln k.}
\]

This gives a precise meaning to \(\ln k\) in BRC: it is the information/scale increment contributed by equal branch multiplicity at recoalescence after the dominant-path scale has been factored out.

`LN` is not required during exact path accumulation. When the ratio \(W/M\) is rational, \(\Delta\) may be materialized only at readout time through the existing exact BRC logarithm runtime.

## 6. Relation to max-path / idempotent path closure

The dominant coordinate \(M\) is the max-times path envelope. In log coordinates its value is the max-plus path envelope

\[
T=\ln M.
\]

The total-mass log value is

\[
L=\ln W=T+\Delta.
\]

Thus the idempotent max-path layer is a lower envelope of the non-idempotent weighted BRC layer, and \(\Delta\) measures the exact recoalescence gap between them.

This does not merge the two tool families: max-plus closure forgets multiplicity by idempotence, while weighted BRC intentionally retains it.

## 7. All-prefix safe weighted quotient

Fix a declared family of terminal observations/targets. For a state \(x\), let

\[
F_t(x)=\bigl(C_{x\to t},W_{x\to t},M_{x\to t}\bigr)
\]

be its exact future CWM transfer to target \(t\).

If arbitrary admissible incoming prefixes must remain valid without modifying their weights, then two states are weighted-BRC safe-equivalent exactly when

\[
\boxed{F_t(x)=F_t(y)\quad\text{for every declared target }t.}
\]

The kernel of the complete future CWM transfer vector is therefore the coarsest all-prefix quotient preserving all declared terminal CWM observations.

Boolean future equivalence is generally strictly coarser and may merge states whose supported targets agree while their multiplicity or mass behavior differs.

A one-step local weighted bisimulation condition is sufficient but not necessary: edge factors may be redistributed between an incoming edge and the downstream future while preserving complete path transfer. The canonical safety object is the full future transfer, not the raw one-step table.

## 8. Projective / gauge-compensated quotient

A second, larger equivalence is available only when the representation is allowed to change incoming weights coherently.

For \(\lambda>0\), define

\[
G_\lambda(c,w,m)=(c,\lambda w,\lambda m).
\]

Two live future signatures are projectively equivalent when their count coordinates agree and one common positive rational \(\lambda\) scales both \(W\) and \(M\) for every declared target.

Such states are not ordinary quotient-equivalent. They become exactly mergeable only if every redirected incoming weighted transition is compensated by the same factor so that complete path weights remain unchanged.

In log coordinates this scale is the additive gauge

\[
g=\ln\lambda.
\]

The multiplicity surplus is gauge-invariant:

\[
\Delta'=\ln\frac{\lambda W}{\lambda M}=\Delta.
\]

Therefore absolute log scale and internal recoalescence structure are distinct coordinates.

## 9. One-state recurrent closure and multiplicity stability

For one recurrent state with positive rational self-loop branch weights

\[
q_1,\ldots,q_k,
\]

define

\[
S=\sum_iq_i,
\qquad
Q=\max_iq_i.
\]

After exactly \(n\) loop traversals, the CWM value is

\[
(k^n,S^n,Q^n).
\]

The number of finite walks over all depths is infinite whenever at least one loop exists, so the finite-DAG natural count coordinate does not remain finite on recurrent closure.

The total sum-product mass over all depths is finite exactly when

\[
\boxed{S<1,}
\]

in which case

\[
\sum_{n\ge0}S^n=\frac1{1-S}.
\]

The dominant-path envelope is bounded under the weaker condition

\[
Q\le1.
\]

Writing

\[
T=\ln Q,
\qquad
L=\ln S,
\qquad
\Delta_{\mathrm{loop}}=\ln\frac SQ,
\]

we have

\[
L=T+\Delta_{\mathrm{loop}}.
\]

Thus recurrent total-mass stability is controlled by the multiplicity-corrected exponent \(L\), not by the dominant-path exponent \(T\) alone.

For \(k\) equal loops of weight \(q\),

\[
S=kq
\]

and the stable region is

\[
\boxed{kq<1}
\]

or equivalently

\[
\boxed{\ln q<-\ln k.}
\]

Hence the same \(\ln k\) that measures finite recoalescence surplus becomes the exact multiplicity stability penalty for equal recurrent branches.

A minimal boundary witness is two loops of weight \(3/5\): every individual loop contracts since \(Q=3/5<1\), while total branch mass diverges since \(S=6/5>1\).

When \(S=N/D<1\), recurrent closure may be materialized exactly as

\[
\frac1{1-S}=\frac D{D-N},
\]

and any logarithmic readout may use the canonical BRC `DIV -> LN` path rather than numerical infinite summation.

## 10. Hard boundaries and non-promotions

This foundation extension does **not** assert:

- that R023 Boolean BRC preserves weight, multiplicity, probability or branch provenance;
- that signed/amplitude cancellation is covered by the positive weighted carrier;
- that `LN` or `LOG` is a primitive arithmetic state;
- that complex logarithm branches are included;
- that the finite-DAG count coordinate remains finite on recurrent graphs;
- a general strongly-connected-component closure theorem;
- a Perron-Frobenius or spectral-radius theorem for arbitrary weighted BRC transition matrices;
- a physical probability interpretation of positive weights;
- a new Foundation axiom replacing integer/discrete native commitments.

General cyclic/SCC behavior beyond the exact one-state loop family remains a research frontier and requires separately proved exact certificates.

## 11. Research consumption rule

For TASK research, Driver review and FREE Phase B, use this extension whenever the problem explicitly contains:

- multiple branch representatives whose multiplicity or positive weight matters;
- a comparison of total branch mass with a dominant branch;
- a weighted future-safe quotient or projective/gauge reparameterization;
- a recurrent positive weighted branch family where multiplicity can alter stability.

Do **not** inject this file into blind FREE Phase A solely because it is successful downstream mathematics. The canonical anti-anchoring rule remains:

```text
FOUNDATION_FOR_CURRENT_RESEARCH != FREE_PHASE_A_DISCOVERY_PRIOR
```

## 12. Executable evidence

Canonical executable/checker surfaces include:

- `src/enterprise_math/brc_logarithm.py`;
- `experiments/brc_weighted_log_semiring_check.py`;
- `experiments/brc_weighted_rational_runtime_prototype.py`;
- `experiments/brc_weighted_multiplicity_tower_check.py`;
- `experiments/brc_weighted_cwm_safe_quotient_check.py`;
- `experiments/brc_weighted_local_bisimulation_boundary_check.py`;
- `experiments/brc_weighted_cwm_realizability_check.py`;
- `experiments/brc_weighted_projective_gauge_check.py`;
- `experiments/brc_cyclic_log_multiplicity_check.py`;
- `.github/workflows/brc-weighted-research.yml`.

The merged dedicated weighted-BRC research gate passed all listed exact checkers at the cited main-backed generations. Repository-wide unrelated control-plane failures do not alter the mathematical scope frozen above.
