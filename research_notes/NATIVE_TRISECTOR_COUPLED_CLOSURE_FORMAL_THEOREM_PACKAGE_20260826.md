# Native tri-sector coupled closure — formal theorem package

Status: `FORMAL_THEOREM_PACKAGE_DRAFT / INDEPENDENTLY_MATH_AUDITED / INDEPENDENTLY_LITERATURE_CLASSIFIED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-26`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent research PR: `#627`

Canonization review brief:
`research_notes/NATIVE_TRISECTOR_COUPLED_CLOSURE_CANONIZATION_REVIEW_BRIEF_20260826.md`.

Canonization decision packet:
`research_notes/NATIVE_TRISECTOR_COUPLED_CLOSURE_CANONIZATION_DECISION_PACKET_20260826.md`.

Mathematical audit authorities:

- original coupled-selection blind audit: PR `#631`, verdict `PACKAGE_VERIFIED_WITH_NARROWING`;
- post-audit hyperbola/Joukowski blind replication: PR `#637`, verdict `POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`.

External-literature authority:

- final narrow independent novelty audit: PR `#642`, package verdict `KNOWN_COMPONENTS_ONLY`;
- maximum allowed literature statement: `NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`.

This file is the compact theorem-facing package. It does not supersede the detailed proof notes or audit returns as provenance. It does supersede pre-audit informal summaries when they conflict with the exact scope frozen here.

---

## 0. Promotion thesis

The research candidate is **not** the standalone mathematics of:

- conic/parabola tangent parametrization;
- split hyperbolas / rank-one tori;
- Burnside or orbit-stabilizer;
- Dickson/Joukowski quotients;
- quadratic-character or value-set formulas.

Those components are classical or immediate corollaries.

The surviving research object is the exact **geometry-selected coupling**:

`native tri-sector allocation`

`-> common scalar s=B=3`

`-> longitudinal breaker channel constrained by a split-hyperbola/sign-orbit readout`

`+ transverse central-lane Joukowski quotient`

`-> unique extremal transverse saturations (3,5) and (3,7)`

`-> unique longitudinal/transverse boundary closure (3,5,9)`

`-> exact arithmetic closure 35,105,53`.

Only this coupled closure is a promotion candidate.

---

# Part I. Controlled odd-sector family

## Definition 1 — odd-sector shell allocator

Let `s>=3` be odd. On shell `r>=1`, use `s` cyclic half-open blocks of length `r`, filled consecutively.

The unique central block is

`sigma_*=(s-1)/2`.

On the admissible central zigzag coordinate

`t=h+ceil(r/2)`,

the label is

`N_s(r)=h+1+(s r^2+eps(r))/2`,

with `eps(r)=r mod 2`.

Hence the odd-curvature coefficient is exactly

`B=s`.

Only `s=3` is current native Enterprise geometry. All other odd `s` are controlled comparator models.

### Authority

Independently verified in the original blind audit `#631`.

---

## Definition 2 — central filament

For positive odd `B`, define

`F_B(H,r)=H+(B r^2+eps(r))/2`.

In the controlled odd-sector family use `B=s`.

For the native specialization:

`B=s=3`.

---

# Part II. Classical support layer

The statements in this part are mathematically exact and required by the main theorem, but are **not** external-novelty claims.

## Lemma A — punctured split-hyperbola tangent bridge

Let `K` be a field with `char(K)!=2`, let `B in K^*`, let `d_0!=d_1`, and put

`C_i=2(d_i-d_(1-i))`.

For

`Q_i(x)=x^2/(2B)-d_i`,

the tangent at `x=-Bu` is

`T_(i,u): y=-u x-Bu^2/2-d_i`.

For `u!=v`,

`T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff

`B(w-u)(w-v)=C_i`.

The negative dual-overlap representation variety is

`R_i={(x,y):B(y^2-x^2)=C_i}`,

and

`Phi(x,y)=(y-x,y+x)`

identifies `R_i` with the full split hyperbola

`H_(B,C_i)={(a,b):Bab=C_i}`.

If

`X_i={(u,v,w):u!=v, B(w-u)(w-v)=C_i}`,

then simultaneous translation of `(u,v,w)` is free and

`X_i / G_a ~= H_(B,C_i) \\ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

Therefore the distinct-tangent quotient is **punctured** hyperbola, not unconditionally the full hyperbola.

### Literature classification

`KNOWN_IMMEDIATE_COROLLARY` in independent audit `#642`.

---

## Lemma B — sign-orbit breaker bound

Let `F_q` be a finite field of odd cardinality and let `B,C in F_q^*`.

For

`R={(x,y):B(y^2-x^2)=C}`,

`|R|=q-1`.

The sign group `G={+/-1}^2` has order four. Hence if the global dual-value quotient has one orbit, then

`q-1<=4`,

so

`q<=5`.

Thus every nonsingular odd universal breaker lies at or below channel `5`.

For arbitrary odd `F_q`, use its quadratic character `chi_q`; literal Legendre notation is restricted to odd prime `q`.

### Literature classification

`KNOWN_IMMEDIATE_COROLLARY` in independent audit `#642`.

---

## Lemma C — central-lane Joukowski quotient

Let `s>=3` be odd and `q` an odd prime with `q∤2s`.

For lane index

`j in J_s={-(s-1)/2,...,(s-1)/2}`,

define

`P_(s,j)(m)=2s m^2+2jm+1`.

For `a in F_q^*`, lane divisibility is equivalent to

`j=Lambda_s(a)`,

where

`Lambda_s(a)=-sa-1/(2a)`.

With

`c=(2s)^(-1)`,

`Lambda_s` is the quotient by the involution

`a -> c/a`.

Hence

`|Im Lambda_s|=[q+Legendre(c,q)]/2`.

The central packet saturates every nonzero residue iff

`Im Lambda_s subseteq J_s (mod q)`.

### Literature classification

`KNOWN_IMMEDIATE_COROLLARY` in independent audit `#642`.

---

# Part III. Research-facing exact theorems

## Theorem 1 — extremal centered-lane saturation uniqueness

Let `s>=3` be odd.

### Lower extremal boundary

If

`q_-=2s-1`

is prime and the central packet saturates every nonzero residue modulo `q_-`, then

`q_- | 75`,

hence

`(s,q_-)=(3,5)`.

### Upper extremal boundary

If

`q_+=2s+1`

is prime and the central packet saturates every nonzero residue modulo `q_+`, then

`q_+ | 21`,

hence

`(s,q_+)=(3,7)`.

Both saturations occur when `s=3`.

Therefore

`TRI-SECTOR s=3 IS THE UNIQUE NONTRIVIAL ODD-SECTOR PARAMETER SATURATING BOTH PRIME EXTREMAL CENTRAL-LANE BOUNDARIES`.

### Mathematical authority

`VERIFIED_EXACT` in blind replication `#637` by an independent second-moment derivation and independent finite pressure tests.

### Literature status

`NO_DIRECT_MATCH_FOUND` in independent audit `#642`.

This is not a priority or publication-originality claim.

---

## Theorem 2 — unique longitudinal/transverse boundary closure

Assume an odd universal breaker `q_b` has exact breaker-coprime capacity

`k_*=2q_b-1`

and satisfies the global bound

`q_b<=5`.

For nontrivial odd `s>=3`, impose simultaneous boundary matching:

`k_*-4=2s-1`,

`k_*-2=2s+1`.

These equations are equivalent to

`q_b=s+2`.

Since `s>=3` and `q_b<=5`, the unique solution is

`(s,q_b,k_*)=(3,5,9)`.

### Mathematical authority

`VERIFIED_EXACT` in blind replication `#637`.

### Literature status

`NO_DIRECT_MATCH_FOUND` in independent audit `#642` for the exact coupling of the two supplied boundary mechanisms.

The algebra after the boundary formulas are supplied is elementary and is not claimed externally deep by itself.

---

## Theorem 3 — native tri-sector coupled closure theorem

Inside the controlled odd-sector comparator family, the native parameter `s=3` is uniquely selected by the simultaneous conditions:

1. its central shell allocator supplies the common scalar `B=s`;
2. the longitudinal universal-breaker mechanism is constrained by Lemma B to `q_b<=5`;
3. its transverse central-lane Joukowski quotient saturates both prime extremal boundaries only at
   `(s,q)=(3,5)` and `(3,7)`;
4. its longitudinal sharp-window capacity and the two transverse extremal boundaries close simultaneously only at
   `(s,q_b,k_*)=(3,5,9)`.

Thus the coupled geometry/arithmetic selection closes uniquely at

`(s,q_b,k_*)=(3,5,9)`.

At this solution,

`M_9=(9-4)(9-2)=35`,

`3M_9=105`,

and

`3M_9+1=106=2*53`.

Hence the exact native closure chain is

`3 -> (5,7) -> 9 -> 35 -> 105 -> 53`,

with the roles separated as follows:

- `3`: native sector count / curvature coefficient;
- `5`: odd universal-breaker terminal channel in the native phase;
- `7`: upper extremal transverse saturation boundary, not a longitudinal breaker;
- `9`: breaker-coprime capacity in this theorem;
- `35`: maximal mixed-parity distance product at the sharp odd window;
- `105`: exact product `3*35`;
- `53`: terminal odd prime factor of the extremal sampled-tangent obstruction `106`.

### Mathematical authority

All ingredients and the closure statement survive independent mathematical audits `#631` and `#637` at the exact narrowed strength stated here.

### Literature status

The full geometry-selected coupled statement is `NO_DIRECT_MATCH_FOUND` in independent theorem-level audit `#642`.

Maximum allowed external wording:

`NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`.

No priority, first-occurrence, or publication-originality claim is made.

---

# Part IV. Native specialization and scope guards

## Corollary 1 — native lane formulas

At `s=3`, the lane set is

`j=-1,0,1`,

and the central even-shell lane values are exactly

`6m^2-2m+1`,

`6m^2+1`,

`6m^2+2m+1`.

The middle lane is the even-shell `h=0` central filament.

---

## Guard G1 — `9` is not an unrestricted prime-run theorem

The `9` in Theorems 2--3 is the exact breaker-coprime capacity

`k_*=2q_b-1`.

It is not by itself an unrestricted prime-run bound.

The separate native typed-Cell theorem on the parent research branch establishes the stronger actual prime-incidence island cap `9` using full native incidence/seam/domain analysis.

These two statements must remain logically distinct.

---

## Guard G2 — `105` is an exact equality, not automatically common provenance

This package certifies

`3M_9=105`.

It also records that an independently defined native bouquet gate has value `105`.

The package may state exact integer coincidence. It may not infer a stronger common historical/genealogical mechanism without an additional native proof.

---

## Guard G3 — `53` is local, not a global breaker

`53` arises as the terminal odd prime factor of the extremal finite-window sampled-tangent obstruction

`3*35+1=106`.

It is not a universal breaker. The global odd breaker bound is `q_b<=5`.

---

## Guard G4 — comparator geometry

Only `s=3` carries the current native Enterprise tri-sector incidence interpretation.

For `s!=3`, this package uses only the controlled odd-sector shell allocator and central-lane arithmetic. It does not claim a canonical `s`-sector Enterprise geometry.

---

# Part V. Dependency DAG

```text
A0  odd-sector shell allocator -> B=s                       [#631 exact]
 |
 +--> A1 central filament / breaker phase                  [#631 exact]
 |     |
 |     +--> B1 split-hyperbola/sign-orbit q_b<=5           [#637 exact; #642 known corollary]
 |
 +--> A2 central lane polynomials P_(s,j)                  [#637 exact]
       |
       +--> B2 Joukowski quotient Lambda_s                 [#637 exact; #642 known corollary]
             |
             +--> T1 lower extremal uniqueness (3,5)       [#637 exact; #642 no direct match]
             +--> T2 upper extremal uniqueness (3,7)       [#637 exact; #642 no direct match]

B1 + breaker-capacity law -> T3 k_*=2q_b-1
T1 + T2 + T3 -> T4 boundary equations
T4 + q_b<=5 -> UNIQUE (s,q_b,k_*)=(3,5,9)                 [#637 exact]
UNIQUE closure -> 35 -> 105 -> 53                         [exact arithmetic]

T1 + T2 + T4 + native A0 -> MAIN COUPLED CLOSURE          [#642 no direct theorem match]
```

---

# Part VI. Audit and prior-art matrix

| Object | Mathematical status | External literature status | Promotion role |
|---|---|---|---|
| Odd-sector provenance `B=s` | independently verified | elementary/classical ingredients | native-selection input |
| Punctured split-hyperbola tangent bridge | independently narrowed/verified | `KNOWN_IMMEDIATE_COROLLARY` | support only |
| Sign-orbit `q<=5` bound | independently verified | `KNOWN_IMMEDIATE_COROLLARY` | support only |
| Joukowski quotient/image size | independently verified | `KNOWN_IMMEDIATE_COROLLARY` | support only |
| Extremal saturation `(3,5),(3,7)` | independently verified | `NO_DIRECT_MATCH_FOUND` | primary candidate theorem |
| Boundary closure `(3,5,9)` | independently verified | `NO_DIRECT_MATCH_FOUND` | primary candidate theorem |
| Full geometry-selected coupling | independently verified at component level and exact closure | `NO_DIRECT_MATCH_FOUND` | primary package candidate |
| `35,105,53` arithmetic | exact | elementary once closure is fixed | corollary / interpretation |

---

# Part VII. Canonization posture

Recommended current status:

`PROMOTION_READY_AS_AUDITED_RESEARCH_THEOREM_PACKAGE`

but

`NOT_YET_CANONICAL_FOUNDATION`.

Reason:

- mathematical statement strength has completed independent audit;
- final narrow literature status has completed independent classification;
- all known classical components are explicitly downgraded;
- remaining decision is institutional: where the theorem package belongs in Enterprise Math and whether it should become a canonical theorem node, a research theorem node, or remain an audited companion to the native-prime line.

No further mathematical proof pass or component-level novelty search is required unless the theorem statement changes or materially stronger prior art is found.
