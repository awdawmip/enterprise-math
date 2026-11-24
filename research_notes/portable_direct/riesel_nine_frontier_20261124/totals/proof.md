# Exact unrestricted total costs of four compact roots

Research continuation, 2026-11-24, Asia/Hong_Kong. Researcher `EM-DIRECT-970E1C / TASK_RESEARCH`; Activity `RA-D2EC212845B63844081F9A14`. Author proof and exact computation, with collaborative checking; independent project Review and formal proof acceptance are not claimed.

## 1. What is strengthened

Keep the full integer trajectory

\[
F_n(a)=a^2 2^n-1
\]

and the old twenty-prime dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

Here \(\delta_P(a)\) is the minimum number of supplementary primes needed with P to cover every positive-index term by a proper prime divisor. The unrestricted minimum number of primes is \(\tau(a^2)\). All upper covers below also cover index zero; all lower-bound witnesses have positive indices. Thus both index conventions give the same displayed values.

The preceding papers had proved the minimum-root scopes in the following table, and total-cost upper bounds. This note proves the matching unrestricted lower bounds for the original compact integers, without changing them.

| Root | Digits | Minimum scope | Exact supplementary cost | Exact total cost |
|---|---:|---|---:|---:|
| \(a_6\) | 76 | All \(a\in R_1\) with \(\delta_P(a)=6\) | 6 | **26** |
| \(a_7\) | 84 | All \(a\in R_2\) with \(\delta_P(a)=7\) | 7 | **27** |
| \(a_8\) | 146 | All \(a\in R_3\) with \(\delta_P(a)=8\) | 8 | **28** |
| \(a_9^{Q_7}\) | 156 | All exact-cost-nine roots in \(R_3\) admitting a nine-prime supplement containing \(Q_7\) | 9 | **29** |

The last row has the explicitly restricted scope

\[
Q_7=\{5,13,19,73,38737,246241,487824887233\}.
\]

Its minimum theorem is the current two-tail classification, `../tail/proof.md`. It is not a minimum over the full cost-nine class in R3. None of the four minimum scopes is replaced by a minimum over all coefficients with a prescribed unrestricted total cost.

The exact roots are:

```text
a6 = 1597463687996365290740241630260436015028835427889255944107518938773290244463

a7 = 168515727251568031139784117408423468924151126118048106286760549300706338389494633573

a8 = 25391491002591320391732108159477707323814206756039394016382357924666368039179689189103105696777816709091120408108658618711788120139363377072408503

a9_Q7 = 112755110470612891256156246069109596727720684467884590849485136661471023397130974501713495184000901218767521913670185762743636668514043005915407753161112053
```

The old minimum statements are reused from these immutable sources:

- `awdawmip/enterprise-math@f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5:research_notes/portable_direct/riesel_finite_observers_20261124/six/proof.md`, section 6.
- `awdawmip/enterprise-math@cadc7197ec1f1169aba937894a5988e05ed5ed24:research_notes/portable_direct/riesel_seven_cover_20261124/observer/proof.md`, section 7.
- `awdawmip/enterprise-math@e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124/minimum/proof.md`.

## 2. A finite witness proves an unrestricted lower bound

**Lemma.** Let a be an integer. If m positive-index terms

\[
F_{n_1}(a),\ldots,F_{n_m}(a)>1
\]

are pairwise coprime, then every prime dictionary covering the full sequence contains at least m primes.

**Proof.** Pick a covering prime divisor for each displayed term. If the same prime were picked for two distinct terms, it would divide their greatest common divisor. That gcd is one. Hence all m picked primes are different. This applies to every possible prime dictionary, without a bound on prime size, order, or the indices it might cover. \(\square\)

In particular, if a full dictionary P union Q has size m=20+s and such m witnesses exist, then

\[
\tau(a^2)=20+s,
\qquad
\delta_P(a)=s.
\]

Indeed, the displayed dictionary gives both upper bounds. A supplement of fewer than s primes would, when adjoined to all twenty old primes, give a total cover of fewer than m primes. The lemma rules this out. Therefore the exact costs in this note are independently certified by the finite witnesses and periodic upper covers; their numerical equalities do not depend on the previous complete classifications. Those classifications are used only for the minimum-root ranges in section 1.

Private terms for a selected dictionary by themselves prove only that dictionary's irredundancy. The decisive strengthening here is that the chosen full integer terms are pairwise coprime, including all unlisted possible factors. The root stays fixed while the witness indices are chosen to avoid shared divisors.

## 3. Explicit upper dictionaries and complete verification domain

The supplements, in addition to P, are

| Root | Supplement Q |
|---|---|
| \(a_6\) | 5, 13, 19, 73, 433, 38737 |
| \(a_7\) | 5, 13, 19, 73, 181, 631, 23311 |
| \(a_8\) | 5, 13, 19, 73, 38737, 487824887233, 1153, 193 |
| \(a_9^{Q_7}\) | 5, 13, 19, 73, 38737, 246241, 487824887233, 33975937, 4261383649 |

The checker proves primality of every selected prime by deterministic trial division through its square root. It computes the exact multiplicative order of 2 by the first return to one, then computes the unique zero phase of \(a^2 2^n-1\) for each selected prime.

For the first three dictionaries, the least common multiple of all selected prime orders is 20,160. For the fourth it is 60,480. The checker covers every residue in the corresponding full period by the selected phase classes. All four roots satisfy \(a^2-1>\max(P\cup Q)\), so every divisibility used is by a proper prime factor at every nonnegative index.

This is an exact finite verification of a periodic upper-cover statement. It supplies the upper bounds for the entire sequence; the finite witness lemma supplies the lower bounds for every possible dictionary.

## 4. Small witness intervals and actual native execution

The pairwise-coprime witnesses lie in the following positive index intervals:

| Root | Witness count | Greatest witness index | Pairwise gcds equal to one |
|---|---:|---:|---:|
| \(a_6\) | 26 | 773 | 325 |
| \(a_7\) | 27 | 1,133 | 351 |
| \(a_8\) | 28 | 2,480 | 378 |
| \(a_9^{Q_7}\) | 29 | 2,048 | 406 |
| Total | 110 | — | 1,460 |

The exact (selected prime, index) pairs are embedded in `verify_exact_totals.py` and repeated in `exact_total_certificate.json`, which also retains every full integer witness and its selected-prime cofactor in hexadecimal. A reader can verify the unrestricted lower bounds simply by reconstructing these integers from the four roots and the listed indices and computing the indicated gcds; their prime factorizations are unnecessary.

The same terms were actually produced by the frozen native implementation

`awdawmip/enterprise-math@b1efc6c805661ed7b476e6e730107da6043176ee`.

The execution retains the fixed Heartbeat X6 anchor and the full typed integer register. It constructs the positive singleton BRC effect \(x\mapsto2x+1\), with weight and multiplicity one, and the composed effect \(x\mapsto4x+3\). The scalar closed formula is used to check the generated state. At each index, independent prime quotient/remainder readouts and a joint mixed-radix readout retain the cofactors; native recomposition recovers the complete integer.

Actual operations in this new four-root run were:

| Operation | Executed count |
|---|---:|
| Native one-step BRC updates | 6,434 |
| Native two-step composed evaluations | 3,216 |
| Independent native prime quotient/remainder readouts | 179,521 |
| Native joint readouts | 6,434 |
| Native joint recompositions | 6,434 |
| Retained native integer witnesses | 110 |
| Distinct pairwise gcd checks | 1,460 |

Each root's native execution stops at its last witness index. These native intervals are witness-production intervals, not complete covering periods. The complete periodic upper-cover check in section 3 is separately executed by the exact phase calculator. Thus neither the lower bound nor the upper bound is extrapolated from a partial native interval.

## 5. Reproduction

For arithmetic verification alone:

```sh
python verify_exact_totals.py
```

For the full native execution, supply the frozen package's parent directory:

```sh
python verify_exact_totals.py --source-dir /path/to/src
```

The four frozen module Git blob identities are embedded in the checker and are verified before import. The standard-library arithmetic checks do not depend on the native runtime. The saved certificate was generated with native execution enabled and finished with `PASS`.
