# RSA-270 continuation: character-weighted BRC interface and faithful residue recovery

Status: `RESEARCH NOTE / EXACT INTERFACE / N-ONLY EVALUATION OPEN`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T20:31:34+08:00`  
Parents: level-9 character split + explicit ternary trace decoder in PR #1331.

No RSA-270 factor is obtained.

## 1. The arithmetic interface is simpler than the full torsion packet

For `e>=1`, let

`M=3^e`, `phi=2*3^(e-1)`.

The unit group `(Z/MZ)^*` is cyclic of order phi, with 2 a primitive root. Let `chi_e` be the faithful primitive Dirichlet character defined by

`chi_e(2)=zeta_phi`.

It is odd because `chi_e(-1)=-1`.

Define the twisted divisor sum

`A_e(n) := sum_(d|n) chi_e(d)`.

For any squarefree semiprime `N=pq`, `3∤N`,

`A_e(N)=(1+chi_e(p))(1+chi_e(q))
       =1+chi_e(N)+chi_e(p)+chi_e(q)`.

N itself determines the product

`P_e=chi_e(p)chi_e(q)=chi_e(N)`.

Therefore an exact value of `A_e(N)` determines the sum

`T_e=chi_e(p)+chi_e(q)=A_e(N)-1-P_e`.

The two character values are the unordered roots of

`X^2-T_e X+P_e=0`.

Because `chi_e` is faithful, their character values determine the unordered factor residues `{p,q} mod 3^e`. Since p and q are odd, this also determines the residues modulo `2*3^e`.

**Theorem (faithful-character coefficient).** `A_e(N)` is factor-residue complete modulo `3^e` for squarefree semiprimes coprime to 3.

For hierarchical use, previous-level residues reduce the inversion to comparison with only the 2-3 Hensel candidate lifts, so no large discrete-log search is required.

## 2. Generating-function form

The coefficients have the elementary Lambert-series generating function

`sum_(n>=1) A_e(n) q^n
 = sum_(d>=1) chi_e(d) q^d/(1-q^d)`.

For primitive odd `chi_e`, this is, up to the standard constant/normalization, the positive-index q-expansion of a weight-1 Eisenstein series with nebentypus `chi_e`.

This modular-form identification is useful for routing possible recurrences/dissections, but it does not imply an index-fast algorithm for computing `A_e(N)` at a large composite N.

## 3. Exact BRC noncommutation law

Let the divisor-branch multiset of a squarefree semiprime be

`D(N)={1,p,q,N}`.

Two operations do not commute:

### Weight first, then collapse

`CHARACTER_WEIGHT -> SUM_BRANCHES`

gives

`A_e(N)=1+chi_e(p)+chi_e(q)+chi_e(N)`.

This retains the factor-split sum.

### Collapse factors first, then apply character

`MULTIPLY_BRANCHES -> N -> chi_e(N)`

gives only

`chi_e(N)=chi_e(p)chi_e(q)`.

The information defect is exactly

`A_e(N)-chi_e(N)=1+chi_e(p)+chi_e(q)`.

Thus:

**CHARACTER_BEFORE_BRC_COLLAPSE != CHARACTER_AFTER_BRC_COLLAPSE.**

This is a precise example of the canonical BRC provenance principle: a multiplicative observable applied after provenance erasure cannot recover the factor split, while branchwise weighting before collapse can.

No new top-level tool family is needed; this is a direct reuse/specialization of provenance-aware BRC semantics.

## 4. Relation to the multiplied torsion decoder

At level `e=2`, under H2 and `N≡1 mod9`, the previous note proved the exact equality

`Tr(P_(9N)(zeta_9)) = 12 A_2(N)`

for the primitive order-6 character modulo 9.

At general e, the explicit ternary twisted-trace decoder already gives a constant-width BRC branch selector. The present theorem identifies a second, purely arithmetic target `A_e(N)` that is also sufficient to select the lift.

What is **not yet proved** is that one fixed simple linear functional of the general multiplied profile equals `A_e(N)` for all e. The two interfaces are known to be factor-residue equivalent, not yet identical as explicit BRC formulas beyond e=2.

## 5. Factorization consequence

If an N-only procedure can evaluate `A_e(N)` successively for `e=2,...,E`, previous-level candidate comparison recovers `{p,q} mod 3^E` one trit at a time.

For RSA-270, `2*3^282 > sqrt(N)`, so such evaluations through e=282 would determine the smaller factor exactly.

Hence the meaningful computational question is now sharply stated:

> Can a provenance-preserving Enterprise/BRC construction evaluate a faithful twisted divisor sum coefficient `A_e(N)` (or the equivalent 2-4 ternary residue-flow traces) without enumerating divisors/factors?

## 6. Current barrier interpretation

The e=2 case is already a hidden cyclic-cubic splitting decision. More generally, the compatible characters `chi_e` form a 3-adic cyclotomic tower. N determines only the product of the two factor symbols; the missing information is their unordered split.

Therefore any route that only evaluates ordinary residue classes or multiplicative characters of N **after** collapsing to N cannot progress. A successful method must preserve a branchwise/representation-level statistic long enough to form the character-weighted sum.

This narrows the search space considerably: stop testing ordinary N-only congruences and focus on weighted BRC counts, 3-dissections of the corresponding weight-1 Eisenstein/Lambert series, or a proof that their target coefficient evaluation is itself equivalent to the hidden splitting problem.
