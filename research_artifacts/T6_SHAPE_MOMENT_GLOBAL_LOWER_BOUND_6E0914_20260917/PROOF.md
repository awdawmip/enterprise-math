# T6 maximal-p=19 vertical order 9: exact clearance of split (3,6)

Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`  
Publication: `TP2-34B106D2512A298C9647`  
Claim: `CLM-T6SM-6E0914-20260917T1340Z`  
Researcher-ID: `EM-DIRECT-6E0914`  
Status: `EXACT PROGRESS / (3,6) BLOCK CLEARED / (4,5) REMAINS`

## Scope

This certificate begins at the accepted durable frontier: maximal prime `p=19`, vertical orders `0,...,8` are already closed at separate side exponent-mass budget 2331.  It does not replay those layers.  It treats only vertical order 9, split `(3,6)` up to global sign.  The other order-9 split `(4,5)` is not claimed here.

The BRC carrier remains the exact signed exponent/valuation state.  No prime-only, total-mass-only, logarithmic, or floating-point quotient is used as theorem evidence.

## Exact carrier

For the `p=19` layer, write a denominator as `19m`, with vertical representatives

`m = r + 19q`, `1 <= r <= 18`, `q >= 0`.

The q0 exponent-mass weight is

`w_r = 19r - 1`,

and every vertical unit raises exponent mass by exactly `19^2 = 361`.

For q0 signed multiplicities `u=(u_1,...,u_18)`, the homogeneous saturated congruence lattice is

`L0 = {u in Z^18 : sum_r u_r r^(-k) == 0 mod 19^k, k=1,...,6}`.

The builder reconstructs this lattice by six exact sequential saturations.  Their indices are

`19, 19^2, 19^3, 19^4, 19^5, 19^6`,

so `[Z^18:L0]=19^21` exactly.  The generated basis is independently checked against all six congruences.

For a fixed positive vertical state `V+` and negative vertical state `V-`, the q0 completion lies in the affine congruence class

`sum_r u_r r^(-k) == -sum_{(q,r) in V+}(r+19q)^(-k) + sum_{(q,r) in V-}(r+19q)^(-k)  (mod 19^k)`

for every `k=1,...,6`.

The checker constructs an exact particular representative of this affine class; no floating approximation enters this step.

## Exhaustive vertical states

At one-side budget 2331, the exact state enumerator reproduces the accepted state counts

- order 2: 189;
- order 3: 1,482;
- order 4: 8,124;
- order 5: 8,506;
- order 6: 262.

For split `(3,6)`, common identical vertical atoms are cancelled before q0 completion.  Exactly

`335,374`

primitive disjoint affine cosets remain.

For every such coset, after subtracting fixed vertical masses, the total available q0 weighted l1 mass is at most

`R = B+ + B- <= 1377`.

Any side-feasible q0 completion therefore obeys

`||W u||_2 <= ||W u||_1 <= R`,

where `W=diag(18,37,...,341)`.

## Exact flatness certificate

The homogeneous weighted lattice `W L0` is put into a deterministic exact LLL-equivalent integer row basis with `delta=99/100`.  The builder verifies that the LLL transform is integral unimodular (`|det|=1`).  It then computes exact rational Gram-Schmidt squared lengths `D_i`.

For every `i`,

`D_i > 4*1377^2 = 7,584,516`.

The minimum exact diagonal is recorded in `order9_36_certificate.json` as numerator/denominator, so this inequality is checked by integer cross multiplication.

Consequently every Fincke-Pohst coordinate interval inside any radius-`R` ball has length strictly less than one integer spacing.  Thus each affine coset has **at most one** q0 lattice point that could lie in its permitted weighted Euclidean ball.  That point, if it exists, is the exact nearest-plane candidate obtained by the triangular rational Gram-Schmidt recursion.

The generated C++ checker evaluates that recursion with `boost::multiprecision::cpp_int`.  All rational coefficients are converted by the builder to fixed exact integer numerators over exact positive common denominators.  Floating point is not used.

## Exhaustive result

Local exact verification output:

```text
primitive_cosets=335374
sphere_hits=0
side_hits=0
min_gap=5631420
min_norm2=6522556
min_bound=944
min_pair=519,138
```

`sphere_hits=0` means that in **every** primitive `(3,6)` affine coset, even the unique nearest-plane candidate is outside the necessary weighted Euclidean ball.  Therefore no side-feasible q0 completion exists.

Hence

`MAXIMAL_P19_VERTICAL_ORDER9_SPLIT_3_6_EMPTY_AT_SIDE_MASS_2331`.

This is a strict frontier advance only.  It does **not** close vertical order 9 because split `(4,5)` remains.

## Reproduction

From this artifact directory:

```bash
python check_order9_36.py --out-dir ./repro
```

The script reconstructs the lattice and state census from first principles, generates `order9_36_exact_checker.cpp`, compiles it with `g++ -O3 -std=c++17`, executes the exact multiprecision audit, and checks the expected output.  The certificate records the generated C++ SHA-256.

The successful local run used Python 3, SymPy, g++ and Boost multiprecision.  No GitHub-hosted computation was used for the mathematical verification.

## Next exact unit

Continue vertical order 9 with split `(4,5)` using the same saturated affine-lattice carrier and exact flatness certificate.  If that block is empty, order 9 is globally closed and the task proceeds to orders 10--12 as specified by the fixed taskbook.
