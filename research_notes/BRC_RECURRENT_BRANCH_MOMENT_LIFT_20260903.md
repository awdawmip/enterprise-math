# BRC Recurrent Branch-Moment Lift

Status: `RESEARCH CANDIDATE / EXACT EXPLICIT-BRANCH RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent Foundation: `WBRC-T01..T32`

## 1. Problem

Finite-DAG CWM stores

\[
(C,W,M)
\]

= path count, total positive mass and dominant path mass. In recurrent graphs the all-depth count `C` becomes infinite as soon as supported recurrence exists, while total mass may still converge. This breaks the finite CWM count coordinate.

The repair is not to discard multiplicity. It is to keep **walk length** and lift the explicit branch carrier through integer power sums.

Power sums, moment/partition functions, transfer matrices, Renyi-type quantities and thermodynamic formalism are classical/general mathematics. No generic novelty claim is made for them. The Enterprise Math contribution proposed here is the exact typed branch-semiring/recurrent synthesis and its relation to the existing CWM/Weighted-BRC Foundation.

## 2. Explicit branch carrier is required

Let every directed branch `e:i->j` have a positive rational weight

\[
q_e\in\mathbb Q_{>0}.
\]

Parallel branches remain distinct. The aggregated total-mass matrix

\[
W^{(1)}_{ij}=\sum_{e:i\to j}q_e
\]

is **not** enough to reconstruct the new family: higher power sums depend on the explicit branch decomposition.

This is an intentional provenance boundary, consistent with the previously frozen CWM-loss boundary of recurrent Schur collapse.

## 3. Branch moment character

For every integer

\[
m\ge0,
\]

define the power-sum character of a finite positive branch family `Q={q_1,...,q_r}` by

\[
\boxed{
P_m(Q)=\sum_{j=1}^r q_j^m.
}
\]

Use `q^0=1` for every supported positive branch.

Thus

\[
P_0(Q)=r,
\qquad
P_1(Q)=\sum_jq_j.
\]

### Candidate BRC-M1 — semiring character

Let `Q union R` be alternative/recoalesced branch families and let

\[
Q\times R=\{qr:q\in Q,r\in R\}
\]

be serial branch composition. Then

\[
\boxed{P_m(Q\sqcup R)=P_m(Q)+P_m(R)},
\]

\[
\boxed{P_m(Q\times R)=P_m(Q)P_m(R)}.
\]

Therefore every integer `m>=0` is an exact homomorphic projection of the explicit positive branch semiring into non-negative rational sum-product mass.

The special slices are:

```text
m=0 -> branch multiplicity/count
m=1 -> ordinary positive total mass
m->infinity (after 1/m root) -> dominant branch mass
```

## 4. Moment transition matrices

For a finite explicit weighted directed multigraph, define

\[
\boxed{
W^{(m)}_{ij}
=\sum_{e:i\to j}q_e^m.
}
\]

Then:

\[
W^{(0)}_{ij}=\#\{e:i\to j\},
\]

and

\[
W^{(1)}=W
\]

is the current total-mass transition matrix.

### Candidate BRC-M2 — exact length-n path moments

For every `n>=0`,

\[
\boxed{
\left(W^{(m)}\right)^n_{ij}
=
\sum_{\substack{p:i\to j\\|p|=n}}
\operatorname{wt}(p)^m.
}
\]

The proof is the usual matrix-path expansion together with the semiring character law:

\[
\prod_{e\in p}q_e^m
=\left(\prod_{e\in p}q_e\right)^m.
\]

Thus every fixed integer moment is handled by the already canonical finite recurrent positive-mass machinery.

## 5. CWM recovered coefficientwise by length

Fix source `i`, target `j`, and length `n`. Let the finite family of supported length-n path weights be

\[
w_1,\ldots,w_C.
\]

Define

\[
S_m=\left(W^{(m)}\right)^n_{ij}=\sum_{r=1}^Cw_r^m.
\]

Then exactly

\[
\boxed{C=S_0},
\]

\[
\boxed{W=S_1},
\]

and, with `M=max w_r`,

\[
\boxed{
M^m\le S_m\le C M^m
}
\]

for every positive integer `m`. Hence

\[
\boxed{
M\le S_m^{1/m}\le C^{1/m}M
}
\]

and therefore

\[
\boxed{
M=\lim_{m\to\infty}S_m^{1/m}.
}
\]

So the old finite CWM triple is the `(m=0,m=1,m=infinity)` boundary of one moment family, **provided walk length is fixed**.

This explains why recurrent all-depth count fails: recurrence destroys the finite all-length aggregation, not the coefficientwise CWM semantics.

## 6. Moment multiplicity surplus at fixed length

For `m>=1` and live length-n paths, define

\[
E_m=\frac{S_m}{M^m}
=\sum_r\left(\frac{w_r}{M}\right)^m.
\]

Then

\[
1\le E_m\le C.
\]

The normalized log gap

\[
\boxed{
\Delta_m^{(n)}
=\frac1m\ln E_m
}
\]

satisfies

\[
0\le\Delta_m^{(n)}\le\frac{\ln C}{m}.
\]

At `m=1`, this is exactly the existing finite-path recoalescence surplus

\[
\ln(W/M).
\]

As `m->infinity`, the normalized surplus tends to zero and the dominant path remains.

This is a discrete exact-integer version of the earlier temperature/tropical bridge; no continuous temperature parameter is required for the exact core.

## 7. Length-fugacity generating star

Introduce a positive length marker/fugacity `z`. For every moment order `m`, define

\[
\boxed{
G_m(z)
=\sum_{n\ge0}z^n\left(W^{(m)}\right)^n.
}
\]

Whenever the positive matrix `zW^(m)` is stable,

\[
\boxed{
G_m(z)=(I-zW^{(m)})^{-1}.
}
\]

For rational `z>0`, every entry remains exact rational and the entire current recurrent Foundation `WBRC-T12..T32` can be applied to the scaled matrix `zW^(m)`.

Even outside the analytic stable region, `(I-zW^(m))^-1` remains the formal rational generating matrix whenever interpreted algebraically/formally rather than as a convergent positive sum. The current BRC stability semantics must not conflate these two interpretations.

## 8. Exact count generating function

At `m=0`,

\[
W^{(0)}=N
\]

is the integer branch-count adjacency matrix. Thus

\[
\boxed{
G_0(z)=(I-zN)^{-1}
}
\]

is the ordinary exact walk-count generating matrix in the stable/formal sense.

At `z=1`:

\[
\boxed{
N^*=I+N+N^2+\cdots
\text{ is finite}
\iff
\text{the supported directed multigraph is acyclic}.
}
\]

Therefore the old statement “recurrent path count is infinite” becomes a sharper typed statement:

> all-depth count at fugacity 1 diverges on supported recurrence, but each fixed-length coefficient is finite and the whole count sequence has a finite rational generating representation in `z`.

## 9. Exact critical polynomial at every moment

For fixed `m`, choose a common denominator `D_m` and write

\[
W^{(m)}=A_m/D_m.
\]

Under length scale `z`, define

\[
\boxed{
p_m(z)=\det(D_mI-zA_m)\in\mathbb Z[z].}
\]

This is exactly the existing recurrent criticality polynomial `WBRC-T21` applied to the m-th branch-moment lift.

If the moment support is acyclic, `p_m(z)=D_m^n` and every non-negative `z` is stable. Otherwise the positive convergence endpoint is the smallest positive real root of `p_m`.

At rational stable `z`, no numerical root is needed: the star, loop zeta, response and feedback calculus are all exact rational.

## 10. One-state branch family

For one recurrent state with explicit positive loops

\[
q_1,\ldots,q_k,
\]

the moment matrix is the scalar

\[
\boxed{S_m=\sum_{i=1}^kq_i^m}.
\]

Hence

\[
G_m(z)=\frac1{1-zS_m}
\]

and the exact length-fugacity critical value is

\[
\boxed{z_{c,m}=1/S_m}.
\]

For equal loops `q_i=q`,

\[
S_m=kq^m
\]

so

\[
\boxed{z_{c,m}=\frac1{kq^m}}.
\]

The derived log critical exponent is

\[
\boxed{
-\ln z_{c,m}
=\ln k+m\ln q.
}
\]

This extends the existing `ln k` interpretation: equal branch multiplicity contributes one exact additive `ln k` term to every moment-order recurrent length exponent.

At `m=1,z=1`, stability is precisely

\[
\ln k+\ln q<0,
\]

the previously frozen equal-loop law.

## 11. Moment phase separation

Moment stability can differ by order.

Example: two equal loops

\[
q_1=q_2=3/5.
\]

Then

\[
S_1=6/5>1,
\]

so ordinary total mass diverges at `z=1`, but

\[
S_2=18/25<1,
\]

so the squared-mass closure converges.

Thus “total mass unstable” does not imply every positive power-sum observable is unstable. The moment family distinguishes multiplicity-driven divergence from stronger individual-path growth.

No probability or statistical-moment interpretation is implied.

## 12. Provenance/nonrecoverability boundary

The total-mass matrix `W^(1)` does not determine the moment family.

One port pair may carry:

- one explicit branch of mass `1`;
- two explicit branches of mass `1/2` each.

Both have

\[
W^{(1)}=1,
\]

but

\[
W^{(0)}=1\text{ versus }2,
\]

and

\[
W^{(2)}=1\text{ versus }1/2.
\]

Hence no total-mass-only quotient — including recurrent Schur port collapse — can reconstruct the branch-moment hierarchy after explicit branch provenance has been erased.

This is a stronger form of the existing CWM/provenance loss boundary.

## 13. Relation to CWM and recurrent Foundation

The typed hierarchy is now:

```text
explicit positive branch carrier
-> moment matrices W^(m), m=0,1,2,...
-> fixed-length path power sums (W^(m))^n
-> length-fugacity stars (I-zW^(m))^-1
```

with special readings:

```text
m=0 : exact multiplicity/count coefficients
m=1 : canonical total positive mass
m->infinity at fixed length : dominant path mass
```

Every finite integer m and rational z in its stable region can reuse the current exact recurrent BRC theorem/tool stack. `m=infinity` remains a limit/tropical interpretation, not a finite rational carrier.

## 14. Prior-art boundary

Power sums, transfer matrices, walk generating functions, Renyi/partition-function ideas, thermodynamic formalism and tropical large-power limits are classical/general mathematics.

Enterprise Math does not claim those generic constructions as novel.

The project-specific reusable synthesis proposed here is the typed exact bridge

\[
\boxed{
(C,W,M)
\leftrightarrow
\{W^{(m)}\}_{m\ge0}
\text{ coefficientwise in walk length}
}
\]

and the observation that the existing finite rational recurrent BRC machinery applies independently to every integer moment lift.

## 15. Boundaries

This candidate does not claim:

- that aggregated `W^(1)` determines explicit branch moments;
- a probability interpretation of `q_e`;
- a finite all-depth path-count coordinate on recurrent graphs at `z=1`;
- that stability is monotone in `m` without extra weight assumptions;
- a new continuous-temperature theory;
- that the `m->infinity` limit is itself an exact finite-rational BRC state;
- novelty of generic moment/transfer-matrix mathematics.

## 16. Validation plan

Use explicit branch lists and exact `Fraction` arithmetic.

1. Exhaust small branch families with weights `{1/2,1,2}` and moment orders `m=0..4`; verify recoalescence and serial-product semiring character identities.
2. On a fixed three-state multigraph with parallel rational branches, explicitly enumerate all walks of lengths `0..4` and verify path m-power sums equal `(W^(m))^n` for `m=0..5`.
3. For every tested fixed-length path family verify `S_0=C`, `S_1=W`, and `M^m<=S_m<=C M^m`.
4. Verify equal-weight path families saturate the upper bound; one dominant-only path saturates the lower bound.
5. Verify the aggregated-mass nonrecoverability witness: one branch `1` vs two branches `1/2`.
6. Verify count generating behavior: a DAG has finite `G_0(1)` equal to exact finite path-count closure; a directed cycle diverges at `z=1` but is stable at a rational `z` below criticality.
7. Verify one-state equal-loop law `z_c,m=1/(kq^m)` for several `m` and exact critical polynomials.
8. Verify the `3/5,3/5` moment phase separation: `m=1` unstable, `m=2` stable.

A dedicated research CI gate must pass before any Foundation backflow.
