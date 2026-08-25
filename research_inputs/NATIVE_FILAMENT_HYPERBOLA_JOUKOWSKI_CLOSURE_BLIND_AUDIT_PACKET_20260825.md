# Native filament hyperbola/Joukowski closure — blind mathematical-audit packet

Status: `BLIND_AUDIT_INPUT / STATEMENT_ONLY / NO_SOURCE_PROOFS`

Date: `2026-08-25`

Originating Researcher-ID: `EM-FREE-NEPS-239A6D`

Audit objective:
`HYPERBOLA_JOUKOWSKI_CROSS_ROUTE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`.

Do not read PR #627 or branch `research/native-filament-generalization-theorem-package-20260824` before freezing the audit return.

Classical tools may be used freely; this task is mathematical correctness, not novelty.

## H1. Split-hyperbola tangent/dual bridge

Let `K` be a field of characteristic not2. Fix `B!=0` and distinct shifts `d_0,d_1`. Put

`Q_i(x)=x^2/(2B)-d_i`,

`C_i=2(d_i-d_(1-i))`.

The tangent to `Q_i` at `x=-Bu` is

`T_(i,u): y=-u x-Bu^2/2-d_i`.

For distinct same-family indices `u,v` and an opposite-family index `w`:

`T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff

`B(w-u)(w-v)=C_i`.

The common negative Legendre-dual value condition is

`-Q_i^*(x)=-Q_(1-i)^*(y)`

iff

`B(y^2-x^2)=C_i`.

The linear map

`Phi(x,y)=(a,b)=(y-x,y+x)`

is an isomorphism between this representation curve and

`H_(B,C_i): Bab=C_i`.

Verdict target: exact / narrow / refute.

## H2. Intrinsic K4 quotient and breaker orbit theorem

Over `F_q`, q odd, `BC!=0`, let

`H={(a,b):Bab=C}`.

Define

`S(a,b)=(b,a)`,

`R(a,b)=(-a,-b)`.

They generate `K4~=C2xC2`.

For the branch with shift `d_i`, define

`pi_i(a,b)=-B(b-a)^2/8-d_i`.

Claim:

1. the fibers of `pi_i` are exactly the K4 orbits;
2. `H/K4` is naturally identified with the common negative-dual value set `I_i intersect I_(1-i)`;
3. `|H(F_q)|=q-1`;
4. universal breaking is equivalent to `|H/K4|=1`;
5. therefore a nonsingular odd universal breaker must satisfy `q<=5` purely from `q-1<=|K4|=4`.

For native `B=3,C=+/-1`:
- q=5 gives one regular four-point K4 orbit;
- q=53 gives 52 points and13 K4 orbits.

## H3. Odd-sector transverse lane-label Joukowski theorem

Let `s>=1` be odd and use the central even-shell s-slot packet

`P_(s,j)(m)=2s m^2+2j m+1`,

`j=-(s-1)/2,...,(s-1)/2`.

For odd prime `q` with `q` not dividing `2s`, put the same carrier hyperbola

`sab=-1`,

and set `a=m`.

Claim:

`P_(s,j)(a)=0`

iff

`j=Lambda_s(a)`,

where

`Lambda_s(a)=-s a-1/(2a)`

`=-s(a+kappa/a)`, `kappa=1/(2s)`.

Hence for `q>s`, packet saturation of all nonzero `m` classes is equivalent to

`Im Lambda_s subseteq J_s`,

where `J_s` is the s lane-label set.

The image size is

`|Im Lambda_s|=[q+Legendre(kappa,q)]/2`.

Consequently saturation implies:
- if `kappa` is square, `q<=2s-1`;
- if `kappa` is nonsquare, `q<=2s+1`.

The lane fiber count is

`|Lambda_s^(-1)(j)|=1+Legendre(j^2-2s,q)`.

For native `s=3`:
- q=5 gives fibers `1:2:1` on lanes `-1,0,+1`;
- q=7 gives `2:2:2`;
- q=3 is a degenerate coefficient boundary with transverse pattern `1:0:1`.

## H4. Extremal Joukowski saturation uniqueness

Let `s>=3` be odd.

### lower boundary

If `q=2s-1` is prime and the s-slot packet saturates all nonzero residues modulo q, then

`q|75`,

hence necessarily

`(s,q)=(3,5)`.

### upper boundary

If `q=2s+1` is prime and the packet saturates all nonzero residues modulo q, then

`q|21`,

hence necessarily

`(s,q)=(3,7)`.

Thus s=3 is the unique nontrivial odd-sector model saturating both extremal Joukowski image-size boundaries.

The intended proof may use second moments of the image and the centered lane set, but the auditor should derive independently.

## H5. C3 bouquet / central-filament identity and 3/5/7 orbit decomposition

For native `s=3`, on even shell `r=2m` and central transverse coordinate `h=0`, the central filament value is

`c=6m^2+1`.

Unfolding the three sector slots gives exactly

`c-r, c, c+r`

`=6m^2-2m+1, 6m^2+1, 6m^2+2m+1`.

Modulo3/5/7, the lane root multiplicities are respectively

`1:0:1`,

`1:2:1`,

`2:2:2`.

For q=5, the one regular K4 breaker orbit projects under `m=y-x` to all four nonzero residues and partitions by sign Hamming weight as `1:2:1` across the three lanes.

For q=7, the six-point hyperbola splits into one regular size4 orbit contributing `1:2:1` and one ramified size2 orbit contributing `1:0:1`, totaling `2:2:2`.

## H6. Odd-sector gate theorem and native minimum-gate selection

For general odd s, every odd prime `q<=s` is an automatic saturation gate for the central s-slot packet.

For `q>s`, lane root sets are disjoint and the total bad-residue count is

`omega_s(q)=s+sum_(j in J_s) Legendre(j^2-2s,q)`.

No additional saturation prime can exceed `2s+1`.

Let `G_s` be the product of all saturated odd prime channels.

Claims:
- for every odd `s>=3`, `G_s>=105`;
- `G_s=105` iff `s in {3,5,7}`;
- among these equality cases, first longitudinal breakers are respectively `5,2,3`, so only s=3 attains the latest finite breaker5.

## H7. Unique longitudinal/transverse boundary closure

Let `q_b` be an odd universal breaker and let its breaker-coprime capacity be

`k_*=2q_b-1`.

For odd k, the maximal mixed-parity tangent-distance product factors as

`(k-4)(k-2)`.

The two transverse Joukowski image-size boundaries are

`2s-1,2s+1`.

Claim: for nontrivial odd `s>=3`, exact boundary matching

`k_*-4=2s-1`,

`k_*-2=2s+1`

has the unique solution

`(s,q_b,k_*)=(3,5,9)`.

Hence native:

`(k_*-4,k_*-2)=(5,7)=(2s-1,2s+1)`,

`3*(9-4)*(9-2)=105`,

and the terminal sampled-tangent obstruction satisfies

`105+1=106=2*53`.

This is an exact coherence claim, not a claim that the different proofs are identical.

## H8. Scope / required verdict

For H1--H7 assign one of:

- `VERIFIED_EXACT`;
- `VERIFIED_WITH_NARROWING`;
- `DEPENDENCY_GAP`;
- `REFUTED_COUNTEREXAMPLE`.

Actively test:
- q=3,5,7 and q=13 controls;
- negative/zero lane labels;
- s=3,5,7,9,11,13 and larger odd s;
- boundary cases q=2s-1 and q=2s+1;
- whether K4 fibers really coincide with common-dual values;
- whether any statement silently confuses breaker-coprime capacity with unrestricted prime-run length.

No novelty judgment is required in this audit.