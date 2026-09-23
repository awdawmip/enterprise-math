# BRC base-13 cancellation escape witness

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes `brc_base_branch_dominance_20260924.md` and `brc_uniform_union_record_automaton_20260924.md`. It resolves the smallest mixed support showing when the base-13 cancellation escape mechanism is not merely enough to beat branch 13, but enough to create a genuinely new uniform-union horizon.

## 1. Exact setup

For a finite exponent vector `m`, retain

`Delta_p(m)=W_inf(m)-W_p(m)`

with the exact endpoint / denominator / source-coefficient-cancellation / factorial cocycle.

For every target prime `p>13` with

`p == 13 (mod24)`,

write

`h=(p-1)/2`.

Then `h` is divisible by `6`, so `h` is always a branch-13 endpoint.

Consider the mixed two-port monomial

`m_p = e_3 + e_h`.

The port `j=3` is the primitive branch-13 cancellation fiber because

`1+4^3=65=5*13`

and `c_13=v_13(65)=1`.

## 2. Exact defect identities

### Lemma 2.1 — branch p

For every `p>13`, `p ==13 (mod24)`,

`Delta_p(m_p)=1`.

### Proof

At `j=h`, branch p has exactly one endpoint credit. Since `h<p`, there is no p-denominator credit. The endpoint and p-cancellation progressions are disjoint.

At `j=3`, branch p has no endpoint and no denominator. It also has no source-coefficient cancellation: if a target prime `p>13` cancelled `1+4^3`, then `p` would divide `65`, impossible.

Both multiplicities are one, so factorial credit is zero. Hence only the primitive p-endpoint contributes and the total defect is one.

### Lemma 2.2 — branch 13

`Delta_13(m_p)=v_13(h)`.

### Proof

At `j=3`, branch 13 has cancellation defect `-c_13=-1`.

At `j=h`, because `6|h`, branch 13 has endpoint credit `+1`. The port is not on the branch-13 cancellation progression because `h ==0 (mod6)`, not `3 (mod6)`. It also contributes denominator credit `v_13(h)`.

Thus

`Delta_13(m_p) = -1 + (1+v_13(h)) = v_13(h)`.

This exposes a subtlety missed by a Boolean endpoint comparison: if `13|h`, the base branch keeps a positive record even after its cancellation penalty is paid.

### Lemma 2.3 — every other earlier target branch

For every target prime `q!=13`,

`Delta_q(e_3)=0`.

Therefore

`Delta_q(m_p)=Delta_q(e_h)`.

Indeed, a target q cannot divide 3, cannot have `(q-1)/2|3`, and only class `13 mod24` branches have source-coefficient cancellation; a class-13 q cancelling at j=3 would divide `1+4^3=65`, leaving only q=13 among target primes.

## 3. Exact uniform-novelty criterion

By the uniform-union record automaton, branch p contributes a genuinely new horizon through `m_p` iff its defect 1 is larger than every previous branch record and the generic record 0.

Combining the three lemmas gives:

### Theorem 3.1

For `p>13`, `p ==13 (mod24)`, with `h=(p-1)/2`, the mixed witness

`m_p=e_3+e_h`

is uniformly new at branch p **iff** both conditions hold:

1. `13` does not divide `h`;
2. no smaller target prime `q<p`, `q!=13`, has positive singleton defect on `e_h`.

Using the previously proved singleton coverage criterion, condition 2 is equivalent to saying that no such q satisfies either

- `(q-1)/2 | h`, or
- `q | h` with the q-denominator event not neutralized by q's class-13 coefficient cancellation.

### Proof

Branch p has defect exactly 1.

Branch 13 contributes exactly `v_13(h)`, so it blocks novelty precisely when `13|h`.

Every other smaller target branch sees `e_3` neutrally, hence its defect on `m_p` equals its defect on the primitive endpoint singleton `e_h`. Therefore no such branch blocks the record precisely when none has positive singleton defect on `h`.

The stated two conditions are thus equivalent to previous record defect zero, so p raises the record from 0 to 1.

## 4. Exact new horizon

The generic weight is

`W_inf(m_p)=g(3)+g(h)=7+(2h+1)=p+7`.

When Theorem 3.1 applies, p lowers the weight by exactly one:

`W_p(m_p)=p+6`.

Hence the branch creates exactly one new integer visibility horizon:

`N=p+7`.

This is the minimal mixed manifestation of the base-13 cancellation escape mechanism: the cancellation port erases branch 13's primitive endpoint advantage, allowing the higher p-endpoint to become the first visible carrier when no other smaller target branch already covers it.

The first example is

`p=61, h=30, m=e_3+e_30`.

Here branch 13 has defect 0, branch 61 has defect 1, and all earlier target branches have defect 0; the new horizon is `N=68`.

## 5. Relation to the two escape mechanisms

The previous base-branch dominance theorem said a higher `13 mod24` branch can beat branch 13 only through either:

- an own-denominator port, or
- a base-13 cancellation fiber.

The uniform record automaton now sharpens both minimal mechanisms:

1. **Own denominator:** the singleton `e_p` is always uniformly new and uniquely sourced by p, first visible at `N=2p+1`.
2. **Base-13 cancellation fiber:** the cancellation port alone is record-neutral. The minimal mixed pair `e_3+e_h` is uniformly new exactly under Theorem 3.1, first visible at `N=p+7`.

So merely escaping base-13 dominance is strictly weaker than creating a new union horizon.

## 6. Finite falsification/regression

Checker:

`research_checks/check_brc_base13_cancellation_escape_witness_20260924.py`

Checker publication commit:

`ab5302747bacb896b35acf9ab288c692a4924c3a`.

For all `82` target primes `13<p<5000` with `p ==13 (mod24)`, the checker independently verified:

- `Delta_p(e_3+e_h)=1`;
- `Delta_13(e_3+e_h)=v_13(h)`;
- `Delta_q(e_3)=0` for every target q other than 13;
- Theorem 3.1's arithmetic criterion exactly matches brute record novelty over all smaller target branches.

Failures: `0`.

Finite census below 5000: `20` of the 82 higher class-13 primes have a uniform-new minimal mixed witness. They are

`61, 349, 373, 709, 853, 877, 1069, 1213, 1789, 2293, 2389, 2677, 2797, 3229, 3373, 3469, 3517, 4597, 4813, 4909`.

This list is a finite census, not an infinitude or density theorem.

## 7. BRC meaning / do not repeat

For the observer `UNIFORM_EARLIEST_VISIBILITY`, a base-13 cancellation fiber is not itself positive mass; it removes negative branch-13 credit and can expose another branch's positive endpoint/denominator/factorial carrier. Preserve those sources separately until the record observer is fixed.

Do not use the statement “higher p beats branch 13” as a synonym for “higher p is uniform-new”. The latter is exactly a record comparison.

The next nonredundant auxiliary problem, only while formal D24 control remains blocked, is to generalize Theorem 3.1 from the minimal pair `e_3+e_h` to arbitrary cancellation-fiber multiplicity/support and derive a closed record inequality against the finite candidate set. If #1511 deploys a lawful lossless rollover/disposition operation, stop auxiliary work and resume the Source-native D24 frontier first.
