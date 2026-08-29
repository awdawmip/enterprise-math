# Seed-6 Decorated Carrier Pair Stratified Growth — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

- Task-ID: `RS-SEED6-DECORATED-CARRIER-PAIR-STRATIFIED-GROWTH`
- Publication-ID: `TP2-10D797A2B2129C5F0054`
- Researcher-ID: `EM-S6DCG-105931`
- Claim-ID: `chatgpt-s6dcg-20260830-0721`
- Execution record: `ER-1D9EDEBFFB361D2F2C34`
- Execution branch: `research/seed6-decorated-carrier-pair-stratified-growth-em-s6dcg-105931`
- Execution base: `018aceb60cdf3fab64f15631ab7a9aeb94c15d47`
- Hard target: `DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_ATLAS_CLASSIFIED`
- Terminal verdict: `SUCCESS / EXACT_STRATIFIED_ATLAS_WITH_PROFILE_COMPLETENESS`
- Method harvest: `RESULT_ONLY`; no new general-purpose tool family introduced.

## 1. Executive result

The scalar seed is not the state. The exact fresh-growth state is the carrier valuation profile of the decorated pair

\[
\Sigma=(a,b),\qquad a,b>1.
\]

For every prime \(\ell\mid ab\), write

\[
\alpha_\ell=v_\ell(a),\qquad \beta_\ell=v_\ell(b),
\qquad z_\ell=(\alpha_\ell,\beta_\ell).
\]

The central classification result is:

> **The fresh local triangle is an injective linear encoding of the complete carrier valuation profile.**

For a fresh prime \(r\nmid ab\), with row roles ordered as \((ab,ar,br)\), the \(\ell\)-column of the valuation matrix is

\[
u_\ell=(\alpha_\ell+\beta_\ell,\alpha_\ell,\beta_\ell)^T,
\]

and the fresh column is

\[
w=(0,1,1)^T.
\]

Thus \(z_\ell\) is recovered exactly from the second and third coordinates of \(u_\ell\). Consequently:

- \(\Delta_T=\gcd(a,b)^2\) is an exact overlap detector but is **not** a complete overlap type;
- support-only incidence is not complete once valuation thickness is allowed;
- the scalar product \(ab\) is not an operation-safe identity;
- up to prime relabeling and the optional carrier swap, the multiset of valuation pairs \(\{(\alpha_\ell,\beta_\ell)\}\) is the minimal complete typed interface for the task's fresh gcd/lcm/valuation growth;
- if later operations may use non-fresh named primes, the prime labels must be retained as well.

The five required seed strata are all exact, but the overlap stratum has a forced integral refinement: **rank-one common-base overlap** versus **rank-two overlap**. This refinement is visible in the Smith normal form of the local triangle valuation lattice.

The hard target is satisfied.

## 2. `DECORATED_CARRIER_CELL_V1`

### 2.1 Raw operation-safe cell

Define

\[
\mathcal C(\Sigma)=\left(S,\nu_A,\nu_B;\mathsf{slots}\right),
\]

where

- \(S=\operatorname{Supp}(ab)\) is the finite set of named prime carriers;
- \(\nu_A,\nu_B:S\to\mathbb Z_{\ge0}\) are \(\nu_A(\ell)=v_\ell(a)\), \(\nu_B(\ell)=v_\ell(b)\);
- for every \(\ell\in S\), not both values are zero;
- `slots` records the two carrier roles \(A,B\), but no canonical orientation is asserted.

The numerical presentation is derived:

\[
a=\prod_{\ell\in S}\ell^{\nu_A(\ell)},\qquad b=\prod_{\ell\in S}\ell^{\nu_B(\ell)}.
\]

Thus the integers `(a,b)` are a presentation of the cell rather than a replacement for its carrier decomposition.

### 2.2 Typed normalized cell

For role-normalized classification one may quotient by a bijection of the prime set \(S\). If the downstream construction is invariant under swapping the two carrier rows, one may additionally quotient by

\[
(\nu_A,\nu_B)\longleftrightarrow(\nu_B,\nu_A).
\]

This gives the unordered multiset of valuation pairs

\[
\mathcal P(\Sigma)=\left\{\!\left\{(\alpha_\ell,\beta_\ell):\ell\in S\right\}\!\right\}.
\]

This quotient is safe only for normalized typed isomorphism. It is not safe for interaction with a later non-fresh named prime unless the prime labels are restored.

### 2.3 Canonical common-core/excess coordinates

Let

\[
d=\gcd(a,b),\qquad A=a/d,\qquad B=b/d.
\]

Then \(\gcd(A,B)=1\) and

\[
\boxed{\Sigma\longleftrightarrow(d;A,B)}
\]

is lossless. Primewise this is

\[
c_\ell=\min(\alpha_\ell,\beta_\ell),\quad x_\ell=\alpha_\ell-c_\ell,\quad y_\ell=\beta_\ell-c_\ell,
\]

with \(x_\ell y_\ell=0\). Hence the state splits canonically into a common core plus two disjoint excess carriers.

This is the most useful operation-safe coordinate system for the overlap strata.

## 3. Exact local triangle theorem

Let \(r\) be prime with \(\gcd(r,ab)=1\), and

\[
T_r^{a,b}=\{ab,ar,br\}.
\]

Put \(d=\gcd(a,b)\). Then exactly

\[
\gcd(ab,ar)=a,\qquad \gcd(ab,br)=b,\qquad \gcd(ar,br)=rd,
\]

and

\[
\operatorname{lcm}(ab,ar)=abr,\qquad \operatorname{lcm}(ab,br)=abr,
\]

\[
\operatorname{lcm}(ar,br)=\frac{abr}{d}.
\]

Therefore the common-lcm-top property and the old edge-gcd reconstruction property hold iff \(d=1\).

The overlap defect from the accepted predecessor is

\[
\Delta_T=\frac{\left(\gcd(ab,ar)\gcd(ab,br)\gcd(ar,br)\right)^2}{(ab)(ar)(br)}=d^2.
\]

The product identity

\[
(ab)(ar)(br)=(abr)^2
\]

remains a tautological checksum.

## 4. Valuation-profile completeness theorem

Let \(S=\operatorname{Supp}(ab)\). Define the \(3\times(|S|+1)\) valuation matrix \(M_\Sigma(r)\) with row roles \((ab,ar,br)\) and columns indexed by \(S\cup\{r\}\). Then

\[
M_\Sigma(r)=\left[u_\ell\right]_{\ell\in S}\ \big|\ w,
\]

where

\[
u_\ell=\begin{pmatrix}\alpha_\ell+\beta_\ell\\\alpha_\ell\\\beta_\ell\end{pmatrix},\qquad w=\begin{pmatrix}0\\1\\1\end{pmatrix}.
\]

The map

\[
\phi:\mathbb Z^2\to\mathbb Z^3,\qquad (\alpha,\beta)\mapsto(\alpha+\beta,\alpha,\beta)
\]

is injective. In fact, its inverse on the image is simply

\[
(\alpha,\beta)=(u_2,u_3).
\]

Hence the role-labeled local triangle valuation data recovers \(\mathcal P(\Sigma)\) exactly, prime by prime.

### Completeness consequence

Any quotient that identifies two different valuation-pair profiles cannot be faithful for all fresh local valuation/gcd/lcm observables, because the triangle itself separates those profiles.

Therefore the profile is a complete and fieldwise irreducible interface for the task's local fresh-growth category, modulo only explicitly authorized prime relabeling and carrier-row swap.

## 5. General Smith normal form theorem

Let the carrier profile matrix have columns

\[
z_\ell=\begin{pmatrix}\alpha_\ell\\\beta_\ell\end{pmatrix},\qquad C_\Sigma=[z_\ell]_{\ell\in S},
\]

and let

\[
\rho=\operatorname{rank}_{\mathbb Q} C_\Sigma\in\{1,2\}.
\]

For \(\ell,m\in S\), define

\[
D_{\ell m}=\alpha_\ell\beta_m-\beta_\ell\alpha_m.
\]

Define the second determinantal divisor

\[
H=\gcd\left(\{\alpha_\ell+\beta_\ell,\alpha_\ell-\beta_\ell:\ell\in S\}\cup\{D_{\ell m}:\ell<m\}\right).
\]

Because the fresh column \(w\) contains unit entries, the first determinantal divisor is \(1\).

### Rank-one profile

If \(\rho=1\), all \(D_{\ell m}=0\), the triangle valuation lattice has rank \(2\), and

\[
\boxed{\operatorname{SNF}M_\Sigma(r)=\operatorname{diag}(1,H,0).}
\]

### Rank-two profile

If \(\rho=2\), put

\[
D=\gcd_{\ell<m}|D_{\ell m}|>0.
\]

The \(3\times3\) minors using \(u_\ell,u_m,w\) satisfy

\[
\det[u_\ell,u_m,w]=-2D_{\ell m},
\]

while triples containing only \(u\)-columns vanish. Hence the third determinantal divisor is \(2D\), and

\[
\boxed{\operatorname{SNF}M_\Sigma(r)=\operatorname{diag}\left(1,H,\frac{2D}{H}\right).}
\]

This formula is independent of the numerical value of the fresh prime \(r\).

### Coprime specialization

If \(\gcd(a,b)=1\), every profile vector lies on one coordinate axis. Put

\[
g_A=\gcd\{v_\ell(a):\ell\mid a\},\qquad g_B=\gcd\{v_\ell(b):\ell\mid b\},
\]

and \(g=\gcd(g_A,g_B)\). Then

\[
D=g_Ag_B,\qquad H=g,
\]

so

\[
\boxed{\operatorname{SNF}M_\Sigma(r)=\operatorname{diag}\left(1,g,\frac{2g_Ag_B}{g}\right).}
\]

Consequences:

- distinct prime pair: `(1,1,2)`;
- \(a=p^\alpha,b=q^\beta\): \((1,\gcd(\alpha,\beta),2\alpha\beta/\gcd(\alpha,\beta))\);
- coprime squarefree multisupport pairs can still have `(1,1,2)`, so SNF alone does **not** record support cardinality.

## 6. Exact strata atlas

| Stratum | Exact condition | Profile/integral behavior | Representative |
|---|---|---|---|
| `C0_DISTINCT_PRIME_PAIR` | \(d=1\); each side one distinct prime, exponent 1 | Boolean three-atom coatom cell; rank 3; SNF `(1,1,2)` | `(2,3)` |
| `C1_COPRIME_PRIME_POWER_THICK` | \(d=1\); \(a=p^\alpha,b=q^\beta\), \(p\ne q\), at least one exponent \(>1\) | same two-axis support shape, changed thickness; SNF formula above | `(3,4)` |
| `C2_COPRIME_MULTISUPPORT` | \(d=1\); at least one side has >1 prime support | rank 3; support partition is larger; SNF may coincide with C0 | `(2,15)` |
| `O1_OVERLAP_COMMON_BASE_RANK1` | \(d>1,a\ne b,\rho=1\) | triangle valuation lattice rank 2; all valuation pairs lie on one primitive ray | `(4,8)` |
| `O2_OVERLAP_RANK2` | \(d>1,a\ne b,\rho=2\) | triangle valuation lattice rank 3; general `(1,H,2D/H)` signature | `(2,6)` |
| `E_EQUALITY` | \(a=b\) | \(\rho=1\); carrier rows and pairing states coalesce | `(6,6)` |

The required five broad strata are therefore exact, with `OVERLAP` naturally splitting into `O1` and `O2`.

### Characterization of `O1`

If \(\rho=1\), there is a primitive pair \((m,n)\) and integers \(k_\ell\ge1\) such that

\[
(\alpha_\ell,\beta_\ell)=k_\ell(m,n)
\]

for every support prime. Thus for

\[
c=\prod_\ell \ell^{k_\ell}
\]

one has

\[
a=c^m,\qquad b=c^n.
\]

Conversely every such common-base pair has \(\rho=1\). Equality is the special case \(m=n=1\); the distinct common-base cases are the new `O1` sub-stratum.

## 7. `Delta_T=d^2` is not a complete overlap type

`Delta_T` is exact but one-dimensional.

### Counterexample 1: same defect, different support partition

\[
(2,6)\quad\text{and}\quad(6,10)
\]

both have \(d=2\) and therefore \(\Delta_T=4\).

But their carrier profiles are:

\[
(2,6):\quad 2\mapsto(1,1),\ 3\mapsto(0,1),
\]

while

\[
(6,10):\quad 2\mapsto(1,1),\ 3\mapsto(1,0),\ 5\mapsto(0,1).
\]

The first has no \(A\)-exclusive support prime; the second has one exclusive prime on each side.

### Counterexample 2: even defect + support-shape is insufficient

\[
(2,6)\quad\text{and}\quad(4,6)
\]

again have \(d=2\), the same shared-prime / \(B\)-exclusive support shape, but

\[
v_2(2,6)=(1,1),\qquad v_2(4,6)=(2,1).
\]

Their predicted SNFs are respectively

\[
(1,1,2),\qquad (1,1,4).
\]

Thus valuation excess is essential.

### Minimal exact supplement

The canonical lossless supplement to \(d\) is the coprime excess pair

\[
(A,B)=(a/d,b/d),
\]

or, equivalently at the primewise typed level, the full valuation-pair profile. This is not an arbitrary enlargement: the profile is recoverable from the local triangle itself by the injectivity theorem.

## 8. Scalar decomposition ambiguity

The projection

\[
\pi_\times:(a,b)\mapsto ab
\]

is not operation-safe.

Already

\[
12=3\cdot4=2\cdot6
\]

gives

- `(3,4)`: `C1_COPRIME_PRIME_POWER_THICK`;
- `(2,6)`: `O2_OVERLAP_RANK2`.

A stronger three-way collision occurs at

\[
36=4\cdot9=2\cdot18=6\cdot6:
\]

- `(4,9)`: coprime thick;
- `(2,18)`: overlap distinct;
- `(6,6)`: equality.

Therefore scalar identity erases actual stratum, gcd/lcm law, pairing collapse status, and valuation-lattice rank.

The operation-safe representation is a scalar plus a chosen carrier partition, or directly `DECORATED_CARRIER_CELL_V1`.

## 9. Decorated three-pairing cell

Let \(p,q\) be distinct fresh primes with \(\gcd(pq,ab)=1\). Define

\[
P_0=\{ab,pq\},\qquad P_1=\{ap,bq\},\qquad P_2=\{aq,bp\}.
\]

The abstract four-slot perfect-matching object remains standard. The arithmetic decoration is:

\[
\gcd(ab,pq)=1,
\]

\[
\gcd(ap,bq)=\gcd(aq,bp)=d.
\]

For the bridge rectangle

\[
R=\begin{pmatrix}ap&aq\\bp&bq\end{pmatrix},
\]

one has

\[
\gcd(ap,aq)=a,\qquad \gcd(bp,bq)=b,
\]

\[
\gcd(ap,bp)=pd,\qquad \gcd(aq,bq)=qd,
\]

\[
\gcd(ap,bq)=\gcd(aq,bp)=d.
\]

The rank-one product identity

\[
(ap)(bq)=(aq)(bp)
\]

remains tautological.

### Effect of the strata

- `C0/C1/C2`: the three numerical pairing states are distinct; overlap gcd decoration is trivial because \(d=1\).
- `O1/O2`: the three states are still distinct for \(a\ne b\) under freshness, but the two cross states carry nontrivial gcd \(d\), and row/column valuations retain the entire carrier profile.
- `E_EQUALITY`: \(P_1=P_2\); the four rectangle vertices collapse pairwise \(ap=bp\) and \(aq=bq\). Only two numerical states remain.

Freshness is crucial: it prevents accidental cross-row product collisions for distinct carriers.

## 10. Degeneration and forgetful maps

### 10.1 `CORE_EXCESS` — safe and lossless

\[
(a,b)\mapsto(d;A,B)
\]

with \(d=\gcd(a,b)\), \(A=a/d\), \(B=b/d\). This is an isomorphism of data, not a quotient.

### 10.2 Carrier swap — conditionally safe

\[
(a,b)\leftrightarrow(b,a)
\]

is safe for the present unoriented local/set-valued constructions because all laws are \(S_2\)-equivariant. It is unsafe if a future task assigns an oriented operator, port, or boundary role to the two rows. Such orientation must be carried as explicit presentation data.

### 10.3 Squarefree/support projection — support-safe only

Replace each positive valuation by `1`. This preserves support incidence, but not valuation thickness, exact gcd/lcm multiplicities, or SNF.

Example:

\[
(2,3)\quad\text{versus}\quad(4,9)
\]

have the same two-axis support skeleton but SNFs `(1,1,2)` and `(1,2,4)`.

### 10.4 Common-core projection — unsafe as a full state

\[
(d;A,B)\mapsto d
\]

is exactly what `Delta_T` retains. The counterexamples in §7 show that it forgets essential excess support and thickness.

### 10.5 Scalar projection — unsafe

\[
(d;A,B)\mapsto d^2AB=ab.
\]

The examples at scalar `12` and `36` show stratum collapse.

### 10.6 Pairing-state quotient — combinatorially safe, arithmetically unsafe

Forgetting the six product/support objects and retaining only the three-state switch triangle preserves standard perfect-matching combinatorics. It loses gcd decoration, valuation thickness, support typing, and atom/operator-lift information. It must not be used as the operation-safe arithmetic state.

## 11. Exact checker

The standard-library checker:

`research_checks/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_CHECK_20260830.py`

exhaustively verifies all ordered pairs

\[
2\le a,b\le80,
\]

a total of `6241` decorated pairs. For each pair it chooses fresh primes and checks:

- exact gcd/lcm triangle formulas;
- `Delta_T=d^2`;
- lossless common-core/excess coordinates;
- direct valuation matrix versus profile encoding;
- rank and general SNF formula from determinantal divisors;
- all pairing rectangle gcd laws;
- equality iff collapse from three numerical pairing states to two.

Regression summary:

- `6241` ordered pairs checked;
- `121` rank-two triangle valuation lattices;
- `6120` rank-three lattices;
- strata counts:
  - `DISTINCT_PRIME_PAIR`: `462`;
  - `COPRIME_PRIME_POWER_THICK`: `428`;
  - `COPRIME_MULTISUPPORT`: `2882`;
  - `OVERLAP_DISTINCT`: `2390`;
  - `EQUALITY`: `79`;
- both `Delta_T` incompleteness controls pass;
- scalar decomposition ambiguity controls pass;
- representative SNFs pass:
  - `(2,3) -> (1,1,2)`;
  - `(3,4) -> (1,1,4)`;
  - `(4,9) -> (1,2,4)`;
  - `(2,6) -> (1,1,2)`;
  - `(4,6) -> (1,1,4)`;
  - `(4,8) -> (1,1,0)` with valuation-lattice rank `2`;
  - `(6,6) -> (1,2,0)` with rank `2`.

The census is only regression. The core statements are symbolic consequences of the displayed valuation maps and determinantal-divisor calculations.

## 12. Boundary and novelty discipline

This return does **not** claim:

- an additive distance;
- a factor-recovery method or factorization speedup;
- a new perfect-matching theorem;
- a new rank-one determinant identity;
- a Seed-6 uniqueness theorem;
- nontrivial global topology or holonomy.

The standard substrate remains standard: Boolean/coatom incidence in the prime-pair case, perfect matchings of four slots, `J(4,2)`, and rank-one bridge rectangles.

The positive arithmetic residue is precisely:

1. the primewise carrier valuation profile;
2. its common-core/excess decomposition;
3. the exact overlap/equality strata;
4. the forced rank-one/rank-two overlap refinement;
5. the general integral SNF signature `(1,H,2D/H)` or `(1,H,0)`;
6. the proof that profile data are exactly recoverable from the fresh local triangle and therefore cannot be erased by an operation-safe quotient.

## 13. Hard-target disposition

`DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_ATLAS_CLASSIFIED`:

- minimal legal state interface: `PASS`;
- five required strata: `PASS`;
- forced overlap refinement: `PASS`;
- gcd/lcm/support/valuation/SNF classification: `PASS`;
- `Delta_T` completeness audit: `PASS / NOT COMPLETE`;
- minimal supplement and counterexamples: `PASS`;
- scalar decomposition ambiguity: `PASS`;
- decorated pairing cell: `PASS`;
- degeneration/forgetful maps: `PASS`;
- exact finite checker: `PASS`.

Terminal disposition:

`SUCCESS / EXACT_STRATIFIED_ATLAS_WITH_PROFILE_COMPLETENESS`

## 14. Recommended next question

The accepted first-wave global complex is flat when only generic support-faithful columns are glued. This return now supplies the exact arithmetic decoration that was missing.

The highest-value next test is therefore not a larger integer census. It is:

> Glue `DECORATED_CARRIER_CELL_V1` across mixed `O1/O2/E` singular strata while retaining the primewise valuation profile, and determine whether any non-product link, path dependence, or operator-lift holonomy survives after all support-erasure and gauge artifacts are removed.

That question is already aligned with the separately published task `RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING`; no duplicate successor is proposed here.

## Reproducibility

- taskbook: `research_tasks/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_20260830.md`
- checker: `research_checks/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_CHECK_20260830.py`
- summary artifact: `research_artifacts/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH/atlas_summary.json`
