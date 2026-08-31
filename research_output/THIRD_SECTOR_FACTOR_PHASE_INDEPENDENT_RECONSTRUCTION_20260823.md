# Third-Sector Factor Phase — Independent Reconstruction

Status: `FROZEN_INDEPENDENT_RETURN`

Task-ID: `RS-THIRD-SECTOR-FACTOR-PHASE-INDEPENDENT-RECONSTRUCTION`

Researcher-ID: `EM-TSFPR-D14474`

Frozen source commit: `12725505c636449df7dd913ac06e581bf418b89c`

Locked blind packet: `research_inputs/THIRD_SECTOR_FACTOR_PHASE_BLIND_RECONSTRUCTION_PACKET_20260823.md@87f32a3df7625b76a85944769be82f44e122bc7e` (blob `f755dffbf56af9bf179349105c7107bb998c30b4`)

Independent-freeze statement: no withheld third-sector event, source formula, source checker, source proof, source witness, source enumeration range, free-research branch, or post-freeze source comparison was read. The only mathematical input was the blind packet and classical arithmetic reconstructed below.

## 1. Executive Summary

The complete bridge exists, but its exact factor object is not the full divisor fiber of `n`. It is the divisor lattice of the canonically extracted split core

`C(n) = product_{p == 1 (mod 4)} p^{v_p(n)}`.

When every prime `q == 3 (mod 4)` has even exponent, let

`h(n) = 2^{floor(v_2(n)/2)} product_{q == 3 (mod 4)} q^{v_q(n)/2}`

and `epsilon = v_2(n) mod 2`. Then `n = h(n)^2 2^epsilon C(n)`. After choosing the canonical Gaussian prime `pi_p = r_p+i s_p` with `r_p>s_p>0` and `r_p^2+s_p^2=p`, every divisor

`d = product_p p^{k_p} | C`

produces

`Z_d = h(1+i)^epsilon product_p pi_p^{k_p} conjugate(pi_p)^{e_p-k_p}`.

The map taking `Z_d` to the unique cell `(a,b)` with `a>=b>=0` in its unit/conjugation orbit induces a bijection

`Div(C) / (d ~ C/d)  <->  {(a,b): a>=b>=0, a^2+b^2=n}`.

Its fixed point exists exactly when `C` is a square. It is an axis cell when `epsilon=0` and a diagonal cell when `epsilon=1`. Consequently the exact unordered nonnegative count is

`(tau(C) + 1_{C is a square}) / 2`.

The common additive scale is not merely the inert square part. It is exactly

`gcd(a,b) = h(n) gcd(d,C/d)`.

The same factor choices give a sound and complete recursive generator. Gaussian unique factorization proves injectivity, surjectivity, and generator completeness; the finite checker is corroboration, not a substitute.

For two distinct primitive quotient cells `(a,b)` and `(c,d)` of norm `n`, put

`t = gcd(n,2)` and `m=n/t`.

Then the four observable gcds recover a coprime, nontrivial complementary partition `A B=m`:

`A = gcd(m, |ac+bd|/t) = gcd(m, |ad-bc|/t)`,

`B = gcd(m, |ac-bd|/t) = gcd(m, |ad+bc|/t)`.

No factorization oracle occurs in this reverse algorithm. Units and conjugation can exchange `A` and `B`, but cannot change the unordered pair `{A,B}`. The primitive and distinct-quotient hypotheses are necessary.

Final classification:

`FULL_BIDIRECTIONAL_BRIDGE_INDEPENDENTLY_RECONSTRUCTED`

This classification applies to the precisely normalized split-core quotient. A naive bijection with all of `M(n)`, omission of the complement quotient, omission of the `2`-adic reverse normalization, or admission of an odd inert exponent is false.

## 2. Research Question and Claim Boundary

The packet defines

`S_2(n)={(a,b) in N_0^2:a^2+b^2=n}`

and, for `n>1`,

`M(n)={(x,y) in N_0^2:(x+1)(y+1)=n}`.

The question was whether a multiplicative factor phase exactly controls existence, counting, every square cell, common scale, generation, and reverse recovery. These are logically separate claims. This report proves or delimits each one.

The bridge is an auxiliary arithmetic presentation. Nothing below makes `M(n)` a native metric, a native sector, a topological coordinate, or a foundational Enterprise object. Historical novelty is also not claimed.

The degenerate norm `n=0` has the single cell `(0,0)` and no positive multiplicative factor object. All factor theorems below are for `n>=1`; `n=0` is handled separately by the checker.

### Elementary multiplicative fiber

Writing `r=x+1` and `s=y+1` gives an immediate bijection between `M(n)` and ordered positive factor pairs `rs=n`. Therefore, for `n>1`:

1. `|M(n)|=tau(n)`.
2. `n` is prime exactly when `M(n)={(0,n-1),(n-1,0)}`, equivalently it has no point with both coordinates positive.
3. `n` is composite exactly when an interior point `x,y>=1` exists.
4. The diagonal is met exactly when `n` is a square, at the unique point `(sqrt(n)-1,sqrt(n)-1)`.
5. Under the declared orientation `x<=y`, the lexicographically least interior point is
   `(spf(n)-1,n/spf(n)-1)`, where `spf(n)` is the least prime factor. Indeed the least divisor of a composite `n` exceeding one is prime and does not exceed `sqrt(n)`.
6. The swap quotient of `M(n)` has `(tau(n)+1_{n square})/2` elements.

These statements are controls only. The full `M(n)` includes factors from `2` and inert square primes that affect scale but not square-cell shape. Hence it is generally too large to be the forward parameter space.

## 3. Inputs, Conventions, and Method

### Input firewall

Only the frozen taskbook and blind packet were used. The independent package was frozen before any toolbox lookup, prior-result lookup, or source comparison, as required by the task-local discovery firewall.

### Classical infrastructure

The proof uses these classical facts, with no novelty claim:

- the Euclidean-domain and unique-factorization structure of `Z[i]`;
- `2` ramifies as a unit times `(1+i)^2`;
- an odd prime `p==1 (mod 4)` splits as `pi_p conjugate(pi_p)` and has a unique positive ordered two-square presentation `p=r_p^2+s_p^2`, `r_p>s_p>0`;
- an odd prime `q==3 (mod 4)` stays Gaussian-prime;
- the Gaussian norm is multiplicative, which contains the Brahmagupta-Fibonacci composition identity;
- the classical two-square existence criterion follows from the preceding factorization.

Every overlay-specific quotient, scale, generator, and reverse formula is derived here rather than cited from a source statement.

### Arithmetic notation

For `n>=1`, write

`n = 2^alpha product_{p==1 (4)} p^{e_p} product_{q==3 (4)} q^{f_q}`.

Define:

- `C = product_{p==1 (4)} p^{e_p}` (split core);
- `Q = product_{q==3 (4)} q^{f_q/2}` when every `f_q` is even;
- `epsilon = alpha mod 2`;
- `h = 2^{floor(alpha/2)} Q`, so `n=h^2 2^epsilon C`;
- `K(C)=Div(C)`, represented by exponent vectors `k=(k_p)` with `0<=k_p<=e_p`;
- `J(d)=C/d`, equivalently `J(k)_p=e_p-k_p`.

The empty products are one. Thus the notation includes `n=1`, powers of `2`, and pure inert squares.

## 4. Results and Proofs

### Quotient and Convention Ledger

The following levels are kept distinct.

| Level | Object | Exact quotient/representative |
|---|---|---|
| signed ordered | `(A,B) in Z^2`, `A^2+B^2=n` | Gaussian integer `A+iB` |
| unit quotient | signed ordered representations modulo multiplication by `±1,±i` | exponent choice `k in K(C)` |
| reflection quotient | unit classes modulo complex conjugation | `k ~ e-k`, or `d ~ C/d` |
| nonnegative unordered cell | `(a,b)` with `a>=b>=0` | unique representative of the unit/conjugation orbit |
| nonnegative ordered cell | `(a,b)` with `a,b>=0` | restore swap except on the diagonal |
| split-factor point | `(d-1,C/d-1)` for `C>1` | point of `M(C)`; swap is complement |

The full symmetry group of a square representation is generated by Gaussian units and conjugation. Coordinate swap is `z -> i conjugate(z)`. A global reflection is conjugation up to a unit. Therefore swap, conjugation, unit action, and global reflection are not four independent quotients. Quotienting by units and then by the single residual conjugation action gives exactly the nonnegative unordered cells; quotienting again would overidentify valid cells.

### Forward Bijection

#### Theorem 1 — existence and exact parameterization

`S_2(n)` is nonempty exactly when every `f_q` is even. Under that condition, choose for each split prime the canonical

`pi_p=r_p+i s_p`, with `r_p>s_p>0` and `N(pi_p)=p`.

For `d=product p^{k_p}|C`, define

`Z_d=h(1+i)^epsilon product_p pi_p^{k_p} conjugate(pi_p)^{e_p-k_p}`

and let `Phi([d])` be the unique `(a,b)`, `a>=b>=0`, in the unit/conjugation orbit of `Z_d`. Then

`Phi: Div(C)/<J> -> U_2(n)`

is a bijection, where `U_2(n)={(a,b):a>=b>=0,a^2+b^2=n}`.

#### Proof — soundness

Norm multiplicativity gives

`N(Z_d)=h^2 2^epsilon product_p p^{k_p+e_p-k_p}=n`.

Unit multiplication, conjugation, signs, and swap preserve norm, so `Phi([d])` is a valid square cell.

#### Proof — the complement action is exactly reflection

Conjugating `Z_d` exchanges every `pi_p` and `conjugate(pi_p)`. Also

`conjugate(1+i)^epsilon=(1-i)^epsilon=(-i)^epsilon(1+i)^epsilon`.

Hence `Z_{C/d}` is a unit multiple of `conjugate(Z_d)`. Thus `d` and `C/d` yield the same nonnegative unordered cell.

#### Proof — surjectivity

Let `z=A+iB` have norm `n`. Gaussian unique factorization forces:

- exactly `alpha` factors associated to `1+i`;
- for every inert `q`, a rational factor `q^{f_q/2}`, so `f_q` must be even;
- for every split `p`, a distribution `pi_p^{k_p} conjugate(pi_p)^{e_p-k_p}` for a unique `0<=k_p<=e_p`;
- one residual Gaussian unit.

Replacing `(1+i)^alpha` by the unit-associated `2^{floor(alpha/2)}(1+i)^epsilon` shows `z` is a unit multiple of some `Z_d`. Therefore every cell lies in the image.

#### Proof — injectivity

If `Phi([d])=Phi([d'])`, then the corresponding Gaussian integers satisfy either

`Z_{d'}=u Z_d`

or

`Z_{d'}=u conjugate(Z_d)`

for a unit `u`. Comparing the `pi_p` valuations in the unique factorization gives, respectively, `k'_p=k_p` for every `p`, or `k'_p=e_p-k_p` for every `p`. Thus `d'=d` or `d'=C/d`, precisely the declared orbit. No prime-by-prime partial reflection is silently quotiented out.

This proves the bijection and, independently, the classical existence criterion.

#### Canonical dependence

The integer divisor label uses the declared canonical positive decomposition of each split prime. Replacing one `pi_p` by its conjugate relabels `k_p` by `e_p-k_p` but leaves the generated cell set invariant. The exact object before that convention is the oriented Gaussian split-divisor choice; after the convention it is the ordinary divisor lattice `Div(C)`.

### Representation Count and Fixed Points

The complement involution `J` acts on `K(C)`, whose size is

`R=tau(C)=product_p(e_p+1)`.

It has a fixed point exactly when every `e_p` is even, equivalently when `C` is a square. In that case the unique fixed divisor is `sqrt(C)`. Burnside's lemma gives

`|U_2(n)|=(R+F)/2`, where `F=1_{C square}`.

At the fixed choice,

`Z_{sqrt(C)}=h sqrt(C) (1+i)^epsilon`.

Therefore:

- if `epsilon=0`, the fixed cell is the axis cell `(h sqrt(C),0)` and `n` is a square;
- if `epsilon=1`, the fixed cell is the diagonal cell `(h sqrt(C),h sqrt(C))` and `n` is twice a square.

The signed ordered representation count is `4R`: multiplication by the four units acts freely for `n>0`. If nonnegative coordinate order is restored, the count is `R+F` when `epsilon=0` and `R` when `epsilon=1`; the different fixed-point corrections are exactly the axis versus diagonal stabilizers.

### Scale/Shape Bridge

#### Theorem 2 — exact common scale

For `d=product p^{k_p}` and `Phi([d])=(a,b)`,

`gcd(a,b)=h product_p p^{min(k_p,e_p-k_p)}=h gcd(d,C/d)`.

#### Proof

For each split prime,

`pi_p^{k_p} conjugate(pi_p)^{e_p-k_p}`

contains the rational factor `p^{min(k_p,e_p-k_p)}`. Factoring all such terms gives

`Z_d = g W`,

where

`g=h product_p p^{min(k_p,e_p-k_p)}`

and `W` has at most one residual prime from each conjugate split pair, has no inert prime, and contains `(1+i)` to exponent only `epsilon in {0,1}`.

If a rational odd split prime divided both coordinates of `W`, both of its conjugate Gaussian primes would divide `W`, contrary to the one-sided residual support. If an inert prime divided both coordinates, that Gaussian prime would occur, contrary to construction. If `2` divided both coordinates, `(1+i)^2` would divide `W`, contrary to its exponent at most one. Thus the coordinates of `W` are coprime. Unit action and conjugation do not change their ordinary gcd, so `gcd(a,b)=g`.

Finally, `gcd(d,C/d)=product p^{min(k_p,e_p-k_p)}`, proving the formula.

#### Primitive criterion

A generated cell is primitive exactly when all three conditions hold:

1. `alpha in {0,1}`;
2. no inert prime divides `n`;
3. for every split prime, `k_p in {0,e_p}`.

If `s` distinct split primes divide `n`, the number of primitive nonnegative unordered cells is `1` for `s=0`, and `2^{s-1}` for `s>=1`. Therefore two distinct primitive quotient cells exist exactly when at least two distinct split primes occur.

### Factor-Driven Generator

The complete generator is:

1. Factor `n` and reject if an inert exponent is odd.
2. Compute `h`, `epsilon`, and `C`.
3. Compute the canonical `pi_p` for every split prime.
4. Recursively choose `k_p in {0,...,e_p}` and update both
   `d <- d p^{k_p}` and
   `z <- z pi_p^{k_p} conjugate(pi_p)^{e_p-k_p}`,
   starting from `d=1`, `z=h(1+i)^epsilon`.
5. At a leaf, retain it exactly when `d<=C/d` and output
   `sort_desc(|Re z|,|Im z|)`.

#### Soundness proof

Every recursive multiplier has norm `p^{e_p}` and the base has norm `h^2 2^epsilon`, so every leaf has norm `n`. The leaf normalization is a unit/conjugation operation. No spurious cell is produced.

#### Completeness proof

Every divisor of `C` occurs at exactly one recursion leaf. The inequality `d<=C/d` selects exactly one member of each two-element complement orbit and selects the fixed member when `d=C/d`. Theorem 1 proves every cell comes from such an orbit; its injectivity proof shows distinct retained leaves cannot normalize to the same cell. Hence the generator returns every cell exactly once.

The generator uses factorization and canonical split-prime decompositions; it does not consult the direct square-cell enumeration. That makes it a factor-driven index, not a factorization-free algorithm.

### Reverse Two-State Recovery

#### Theorem 3 — exact reverse recovery

Let `(a,b)` and `(c,d)` be two distinct primitive nonnegative unordered cells of the same norm `n`. Put

`t=gcd(n,2)` and `m=n/t`.

Then all four bilinear expressions are divisible by `t`, and

`A=gcd(m,|ac+bd|/t)=gcd(m,|ad-bc|/t)`,

`B=gcd(m,|ac-bd|/t)=gcd(m,|ad+bc|/t)`

satisfy

`A B=m`, `gcd(A,B)=1`, and `1<A,B<m`.

Thus `(A-1,B-1)` is a nontrivial point of `M(m)`, determined up to swap, and is recovered without first factoring `m`.

#### Proof — primitive factor support

Primitivity and Theorem 2 force

`n=2^epsilon C`, with `epsilon in {0,1}` and only split odd primes in `C`.

For the actual Gaussian representatives `z=a+ib` and `w=c+id`, each split prime power occurs wholly on one side of its conjugate pair:

`z=u(1+i)^epsilon product_p eta_p^{e_p}`,

`w=v(1+i)^epsilon product_p theta_p^{e_p}`,

where each `eta_p,theta_p` is either `pi_p` or `conjugate(pi_p)`.

Partition the split primes into those for which `eta_p=theta_p` and those for which they differ. Let `A` be the product of the full prime powers in the first class and `B` the product in the second. By construction `AB=C=m` and `gcd(A,B)=1`.

#### Proof — bilinear products

The products are

`z conjugate(w)=(ac+bd)-i(ad-bc)`

and

`z w=(ac-bd)+i(ad+bc)`.

In `z conjugate(w)`, equal orientations contribute the rational factor `p^{e_p}`, while different orientations contribute a one-sided Gaussian power `pi_p^{2e_p}` or its conjugate. Thus its exact rational common factor from `C` is `A`. In `z w`, the roles reverse, so the exact rational common factor is `B`.

The factor `(1+i)^epsilon` contributes the rational factor `2^epsilon=t` to both products. Dividing every displayed coordinate by `t` is therefore necessary and integral.

To see that no prime from the opposite class contaminates an individual coordinate gcd, reduce modulo a split prime `p`. A Gaussian integer with positive valuation at exactly one of `pi_p` and `conjugate(pi_p)` maps to zero in exactly one of the two components of `Z[i]/(p) ~= F_p x F_p`. If either its real or imaginary coordinate alone were zero modulo `p`, the two component values would be simultaneously nonzero or simultaneously zero, a contradiction. Hence neither coordinate is divisible by `p`. This proves each of the four exact gcd equalities, not merely their pairwise product.

Gaussian units rotate or sign the two coordinates; conjugating one input exchanges the two products. Therefore these ambiguities can only swap `A` and `B` or swap the two equal gcd witnesses for a factor. The unordered factor pair is invariant.

#### Proof — nontriviality

If every split-prime orientation agreed, `z` and `w` would be unit associates and would represent the same quotient cell. If every orientation differed, one would be a unit associate of the other's conjugate, again the same quotient cell. Since the cells are distinct, both orientation classes are nonempty, so `1<A,B<m`.

### Degenerate and Failure Cases

- `n=0`: one cell `(0,0)`; outside the positive factor bridge.
- `n=1`: `C=1`, one axis cell `(1,0)`; `M(1)` is not part of the packet definition.
- `n=2`: `C=1`, one diagonal cell `(1,1)`.
- powers of `2`: exactly one cell, axis for even exponent and diagonal for odd exponent.
- an odd exponent at any `q==3 (mod 4)`: no cell. The smallest negative control is `n=3`.
- pure inert squares: `C=1`; they only scale the single axis/diagonal shape. Example `n=9` gives `(3,0)`.
- split prime powers `p^e`: exactly `floor(e/2)+1` unordered cells, but only one primitive quotient cell. Thus reverse recovery has no distinct primitive pair even when imprimitive cells also exist.
- all split exponents even: the complement action has one fixed cell. It is axis/diagonal according to `v_2(n)` parity, not an uncorrected generic orbit.
- signs, swap, unit rotations, or conjugation of one cell do not provide a second quotient state. Using `(8,1)` and its swapped ordered copy `(1,8)` at `n=65` gives only the trivial partition `{1,65}`.
- equal nonprimitive scale can be repaired only by explicitly dividing both cells by their common gcd. At `n=260`, `(16,2)` and `(14,8)` both have scale `2`; division reduces to the primitive norm `65` and recovers `{5,13}`. Applying the primitive formula directly gives contaminated gcds `{20,52}` with gcd `4`.
- unequal nonprimitive scales do not reduce to two primitive states of a common norm. At `n=25`, `(5,0)` and `(4,3)` have scales `5` and `1`; all raw bilinear gcds are `5`, not a coprime complementary partition.
- for primitive even `n`, omitting division by `t=2` is false. The smallest distinct-pair example is `n=130`, cells `(9,7)` and `(11,3)`: correct normalization recovers `{5,13}` from core `65`, while the flawed rule returns `{10,26}` against `130`.
- repeated split-prime exponents cause no failure. Reverse recovery partitions whole prime-power blocks between `A` and `B`; it does not split the exponent of one rational prime between the two recovered coprime factors.

### Classical Boundary

The existence theorem, Gaussian unique factorization, split/inert/ramified prime behavior, and norm-composition identity are classical. The independently established overlay package consists of choosing the split-core divisor lattice as the exact factor object, identifying the single global complement quotient, deriving its fixed-point corrections, deriving the common-scale formula, specifying the complete recursive generator, and proving the factorization-free reverse gcd recovery from two primitive quotient states.

This makes the third-sector construction an exact arithmetic presentation and computational index after normalization. It does not make the multiplicative readout native geometry, and it does not establish historical novelty.

### Final Classification

`FULL_BIDIRECTIONAL_BRIDGE_INDEPENDENTLY_RECONSTRUCTED`

Forward status: exact bijection proved.

Generator status: soundness and completeness proved.

Reverse status: exact on every pair of distinct primitive quotient cells, with necessary hypotheses and parity normalization proved.

Naive full-`M(n)` and unnormalized variants: refuted by the declared scope and smallest controls above.

## 5. Exact Validation and Evidence

The independent checker is `experiments/third_sector_factor_phase_independent_checker.py`. Its modules are separated by construction:

1. `direct_cells` enumerates `a>=b>=0` without factoring `n`.
2. `factor_driven_records` factors `n`, recursively builds Gaussian products, and never consults `direct_cells`.
3. `reverse_recovery` receives two cells and uses only their norm, bilinear integer arithmetic, parity division, and gcd. It contains no factorization call. Factorization appears only outside it for forward generation and validation orchestration.

Frozen run:

- direct-versus-factor range: every `0<=n<=4096`;
- reverse range: every `1<=n<=20000` and every pair of distinct primitive normalized cells;
- forward mismatches: `0`;
- count mismatches: `0`;
- scale mismatches: `0`;
- injectivity/duplicate mismatches: `0`;
- fixed-point kind mismatches: `0`;
- reverse pairs checked: `2028`;
- reverse failures: `0`;
- normalized direct cell-map SHA-256: `2f918b91795a79dd7b4d3fa3951e262917a36bf5cef3c63920c27f33ec4d42f1`;
- normalized factor cell-map SHA-256: `2f918b91795a79dd7b4d3fa3951e262917a36bf5cef3c63920c27f33ec4d42f1`;
- normalized reverse-result SHA-256: `4d96fe911d42dd87fecaab057d1e1ab09dba64617a98578c59b05ef3abf44306`;
- odd-inert negative control: smallest mismatch `n=3`;
- removed-2-adic negative control: smallest even primitive pair `n=130`, flawed factors `{10,26}` versus correct `{5,13}`.

The first development run reported 391 tuple mismatches because the direct module emitted cells in increasing-`b` order while the factor module emitted lexicographic order. Counts, scales, injectivity, and fixed points were already zero-mismatch. The checker was corrected so each module freezes its own lexicographically normalized output before comparison; the retained set comparison then had zero mismatches. This normalization bug is disclosed rather than presented as mathematical evidence.

Generated evidence:

- `research_output/THIRD_SECTOR_FACTOR_PHASE_TEST_CORPUS_20260823.csv`;
- `research_output/evidence/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.jsonl`;
- `research_output/reducer_results/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_REDUCER_20260823.md`;
- `research_output/THIRD_SECTOR_FACTOR_PHASE_QUOTIENT_DICTIONARY_20260823.md`.

Finite zero mismatch does not prove the theorems. The proofs in Section 4 establish the infinite claims; the checker independently attacks implementation errors, normalization errors, and small/degenerate cases.

## 6. Limitations, Closure, and Next Action

The forward generator presupposes ordinary integer factorization and canonical two-square decomposition of each split prime. It is therefore a complete factor-driven generator, not a claim that factorization is free.

The reverse algorithm does not presuppose factorization, but it requires two genuinely distinct primitive quotient cells. With one representation, repeated symmetry copies, or nonprimitive inputs lacking a common normalization, it cannot be promoted to the retained theorem.

The exact bridge is to `M(C)` (or equivalently `Div(C)`), not generally to all of `M(n)`. Factors removed in forming `C` remain visible in the additive common scale `h`, so no arithmetic information used by the square cells is silently discarded.

The independent report stops at the source-comparison boundary. No comparison with withheld event `f0f59174a29b25ff541da5738ed1539c7df7cf78` was performed. The package is internally closed and ready for Driver-side comparison or promotion as one atomic proof/checker/corpus/dictionary/evidence unit.
