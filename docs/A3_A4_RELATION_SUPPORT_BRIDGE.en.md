# A3 ↔ A4 Relation-Support Bridge — Stage 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: first proved generator from A3 weighted relation states to A4 admissible support families  
Source homes: A3 `research/core/relation-quotient`; A4 `research/core/admissible-support-relations`

## 1. Why this bridge is not an identification

A3 and A4 remain different structures.

- A3 stores an integer present-state relation field
  \[
  Z_{ij}=m_jc_i-m_ic_j,
  \]
  where `m_i>0` is block capacity and `c_i` is the block total.
- A4 stores a finite multivalued support relation
  \[
  R_r\subseteq X\times X
  \]
  and composes supports relationally.

This note proves a **generator** from A3 to one restricted class of A4 families. It does not claim that every A4 relation arises from an A3 state.

## 2. A3 weighted closure

For every closed A3 field,

\[
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.
\]

Using antisymmetry,

\[
\boxed{m_jZ_{ik}=m_kZ_{ij}+m_iZ_{jk}}.
\]

Therefore

\[
\boxed{
m_j|Z_{ik}|\le m_k|Z_{ij}|+m_i|Z_{jk}|.
}
\]

This is an integer weighted triangle inequality. No division or hidden real-valued density is required.

## 3. Zero-relation quotient

Define

\[
i\sim_0 j\iff Z_{ij}=0.
\]

Because capacities are positive and the weighted closure holds, `~_0` is an equivalence relation:

- reflexive: `Z_ii=0`;
- symmetric: antisymmetry;
- transitive: if `Z_ij=Z_jk=0`, then weighted closure gives `m_j Z_ki=0`, hence `Z_ki=0`.

Let

\[
X_0=X/{\sim_0}.
\]

This quotient is essential. On raw A3 blocks, radius zero would relate distinct blocks having the same capacity-normalized state. On `X_0`, radius zero can become the A4 identity relation.

## 4. Bridge theorem B01 — A3 generates an A4 admissible support family

For integer `r>=0`, define on zero-relation classes

\[
\boxed{
[i]R_r[j]
\iff
|Z_{ij}|\le r m_i m_j.
}
\]

### B01a — representative independence

If `i~_0 i'` and `j~_0 j'`, then the truth value of

\[
|Z_{ij}|\le r m_i m_j
\]

is unchanged after replacing `i,j` by `i',j'`.

Equivalently, the cross-multiplied normalized relation magnitude is constant on zero-relation classes. This follows from the weighted closure with `Z_(ii')=0` and `Z_(jj')=0`.

### B01b — zero identity

On `X_0`,

\[
R_0=I.
\]

Indeed, `[i]R_0[j]` iff `Z_ij=0` iff `[i]=[j]`.

### B01c — monotonicity

If `r<=s`, then

\[
R_r\subseteq R_s.
\]

### B01d — relational subadditivity

If

\[
[i]R_r[j],\qquad [j]R_s[k],
\]

then

\[
|Z_{ij}|\le r m_i m_j,
\qquad
|Z_{jk}|\le s m_jm_k.
\]

The weighted triangle inequality gives

\[
m_j|Z_{ik}|
\le
m_k r m_im_j+m_i s m_jm_k.
\]

Since `m_j>0`, exact integer cancellation yields

\[
|Z_{ik}|\le(r+s)m_im_k.
\]

Hence

\[
\boxed{R_r;R_s\subseteq R_{r+s}.}
\]

Therefore the A3 state canonically generates an A4-admissible radius family on `X_0`.

## 5. What this bridge means

A3's weighted relation coordinate can be read operationally: `r` is an integer tolerance budget on capacity-normalized relational difference. A4 support then means that two zero-distinct quotient states fit within that declared budget.

This is a genuine bridge because the A4 relation is derived entirely from A3 integer data, while its composition law is supplied by the A3 weighted closure identity.

It is **not** an ontology claim that every support/collision relation should be generated this way.

## 6. Bridge theorem B02 — universal fine support descends through an A3 partition quotient

Let fine blocks be grouped into two coarse blocks `A,B`. A3 quotient gives

\[
Z'_{AB}=\sum_{i\in A,j\in B}Z_{ij},
\qquad
m'_A=\sum_{i\in A}m_i,
\qquad
m'_B=\sum_{j\in B}m_j.
\]

Assume every fine cross pair is `r`-supported:

\[
|Z_{ij}|\le r m_i m_j
\quad
\text{for all }i\in A,j\in B.
\]

Then

\[
|Z'_{AB}|
\le
\sum_{i,j}|Z_{ij}|
\le
r\sum_{i,j}m_im_j
=
r m'_A m'_B.
\]

Thus

\[
\boxed{
(\forall i\in A,j\in B:\ iR_rj)
\Longrightarrow
A R'_r B.
}
\]

This is a one-way quotient compatibility theorem.

## 7. Negative boundary B03 — coarse support does not recover fine support

The converse of B02 is false.

Take unit capacities and totals

\[
(c_0,c_1,c_2,c_3)=(0,10,0,10),
\]

with coarse groups

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

The four fine cross relations are

\[
0,-10,10,0,
\]

so

\[
Z'_{AB}=0.
\]

Hence the coarse blocks are radius-0 supported, while several fine cross pairs are not radius-0 supported.

Therefore

\[
\boxed{
A R'_r B
\not\Longrightarrow
\forall i\in A,j\in B:\ iR_rj.
}
\]

The obstruction is signed cancellation inside the A3 quotient.

## 8. Consequence for A2/P018/P023

B03 gives a precise interpretation of hidden refinement information:

> coarse support can be a legal coarse observable without being a certificate of universal fine support.

If a future operation/query requires fine support witnesses, the coarse A3 quotient is not sufficient merely because the coarse support predicate is true. The required refinement must be decided by the A2/P023 future-compatibility criterion.

This is the first direct three-way bridge:

\[
\boxed{
A3\ \text{relation state}
\longrightarrow
A4\ \text{support observable}
\longrightarrow
A2\ \text{future-sufficiency test}.
}
\]

## 9. Current classification

- A3 → A4 threshold-support construction: `GENERATOR`.
- A3 partition quotient → A4 support: one-way `SPECIALIZATION / LAX COMPATIBILITY`, not an isomorphism.
- coarse-support ⇒ universal-fine-support: `CONFLICT / NEGATIVE_BOUNDARY` by B03.
- A3 and unrestricted A4: still `COMPOSABLE_INDEPENDENT`; no equivalence is claimed.

## 10. Executable reference

- `src/enterprise_math/relation_support_bridge.py`
- `tests/test_relation_support_bridge.py`

The executable layer checks zero-class formation, representative independence, radius-zero identity, monotonicity, relational subadditivity, B02, and the B03 cancellation counterexample.
