# Native filament final narrow novelty packet — statement only

Status: `BLIND_EXTERNAL_NOVELTY_INPUT / POST-INDEPENDENT-MATH-NARROWING`

Date: `2026-08-25`

Originating Researcher-ID: `EM-FREE-NEPS-239A6D`

Purpose: independently classify the external theorem-level novelty of the mathematically verified-and-narrowed post-audit core.

The mathematical statement strength has already passed blind replication. This packet does not expose source proofs/checkers.

## Conceded classical ingredients

Do not assign novelty to any of the following in isolation:

- parabola/conic tangent parametrization and conic duality;
- difference-of-squares factorization;
- split one-dimensional tori/hyperbolas;
- sign actions, Weyl inversion, Burnside orbit counting;
- quadratic characters and cyclotomic numbers;
- Dickson polynomials and the identity `D_n(u+a/u,a)=u^n+(a/u)^n`;
- Joukowski maps `u+c/u`;
- rational-function many-to-one / 2-to-1 theory over finite fields;
- Dickson/Joukowski value-set cardinality;
- elementary second-moment/power-sum arguments;
- CRT and standard finite-field algebra.

The novelty target is only the exact geometry-selected coupling below.

## F1 — punctured split-hyperbola tangent bridge

Work over a field `K`, `char(K)!=2`, with `B!=0`, distinct shifts `d_0,d_1`, and

`Q_i(x)=x^2/(2B)-d_i`,
`C_i=2(d_i-d_(1-i))`.

For `u!=v`, tangents `T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff

`B(w-u)(w-v)=C_i`.

Common negative-dual values are represented by

`B(y^2-x^2)=C_i`,

and `(x,y)->(a,b)=(y-x,y+x)` identifies the dual-overlap variety with the full split hyperbola

`H_(B,C_i)={(a,b):Bab=C_i}`.

After quotienting distinct-tangent concurrence triples by simultaneous translation, the tangent side is

`H_(B,C_i) \ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

Question: is this exact **translated-two-parabola / distinct-tangent / translation-quotient = punctured-hyperbola** theorem directly present in the literature, or only an immediate packaging of classical tangent formulas and torus algebra?

## F2 — finite-field sign quotient / breaker capacity

Over odd `F_q`, `B,C!=0`, the full dual-overlap hyperbola

`R={(x,y):B(y^2-x^2)=C}`

has `q-1` points. The independent sign group `{+-1}^2` acts on `R`, and the common-dual-value set is the orbit quotient.

If the quotient has one orbit, then orbit size gives

`q-1<=4`, hence `q<=5`.

Question: is any novelty left in this bound/correspondence after standard split-torus and orbit theory are conceded?

## F3 — odd-sector Joukowski lane quotient

For odd sector count `s>=3`, define the centered lane set

`J_s={-(s-1)/2,...,(s-1)/2}`

and, over odd prime `q` with `q∤2s`,

`Lambda_s(a)=-s a-1/(2a)`, `a in F_q^*`.

Put `c=(2s)^(-1)`. Then `Lambda_s` is exactly the quotient by the involution

`a -> c/a`,

and

`|Im Lambda_s|=[q+Legendre(c,q)]/2`.

The central packet saturates every nonzero residue iff

`Im Lambda_s subseteq J_s (mod q)`.

Question: after Dickson/Joukowski and low-degree many-to-one theory are conceded, is this lane-map theorem anything beyond direct specialization?

## F4 — extremal saturation uniqueness

If `q_-(s)=2s-1` is prime and the central packet saturates, then

`(s,q)=(3,5)`.

If `q_+(s)=2s+1` is prime and the central packet saturates, then

`(s,q)=(3,7)`.

Thus `s=3` is the unique nontrivial odd-sector parameter saturating both prime extremal Joukowski boundaries.

The known proof compares the exact Joukowski image with the centered lane set via second moments and produces the divisibility obstructions `q|75` and `q|21`.

Question: is there a theorem in Dickson/Joukowski/value-set literature directly classifying equality of this image with this specific centered arithmetic-progression target under `q=2s+-1`?

## F5 — longitudinal/transverse unique boundary closure

Suppose an odd universal breaker `q_b` has exact breaker-coprime capacity

`k_*=2q_b-1`,

and the independently established global bound gives `q_b<=5`.

The transverse Joukowski extremal boundaries are

`2s-1, 2s+1`.

Simultaneous closure

`k_*-4=2s-1`,
`k_*-2=2s+1`

is equivalent to `q_b=s+2`, and therefore the unique nontrivial solution is

`(s,q_b,k_*)=(3,5,9)`.

At this solution:

`M_9=(9-4)(9-2)=35`,
`3M_9=105`,
`3M_9+1=106=2*53`.

The integer `9` here is a breaker-coprime capacity, not an unrestricted prime-run theorem.

Question: is this exact simultaneous matching of independently derived longitudinal and transverse boundaries already present in any arithmetic-dynamics, finite-field value-set, covering-system, or deterministic-percolation framework?

## F6 — final coupled selection statement

The native tri-sector shell allocation fixes `s=B=3` before primality. The same sector parameter then controls:

1. a longitudinal translated-parabola tangent sample whose distinct-tangent quotient is a punctured split hyperbola;
2. a transverse Joukowski lane quotient;
3. extremal transverse saturation only at `(3,5)` and `(3,7)`;
4. simultaneous longitudinal/transverse boundary closure only at `(3,5,9)`.

Question: does the literature contain a direct theorem statement subsuming this exact geometry-selected coupling, even if every component object is classical?

## Required verdict labels

For F1--F6, assign exactly one:

- `KNOWN_DIRECT_THEOREM`;
- `KNOWN_IMMEDIATE_COROLLARY`;
- `KNOWN_COMPONENTS_ONLY`;
- `PARTIAL_OVERLAP_REQUIRES_NARROWING`;
- `NO_DIRECT_MATCH_FOUND`.

Then assign one package-level verdict.

For every known/partial verdict, map hypotheses and conclusions to an exact source.

For every `NO_DIRECT_MATCH_FOUND`, list the search areas and closest false positives.

Hard guard:

`NO_DIRECT_MATCH_FOUND != PROVEN_NOVEL`.
