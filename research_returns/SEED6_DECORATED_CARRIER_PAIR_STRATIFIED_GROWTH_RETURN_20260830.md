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
- Terminal verdict: `SUCCESS`

## 1. Main theorem: the state is the carrier valuation profile

Let `Sigma=(a,b)`, `a,b>1`. For every prime `l|ab`, put

`alpha_l=v_l(a)`, `beta_l=v_l(b)`, `z_l=(alpha_l,beta_l)`.

For a fresh prime `r` (`gcd(r,ab)=1`), order the triangle rows as `(ab,ar,br)`.
The valuation column at `l` is

`u_l=(alpha_l+beta_l, alpha_l, beta_l)^T`

and the fresh column is `w=(0,1,1)^T`.

Therefore the map

`phi(alpha,beta)=(alpha+beta,alpha,beta)`

is injective, with inverse given by the second and third coordinates. Hence the
role-labelled fresh triangle recovers the complete primewise carrier valuation
profile exactly.

This proves that the operation-safe local state is not the scalar `ab`. A raw
`DECORATED_CARRIER_CELL_V1` retains the named prime support and the two valuation
maps `p -> (v_p(a),v_p(b))`. For normalized typed isomorphism, prime names may be
relabelled and the two carrier slots may be swapped only when downstream
operations are S2-equivariant. If later inputs may reuse named, non-fresh
primes, the prime labels must remain.

## 2. Canonical overlap coordinates

Let

`d=gcd(a,b)`, `A=a/d`, `B=b/d`.

Then `gcd(A,B)=1` and

`(a,b) <-> (d;A,B)`

is lossless. Primewise, write

`c_l=min(alpha_l,beta_l)`,
`x_l=alpha_l-c_l`,
`y_l=beta_l-c_l`.

Then `x_l*y_l=0`. Thus every decorated carrier pair splits canonically into a
common core and two disjoint excess carriers.

For `T_r^{a,b}={ab,ar,br}`:

`gcd(ab,ar)=a`,
`gcd(ab,br)=b`,
`gcd(ar,br)=r*d`;

`lcm(ab,ar)=abr`,
`lcm(ab,br)=abr`,
`lcm(ar,br)=abr/d`.

So the common-lcm-top and edge-gcd reconstruction properties hold iff `d=1`.

The accepted predecessor defect satisfies exactly

`Delta_T=d^2`.

It detects whether overlap exists and the exact common gcd, but it is not a
complete overlap type.

## 3. General integral/SNF classification

Let `C_Sigma` be the 2-by-|S| matrix whose columns are
`z_l=(alpha_l,beta_l)^T`, and let `rho=rank_Q(C_Sigma)`.

For support primes `l,m`, define

`D_lm=alpha_l*beta_m-beta_l*alpha_m`.

Define

`H=gcd({alpha_l+beta_l, alpha_l-beta_l}_l union {D_lm}_{l<m})`.

The first determinantal divisor of the triangle valuation matrix is `1` because
the fresh column has unit entries.

If `rho=1`, every `D_lm=0`, the triangle valuation lattice has rank 2, and

`SNF(M_Sigma(r)) = diag(1,H,0)`.

If `rho=2`, put `D=gcd_{l<m}|D_lm|`. The only nonzero 3-by-3 minors are generated
by columns `u_l,u_m,w`, and

`det[u_l,u_m,w] = -2*D_lm`.

Therefore the third determinantal divisor is `2D` and

`SNF(M_Sigma(r)) = diag(1,H,2D/H)`.

This is independent of the numerical fresh prime `r`.

For coprime carriers, put

`g_A=gcd{v_p(a):p|a}`, `g_B=gcd{v_p(b):p|b}`, `g=gcd(g_A,g_B)`.

Then `D=g_A*g_B`, `H=g`, so

`SNF = diag(1,g,2*g_A*g_B/g)`.

Consequences:
- distinct prime pair -> `(1,1,2)`;
- `a=p^alpha`, `b=q^beta` -> `(1,gcd(alpha,beta),2*alpha*beta/gcd(alpha,beta))`;
- coprime squarefree multisupport can also have `(1,1,2)`, so SNF alone does not
  remember support cardinality.

## 4. Exact strata atlas

| Stratum | Exact condition | Structural effect | Example |
|---|---|---|---|
| `C0_DISTINCT_PRIME_PAIR` | `d=1`; one prime on each side, exponent 1 | Boolean 3-atom coatom case; rank 3; SNF `(1,1,2)` | `(2,3)` |
| `C1_COPRIME_PRIME_POWER_THICK` | `d=1`; `p^alpha,q^beta`, at least one exponent >1 | same support skeleton, nontrivial valuation thickness | `(3,4)` |
| `C2_COPRIME_MULTISUPPORT` | `d=1`; at least one side has >1 prime support | larger support partition; SNF may equal C0 | `(2,15)` |
| `O1_OVERLAP_COMMON_BASE_RANK1` | `d>1`, `a!=b`, `rho=1` | triangle valuation lattice rank 2 | `(4,8)` |
| `O2_OVERLAP_RANK2` | `d>1`, `a!=b`, `rho=2` | rank 3 with general `(1,H,2D/H)` | `(2,6)` |
| `E_EQUALITY` | `a=b` | carrier rows and two cross pairing states collapse | `(6,6)` |

Thus the five required broad strata are exact, but `OVERLAP` has a forced
integral refinement into rank 1 and rank 2.

Moreover `rho=1` iff all valuation pairs lie on one primitive ray. Equivalently
there is an integer `c>1` and positive integers `m,n` such that
`a=c^m`, `b=c^n`. Equality is the special `m=n=1` case; distinct common-base
powers form `O1`.

## 5. Why `Delta_T` is incomplete

Same defect, different support geometry:

`(2,6)` and `(6,10)` both have `d=2`, hence `Delta_T=4`, but their valuation
profiles have respectively two and three support primes and different
exclusive-support partitions.

Even defect plus the same support-incidence shape is insufficient:

`(2,6)` and `(4,6)` both have `d=2`; both have shared prime `2` and a
B-exclusive prime `3`. But the shared valuation pairs are `(1,1)` and `(2,1)`,
and their SNFs are `(1,1,2)` and `(1,1,4)`.

The minimal exact supplement to `d` is therefore the coprime excess pair
`(A,B)=(a/d,b/d)`, equivalently the complete valuation-pair profile. This
supplement is not ad hoc: the fresh local triangle itself recovers it.

## 6. Scalar decomposition ambiguity

The projection `(a,b) -> ab` is unsafe.

Already

`12=3*4=2*6`

places `(3,4)` in the coprime-thick stratum and `(2,6)` in overlap.

At scalar 36 there is a three-way collapse:

`36=4*9=2*18=6*6`,

giving respectively coprime-thick, overlap-distinct, and equality states.

Thus scalar identity loses stratum, gcd/lcm law, valuation-lattice rank, and
pairing-collapse status. An operation-safe representation is a scalar plus a
chosen carrier partition, or directly `DECORATED_CARRIER_CELL_V1`.

## 7. Decorated three-pairing cell

For fresh distinct primes `p,q`, define

`P0={ab,pq}`, `P1={ap,bq}`, `P2={aq,bp}`.

The abstract three perfect matchings remain standard. The arithmetic decoration
is

`gcd(ab,pq)=1`,
`gcd(ap,bq)=gcd(aq,bp)=d`.

For the bridge rectangle `[[ap,aq],[bp,bq]]`:

`gcd(ap,aq)=a`,
`gcd(bp,bq)=b`,
`gcd(ap,bp)=p*d`,
`gcd(aq,bq)=q*d`,
`gcd(ap,bq)=gcd(aq,bp)=d`.

The rank-one identity `(ap)(bq)=(aq)(bp)` remains tautological.

For `a!=b`, freshness keeps all three numerical pairing states distinct.
For `a=b`, `P1=P2` and rectangle rows collapse pairwise. Overlap and valuation
thickness do not alter the standard matching combinatorics; they alter the
arithmetic decoration that must be retained.

## 8. Forgetful/degeneration maps

1. `CORE_EXCESS: (a,b)->(d;A,B)` is lossless and safe.
2. Carrier swap is safe only for S2-equivariant, unoriented downstream work.
3. Replacing positive valuations by 1 is safe only for support incidence; it
   loses thickness and SNF. Example: `(2,3)` vs `(4,9)`.
4. `(d;A,B)->d` is the `Delta_T` quotient and is unsafe as a full state.
5. `(d;A,B)->d^2*A*B=ab` is scalarization and is unsafe.
6. Forgetting the six typed product/support objects to the three-state matching
   triangle is safe for standard switch combinatorics only; it loses gcd,
   valuation, support, and lift data.

## 9. Exact checker

`research_checks/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_CHECK_20260830.py`

uses only the Python standard library and checks all 6241 ordered pairs
`2<=a,b<=80`, choosing fresh primes for each pair. It verifies the symbolic
gcd/lcm formulas, `Delta_T=d^2`, lossless common/excess coordinates, direct
valuation encoding, the general SNF formula from determinantal divisors, all
pairing gcd laws, and equality collapse.

Observed regression counts:
- 6241 ordered pairs;
- 121 rank-2 triangle valuation lattices;
- 6120 rank-3 lattices;
- broad strata: 462 distinct-prime, 428 coprime-thick, 2882 coprime
  multisupport, 2390 overlap-distinct, 79 equality.

Required counterexamples and representative SNFs all pass. The finite census is
a regression certificate only; the core result is symbolic.

## 10. Boundaries and disposition

No additive distance, factor-recovery objective, factorization-performance
claim, new perfect-matching theorem, new rank-one identity, Seed-6 uniqueness,
or global topology/holonomy claim is made.

The positive arithmetic residue is the valuation profile, its common/excess
decomposition, the exact strata, the forced rank-1/rank-2 overlap refinement,
and the general SNF signature.

Hard target:
`DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_ATLAS_CLASSIFIED` = `SATISFIED`.

Recommended next step: consume this exact decoration in the already-published
`RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING` task and test whether mixed
`O1/O2/E` gluing creates any intrinsic non-product link, path dependence, or
operator-lift holonomy after support-erasure and gauge artifacts are excluded.

Reproducibility:
- checker: `research_checks/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_CHECK_20260830.py`
- summary: `research_artifacts/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH/atlas_summary.json`
