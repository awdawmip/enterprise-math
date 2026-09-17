# PCF7 fixed-probe zero-value statement correction — Research Return

Status: `SUCCESS / RESEARCH RETURN FROZEN / AWAITING INDEPENDENT DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`  
Publication-ID: `TP2-1C146C521C5946742C17`  
Researcher-ID: `EM-PCF7FIX-B603FA`  
Claim-ID: `CLM-PCF7FIX-0BFF2D2CD73646AD`  
Execution record: `ER-E90FEF513B0AEE96C73E`

## 1. Exact correction

The original PCF7 Section 7 sentence overstates the fixed-probe regression when it says that after choosing semiprime factors away from all **nonzero** fixed-probe prime supports, “every gcd is `1`.” The sixth-power family contains the zero probe

\[
|1^6-1|=0,
\]

so for every integer `N>1`,

\[
\gcd(N,0)=N.
\]

The corrected fixed-family statement is therefore:

- if a fixed probe value `a != 0` and the prime support of `a` is avoided by the chosen semiprime factors, then `gcd(N,a)=1`;
- if `a=0`, then `gcd(N,a)=N`;
- hence every fixed-probe output in the support-avoidance construction is trivial, lying in `{1,N}`, and no proper factor is returned.

This is the entire authorized mathematical delta.

## 2. Proof of the corrected statement

Let `N=pq>1` be one of the fixed-family support-avoidance semiprimes.

For a nonzero fixed probe `a`, the construction chooses `p,q` outside the prime support of every nonzero fixed probe. Thus neither `p` nor `q` divides `a`, so `gcd(N,a)=1`.

For a zero fixed probe, the defining property of gcd gives `gcd(N,0)=N`.

Therefore every output is either the unit gcd `1` or the whole modulus `N`. Neither satisfies `1<gcd(N,a)<N`, so no proper factor occurs. ∎

## 3. BRC statement audit

The local defect is a type-collapse error: the original prose projected both `a=0` and `a!=0` support-avoiding probes into one “outside prime support => gcd 1” description. The missing carrier bit is `ZERO_FLAG(a)=[a=0]`.

Restoring that distinction produces two typed trivial-output branches:

- `ZERO_FLAG=0` plus avoided prime support -> unit output `1`;
- `ZERO_FLAG=1` -> whole-object output `N`.

The proper-factor observable remains false in both branches. No relation, campaign, complexity, benchmark, or provenance type outside this local fixed-probe sentence changes.

## 4. Frozen conclusions preserved

Unchanged from the frozen PCF7 result and its Driver revision boundary:

1. Theorem 6.1: every polynomial public-prefix cap admits infinitely many balanced semiprimes on which every allowed PCF4 public-prefix gcd is `1`.
2. The declared polynomial-prefix campaign model therefore has exact worst-case proper-split probability `0`; repetition does not change a zero one-trial probability.
3. The `L=N` recurrence classification remains `Omega(N)=Omega(2^(n-1))` recurrence stages before the final gcd under the frozen implementation, hence square-root scale or worse in the task-local comparison.
4. T1–T5 are unchanged in theorem strength; T5 is read with the corrected trivial-output `{1,N}` distinction.
5. The PCF2 89-case benchmark remains sealed and is not regenerated or mutated.
6. No generic factorization speedup, universal factoring lower bound, Working Truth, Foundation promotion, or canonical-promotion claim is introduced.

## 5. Deterministic checker replay

The existing checker already encodes the correct distinction: `fixed_probe_values()` removes zero values from support construction and the fixed-probe assertion is guarded by `if v:`. Its bytes were preserved exactly.

Source checker:
`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

- Git blob SHA-1: `b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`
- raw SHA-256: `8a878f62fd213177036d14704dcd4efd19cad5b7e6f40dd96f3f91531b3492d9`
- local runtime: `Python 3.13.5`
- replay command: `python3 research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`
- exit code: `0`
- stdout: `PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

An independent task-local statement audit also passed over all `N=2..500` and `a=-50..50` (50,399 pairs), plus six explicit zero-probe examples including the checker witness modulus. It verified that `a=0` returns `N`, support-disjoint/nonzero unit cases return `1`, and neither branch is a proper factor.

## 6. Research disposition

Hard target:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`

Researcher disposition: `SUCCESS / HANDOFF FOR INDEPENDENT DRIVER REVIEW`.

No independent acceptance is asserted here. The next legal action is Driver review of this current-generation Result at the exact local statement-correction boundary.
