# Native execution of the complete optimal phase family

Status: author integration evidence, not independent Review. Researcher `EM-DIRECT-970E1C`; Activity `RA-D2EC212845B63844081F9A14`.

The mathematical phase classification is proved in the companion staircase and observer notes. This integration checks the actual pinned native state update and residue readouts for every one of the twelve nested-optimal phase dictionaries, and for the least positive root of that classified subclass.

The native source is frozen at `b1efc6c805661ed7b476e6e730107da6043176ee`; the four module Git blobs are recorded in the original base certificate and in `native_certificate.json`. The executed packet is

```python
EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
```

Its weight and multiplicity are both one. Packet composition gives the even update `4*x+3`. Starting from `a*a-1`, each actual step equals `a*a*2**n-1` exactly. Every selected prime residue is read with the native `euclidean_digits` implementation and reconstructed with its quotient to check the integer division identity.

For each parity choice and each bijection between `{11,61,331}` and categories `{0,1,4}`, the verifier constructs one CRT root using positive inverse signs. It executes 420 updates and 25 prime readouts per update. It checks that every old readout equals the old-root readout, every new zero agrees with its derived exact phase, and each divisor recorded as a hit is proper.

It also executes the separately classified least positive root

\[
39741911323337250951212360989279347168190786597922987443929
\]

with the ordered chain `5,13,61,11,331`.

Across all thirteen runs, the recorded totals are:

| Check | Count |
|---|---:|
| Actual native updates | 5,460 |
| Native prime readouts | 136,500 |
| Equalities with old-root readouts | 109,200 |
| Phase dictionaries exercised | 12 |
| Additional least-root run | 1 |

Every run gives the uncovered counts

\[
(72,36,13,8,3,0)
\]

over one exponent period of length 420 as the first zero through five channels are included. The four-channel holes are `{128,308,368}` for parity0 and `{98,158,338}` for parity1.

This finite period is sufficient for these coverage observables because the established old-hole predicate has period210 in n, while all five new zero phases have base-2 orders dividing60. Their least common multiple is420. The previous full old trajectory evidence is reused; a finite run alone is not presented as a proof of the infinite claim.

Changing any of the five root-residue signs leaves its square and every readout at that prime unchanged. CRT makes these signs independent, accounting for all32 sign choices per phase dictionary. The observer certificate supplies the full384-root-class enumeration and least-root comparison; this native execution checks membership and state semantics, not minimality by itself.

The fixed X6 anchor and typed integer state remain intact. The index n labels arithmetic updates, not physical time. Prime observations are readout channels, not extra spatial axes or native branches. The finite observer is used only for the specific predicates for which sufficiency is proved; full integer and joint-cofactor information remain available for covering-cost questions.

Reproduce with `python verify_native.py`, optionally supplying `--source-dir` for the pinned native source. The default finds the existing `src` or `vendor_src` folder.
