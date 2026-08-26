# Post-audit hyperbola/Joukowski V2 statement freeze

Status: `AUTHORITATIVE_POST_REPLICATION_STATEMENT_LAYER / FREE_RESEARCH / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Authority for statement strength:
- blind replication PR `#637`;
- independent Researcher-ID `EM-POSTHJ-EE1141`;
- verdict `POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`.

This file supersedes any stronger pre-replication wording in the post-audit hyperbola/Joukowski notes.

## Theorem A — split-hyperbola duality and distinct-tangent bridge

Let `K` be a field with `char(K)!=2`, let `B in K^*`, let `d_0!=d_1`, and put

`C_i=2(d_i-d_(1-i))`.

Define

`Q_i(x)=x^2/(2B)-d_i`,

and let `T_(i,u)` be the tangent at `x=-Bu`:

`T_(i,u): y=-u x-Bu^2/2-d_i`.

For `u!=v`,

`T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff

`B(w-u)(w-v)=C_i`.

The negative algebraic Legendre-dual maps are

`L_i(t)=-Bt^2/2-d_i`.

Their common-value representation variety is exactly

`R_i={(x,y):B(y^2-x^2)=C_i}`.

The linear map

`Phi(x,y)=(a,b)=(y-x,y+x)`

is an isomorphism

`R_i ~= H_(B,C_i)`,

where

`H_(B,C_i)={(a,b):Bab=C_i}`.

Now let

`X_i={(u,v,w):u!=v, B(w-u)(w-v)=C_i}`.

Simultaneous translation

`(u,v,w)->(u+t,v+t,w+t)`

acts freely, and

`X_i / G_a ~= H_(B,C_i) \ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

Therefore:

- dual-overlap representations use the full split hyperbola;
- distinct-tangent concurrence modulo translation uses the split hyperbola with its diagonal points removed;
- the two are equal on `K`-points iff `Delta_i(K)=empty`;
- if repeated tangents are explicitly admitted, the diagonal is restored.

Freeze:

`DISTINCT TANGENT BRIDGE = PUNCTURED SPLIT HYPERBOLA`,

not an unqualified full-torsor identity.

## Theorem B — finite-field sign quotient

Let `F_q` be a finite field of odd cardinality, let `B,C in F_q^*`, and let `chi_q` be its quadratic character.

For

`R={(x,y):B(y^2-x^2)=C}`,

we have

`|R|=q-1`.

The independent sign group

`G={+/-1}^2`

acts on `R`, and

`|R/G|=[q+1+chi_q(BC)+chi_q(-BC)]/4`.

If `C=2(d_0-d_1)`, the quotient is canonically the common negative-dual-value set of the two shifted quadratics.

If `|R/G|=1`, then the complete `q-1` point hyperbola is one orbit of a group of order `4`, so

`q-1<=4`,

hence

`q<=5`.

This breaker terminal bound is independent of the explicit character-sum formula.

For odd prime `q`, `chi_q` may be written as the Legendre symbol.

## Theorem C — central-lane Joukowski quotient

Let `s>=3` be odd and let `q` be an odd prime with `q∤2s`.

For the central lane family

`P_(s,j)(m)=2s m^2+2jm+1`,

put

`Lambda_s(a)=-sa-1/(2a)`, `a in F_q^*`.

Then

`P_(s,j)(a)=0`

iff

`j=Lambda_s(a)`.

Let

`c=(2s)^(-1)`.

The map `Lambda_s` is exactly the quotient by the involution

`a -> c/a`.

Its fibers are the involution orbits, and

`|Im Lambda_s|=[q+Legendre(c,q)]/2`.

The central packet saturates every nonzero residue modulo `q` iff

`Im Lambda_s subseteq J_s (mod q)`,

where

`J_s={-(s-1)/2,...,(s-1)/2}`.

When the two sets have equal cardinality, saturation is equality.

## Theorem D — extremal Joukowski saturation uniqueness

Let `s>=3` be odd.

If

`q_-=2s-1`

is prime and the lower extremal central packet saturates every nonzero residue, then

`q_- | 75`,

hence

`(s,q_-)=(3,5)`.

If

`q_+=2s+1`

is prime and the upper extremal central packet saturates every nonzero residue, then

`q_+ | 21`,

hence

`(s,q_+)=(3,7)`.

Both saturations occur at `s=3`.

Therefore

`TRI-SECTOR s=3 IS THE UNIQUE NONTRIVIAL ODD-SECTOR PARAMETER SATURATING BOTH PRIME EXTREMAL JOUKOWSKI BOUNDARIES`.

## Theorem E — longitudinal/transverse boundary closure

Assume an odd universal breaker `q_b` has exact breaker-coprime capacity

`k_*=2q_b-1`

and satisfies the independently established global bound

`q_b<=5`.

For nontrivial odd `s>=3`, simultaneous boundary closure

`k_*-4=2s-1`,

`k_*-2=2s+1`

is equivalent to

`q_b=s+2`.

Because `s>=3` and `q_b<=5`, the unique solution is

`(s,q_b,k_*)=(3,5,9)`.

At this solution,

`M_9=(9-4)(9-2)=35`,

`3M_9=105`,

`3M_9+1=106=2*53`.

This is a breaker-coprime capacity theorem only.

It does not by itself prove an unrestricted prime run of length nine or replace the separate native typed-Cell prime-incidence island theorem.

## Corollary F — tri-sector lane arithmetic

For `s=3`, the central lane set is

`j=-1,0,1`.

The three lane polynomials are exactly

`6m^2-2m+1`,

`6m^2+1`,

`6m^2+2m+1`.

The middle lane is the even-shell `h=0` central-filament value.

Also

`3M_9=105`.

Hence the longitudinal closure extremum and the independently stated bouquet-gate integer coincide exactly as the integer `105`.

This statement freeze does not certify a stronger historical/genealogical claim that both definitions arise from one pre-existing mechanism unless that common provenance is proved from additional native inputs.

## Promotion boundary

Mathematical statement strength above has survived independent blind replication with the explicit narrowing in Theorem A and Corollary F.

External novelty remains unresolved.

Do not promote classical components such as split tori, Joukowski/Dickson maps, Burnside counting, quadratic characters, or conic duality as new mathematics.

The only surviving research candidate is the geometry-selected coupling and the unique tri-sector boundary closure, stated at exactly the strength frozen here.
