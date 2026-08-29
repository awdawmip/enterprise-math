# Seed-6 Bridge Cell Degeneracy Stratification — Research Return

Task: `RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION`  
Publication: `TP2-21F2222D8552EC3071C0`  
Researcher-ID: `EM-S6D-2E4C14`  
Claim: `chatgpt-s6d-20260829-2047-6ea92e`  
Owner branch: `research/seed6-bridge-cell-degeneracy-stratification-em-s6d-2e4c14`  
Hard target: `SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CLASSIFIED`

## 0. Terminal verdict

**Primary return:** `DEGENERATION_SPECTRUM_CLASSIFIED`  
**Secondary positive structure:** `PRIME_POWER_FIBER_STRUCTURE_FOUND`

The Seed-6 degeneration spectrum is not controlled by one scalar notion of singularity. Three exact mechanisms must be separated:

1. **pairing-state identification**, controlled by equality of the four bundle values `2,3,r,s`;
2. **bridge-rectangle vertex identification**, which has an additional `3:2` ratio-resonance stratum even when all pairing states remain distinct;
3. **valuation/support decoration**, controlled prime-by-prime by valuation vectors and gcd data, usually without changing the pairing-state count.

This separation is the main structural result. It supplies a natural reduced-state cell, a degeneration adjacency diagram, and a valuation-decorated extension to prime powers and composites without turning the construction into a factorization claim.

---

## 1. Reference model

For positive bundle labels `r,s`, define three unordered pairing states

\[
P_0(r,s)=\{6,rs\},\qquad
P_1(r,s)=\{2r,3s\},\qquad
P_2(r,s)=\{2s,3r\}.
\]

Every state has common product `6rs`.

Define the bridge-rectangle positions

\[
A=2r,\quad B=2s,\quad C=3r,\quad D=3s,
\]

so that `AD=BC=6rs`.

The clean taskbook model is recovered by `r=p`, `s=q` with distinct primes `p,q>3`.

---

## 2. Complete four-atom equality-pattern classification

For an abstract multiset of four atoms, the equality partition types and numbers of distinct unordered perfect matchings are:

| equality partition | representative multiset | distinct perfect matchings |
|---|---|---:|
| `1+1+1+1` | `{a,b,c,d}` | 3 |
| `2+1+1` | `{a,a,b,c}` | 2 |
| `2+2` | `{a,a,b,b}` | 2 |
| `3+1` | `{a,a,a,b}` | 1 |
| `4` | `{a,a,a,a}` | 1 |

Proof is direct from the three labeled pairings `(12)(34)`, `(13)(24)`, `(14)(23)` after quotienting permutations of equal atoms.

For the Seed-6 multiset `{2,3,r,s}`, the `4` stratum is unreachable because `2 != 3`. The remaining types occur exactly as follows:

- `1+1+1+1`: `r,s` are distinct and neither is `2` or `3`;
- `2+1+1`: one equality only, e.g. `r=s` away from `2,3`, or exactly one external bundle equals a seed carrier;
- `2+2`: `(r,s)=(2,3)` or `(3,2)`;
- `3+1`: `(r,s)=(2,2)` or `(3,3)`.

This equality partition already predicts the number of distinct pairing states exactly.

---

## 3. Pairing-state collision theorem

### Theorem 3.1
For positive integers `r,s`,

\[
P_1=P_2 \iff r=s,
\]

\[
P_0=P_1 \iff (r=3)\ \text{or}\ (s=2),
\]

\[
P_0=P_2 \iff (r=2)\ \text{or}\ (s=3).
\]

### Proof
For two-element multisets, equality has only the direct and crossed identifications.

For `P1=P2`, either `2r=2s` and `3s=3r`, giving `r=s`, or the crossed equations `2r=3r`, `3s=2s`, impossible for positive `r,s`.

For `P0=P1`, either

- `6=2r` and `rs=3s`, giving `r=3`, or
- `6=3s` and `rs=2r`, giving `s=2`.

The `P0=P2` statement is symmetric.

### Corollary 3.2 — exact state count
The number of distinct states among `P0,P1,P2` is exactly the number of distinct perfect matchings of the multiset `{2,3,r,s}`:

- `3` iff all four values are distinct;
- `2` for equality types `2+1+1` and `2+2`;
- `1` for `3+1` in the Seed-6 universe.

Thus no hidden arithmetic collision among these three product states occurs beyond equality of the bundle values themselves.

---

## 4. The required `p=q` degeneration

Let `p>3` and set `r=s=p`. Then

\[
P_0=\{6,p^2\},\qquad
P_1=P_2=\{2p,3p\}.
\]

Exactly two state values remain.

### Cell decision
There are three sensible quotients, but only one is minimal without adding event-history data:

1. **Reduced-state model:** identify equal state values and deduplicate identity/parallel switches. The cell becomes a single **edge** between `P0` and `P*={2p,3p}`.
2. **Labeled-event quotient:** retain symbolic labels `P1` and `P2` even after their values coincide. The generic triangle maps to a quotient with two parallel `P0-P*` switch events and one self-loop at `P*`.
3. **Weighted-history decoration:** use the reduced edge as geometry, but record preimage multiplicity `(1,2)` and the collapsed-switch multiplicities as metadata.

The canonical recommendation is **(1) + optional multiplicity decoration (3)**. A filled two-dimensional triangle is not justified by only two distinct state values; calling the quotient a genuine 2-cell would preserve dimension by notation rather than incidence.

Hence the natural state geometry degenerates `triangle -> edge` at `p=q`, while a multiplicity certificate remembers how the generic three-label cell approached the edge.

---

## 5. Seed collisions `r=2` and `r=3`

For external `q>3`:

### `r=2`

\[
P_0=\{6,2q\}=P_2,\qquad
P_1=\{4,3q\}.
\]

The reduced pairing cell has two states.

The bridge rectangle still has four different integer vertices

\[
(4,2q,6,3q),
\]

so **pairing-state collapse occurs without rectangle-vertex collapse**.

Its six basic gcd labels are

\[
(\text{top},\text{bottom},\text{left},\text{right},\text{diag}_{AD},\text{diag}_{BC})
=(2,3,2,q,1,2).
\]

### `r=3`
Similarly,

\[
P_0=P_1=\{6,3q\},\qquad P_2=\{2q,9\},
\]

with gcd labels `(2,3,3,q,3,1)`.

### Double seed collision
For `(r,s)=(2,3)` or `(3,2)`, the atom pattern is `2+2`, there are two pairing states, and the rectangle has three distinct integer vertices because one diagonal ratio resonance also occurs.

### Triple collision
For `(r,s)=(2,2)` or `(3,3)`, the atom pattern is `3+1`; all three symbolic pairing states map to one value. The reduced pairing cell is a point, while the bridge rectangle has two distinct integer vertices.

---

## 6. A second singularity: rectangle `3:2` ratio resonance

Pairing-state equality does **not** exhaust bridge-cell degeneration.

### Theorem 6.1 — rectangle vertex collision
For

\[
(A,B,C,D)=(2r,2s,3r,3s),
\]

the number of distinct integer vertices is:

- `2` iff `r=s`;
- `3` iff `r!=s` and either `2r=3s` or `2s=3r`;
- `4` otherwise.

The three-vertex case is equivalently

\[
(r,s)=(3t,2t)\quad\text{or}\quad(r,s)=(2t,3t),\qquad t\ge1.
\]

### Proof
The only possible position equalities are

- `A=B` and `C=D`, both equivalent to `r=s`;
- `A=D`, equivalent to `2r=3s`;
- `B=C`, equivalent to `2s=3r`.

Vertical equalities `A=C` or `B=D` would require `2=3`. The two cross-ratio equalities cannot both hold for positive `r,s`, and neither can coexist with `r=s`.

### Example showing independence from pairing collapse
Take `(r,s)=(6,4)`:

\[
(P_0,P_1,P_2)=\bigl(\{6,24\},\{12,12\},\{8,18\}\bigr)
\]

are three distinct states, but

\[
(A,B,C,D)=(12,8,18,12)
\]

has only three distinct integer vertices.

Therefore `PAIRING_STATE_SINGULARITY` and `RECTANGLE_POSITION_SINGULARITY` are independent coordinates of the degeneration spectrum.

For `1<=r,s<=200`, the checker finds exactly `132` ordered ratio-resonant pairs, matching

\[
2\lfloor 200/3\rfloor=132.
\]

---

## 7. Exact gcd/support decoration

Let `d=gcd(r,s)`. The bridge rectangle has exact gcd labels

\[
\gcd(A,B)=2d,\qquad \gcd(C,D)=3d,
\]

\[
\gcd(A,C)=r,\qquad \gcd(B,D)=s,
\]

\[
\gcd(A,D)=\gcd(2r,3s),\qquad
\gcd(B,C)=\gcd(2s,3r).
\]

Prime-by-prime, if `a_l=nu_l(r)` and `b_l=nu_l(s)`, then for example

\[
\nu_l(\gcd(2r,3s))
=\min(\mathbf 1_{l=2}+a_l,\mathbf 1_{l=3}+b_l).
\]

All other gcd labels are obtained by the same `min` rule. Therefore valuation data is a complete exact certificate for the gcd-support decoration.

### Seed-free overlap
If `gcd(rs,6)=1`, then

\[
\gcd(2r,3s)=\gcd(2s,3r)=d.
\]

Thus partial common support `d>1` changes the gcd decoration while leaving the three pairing states and usually all four rectangle vertices distinct.

Example `(r,s)=(35,55)` has `d=5`:

- three distinct pairing states;
- four distinct rectangle vertices;
- diagonal gcds both equal `5`;
- horizontal gcds `10` and `15`.

This is a **support-overlap-only singular decoration**, not a state collapse.

---

## 8. Prime-power columns and exponent thickness

Let

\[
r=p^a,\qquad s=q^b,
\]

with primes `p,q>3`.

### Case 8.1 — different prime bases `p!=q`
Then `gcd(r,s)=1`. For every `a,b>=1`:

- three pairing states;
- four rectangle vertices;
- diagonal gcds `1`;
- horizontal labels `2,3`;
- vertical labels `p^a,q^b`.

After forgetting exponent labels, the combinatorial cell is the same as the clean prime case. Exponents are therefore **thickness/radial coordinates inside carrier fibers**, not new matching types.

### Case 8.2 — same base, unequal exponents
Let `p=q>3`, `a!=b`, and `m=min(a,b)`. Then

- `r!=s`, so all three pairing states remain distinct;
- all four rectangle vertices remain distinct;
- common support is `p^m`;
- both diagonal gcds equal `p^m`;
- horizontals are `2p^m,3p^m`.

This gives a genuine valuation-thickened overlap stratum with unchanged pairing combinatorics.

### Case 8.3 — same base, equal exponents
If `a=b`, then `r=s=p^a` and the cell hits the equality boundary:

- pairing states `3 -> 2`;
- rectangle vertices `4 -> 2`.

### Verdict on prime powers
`PRIME_POWER_FIBER_STRUCTURE_FOUND`: exponent data creates a valuation hierarchy, but it is a fiber thickness, not a new perfect-matching combinatorial dimension. The combinatorial change occurs when valuation vectors become exactly equal, not merely because an exponent exceeds one.

Seed-base powers `2^a` or `3^a` further confirm the distinction: `a=1` is an exact seed collision, while `a>1` is only seed-support overlap unless another equality or ratio resonance is imposed.

---

## 9. Composite columns: atomic vs bundle status

For arbitrary positive `r`, the column

\[
C_r=(2r,3r)
\]

always satisfies

\[
\gcd(2r,3r)=r.
\]

So a mathematically exact **bundle column** exists for every `r`.

But the word **atomic** should be reserved:

| `r` type | recommended structural status |
|---|---|
| prime | atomic carrier column |
| `p^a`, `a>1` | single-support thick column |
| squarefree composite with >=2 primes | multi-carrier bundle column |
| mixed composite | multi-carrier thick bundle column |
| `1` | boundary/unit control |

Treating a composite bundle as one outer column is compatible with the three-state re-pairing formulas. Expanding it into its prime atoms is a strictly finer model with additional internal matchings. These are not the same equivalence relation.

Therefore the natural extension is:

`OUTER BUNDLE CELL + PRIMEWISE VALUATION DECORATION`,

not the assertion that every composite is a new multiplicative atom.

This choice preserves a stable outer Seed-6 cell while keeping internal carrier structure explicit and prevents a silent change of model.

---

## 10. Degeneration adjacency / poset structure

A single scalar severity order is not natural because three different identifications can occur independently. The useful finite **identification poset** is generated by exact equations, while support data lives on a valuation lattice decorating each node.

### 10.1 Equality-partition backbone

\[
1+1+1+1 \longrightarrow 2+1+1
\longrightarrow \{2+2,\ 3+1\}.
\]

`4` is formally present in the full four-atom partition lattice but unreachable with fixed distinct seed carriers `2,3`.

### 10.2 Principal Seed-6 identification signatures

Use the pair

\[
(n_P,n_V)
=(\text{number of distinct pairing states},\text{number of distinct rectangle vertices}).
\]

The principal strata are:

- generic: `(3,4)`;
- ratio resonance `(r,s)=(3t,2t)` or `(2t,3t)`, `t>1`: `(3,3)`;
- one exact seed collision: `(2,4)`;
- repeated external bundle `r=s` away from seed values: `(2,2)`;
- double seed `{r,s}={2,3}`: `(2,3)`;
- triple seed `r=s=2` or `r=s=3`: `(1,2)`.

In the exhaustive `1..200` census the joint signature distribution is:

- `(3,4)`: `38876`;
- `(3,3)`: `130`;
- `(2,4)`: `792`;
- `(2,3)`: `2`;
- `(2,2)`: `198`;
- `(1,2)`: `2`.

The unit boundary contributes some `(2,2)` and `(2,4)` examples but does not alter the classification.

### 10.3 Why this is not one chain

- `(6,4)` lies in `(3,3)`: vertex pinch without pairing collapse.
- `(2,5)` lies in `(2,4)`: pairing collapse without vertex pinch.
- `(35,55)` lies in `(3,4)` combinatorially but has nontrivial support-overlap gcd decoration.

Hence ratio resonance, equality identification, and support overlap are pairwise non-equivalent. The correct degeneration object is a **multi-axis stratification**:

`IDENTIFICATION POSET x VALUATION/SUPPORT DECORATION`,

with equality and ratio equations controlling incidence quotients and valuation vectors controlling carrier thickness/gcd labels.

---

## 11. Reduced cell proposal

Define `DEGENERATE_PAIRING_CELL_V1(r,s)` by:

1. symbolic source labels `P0,P1,P2`;
2. value map from each label to its unordered integer pair;
3. reduced vertex set = distinct image states;
4. reduced switch relation = non-identity image of a symbolic matching switch, deduplicated as a simple edge;
5. preimage multiplicity of each reduced state and switch retained as decoration;
6. rectangle-position partition of `A,B,C,D` retained separately;
7. primewise valuation/gcd signature retained separately.

This definition has the required natural limits:

- clean distinct primes -> three-state pairing triangle candidate;
- `r=s` -> reduced edge;
- `r=s=2` or `3` -> point;
- ratio resonance -> pairing state set may remain three while rectangle-position partition pinches;
- prime-power/composite support overlap -> same reduced combinatorics with thicker valuation decoration unless equality/resonance is reached.

It therefore avoids the failure mode of forcing every degeneration to preserve an artificial two-dimensional visual cell.

---

## 12. Exact checker and census

Checker:

`research_checks/SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CHECK_20260829.py`

Machine-readable census:

`research_artifacts/SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION/census_limit_200.json`

The checker uses only exact integer arithmetic and standard-library factorization/gcd logic.

It exhaustively verifies all ordered pairs

\[
1\le r,s\le 200,
\]

for `40,000` cases, including all primes, prime powers and small composites in that range.

Verified facts include:

- the three pairwise state-collision iff conditions;
- perfect-matching count equals equality-partition prediction;
- rectangle vertex-count theorem;
- all gcd-label formulas;
- prime-power fiber claims;
- support-overlap-only example `(35,55)`;
- ratio-resonance example `(6,4)`;
- exact resonance count `2 floor(200/3)=132`.

Census summary:

- equality pattern `1+1+1+1`: `39006`;
- `2+1+1`: `990`;
- `2+2`: `2`;
- `3+1`: `2`;
- pairing states: `3 -> 39006`, `2 -> 992`, `1 -> 2`;
- rectangle vertices: `4 -> 39668`, `3 -> 132`, `2 -> 200`;
- primes `<=200`: `46`;
- prime powers `<=200` including primes: `60`;
- prime-power ordered pairs checked away from seed bases: `2401`.

No checker counterexample was found.

---

## 13. Boundaries and non-claims

1. No factorization, endpoint recovery, hidden-factor search or complexity benefit is claimed.
2. The three-state clean object is standard perfect-matching combinatorics at the undecorated level; the present contribution is the exact Seed-6 degeneration/decorated extension, not novelty of the three perfect matchings themselves.
3. Composite bundle columns and expanded prime-atom columns are different models; this return does not silently identify them.
4. Valuation thickness is not promoted to a new geometric dimension without an explicit future definition of adjacency/metric along exponent directions.
5. The `3:2` ratio-resonance stratum is an exact arithmetic incidence singularity, not a numerical-nearness phenomenon.

---

## 14. Task-target audit

- **A complete equality-pattern classification:** PASS.
- **B `p=q` exact two-state collapse and cell decision:** PASS; reduced edge + multiplicity decoration.
- **C seed collisions:** PASS.
- **D prime-power exponent thickness:** PASS; valuation fiber, equality boundary at equal exponents.
- **E composite columns:** PASS; bundle/atomic distinction frozen.
- **F degeneration poset/adjacency:** PASS; equality-identification backbone plus ratio-resonance axis and valuation lattice.
- **G exact checker through `<=200`:** PASS; stronger exhaustive `r,s<=200` census.

Hard target `SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CLASSIFIED` is satisfied at the stated model strength.
