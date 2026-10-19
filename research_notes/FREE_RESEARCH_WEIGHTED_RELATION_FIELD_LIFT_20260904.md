# Free Research — Weighted Relation-Field Lift of the Quotient Cloud

Status: `FREE_RESEARCH_FRONTIER / ACCEPTED_TOOL_COMPOSITION / MINIMAL_INFORMATION_BOUNDARY_CLOSED / PRIMITIVE_MIXER_REALIZATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_S3_PROVENANCE_MIXING_GAP_20260904.md`

## 1. Executive advance

The current exact BRC branch denotation is Boolean support.  Exact recoalescence replaces a live configuration by the literal union of its supports.  That operation is lossless for reachability, but it cannot recover a uniform or weighted average over ordered histories after multiplicities have been erased.

This checkpoint proves the corresponding no-go and then reuses the already accepted T8 capacity-weighted relation-field carrier as the minimal sufficient extension.

The result is an exact dichotomy:

\[
\boxed{
\text{support union, even with branch count, is insufficient;}
\qquad
\text{grand total plus internal relation field is sufficient.}
}
\]

No new general-purpose tool family is introduced.  Reuse status:

- `T0_BRC`: exact support/recoalescence semantics;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: the `S_3` transposition action;
- `T8_RELATION_OBSERVABLE_SPECTRUM`: capacity-weighted relation field.

Classification: `COMPOSE_APPLIED`.

---

## 2. Support-only averaging no-go

Encode a list of Boolean point histories as singleton exact branches.  Consider

\[
B=(0,0,0,1,1,1)
\]

and

\[
K=(0,0,0,0,0,1).
\]

They have the same support

\[
\{0,1\}
\]

and the same branch count `6`, but their multiplicity-sensitive true counts are `3` and `1`.  Thus their uniform Boolean averages are different.

Consequently there is no decoder

\[
D:(\text{support},\text{branch count})\longrightarrow\text{uniform-average numerator}
\]

that works for all finite branch lists.  In particular, exact union recoalescence identifies these configurations and cannot later reconstruct their average.

This is formalized in

- `EnterpriseMath/Relation/BranchAverageNoGo.lean`.

The proof is an immediate application of the existing `NO_RESURRECTION` theorem.

The scope is precise.  A raw list of live branches may still retain multiplicity before recoalescence.  What fails is recovery from the canonical Boolean denotation or from the exactly recoalesced union token.

---

## 3. Capacity-weighted relation field

For finite blocks indexed by `i`, let

\[
m_i>0
\]

be their capacities and

\[
c_i
\]

be their carried totals.  Define

\[
\boxed{
Z_{ij}=m_jc_i-m_ic_j.
}
\tag{3.1}
\]

This is the accepted weighted relation field.  It satisfies

\[
Z_{ji}=-Z_{ij}
\tag{3.2}
\]

and the exact weighted closure law

\[
\boxed{
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.}
\tag{3.3}
\]

Let

\[
M=\sum_{j\in S}m_j,
\qquad
C=\sum_{j\in S}c_j,
\qquad
R_i=\sum_{j\in S}Z_{ij}.
\]

Then

\[
R_i=Mc_i-m_iC,
\]

hence

\[
\boxed{
Mc_i=m_iC+R_i.
}
\tag{3.4}
\]

If `M` is nonzero,

\[
\boxed{
c_i=\frac{m_iC+R_i}{M}.}
\tag{3.5}
\]

Therefore capacities, the grand total, and the relation-row sums reconstruct every block total exactly.

This is the positive counterpart to the support no-go: the internal relation field is sufficient because it stores precisely the information lost by union recoalescence.

---

## 4. Quotient-cloud specialization

For the quotient endpoint cloud, take

\[
m_a=u_a,
\qquad
x_a=f(q_a(n)),
\qquad
c_a=u_ax_a.
\]

Then

\[
\boxed{
Z_{ab}=u_au_b(x_a-x_b).
}
\tag{4.1}
\]

Pairing the relation field with the endpoint difference gives

\[
\mathcal E_Z
:=\sum_{a,b}Z_{ab}(x_a-x_b)
=\sum_{a,b}u_au_b|x_a-x_b|^2.
\tag{4.2}
\]

For

\[
U=\sum_a u_a,
\]

the weighted quotient-cloud variance is therefore

\[
\boxed{
\Gamma_S(f;n)=\frac{\mathcal E_Z}{2U}.
}
\tag{4.3}
\]

The ordered cubic curvature energy from the preceding checkpoint satisfies

\[
\boxed{
\mathcal C_{3,S}(f;n)=U\mathcal E_Z=2U^2\Gamma_S(f;n).
}
\tag{4.4}
\]

Thus the three descriptions are exactly the same finite object:

\[
\boxed{
\text{ordered cubic curvature}
\equiv
\text{weighted internal relation-field energy}
\equiv
\text{quotient-cloud variance}.
}
\]

---

## 5. The `S_3` mixer as relation-field annihilation

A fully averaged block state has

\[
c_i=m_i\bar x.
\]

Substituting into (3.1) gives

\[
\boxed{Z_{ij}=0.}
\tag{5.1}
\]

The uniform transposition mixer on the six ordered histories sends the closing-edge readout to its common mean in one step.  In the relation-field language it therefore annihilates the internal field exactly.

The gap-one standard-sector dissipation is the disappearance of `Z`, while the grand total and common support remain unchanged.

This gives an exact finite realization at the state-description level.  It does not yet prove that current primitive deterministic operations generate the convex transposition mixer dynamically.

---

## 6. Minimal state boundary

The combined formal results establish:

### Insufficient state

\[
(\text{union support},\text{branch count})
\]

cannot recover history weights or means.

### Sufficient state

\[
(\text{capacities }m_i,\text{ grand total }C,\text{ relation field }Z_{ij})
\]

recovers all block totals and therefore all weighted means and fluctuations.

Accordingly, the minimal viable native extension is not an arbitrary probability layer.  It is the existing capacity/total/relation triple already recognized by T8.

What must remain live until polarization is the internal relation field.  After its energy has been read, all histories may recoalesce to the common endpoint.

---

## 7. Formal status

Lean files:

- `EnterpriseMath/Relation/BranchAverageNoGo.lean`;
- `EnterpriseMath/Relation/WeightedQuotientRelationField.lean`.

The first proves the support and exact-recoalescence no-go.  The second proves:

1. antisymmetry and weighted three-block closure;
2. row-sum recovery of all block totals;
3. quotient-cloud relation formula;
4. equality with pair curvature energy;
5. nonnegativity for nonnegative capacities;
6. equality with quotient-cloud variance;
7. equality with ordered cubic curvature energy;
8. annihilation under full averaging.

Lean-green status is not claimed until the branch workflow succeeds.

---

## 8. Updated next target

The state-carrier problem is closed.  The remaining dynamic question is:

> Can the accepted weighted relation field be transported by an allowed branch operation whose induced action on every three-history fiber is the transposition projector `M_3`, or must convex mixing be added as an explicit weighted-branch primitive?

For prime distribution, the analytic question is now equivalently:

> Can the arithmetic dynamics force the normalized internal relation-field energy
> \[
> \mathcal E_Z/U
> \]
> to decay at a quantitative rate before product-label recoalescence?

A proof would yield a native remainder mechanism.  The current real-smoothing PNT theorem remains valid independently.
