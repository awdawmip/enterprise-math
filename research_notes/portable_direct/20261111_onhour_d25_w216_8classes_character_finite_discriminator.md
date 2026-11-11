# D25: signed original W216 quadratic-character finite discriminator (2026-11-11)

**Status:** AUTHOR_SIDE / FINITE_EXACT_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0. No original-class divided-power or Researcher CLAIM/open/Source semantic checkpoint is asserted.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source: c47e13e4aba0e006366f989d6334d443f6333ae3.
Ordinary logical conversation: chatgpt-research-onhour-enterprise-math-20260923 (not the maintenance lane).

## Distinct finite discriminator: retain the other quadratic-character branch

For every prime 5 <= p <= 5000 (exactly 667), compute the **original** weighted truncated hypergeometric sum

[
a_k=rac{(2k)!(3k)!}{216^k(k!)^5}
=rac{inom{2k}{k}^2inom{3k}{k}}{216^k}, qquad
W_p=sum_{k=0}^{p-1}(6k+1)a_k .
]

The verified finite-domain statement is

[
oxed{W_pequiv chi_{-3}(p),ppmod{p^3}quad(5le ple5000, p	ext{ prime})}
]

where (chi_{-3}(p)=(rac{-3}{p})=+1) for (pequiv1mod6), and (-1) for (pequiv5mod6). The original Task target (pequiv13,19mod24) belongs to the positive-sign branch. The negative branch (pequiv5mod6), omitted from the original target, supplies a **distinct exact signed control** rather than another scan only inside the original target.

Counts for (pmod24): 1:76; 5:85; 7:88; 11:84; 13:83; 17:85; 19:83; 23:83. This covers 330 positive-sign and 337 negative-sign primes. No counterexample was observed in the complete declared finite domain. The broader all-prime statement is a **conjectural research route**, not established by this test.

Examples: (p=5): (W_pmod125=120=-5mod125); (p=7): (7); (p=11): (1320=-11mod1331); (p=373): (373mod51895117). Fourth-digit residual (arepsilon_p=(W_p-chi_{-3}(p)p)/p^3mod p) was additionally retained for every tested prime. Among 667 primes, (arepsilon_p=0) only at (p=5); for (p=373), (arepsilon_p=228).

## Exact computation and crosschecking

A coefficient recurrence valid in (mathbf Z_{(p)}) for (0le k<p-1) is

[
a_{k+1}=a_k,rac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
]

The provided deterministic stdlib-only checker enumerates all primes in the declared finite range via the sieve, evaluates the original weighted sum modulo (p^4) with exact modular inverses (every (k+1) used is a (p)-unit), and asserts the character claim modulo (p^3) for all 667 primes. It records the additional fourth digit without extending the proof claim.

An independent stripped-factorial algorithm (not using the recurrence) checks 21 selected primes:
5, 7, 11, 13, 17, 19, 23, 31, 37, 43, 73, 109, 139, 157, 373, 997, 1009, 1997, 3001, 4001, 4999. Each matched the recurrence output. The full 667-row locally materialized JSON has SHA-256 `522e3637b07b12cf1f8db22011fff9807aca11793156c51c14707a7df4cfd1d1`; running the uploaded checker recreates those bytes.

The external infinite Ramanujan series uses the **same exact coefficient** and is recorded as (sum_{kge0}(6k+1)a_k=3sqrt3/pi) in the linked literature discussion: https://mathoverflow.net/questions/508786/conjectural-series-arising-from-ramanujans-series-for-1-pi . This exact integrand match is a potentially useful prior-art direction; the cited discussion does **not** establish the p-adic claim above.

## Frozen task and native evidence

The original frozen scalar reduction (Delta_p-R_p=(W_p-p)/p^2mod p) remains valid on its original target (pequiv13,19mod24) under previously declared Source-aligned hypotheses. No change is made to the definition of (Delta_p), cutoff (R_p), signed observer or target scope. The broader finite character pattern is a new **test discriminator** for seeking a uniform proof, not an accepted expansion of the Task.

The highest-priority native evidence remains **NOT_RUN**: same-original-class H0/B0 divided-power ([X]Umod139129) at (p=373), actual module rank, semilinear Frobenius direction and (eta), signed odd Green/Hesse (kappa), original (Delta_p-R_p), and independent native replay. Capability-support Issue #1559 is OPEN / PENDING_OWNER at last verified read; this report does not replace the native evaluator.

The ordinary bridge prior continuation request #6762 (`onhour-d25-20261111-gosper-fresh-source-01`) was read as SUCCEEDED with Source SHA fbee999c36d3a31601256192f10b817a50329782. It required `PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER`, with predecessor claim MCP-d0d70cd041b01e5db192870a and prior comment 6390431276; this is **read-only source routing**, not this lane's winning CLAIM. This logical lane's earlier recovery #6759 showed historical registration FAILED / UPSTREAM_CODE_REVIEW_REQUIRED. No new identity, session, claim, open or native writer mutation was attempted.

**Next exact action:** Check any original-class H0/B0 evaluator against Issue #1559 and obtain native sample raw object/normalization; for scalar LIFT, investigate whether the shared character twist can be derived by a terminating hypergeometric transformation or WZ/q-microscopy, and compare claims against exact published statements before claiming a theorem. Preserve frozen pins and independent acceptance scope.
