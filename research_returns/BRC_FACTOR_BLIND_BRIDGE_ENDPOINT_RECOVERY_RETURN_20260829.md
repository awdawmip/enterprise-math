# BRC Factor-Blind Bridge Endpoint Recovery — Research Return

Status: `FROZEN / ENDPOINT_BRIDGE_PRIOR_ART_EQUIVALENT`
Task-ID: `RS-BRC-FACTOR-BLIND-BRIDGE-ENDPOINT-RECOVERY`
Publication-ID: `TP2-963527C2A010BDF9E72F`
Researcher-ID: `EM-BRCFBBE0-A7C931`
Claim-ID: `chatgpt-brcfbbe0-20260829-1851-a7c931`
Execution branch: `research/brc-factor-blind-endpoint-recovery-em-brcfbbe0-a7c931`
Taskbook blob: `sha1:b8333721bc4ed6c3f10b579d70b20e4953f207a0`

## 1. Executive result

The first exact BRC-derived endpoint family is factor-blind and nonperiodically adaptive, but it does **not** create a new hidden-carrier endpoint mechanism.

Using the Driver-accepted F3R2 survivor witness, for every odd prime `r` define

\[
A_r=
\begin{pmatrix}
r & 2\\
(r^2-1)/2 & r
\end{pmatrix},
\qquad B=0,\qquad D=I_2\pmod 3.
\]

Then `det(A_r)=1`, `gcd(|a|,|d|)=r>1`, and `gcd(|b|,|c|)=2>1`, so this is an accepted survivor. The corresponding explicit conserved witness is

\[
q_{r,2}(n,t)=\frac12\left(\mathbf 1_{r\nmid n}+\mathbf 1_{2\nmid n}\right).
\]

For every odd semiprime `N`,

\[
R_r(N):=q_{r,2}(N,0)
=\frac12\left(\mathbf 1_{r\nmid N}+1\right).
\]

Hence

\[
R_r(N)<1
\iff r\mid N
\iff 1<\gcd(2r,N)<N
\]

except for the trivial control `N=r^2`, where the same gcd still returns the repeated prime `r`.

Therefore the F3R2 support-response is exactly a divisibility test for the public support prime `r`. It is computationally equivalent to trial division along the same public candidate schedule. This remains true when `r=r_j(N)` is selected adaptively and nonperiodically from `N` by a public hash.

A stronger algebraic control based on
\[
C_B(N)=2^{\operatorname{lcm}(1,\dots,B)}-1\pmod N
\]
does recover many endpoints by `gcd(C_B(N),N)`, but that is exactly fixed-base Pollard `p-1` Stage 1 and therefore fails the novelty gate.

Final task verdict:

`ENDPOINT_BRIDGE_PRIOR_ART_EQUIVALENT`.

No competitive factorization successor is authorized.

## 2. Frozen public/private contract

### Worker-visible

- odd composite `N`;
- coarse adversarial class label and nominal bit band;
- public seed;
- frozen BRC support-operator construction;
- fixed support primes: all odd primes `<=97`;
- 16 additional distinct support primes selected factor-blindly from the prime pool `[101,5000)` via
  `SHA256("BRC-SUPPORT-V1|N|slot")`.

### Verifier-only / not serialized

- `p,q`;
- factor midpoint/gap;
- factor rank;
- any bucket computed from the true factors.

The operator family was fixed before inspecting verifier factor labels.

Public corpus digest:

`sha256:8ea0570220fa970ac278f010af4744f7aa6cee10d915bb5174a06ae9799d33bd`

Private label manifest digest:

`sha256:5ef671ebe559dcd81af2edbb7b87fd2a6a31288dd7ff183250d8caf3dcab5edc`

## 3. Tool-reuse resolution

Project tool coverage was consulted after task understanding.

- `T0_BRC`: `REUSE_APPLIED`.
- No new general-purpose tool family was created.
- The exact checker is task-local validation code, not a proposed Enterprise tool.

## 4. Exact support-endpoint equivalence theorem

### Theorem

Let `N` be odd. Let `r(N)` be any public factor-blindly computed odd prime. Let `A_{r(N)}` be the survivor above and let

\[
R(N)=q_{r(N),2}(N,0).
\]

Then

\[
R(N)=\frac12
\iff r(N)\mid N,
\qquad
R(N)=1
\iff r(N)\nmid N.
\]

Consequently the public extraction rule

\[
d(N)=\gcd(2r(N),N)
\]

returns a nontrivial endpoint if and only if the BRC response detects a support hit.

### Proof

Because `N` is odd, `2\nmid N`; therefore the second indicator in `q_{r,2}` is identically `1`. The first indicator is `0` exactly when `r|N`. Substitution gives the two response values above. Since `r` is prime and `N` is odd, `gcd(2r,N)=gcd(r,N)`, which is `1` when `r\nmid N` and is a nontrivial divisor when `r\mid N` and `r<N`. For a repeated-prime control `N=r^2`, the gcd is `r`, still a nontrivial factor. QED.

### Adaptive corollary

For any precommitted public schedule
\[
r_1(N),\dots,r_k(N),
\]
including hash-adaptive or other nonperiodic schedules, the full BRC response vector is computably equivalent to the direct divisibility signature
\[
(1_{r_j(N)\mid N})_j.
\]

If none of the scheduled support primes divides `N`, every response component equals `1`, so the BRC response contributes no endpoint information beyond `N`. If a component changes, the successful public support prime itself is already a factor candidate.

This is an exact boundary for the accepted F3R2 support-witness mechanism; it is **not** a universal no-go for all conceivable BRC-derived operators.

## 5. Sealed exact experiment

Corpus: `75` records.

- bit bands: `32 / 48 / 64`;
- 5 records for each `(band,class)`;
- classes: balanced, moderate imbalance, strong imbalance, near-twin, repeated/square.

Per `N`, the frozen support family uses `40` candidate primes:

- 24 fixed odd primes `<=97`;
- 16 SHA256-selected distinct primes from `[101,5000)`.

Independent checker result:

- support-response vs endpoint-gcd equivalence mismatches: **0**;
- support endpoint successes: **1 / 75 = 1.33%**;
- failures: **74**;
- distinct response signatures among all 74 failures: **1** (the all-constant vector);
- median successful probe index: **21** of 40.

The success concentration is exactly what trial division predicts: 1/5 of the 32-bit strong-imbalance cases had a factor in the public candidate schedule. No balanced, near-twin, square, 48-bit, or 64-bit sample was recovered by the support family.

### Per-split summary

| bits | class | n | BRC support endpoint | order-collision control |
|---:|---|---:|---:|---:|
| 32 | balanced | 5 | 0 | 3 |
| 32 | moderate | 5 | 0 | 4 |
| 32 | strong | 5 | 1 | 5 |
| 32 | near_twin | 5 | 0 | 3 |
| 32 | square | 5 | 0 | 3 |
| 48 | balanced | 5 | 0 | 2 |
| 48 | moderate | 5 | 0 | 1 |
| 48 | strong | 5 | 0 | 5 |
| 48 | near_twin | 5 | 0 | 3 |
| 48 | square | 5 | 0 | 1 |
| 64 | balanced | 5 | 0 | 0 |
| 64 | moderate | 5 | 0 | 0 |
| 64 | strong | 5 | 0 | 5 |
| 64 | near_twin | 5 | 0 | 1 |
| 64 | square | 5 | 0 | 1 |

## 6. Algebraic one-sided-collapse control

To test whether the missing ingredient is merely a stronger response function, a fixed public comparator was frozen:

- base `a=2`;
- stages `B in [16, 32, 64, 128, 256, 512, 1024]`;
- `M_B=lcm(1,...,B)`;
- `C_B=2^M_B mod N - 1`;
- extraction `gcd(C_B,N)`.

It factors `37/75` toy records.

This does **not** count as a BRC endpoint advance. The mechanism is exactly Pollard `p-1` Stage 1: it succeeds when the multiplicative order modulo one hidden prime divides the chosen smooth exponent while the other channel does not collapse simultaneously.

Wrapping a BRC support observable around this collision does not create the endpoint; the zero divisor `C_B` already contains the entire factorization event.

Disposition:

`PRIOR_ART_EQUIVALENT / POLLARD_P_MINUS_1_STAGE_1`.

The success count is retained only as a mechanism-control result, not as a performance claim.

## 7. E1–E6 disposition

### E1 — BRIDGE_DETECTION

`PASS_ONLY_AT_SUPPORT_OVERLAP / NO_NEW_CHANNEL_DETECTION`.

The BRC response detects exactly whether a scheduled public support prime divides `N`. Relative to that label, recall is 100% and false positive rate is 0. Relative to the harder event “the two hidden CRT channels differ in a way not already naming a factor candidate,” the support family has no signal: all no-support-hit responses are identical.

### E2 — ENDPOINT_RECOVERY

`PASS / PRIOR_ART_EQUIVALENT`.

Public rule:

\[
d=\gcd(2r,N).
\]

It returns a factor precisely on support hits. This is exactly trial division by the scheduled public prime `r`.

### E3 — SEARCH_REDUCTION

`FAIL`.

For odd `N`, computing `R_r(N)` requires the same divisibility predicate `N mod r` as trial division. The fixed family therefore has exactly the same candidate count as its trial-division comparator; the hash-adaptive extension adds hash overhead and still tests the same candidates. There is no search reduction.

### E4 — PRIOR_ART_EQUIVALENCE

`FAIL_NOVELTY`.

- native F3R2 support endpoint: exact trial-division equivalence;
- modular order-collision control: exact Pollard `p-1` Stage-1 equivalence.

### E5 — ADVERSARIAL SPLIT

`PASS`.

Balanced, moderate, strong, near-twin, square/repeated controls were included across 32/48/64-bit nominal bands with sealed factor labels.

### E6 — THEORY BOUNDARY

`PASS / NARROW EXACT BOUNDARY`.

The accepted F3R2 support witness only sees divisibility by its own support primes. A factor-blind public support schedule therefore cannot reveal a hidden factor except by scheduling that factor itself. Adaptive/nonperiodic scheduling changes which primes are trial-divided; it does not change the information type.

## 8. LEAKAGE_AUDIT

`PASS`.

No operator, candidate schedule, response, stage parameter, or extraction branch used:

- `p,q`;
- `|p-q|`;
- midpoint/gap;
- prime rank;
- factor-derived bucket;
- verifier-selected successful operator.

The public worker functions accept `N` only.

The private generator used factor labels only to construct the sealed corpus and adversarial class assignment. Raw factors are not serialized in the public artifacts.

## 9. PRIOR_ART_EQUIVALENCE_AUDIT

### Support bridge

Exact map:

`BRC q_{r,2} response change`
`<=> r divides N`
`<=> gcd(r,N)>1`.

This is ordinary trial division / candidate-prime gcd testing. The BRC matrix and conserved witness add representation but not endpoint power.

### Order bridge

Exact map:

`one-sided modular order collapse`
`<=> gcd(2^M-1,N) nontrivial`

with `M=lcm(1,...,B)`.

This is fixed-base Pollard `p-1` Stage 1.

No claim of new factorization algorithm is admissible.

## 10. What is actually missing

The negative boundary is informative. To get a genuinely new endpoint bridge, BRC would need a primitive that is not reducible to either of the following:

1. **support naming** — choosing a public candidate prime and asking whether it divides `N`;
2. **known modular singularization** — order/smoothness/cyclotomic/collision machinery that already yields a zero divisor.

A genuinely new BRC endpoint mechanism would need a factor-blind public relation `C_lambda(N)` such that

\[
C_\lambda(N)\equiv0\pmod p,
\qquad
C_\lambda(N)\not\equiv0\pmod q
\]

(or the reverse) **without** preselecting `p` as a support prime and without importing a known order/collision algorithm.

The present F3R2 conserved support scalar cannot do this: its asymmetry is indexed by declared support primes, not generated by the hidden CRT decomposition of `N`.

A useful next conceptual target, if separately authorized, is therefore:

`N-COUPLED ASYMMETRIC SINGULARIZATION WITHOUT SUPPORT-NAMING OR ORDER-COLLISION`.

That is a much sharper target than “search nearer to sqrt(N).”

## 11. Required artifacts

- `research_returns/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY_RETURN_20260829.md`
- `research_artifacts/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY/public_corpus.json`
- `research_artifacts/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY/private_verifier_manifest_summary.json`
- `research_artifacts/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY/result_summary.json`
- `research_checks/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY_CHECK_20260829.py`

Independent checker status:

`PASS / 75 records / 0 support-equivalence mismatches`.

## 12. Final disposition

`ENDPOINT_BRIDGE_PRIOR_ART_EQUIVALENT`

The task does produce a correct factor-blind endpoint interface, but the native BRC support witness is exactly trial division over a public support schedule. The stronger one-sided collapse comparator is exactly Pollard `p-1`.

Therefore:

- no new factorization algorithm;
- no search-reduction claim;
- no competitive benchmark successor;
- exact theory boundary accepted for the tested F3R2 support-witness class;
- the open mathematical residue is a genuinely `N`-coupled asymmetric singularization primitive not already equivalent to support naming or classical order/collision factoring.
