# Valley Band / CFRAC Prior-Art Map

## Scope and method

This map was prepared independently for `RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION`. It uses primary papers, original/public-domain books, official publisher records, and authoritative monographs. No Valley prototype, source conversation, source script, withheld checkpoint, or prior Valley research branch was consulted.

Search families were limited to: indefinite binary quadratic-form reduction; complete quotients and intermediate convergents; continued-fraction factorization and multipliers; modular-root polynomial sieving; large-prime relation recombination; and square-form factorization. The result is a technical-priority boundary, not a patent opinion or an exhaustive historical bibliography.

## Source register

1. Carl Friedrich Gauss, *Disquisitiones Arithmeticae* (1801), especially the articles on reduction and neighboring indefinite binary quadratic forms. Official public-domain records/scans: [Library of Congress](https://www.loc.gov/item/36021572/) and [Smithsonian Libraries DOI record](https://doi.org/10.5479/sil.324926.39088000932822). Primary source.

2. Duncan A. Buell, *Binary Quadratic Forms: Classical Theory and Modern Computations*, Springer, 1989, [publisher DOI](https://doi.org/10.1007/978-1-4612-4542-9). Authoritative monograph for modern form notation, equivalence, reduction, ambiguous classes, and computational cycles.

3. Henri Cohen, *A Course in Computational Algebraic Number Theory*, Graduate Texts in Mathematics 138, Springer, 1993, [publisher DOI](https://doi.org/10.1007/978-3-662-02945-9). Authoritative computational-number-theory reference for continued fractions, binary quadratic forms, Hensel lifting, factorization, and exact algorithms.

4. D. H. Lehmer and R. E. Powers, “On Factoring Large Numbers,” *Bulletin of the American Mathematical Society* 37(10), 1931, 770–776, [AMS DOI](https://doi.org/10.1090/S0002-9904-1931-05271-X). Primary paper connecting continued fractions and factorization residues.

5. Michael A. Morrison and John Brillhart, “A Method of Factoring and the Factorization of F7,” *Mathematics of Computation* 29(129), 1975, 183–205, [AMS DOI](https://doi.org/10.1090/S0025-5718-1975-0371800-5). Primary CFRAC implementation paper: complete-quotient recurrences, convergent residues, factor bases, square dependencies, and multiplier experiments.

6. Carl Pomerance and Samuel S. Wagstaff Jr., “Implementation of the Continued Fraction Integer Factoring Algorithm,” *Congressus Numerantium* 37, 1983, 99–118, [author-hosted primary PDF](https://math.dartmouth.edu/~carlp/PDF/implementation.pdf). Primary implementation study for CFRAC relation collection and square-congruence processing.

7. Carl Pomerance, “The Quadratic Sieve Factoring Algorithm,” EUROCRYPT 1984, LNCS 209, 1985, 169–182, [Springer DOI](https://doi.org/10.1007/3-540-39757-4_17). Primary paper for sieving quadratic-polynomial values by their modular roots.

8. Jason E. Gower and Samuel S. Wagstaff Jr., “Square Form Factorization,” *Mathematics of Computation* 77(261), 2008, 551–588, [AMS DOI](https://doi.org/10.1090/S0025-5718-07-02010-8). Primary paper and closest established comparison for carrying quadratic-form states in a continued-fraction-derived factoring algorithm; its square-form shortcut and control logic are not the full-band construction analyzed here.

## Claim-by-claim map

| Packet component | Established antecedent | Exact correspondence found here | Classification |
|---|---|---|---|
| Recurrence on `(A,B,C)` with `C^2-AB=T` | Gauss neighboring-form reduction; Buell's modern binary-form treatment | The substitution `S_a=[[a,1],[1,0]]` sends `[A,2C,B]` to `[Aa^2+2Ca+B,2(Aa+C),A]` exactly | Established orbit in signed coordinates; not a new recurrence |
| Digit `floor((floor(sqrt(T))+|C|)/|A|)` | Standard complete quotient `a=floor((floor(sqrt(T))+m)/d)` | Exact under `d=|A|`, `m=|C|`, forward orientation `AC<0`, and the standard reduced inequalities | Established only after sign/domain repair |
| Canonical initial state `(1,-T,0)` | Principal form `x^2-Ty^2` and the ordinary `sqrt(T)` continued fraction | Its first candidate step is `(-d_1,d_0,m_1)` | Established canonical initialization |
| State-to-complete-quotient bijection | Classical complete quotients and reduced forms | `(A,B,C)=(sigma d,-sigma d_prev,-sigma m)`; global negation is the orientation double cover | Coordinate presentation of established state |
| Accumulated square relation | Lehmer–Powers; Morrison–Brillhart; Pomerance–Wagstaff | With `P_n=product S_{a_i}`, `D_n(t)=X_t^2-TY_t^2`, hence `X_t^2==D_n(t) mod N` | Standard CFRAC-type relation |
| Growing convergent omitted from the local state | Classical periodic complete quotients versus growing convergents | The triple continues the local orbit but cannot uniquely recover `P_n` after cycle recurrence; replay restores it | Compression distinction, not a new mathematical object |
| `0<t<a_n` band points | Standard intermediate convergent / semiconvergent columns | `P_n(t,1)` is exactly `t` times the current column plus the previous column | Established intermediate-convergent algebra |
| Band values outside `0<=t<=a_n` | Evaluation of the same indefinite form on arbitrary integer columns | The identity remains true, but these values are extrapolations rather than standard semiconvergents | Valid extension of evaluation range; no new orbit |
| Root formula for `D(t)` | Elementary quadratic congruences; Cohen for exact modular algorithms and Hensel lifting | `A D(t)=(At+C)^2-T` gives every generic and degenerate root case | Established algebra, fully classified here for this presentation |
| Sieve by modular roots of a quadratic polynomial | Pomerance's quadratic sieve | Roots select residue classes of `t` for which a form/polynomial value is divisible by a factor-base prime | Structurally established polynomial sieving |
| Multiplier `M` and quadratic characters | Morrison–Brillhart multiplier experiments and later CFRAC implementations | `T=MN`; square-class changes preserve unramified characters but not integer form orbits | Established multiplier principle; orbit caveat is necessary |
| Signed square dependencies and `gcd(X±Y,N)` | CFRAC papers above | Include `-1`, all prime parities, and reverify the final square congruence | Established relation algebra |
| Single- and double-large-prime recombination | Established relation-management variants in integer factorization implementations | Pair equal single large primes; use graph cycles for double large primes; then reverify | Established generic relation machinery, not an orbit novelty |
| Closed quadratic-form factoring state | Square Form Factorization is the closest explicit form-state comparator | Both use form coefficients, but SFF's square-form event and transitions differ from the all-`t` band | Related prior art, not identity of algorithms |

## Exact novelty boundary

### What is not new

- the complete-quotient orbit;
- the neighboring indefinite-form orbit;
- the canonical principal form and accumulated unimodular transforms;
- principal and intermediate convergent columns;
- the square-congruence dependency method;
- multiplier character selection;
- modular-root sieving of quadratic values;
- single/double-large-prime recombination as generic relation management.

### What may be presentation-level synthesis

- carrying the local complete quotient as the signed coefficient triple `(A,B,C)`;
- exposing many `D_n(t)=F_n(t,1)` values as one explicit “band” interface;
- choosing between a replayed global witness for `D_n(t)` and the local closed-state witness for `A_nD_n(t)`.

Those points may be useful engineering or notation, but the analysis proves that they do not create a different reduction orbit. No exact historical-priority claim is made for the particular name “Valley band” or for this exact packaging.

### What is false without repair

The packet's weak state conditions do not guarantee the forward continued-fraction orientation. The smallest counterexample is `T=3`, `(-2,1,-1)`. Also, a closed triple without the accumulated transform does not by itself justify a CFRAC relation with `D(t)` alone; it justifies the local right-hand side `A D(t)`. These are mathematical qualification requirements, not novelty features.

## Search-limit statement

The primary literature establishes every structural component needed for the classification. This search did not identify, and therefore does not claim, an earlier paper that used the exact same full integer-band API around each signed form state. Establishing exact priority for that packaging would require a dedicated multilingual historical and patent search. That unresolved historical naming question does not affect the proved orbit equivalence or the final task classification.
