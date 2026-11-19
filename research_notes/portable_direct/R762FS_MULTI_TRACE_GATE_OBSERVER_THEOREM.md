# R762FS — Multi-trace fail-stop gate observer: exact capacity, fibers, and all-policy residual

2026-11-19 · Status: AUTHOR_PROVED / EXACT_ENUMERATION_PASS / NOT_REVIEWED.

Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; frozen taskbook 857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md and P000 a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Direct antecedents: R762FQ and R762FR, Draft PR #2790@087b9ab39bfe8cff011fbe82f61d03001b1b2f6c. Source input is the explicit candidate named-source positive BRC incidence carrier, not a certified native signed Cell/Link/Port update.

## Model and two different quantifiers

Let m>=1 source blocks have independently selected hidden states in {H0,H1,H2}. Each named remote gate i reports BLOCK exactly on H1 and SUCCESS on H0/H2. A SUCCESS swaps H0/H2 of that gate, preserving its enabled status; a BLOCK leaves it unchanged. The public root is always (1,1). Each BLOCK ends the current trace; the observer can restart from the original hidden state if fewer than r blocked attempts have occurred. After the r-th BLOCK, observation stops. Across all traces there are at most h gate attempts. Here r>=1, h>=0. A deterministic policy may select named gates based on previous public outcomes. Successful attempts consume an attempt, and previously observed gates may be retested, though that provides no new status information.

We distinguish (A) the maximum number of public transcripts produced by ONE fixed deterministic policy and (B) the smallest hidden-state quotient preserving the outcomes of EVERY admissible policy. These are not interchangeable information quantities.

## Theorem A — sharp multi-trace transcript capacity

For every m>=1, r>=1, h>=0, put t=min(m,h). The maximum distinct transcripts over one deterministic policy are exactly

    C(m,h,r) = sum_{a=0}^{min(r,t)} binom(t,a).

A fixed policy that tries t distinct named gates in order, restarting after a BLOCK while r permits, attains the upper bound. Its fixed-length transcript code uses ceil(log2 C(m,h,r)) bits. For h=0 the unique transcript is empty.

For that fixed policy, ALL fiber sizes in the full 3^m hidden-history population are exact:

1. Fewer than r blocked gates after testing all t: for each a with 0<=a<r and a<=t, there are binom(t,a) transcripts of fiber size 2^(t-a)*3^(m-t).
2. The r-th BLOCK at attempt j, r<=j<=t: there are binom(j-1,r-1) transcripts of fiber size 2^(j-r)*3^(m-j).

The two families are disjoint and cover all histories.

### Proof

A previously successful gate changes only H0<->H2, preserving its gate status and root. A previously blocked gate remains blocked. Repeatedly testing an already observed gate therefore cannot refine the partition of possible histories. A capacity-maximizing policy can choose an untested gate whenever it has an attempt left.

Let L(k,a,b) be the maximum leaf count from k untested gates, a remaining attempts and b remaining permitted BLOCK outcomes. The boundary value is 1 if k=0, a=0 or b=0. Otherwise, the next previously untested gate has exactly two possible public branches, both realizable independently of other gates. After SUCCESS, the remaining parameters are (k-1,a-1,b). After BLOCK, a new trace is allowed only if b-1>0, with parameters (k-1,a-1,b-1); b-1=0 gives a terminal leaf. Hence

    L(k,a,b)=L(k-1,a-1,b)+L(k-1,a-1,b-1).

Induction using Pascal's identity, with min(k,a) as the remaining available number of distinct tests, yields precisely the displayed sum of binomial coefficients. A named fixed order implements every branch, proving sharpness.

A successful observed gate has two possible original states, a blocked observed gate has exactly one, and an untouched gate has three. If all t gates were observed with a BLOCK positions, the fiber is 2^(t-a)*3^(m-t). If the r-th BLOCK occurs at position j, then j-r observed SUCCESS and m-j untouched gates give 2^(j-r)*3^(m-j). Their multiplicities follow from selecting the blocked positions. Every hidden history yields exactly one transcript, so the partition is complete. QED.

## Theorem B — all-policy source compression stays m bits

For h>=1 and r>=1, define s~s' when every permissible deterministic policy returns the same named public transcript for s and s'. Then

    s~s'  iff  for all i, (s_i=H1) iff (s'_i=H1).

Consequently the universal-policy observer quotient has exactly 2^m classes, and the optimal fixed-length representation for ALL future policy choices requires m bits. If z named gates are blocked, that quotient class has exactly 2^(m-z) full hidden histories.

### Proof

If two hidden states share the same binary blocked/enabled status vector, every gate attempt yields the same public result. Every success only swaps H0 and H2 and leaves status invariant, so induction on the observed policy path gives identical outputs and next actions for every policy. Conversely, if the vectors differ at named gate i, the permissible first-action policy "try i" distinguishes them immediately, even if all further attempts would be prohibited. Thus the quotient is exactly the binary status vector. Every vector occurs among the 3^m histories. QED.

**Quantifier distinction:** Theorem A is an existence/maximum over ONE fixed policy's possible outputs. Theorem B preserves ALL possible later policy choices. The R762FR result C(m,h,1)=min(m,h)+1 remains correct for one trace, but its outcome bit count is not an all-policy state-compression theorem. For m=6,h>=6,r=1, the former requires 3 bits, while the latter requires 6 bits. An outcome code of equal length to the all-policy code also need not carry the same semantics.

## Explicit m=6 values

Full named histories: 3^6=729, minimum 10 bits. All-policy gate-status classes: 2^6=64, minimum 6 bits. With attempt budget h>=6:

| Max BLOCK count r | One-policy transcripts | One-policy code | All-policy source quotient |
|---:|---:|---:|---:|
| 1 | 7 | 3 bits | 6 bits |
| 2 | 22 | 5 bits | 6 bits |
| 3 | 42 | 6 bits | 6 bits |
| 4 | 57 | 6 bits | 6 bits |
| 5 | 63 | 6 bits | 6 bits |
| 6 or more | 64 | 6 bits | 6 bits |

## Exact verification and limitations

Companion executable: R762FS_VERIFY.py (Python 3, standard library only). Run: python R762FS_VERIFY.py. Machine-readable evidence: R762FS_EVIDENCE.json.

Executed exact exhaustive enumeration for m=1..6, all 1<=r<=m+1 and 0<=h<=m+1: 166 regimes, 54,126 fixed-order history observations. Compared every observed transcript's fiber-size histogram, the complete 3^m total, the candidate closed form, and an independent adaptive binary-branch dynamic recurrence. Enumerated all 2^m first-gate status signatures and checked class multiplicities. PASS. Computation is a discrete combinatorial observer check on the stated candidate BRC source carrier, not a non-BRC substitute for a native Heartbeat World scientific evolution. The universal conclusions above follow from the all-m proofs, not finite testing.

The actual signed TRIADIC_CLOSURE_E Cell/Link/Port action permissions, rotation covariance, failure visibility, reset permissions and precise future time ordering remain to be extracted from frozen native sources or established by a typed carrier/observer correspondence. The candidate gate-state quotient is specified with its observer and all-future-policy scope; no unproven deletion of provenance from native states is claimed.

## Scientific continuation

Next discriminate native BLOCK versus silent/no-op semantics and the admissibility of reset: derive typed, signed native event transitions and a provenance-faithful observation morphism. With silent failures or non-involutive updates, rederive the true all-policy equivalence rather than importing the present binomial count. Preserve the frozen P000 and original named branch histories.

Portable direct research artifact only. No current CLAIM, protected Source PROGRESS, Result, independent Review or P000 amendment is asserted.