# Seed-6 Bridge Cell Degeneracy Stratification — Research Return

Task: `RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION`  
Publication: `TP2-21F2222D8552EC3071C0`  
Researcher-ID: `EM-S6D-2E4C14`  
Claim: `chatgpt-s6d-20260829-2047-6ea92e`  
Hard target: `SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CLASSIFIED`

## Terminal verdict

**Primary:** `DEGENERATION_SPECTRUM_CLASSIFIED`  
**Secondary:** `PRIME_POWER_FIBER_STRUCTURE_FOUND`

The correct degeneration object is not a one-dimensional severity scale. Three exact mechanisms must be separated:

1. **pairing-state identification** from equalities in the four bundle values `2,3,r,s`;
2. **rectangle-position identification**, with an additional exact `3:2` ratio-resonance stratum;
3. **valuation/support decoration**, which changes gcd/carrier thickness and can occur with unchanged pairing combinatorics.

This gives a natural multi-axis singular stratification and a consistent extension from distinct primes to prime powers and composite bundle columns.

## 1. Reference cell

For positive integers `r,s`, define unordered two-value states

\[
P_0=\{6,rs\},\qquad
P_1=\{2r,3s\},\qquad
P_2=\{2s,3r\}.
\]

All have product `6rs`. Define rectangle positions

\[
A=2r,\quad B=2s,\quad C=3r,\quad D=3s,
\]

so `AD=BC=6rs`. The generic taskbook case is `r=p,s=q` for distinct primes `p,q>3`.

## 2. Complete equality-pattern classification

For an abstract four-atom multiset, quotient the three labeled perfect matchings `(12)(34)`, `(13)(24)`, `(14)(23)` by permutations of equal atoms. The exact count is:

| equality partition | representative | distinct perfect matchings |
|---|---|---:|
| `1+1+1+1` | `{a,b,c,d}` | 3 |
| `2+1+1` | `{a,a,b,c}` | 2 |
| `2+2` | `{a,a,b,b}` | 2 |
| `3+1` | `{a,a,a,b}` | 1 |
| `4` | `{a,a,a,a}` | 1 |

For `{2,3,r,s}`, type `4` is unreachable because `2 != 3`.

## 3. Pairing-state collision theorem

For all positive `r,s`,

\[
P_1=P_2 \iff r=s,
\]

\[
P_0=P_1 \iff (r=3)\lor(s=2),
\]

\[
P_0=P_2 \iff (r=2)\lor(s=3).
\]

Proof: equality of two unordered two-element multisets has only direct and crossed identifications. For example `P0=P1` gives either `6=2r, rs=3s`, hence `r=3`, or `6=3s, rs=2r`, hence `s=2`; the other theorem statements are analogous.

Therefore the number of distinct `P0,P1,P2` states is exactly the perfect-matching count predicted by the equality partition of `{2,3,r,s}`. There is no extra hidden arithmetic state collision.

## 4. The required repeated-atom stratum `p=q`

For `p>3` and `r=s=p`,

\[
P_0=\{6,p^2\},\qquad P_1=P_2=\{2p,3p\}.
\]

Only two state values remain.

The minimal geometry is a **reduced edge** between `P0` and `P*={2p,3p}`. If event history is retained, the generic three-label triangle maps to two parallel `P0-P*` switch events plus a collapsed self-switch at `P*`; those multiplicities are metadata, not justification for retaining a filled 2-cell. Thus the natural state-cell degeneration is `triangle -> edge`, with optional preimage multiplicity decoration.

## 5. Seed collisions

For `q>3`:

- `r=2` gives `P0=P2={6,2q}`, while `P1={4,3q}`.
- `r=3` gives `P0=P1={6,3q}`, while `P2={2q,9}`.

A key point is that these state collapses do **not** force rectangle-vertex collapse: `(4,2q,6,3q)` and `(6,2q,9,3q)` have four distinct values for `q>3`.

For `{r,s}={2,3}` the equality pattern is `2+2`: two pairing states and three rectangle vertices. For `r=s=2` or `r=s=3`, the pattern is `3+1`: all three symbolic states map to one value and the rectangle has two distinct vertices.

## 6. Independent rectangle singularity: exact `3:2` resonance

For `(A,B,C,D)=(2r,2s,3r,3s)`, the number of distinct integer positions is

- `2` iff `r=s`;
- `3` iff `r!=s` and `2r=3s` or `2s=3r`;
- `4` otherwise.

The three-vertex condition is equivalently

\[
(r,s)=(3t,2t)\quad\text{or}\quad(r,s)=(2t,3t),\qquad t\ge1.
\]

Reason: the only possible position equalities are `A=B`/`C=D` from `r=s`, `A=D` from `2r=3s`, and `B=C` from `2s=3r`; vertical equalities would require `2=3`.

Example `(r,s)=(6,4)` has

\[
(P_0,P_1,P_2)=(\{6,24\},\{12,12\},\{8,18\})
\]

as three distinct states, but rectangle `(12,8,18,12)` has only three distinct positions. Hence pairing-state singularity and rectangle-position singularity are genuinely independent.

## 7. GCD/support decoration

Let `d=gcd(r,s)`. The exact six basic gcd labels are

\[
\gcd(A,B)=2d,\quad \gcd(C,D)=3d,\quad
\gcd(A,C)=r,\quad \gcd(B,D)=s,
\]

\[
\gcd(A,D)=\gcd(2r,3s),\qquad
\gcd(B,C)=\gcd(2s,3r).
\]

Prime-by-prime these are valuation minima. For instance

\[
\nu_\ell(\gcd(2r,3s))
=\min(\mathbf 1_{\ell=2}+\nu_\ell(r),\mathbf 1_{\ell=3}+\nu_\ell(s)).
\]

If `gcd(rs,6)=1`, both diagonal gcds equal `d`.

Example `(r,s)=(35,55)` has `d=5`, three pairing states, four rectangle positions, and both diagonal gcds equal `5`. This is a support-overlap decoration without state or position collapse.

## 8. Prime-power fibers

Let `r=p^a,s=q^b` with primes `p,q>3`.

- If `p!=q`, every `a,b>=1` gives 3 states and 4 rectangle positions; exponents alter valuation labels but not matching combinatorics.
- If `p=q` and `a!=b`, there are still 3 states and 4 positions, while the common support thickness is `p^min(a,b)` and both diagonal gcds equal that value.
- If `p=q` and `a=b`, then `r=s`; the cell reaches the equality boundary and becomes 2 states / 2 rectangle positions.

Thus exponent is naturally a **carrier-fiber thickness/radial parameter**. It is not a new perfect-matching dimension. A combinatorial collapse occurs only when valuation vectors become exactly equal. For seed-base powers `2^a` or `3^a`, exponent `1` is an exact seed collision; larger exponent is seed-support overlap unless another equality or ratio condition is imposed.

## 9. Composite columns

For every positive `r`, the outer column `C_r=(2r,3r)` is exact and satisfies `gcd(2r,3r)=r`.

Recommended status:

- prime: atomic carrier column;
- `p^a`, `a>1`: single-support thick column;
- squarefree composite: multi-carrier bundle column;
- mixed composite: multi-carrier thick bundle column;
- `r=1`: unit/boundary control.

Keeping a composite as one outer bundle and expanding it into prime atoms are different models. The stable extension is therefore

`OUTER BUNDLE CELL + PRIMEWISE VALUATION DECORATION`,

not the claim that every composite is a new multiplicative atom.

## 10. Degeneration poset and signatures

The equality-identification backbone is

\[
1+1+1+1 \longrightarrow 2+1+1
\longrightarrow \{2+2,\ 3+1\},
\]

with type `4` unreachable for fixed distinct seed carriers `2,3`.

A useful incidence signature is

\[
(n_P,n_V)
=(\#\text{distinct pairing states},\#\text{distinct rectangle positions}).
\]

Principal strata are:

- generic `(3,4)`;
- ratio resonance `(3,3)`;
- one exact seed collision `(2,4)`;
- repeated external bundle `r=s` `(2,2)`;
- double seed `{r,s}={2,3}` `(2,3)`;
- triple seed `r=s=2` or `r=s=3` `(1,2)`.

Support/valuation data decorates these incidence nodes rather than sitting on the same chain. The three examples

- `(6,4)`: `(3,3)` ratio pinch,
- `(2,5)`: `(2,4)` state collapse,
- `(35,55)`: `(3,4)` with nontrivial gcd support,

prove the axes are non-equivalent.

The correct object is therefore an **identification poset with a valuation/support lattice decoration**, plus the separate ratio-resonance incidence divisor.

## 11. `DEGENERATE_PAIRING_CELL_V1`

A minimal robust definition consists of:

1. symbolic source labels `P0,P1,P2`;
2. their value map to unordered integer pairs;
3. reduced vertices = distinct image states;
4. reduced edges = distinct non-identity images of symbolic matching switches;
5. preimage multiplicity of vertices/switches as decoration;
6. rectangle-position partition of `A,B,C,D` as a separate incidence record;
7. primewise valuation/gcd signature as a separate carrier-thickness record.

This has natural limits: clean primes give three reduced states; `r=s` gives an edge; triple seed collision gives a point; ratio resonance may pinch rectangle positions without reducing pairing states; prime powers and composite overlap thicken valuations without automatically changing incidence.

## 12. Exact census

The checker exhaustively verifies every ordered pair

\[
1\le r,s\le200
\]

for **40,000 cases**, including all primes, all prime powers and small composites in the interval.

Verified totals:

- equality patterns: `1+1+1+1 = 39006`, `2+1+1 = 990`, `2+2 = 2`, `3+1 = 2`;
- pairing-state counts: `3 -> 39006`, `2 -> 992`, `1 -> 2`;
- rectangle-position counts: `4 -> 39668`, `3 -> 132`, `2 -> 200`;
- joint signatures: `(3,4)=38876`, `(3,3)=130`, `(2,4)=792`, `(2,3)=2`, `(2,2)=198`, `(1,2)=2`;
- exact ratio-resonant ordered pairs: `132 = 2*floor(200/3)`;
- primes `<=200`: `46`;
- prime powers `<=200` including primes: `60`;
- prime-power ordered pairs away from seed bases checked: `2401`, split as `2340` different-base, `12` same-base unequal-exponent, `49` same-base equal-exponent.

No counterexample occurred.

Artifacts:

- `research_checks/SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CHECK_20260829.py`
- `research_artifacts/SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION/census_limit_200.json`

## 13. Boundaries

No factorization, endpoint recovery, hidden-factor search or complexity benefit is claimed. The clean three-state object is standard perfect-matching combinatorics at the undecorated level; the contribution here is the exact Seed-6 degeneration/decorated extension. Composite outer bundles and expanded prime-atom models remain distinct. Valuation thickness is not promoted to a metric dimension without a future adjacency definition. The `3:2` stratum is an exact incidence equation, never a numerical-nearness criterion.

## 14. Hard-target audit

A. equality-pattern classification: **PASS**.  
B. `p=q` two-state collapse and cell decision: **PASS**, reduced edge + multiplicity decoration.  
C. seed collisions: **PASS**.  
D. prime-power thickness: **PASS**, valuation fiber with equality boundary.  
E. composite column status: **PASS**, bundle/atomic distinction frozen.  
F. degeneration poset: **PASS**, multi-axis stratification.  
G. exact checker through `<=200`: **PASS**, strengthened to all `r,s<=200`.

**Hard target satisfied at the stated model strength.**
