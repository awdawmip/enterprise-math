# PCF7 fixed-probe zero-value statement correction — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`  
Publication-ID: `TP2-C4DB35B43FE7334D2B63`  
Researcher-ID: `EM-PCF7FIX-EAA0A6`  
Claim-ID: `CLM-5CA35900B25ABC7BC61A`  
Execution record: `ER-2E488BC934B0630C3968`

## 1. Terminal verdict

`SUCCESS`

Hard target:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`

is met at the exact maintenance scope authorized by the taskbook.

The mathematical delta is one local statement correction only:

> For a fixed probe value `a`, if `a != 0` and both hidden primes avoid the prime support of `a`, then `gcd(N,a)=1`; if `a=0`, then `gcd(N,0)=N`. In either case the probe returns no proper factor.

No other PCF7 theorem, campaign model, benchmark, complexity classification, or factorization claim is changed.

## 2. Exact defect and correction

The frozen PCF7 return Section 7 formed the product `C` of all **nonzero** quadratic and sixth-power probe integers, then stated that primes `p,q` outside the finite prime support of `C` give `N=pq` “on which every gcd is 1.”

That sentence is correct for the frozen quadratic probe values but too strong for the sixth-power family.

For seeds `s=0,...,63`:

- `s^2+1 > 0`;
- `s^2+s+1 > 0`;
- `s^6+1 > 0`;
- `|s^6-1|=0` exactly when `s=1`.

Thus the frozen probe multiset contains exactly one zero value:

`|1^6-1|=0`.

For every positive modulus `N`,

`gcd(N,0)=N`.

Therefore the exact corrected fixed-family statement is as follows.

Let `C*` be the product of the absolute values of all **nonzero** frozen probe integers. Choose distinct primes `p,q` outside the finite prime support of `C*`, and set `N=pq`. Then:

1. for every nonzero frozen probe `a`, `gcd(N,a)=1`;
2. for every zero frozen probe, `gcd(N,0)=N`;
3. hence every returned gcd belongs to `{1,N}`;
4. consequently no probe returns a proper divisor `1<d<N`.

The infinite no-proper-split family therefore survives unchanged. The correction changes only the literal claim “every gcd is 1” to the exact trivial-output claim “every gcd is either 1 or N.”

## 3. Existing checker replay and byte-preservation decision

The existing deterministic checker is:

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Frozen Git-blob SHA-1:

`sha1:b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`

SHA-256:

`sha256:8a878f62fd213177036d14704dcd4efd19cad5b7e6f40dd96f3f91531b3492d9`

Its zero/nonzero semantics are already compatible with the corrected statement:

- `fixed_probe_values()` removes `0` before constructing the finite prime-support set;
- in the fixed-probe regression loop, the checker asserts `gcd(N2,v)==1` only under `if v`;
- it therefore never asserts the false identity `gcd(N,0)=1`.

An exact byte reconstruction was verified against the frozen Git-blob SHA-1 and replayed without changing checker bytes. Replay output:

`PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

The checker’s fixed-probe witness is `p=10007`, `q=10009`, hence

`N=100160063`.

For the unique zero probe at `s=1`,

`gcd(100160063, |1^6-1|)=gcd(100160063,0)=100160063`.

All nonzero fixed probes in the same witness remain coprime to `N`. This is exactly the corrected `{1,N}` trivial-output classification.

Because the source checker already enforces the correct nonzero-support logic, **no checker byte change is made**. The correction certificate binds the existing checker by both Git-blob SHA-1 and SHA-256.

## 4. Before/after statement audit

### Before

The overstrong Section 7 sentence effectively asserted:

`p,q outside supp(C*) => every fixed-family gcd = 1`.

### After

The exact statement is:

`p,q outside supp(C*) => nonzero probes give gcd 1, zero probes give gcd N, so no probe yields a proper factor`.

This is the entire mathematical delta.

The original T5 conclusion — that the frozen fixed public probes have infinitely many semiprime inputs with zero **proper-split** success — remains valid. Its proof now distinguishes the two trivial gcd outputs rather than incorrectly collapsing both to `1`.

## 5. Explicit unchanged boundaries

The following are unchanged:

1. PCF7 Theorem 6.1, the polynomial-prefix infinite balanced-semiprime obstruction;
2. exact worst-case proper-split probability `0` for the declared polynomial-prefix campaign model;
3. the `L=N` term-by-term recurrence-stage classification;
4. T1–T5 at their frozen no-proper-factor strength;
5. all 89-case PCF2 benchmark values and the sealed benchmark generation;
6. the prohibition on retrofitting a numerical PCF4 score into the sealed PCF2 benchmark;
7. the refusal to claim a generic factorization speedup or a universal factorization lower bound;
8. all Working Truth, Foundation, canonical-promotion and novelty boundaries.

No benchmark generation, new algorithm, new complexity lower bound, or new N-dependent theorem was introduced.

## 6. Evidence package

Correction certificate:

`research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_STATEMENT_CORRECTION/PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTION_CERTIFICATE_V1.json`

The certificate records the exact before/after audit, the unique zero probe, the source-checker dual digests, the deterministic replay output, the explicit finite witness, and the zero-math-drift guards.

## 7. Frozen disposition

Terminal task classification:

`SUCCESS / EXACT_LOCAL_STATEMENT_CORRECTION`

`MATHEMATICAL_DELTA = ONLY_FIXED_PROBE_ZERO_VALUE_STATEMENT`

Unresolved residue within this maintenance task:

`NONE`.

Next control-plane action: Driver review this correction at **local statement-repair strength only**. Acceptance must not be read as a new factorization theorem, lower bound, benchmark result, novelty claim, Working Truth, Foundation consequence, or canonical promotion.
