# BRC base-branch dominance criteria

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note does not allocate a new Researcher identity and does not change formal D24/UR ownership. It is a portable auxiliary unit while control issue #1511 remains unresolved.

## 1. Consumed cocycle

For a finite exponent vector `m`, retain the exact branch-gain cocycle

`Gamma_p(m)=E_p(m)+D_p(m)-C_p(m)+F_p(m)`,

with endpoint, denominator, cancellation, and factorial provenance kept separate until the observer is fixed.

The finite candidate theorem already says only positive-credit target primes need be considered for uniform earliest visibility. This note gives two family-level dominance rules that discard many such candidates without evaluating every branch separately.

## 2. Factorial monotonicity lemma

If `q<p` are primes, then for every `n>=0`,

`v_q(n!) >= v_p(n!)`.

Indeed, Legendre gives

`v_q(n!)=sum_(k>=1) floor(n/q^k)`,

`v_p(n!)=sum_(k>=1) floor(n/p^k)`.

Since `q^k<p^k` termwise, each summand for `q` is at least the corresponding summand for `p`.

Thus a smaller base branch never loses factorial credit to a larger target prime.

## 3. Class `13 mod 24`: branch 13 dominance away from two escape mechanisms

Let `p>13` be a target prime with

`p == 13 (mod 24)`.

Then `p-1` is divisible by `12`, so

`h_p=(p-1)/2`

is divisible by `6`, the primitive endpoint period for `p=13`.

Therefore every p-endpoint is automatically a 13-endpoint:

`H_13(j) >= H_p(j)`

for every port `j`.

The class-13 cancellation progression for the base prime `13` is

`j == 3 (mod 6)`,

because `ord_13(4)=6` and `s_13=3`.

### Theorem 3.1

Suppose the occupied support of `m` satisfies both:

1. `p` divides no occupied port index `j`;
2. no occupied port lies on the base-13 cancellation progression `j == 3 (mod 6)`.

Then

`Gamma_13(m) >= Gamma_p(m)`.

Hence branch `p` cannot improve the uniform first-visible horizon beyond branch `13` for such a monomial.

### Proof

Compare the four cocycle channels.

Endpoint:

`E_13(m) >= E_p(m)`

because every p-endpoint is a 13-endpoint.

Denominator:

`D_p(m)=0`

by assumption, while `D_13(m)>=0`.

Cancellation:

`C_13(m)=0`

by the support restriction, while `C_p(m)>=0`. Since cancellation enters with a minus sign,

`-C_13(m) >= -C_p(m)`.

Factorial:

`F_13(m)>=F_p(m)`

by factorial monotonicity.

Adding the four inequalities yields the claim.

### Corollary 3.2 — exact escape mechanisms

If a higher class-13 branch strictly beats branch `13`, then at least one of the following must occur in the occupied support:

- an own-denominator port: `p|j` for some occupied `j`;
- a base-13 cancellation port: `j == 3 (mod 6)` for some occupied `j`.

Thus higher `13 mod24` branches have only two mechanisms by which they can escape base-13 dominance.

Both restrictions are genuine:

- `p=37, m=e_37`: the own denominator lets branch 37 beat branch 13;
- `p=37, m=e_3`: branch 13 is cancellation-delayed while branch 37 is not, so branch 37 again wins.

## 4. Class `19 mod 72`: branch 19 dominance away from own denominators

Now let `p>19` be a target prime with

`p == 19 (mod 72)`.

Then

`h_p=(p-1)/2`

is divisible by `9`, the primitive endpoint period for branch `19`. Hence

`H_19(j) >= H_p(j)`

for every `j`.

Both primes lie in class `19 mod24`, so neither branch has source-coefficient cancellation:

`C_19(m)=C_p(m)=0`.

### Theorem 4.1

If `p` divides no occupied port index of `m`, then

`Gamma_19(m) >= Gamma_p(m)`.

### Proof

Endpoint dominance gives `E_19>=E_p`.

The support restriction gives `D_p=0`, while `D_19>=0`.

Both cancellation terms vanish.

Factorial monotonicity gives `F_19>=F_p`.

Therefore `Gamma_19>=Gamma_p`.

### Corollary 4.2

For every `p == 19 (mod72)`, `p>19`, a strict gain advantage over branch 19 requires at least one occupied own-denominator port `p|j`.

The restriction is genuine: for `p=163`, the singleton `e_163` gains one denominator unit on branch 163 while branch 19 has no matching endpoint or denominator credit there.

## 5. Relation to first-entry redundancy

Earlier first-entry results observed:

- all higher `13 mod24` branches are redundant at their primitive endpoint against branch 13;
- `19 mod72` branches are redundant at their primitive endpoint against branch 19.

The present theorem lifts those observations from one singleton to whole families of exponent vectors. The only ways to escape are now provenance-explicit:

- class `13 mod24`: own p-denominator ports or base-13 cancellation fibers;
- class `19 mod72`: own p-denominator ports.

This is a candidate-dominance theorem, not merely a first-horizon coincidence.

## 6. BRC safe quotient

For the observer `UNIFORM_EARLIEST_VISIBILITY`, the componentwise cocycle comparison proves a safe dominance quotient: a dominated branch may be omitted when the stated support hypotheses hold.

For `EXACT_PER_PRIME_SUPPORT`, the dominated branch must still be retained because its exact pruning/addition pattern and provenance may differ even when it cannot win the uniform earliest-visibility competition.

In particular, the base-13 cancellation restriction must remain explicit; erasing that provenance would make Theorem 3.1 false.

## 7. Exact falsification

Checker:

`research_checks/check_brc_base_branch_dominance_20260924.py`

Checker commit:

`e66dcafd42e08b8bada4b1fe306fdfcfa7e78da5`.

The locally executed checker passed before publication. Regression summary:

- higher class-13 target primes checked below `2000`: `39`;
- higher `19 mod72` target primes checked below `3000`: `17`;
- endpoint-dominance checks: `17920`;
- factorial-monotonicity checks: `10136`;
- class-13 monomials satisfying the theorem hypotheses: `39000`;
- class-19mod72 monomials satisfying the theorem hypotheses: `17000`;
- failures: `0`.

It also fixes the three restriction witnesses `37:e_37`, `37:e_3`, and `163:e_163`.

Finite computation is falsification/regression only. The proof is the exact componentwise comparison of the BRC gain channels.

## 8. Do not repeat / next

Do not re-test higher class-13 branches against branch 13 on supports that avoid both escape mechanisms, and do not re-test `19 mod72` branches against branch 19 on supports avoiding their own denominator ports. Those candidates are now provably dominated for the uniform observer.

If formal D24 control remains blocked, the next nonredundant auxiliary question is to classify the remaining escape-support families themselves: quantify when an own-denominator credit is large enough to overcome base-branch endpoint/factorial advantages, and when a base-13 cancellation fiber is sufficient to make a higher class-13 branch genuinely dominant.

If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary compiler work and resume the Source-native D24 frontier through the lawful successor identity, preserving the existing Source checkpoint and native frontier exactly.
