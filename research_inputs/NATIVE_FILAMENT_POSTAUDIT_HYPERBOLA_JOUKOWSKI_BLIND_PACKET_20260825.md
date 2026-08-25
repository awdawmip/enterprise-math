# Native filament post-audit hyperbola/Joukowski closure — blind replication packet

Status: `BLIND_MATHEMATICAL_REPLICATION_INPUT / STATEMENT_ONLY`

Date: `2026-08-25`

Originating Researcher-ID: `EM-FREE-NEPS-239A6D`

Purpose: independently verify, narrow, or refute the post-audit theorem layer that was discovered after the original V2 package had already passed blind audit.

Do not read source proofs/checkers before freezing the return.

## H1 — split-hyperbola tangent/cover bridge

Work over a field `K` of characteristic not equal to `2`.

Fix `B in K^*`, distinct shifts `d_0,d_1`, and

`Q_i(x)=x^2/(2B)-d_i`, `i=0,1`.

The tangent at `x=-Bu` is

`T_(i,u): y=-u x-Bu^2/2-d_i`.

Let

`C_i=2(d_i-d_(1-i))`.

Claim H1a: for distinct `u,v`, tangents `T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff

`B(w-u)(w-v)=C_i`.

Claim H1b: common values of the negative Legendre-dual images of `Q_i,Q_(1-i)` are represented by pairs `(x,y)` satisfying

`B(y^2-x^2)=C_i`.

Claim H1c: the linear map

`Phi(x,y)=(y-x,y+x)`

is an isomorphism between the dual-overlap representation variety and the split hyperbola

`H_(B,C_i)={(a,b):Bab=C_i}`.

Therefore tangent concurrence and dual-value overlap are two coordinate realizations of the same split-hyperbola torsor.

## H2 — finite-field sign-orbit quotient and breaker bound

Let `K=F_q`, `q` odd, and `B*C !=0`.

Let

`R={(x,y):B(y^2-x^2)=C}`.

The sign group `G={+/-1}^2` acts by independent sign changes.

Claim H2a:

`|R|=q-1`.

Claim H2b: the common dual-value set is naturally identified with `R/G`.

Claim H2c:

`|R/G|=[q+1+Legendre(BC/q)+Legendre(-BC/q)]/4`.

Claim H2d: if a universal breaker is equivalent to `|R/G|=1`, then necessarily

`q<=5`.

The orbit-capacity proof must not depend on the explicit character-sum formula except for classifying the small cases.

## J1 — odd-sector central lane Joukowski map

Fix an odd sector count `s>=3` in the controlled cyclic shell allocator, and work on the central even-shell packet.

For lane index

`j in J_s={-(s-1)/2,...,(s-1)/2}`,

the lane polynomial is

`P_(s,j)(m)=2s m^2+2jm+1`.

For a good prime `q` and nonzero `a=m mod q`, the lane-hit condition may be rewritten as

`j=Lambda_s(a)`,

where

`Lambda_s(a)=-s a-1/(2a)`.

Claim J1a: `Lambda_s` is a Joukowski/Dickson-type quotient map on `F_q^*`.

Claim J1b: for `q` odd, `q∤2s`, its image size is

`|Im Lambda_s|=[q+Legendre(1/(2s),q)]/2`.

Claim J1c: complete central-packet saturation is equivalent to

`Im Lambda_s subseteq J_s` modulo `q`, with equality whenever both sets have the same size.

## J2 — extremal saturation uniqueness

Assume `s>=3` odd.

Lower extremal characteristic:

`q_-(s)=2s-1`.

Claim J2a: if `q_-(s)` is prime and the central packet saturates every nonzero residue modulo `q_-(s)`, then

`(s,q)=(3,5)`.

Upper extremal characteristic:

`q_+(s)=2s+1`.

Claim J2b: if `q_+(s)` is prime and the central packet saturates every nonzero residue modulo `q_+(s)`, then

`(s,q)=(3,7)`.

Claim J2c: hence `s=3` is the unique nontrivial odd-sector parameter saturating both extremal Joukowski boundaries.

The replication should independently reconstruct the argument; do not assume any second-moment identity supplied by the source branch.

## C1 — longitudinal/transverse boundary closure

Let an odd universal breaker be `q_b`, with exact breaker-coprime capacity

`k_*=2q_b-1`.

For odd `k`, let the sharp mixed-parity tangent-product factors be

`k-4`, `k-2`.

The transverse extremal Joukowski boundaries are

`2s-1`, `2s+1`.

Claim C1a: simultaneous boundary closure

`k_*-4=2s-1`,

`k_*-2=2s+1`

is equivalent to

`q_b=s+2`.

Claim C1b: using only the independently established global bound that an odd universal breaker satisfies `q_b<=5`, the unique nontrivial odd-sector solution is

`(s,q_b,k_*)=(3,5,9)`.

Claim C1c: at this solution,

`M_9=(9-4)(9-2)=35`,

`s*M_9=3*35=105`,

and the extremal sampled-tangent obstruction

`s*M_9+1=106`

has terminal odd prime factor `53`.

The replication must distinguish:

- `9` as breaker-coprime capacity in this closure theorem;
- the separate native typed-Cell prime-incidence island cap `9`, which is outside this packet.

## C2 — C3 bouquet coherence

On even shell `r=2m`, the central filament value at `h=0` is

`6m^2+1`.

Claim C2a: slot-unfolding of the native C3 shell gives exactly

`6m^2-2m+1`,
`6m^2+1`,
`6m^2+2m+1`.

Claim C2b: the familiar native `105` bouquet gate and the longitudinal tangent extremum `3*M_9=105` are the same exact integer in the `s=3` closure, not two unrelated fitted constants.

## Required pressure tests

The independent return must include at least:

1. symbolic verification of H1 over generic characteristic-not-2 algebra;
2. finite-field enumeration for H2 across several odd primes, including `q=5,7,13,53`;
3. direct image enumeration for `Lambda_s` for odd `s<=15`, primes through at least `q<=101`;
4. active counterexample search against J2 for odd `s<=101` whenever `2s+-1` is prime;
5. independent derivation of C1 without reading source closure proofs;
6. explicit check that no statement silently promotes breaker-coprime capacity to an unrestricted prime-run theorem.

## Hard target

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`
