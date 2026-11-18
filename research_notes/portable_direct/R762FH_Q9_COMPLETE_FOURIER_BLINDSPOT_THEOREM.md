# R762FH — Complete Fourier-blindness obstruction for q=9 normalized BRC shadows

Date: 2026-11-19, Asia/Shanghai.
Status: AUTHOR-PROVED WITH COMPLETE FINITE INTEGER CERTIFICATE / NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, frozen taskbook at enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8.
Scientific predecessors: R762FG character period obstruction and R762ER normalized-shadow integrality (author-side; the scalar part below does not assume the latter).
Scope: positive integer six-named-branch BRC, full (Z/9Z)^3 terminal coordinates. No native signed TRIADIC_CLOSURE_E semantics, Cell/Link/Port permission or Working Truth promotion is inferred.

## Exact question and central distinction

Does checking the normalized difference modulo 3^h under **all** 729 ninth-root Fourier characters imply congruence of the original 729 integer terminal coefficients modulo 3^h? The answer is no, even for actual later normalized BRC states, not only for arbitrary group-ring elements. The failure is exact and persists for the six tested precision levels h=3,...,8.

Let R=Z[X,Y,Z]/(X^9-1,Y^9-1,Z^9-1), with the six separately retained named transitions represented by
P=1+X+Z+XY+YZ+XYZ.
For n>=9 put f(n)=floor(n/3)-2 and T(n)=3^(-f(n)) P^n in Q tensor R; the previously author-established R762ER integrality statement identifies these rational expressions as integer coefficient vectors. The scalar character statements below remain valid without assuming that antecedent.

For each (a,b,c) in {0,...,8}^3, let zeta be a primitive ninth root and let chi_{a,b,c} evaluate (X,Y,Z)=(zeta^a,zeta^b,zeta^c). Put lambda=chi(P) and beta=lambda^3/3 in O=Z[zeta].

## Theorem FH1 — complete 729-character mod-3 idempotence

For all 729 triples, beta is in O. Moreover exactly 486 characters satisfy
beta^6 = 1 (mod 3O),
and the remaining 243 satisfy the **stronger** congruence beta = 0 (mod 3O).
There are no other cases.

Proof: Use the integral basis (1,zeta,...,zeta^5), reducing zeta^6=-zeta^3-1, zeta^7=-zeta^4-zeta, zeta^8=-zeta^5-zeta^2. For each of the 9^3 triples calculate the integral six-vector lambda as the sum of zeta^e at exponents
(0,a,c,a+b,b+c,a+b+c) modulo 9.
Multiply lambda three times by the exact basis table, check all six entries divisible by 3 and divide entrywise to obtain beta. The exhaustive integer certificate R762FH_VERIFY.py checks the 729 complete cases, yielding 243 exact beta=0 mod3 and 486 exact beta^6=1 mod3; unexpected cases raise an error. Since the domain contains exactly 9^3 choices and all ring operations are exact integral reductions, this is a finite exhaustive proof, subject to ordinary program verification; it does not extrapolate numerical samples.

## Theorem FH2 — universal same-precision Fourier blindness

For **every** integer h>=3 put L_h=18*3^(h-3). For every n=3k+r with r in {0,1,2} and k>=max(3,h-2), **each** of the 729 characters satisfies

chi_{a,b,c}( T(n+L_h)-T(n) ) = 0 (mod 3^h O).

Proof: Since lambda^3=3 beta, we have chi(T(3k+r))=9 beta^k lambda^r. Since L_h/3=6*3^(h-3), exact subtraction yields

chi(T(n+L_h)-T(n))
 = 9 beta^k lambda^r ( beta^(6*3^(h-3)) - 1 ).

When beta belongs to 3O, the factor 9 beta^k belongs to 3^(k+2) O, which is in 3^h O. Otherwise FH1 implies beta^6=1+3u with u in O; the elementary integer binomial identity (1+3u)^(3^t)=1 mod 3^(t+1)O gives beta^(6*3^(h-3))-1 in 3^(h-2)O. Multiplication by 9 gives membership in 3^h O. Every case is covered. QED.

Notice that this is an **all-character observation theorem** at the same precision, not a claim that L_h is a genuine full-terminal period.

## Theorem FH3 — six exact full-terminal counterexamples

For each h in {3,4,5,6,7,8}, set n=36 and L=L_h. Compute the original six-step integer convolution P^m for m=36 and m=36+L, then divide every coefficient by the respective exactly verified power 3^f(m). For all 729 terminal positions, the coefficientwise minimum nonzero 3-adic valuation of
D_h = T(36+L_h)-T(36)
is precisely h-2. At the actual origin terminal (0,0,0) the exact residue is

[D_h]_(0,0,0) = 2*3^(h-2) (mod 3^h).

Thus all 729 characters of D_h vanish modulo 3^h by FH2, yet D_h is nonzero modulo 3^h in the original integral terminal lattice. The explicit origin residues are:

| h | L_h | v3(gcd of nonzero D_h coefficients) | origin modulo 3^h |
|---|---:|---:|---:|
| 3 | 18 | 1 | 6 |
| 4 | 54 | 2 | 18 |
| 5 | 162 | 3 | 54 |
| 6 | 486 | 4 | 162 |
| 7 | 1458 | 5 | 486 |
| 8 | 4374 | 6 | 1458 |

The standalone checker verifies all integer coefficients, every normalization division and all 729 finite character cases; its JSON output is R762FH_EVIDENCE.json. All six comparisons use n=36 and hence are beyond the previously reported h<=8 preperiods, although FH3's assertions depend only on these direct integer calculations, not on the earlier period proof.

## Consequence and interpretation

At all tested h=3,...,8, the map from the integral terminal lattice to the complete family of ordinary cyclotomic characters modulo 3^h has a nonzero kernel containing a concrete normalized BRC **period-difference**. Thus combining *all* 729 characters at unchanged precision is insufficient to prove the full-terminal period; this is a Fourier-order / lattice saturation defect, not merely a poorly selected single character. Over Q(zeta), Fourier inversion divides by |G|=729=3^6; it is therefore not an integral inverse modulo powers of 3.

This new result explains why R762FG's single-character lower bound leaves a substantial gap. It also changes the next attack: use an integral image-lattice / confluent or derivative Fourier observer, rather than simply collecting additional ordinary characters. The sharp possible information-loss exponent beyond h=8, and the proposed general full period T_h=18*3^(h-1), remain open.

## Reproduction and scope

Run: python3 R762FH_VERIFY.py > R762FH_EVIDENCE.json.
The checker uses only Python integer arithmetic and the full six branch transition list; no floats, random sampling, approximations or imported mathematical datasets. The 729 character classification is exhaustive and symbolic over the exact cyclotomic basis; the six terminal collisions are exhaustive over all 729 endpoints but confined to h=3,...,8 and n=36. Scientific status NOT_REVIEWED. The saved checker and evidence allow independent recalculation.

## Open next unit

1. Find an integral saturated Fourier-image / Smith observer that detects the missing two trits without imposing R762FE's worst-case +57 trits on individual scalars.
2. Prove or falsify the general origin witness formula for h>=9 by a uniform 3-adic lift of the integral terminal lattice (avoid treating finite h<=8 data as a universal proof).
3. Independently continue native signed TRIADIC_CLOSURE_E Cell/Link/Port admissibility and provenance-preserving transport, whose scientific interface is distinct from this positive BRC terminal model.
