# PREFIX-851 — A uniform two-heartbeat BRC source observer for every p >= 6

Date: 2026-11-17 (Asia/Shanghai).  
Scientific status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / EXACT_P6_FINITE_EXHAUSTION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).  
Dependencies: PREFIX-849 and PREFIX-850; the general result is a fresh direct construction, not a claim of native X6 event admissibility.

## 1. Model and statement

Use the same named binary positive-source BRC scalar observer as PREFIX-849/850: `X_p={0,1}^p`, `U(x)=sum 2^i x_i`, and at each heartbeat the hidden state may stay unchanged or flip at most one named coordinate. The receiver observes `Y_t=2^floor(t/2)(S_0+U(x_t)) mod m_t`, knows `S_0,t,m_t` and the predetermined schedule, and must recover the current named state from its most recent two reports for every legal source trajectory.

**Theorem (uniform two-heartbeat family).** For every integer `p>=6`, put

```
M_p=2^p-1,       K_p=2^(p-1)+3.
m_1,m_2,m_3,... = K_p,M_p,K_p,M_p,...
```

Every two consecutive readings uniquely identify the final named state for all `t>=2`. Both moduli are odd and satisfy `m_t<=2^p`, so the observation requires at most `p` bits per heartbeat:

```
B_dyn(p,2,2,2) <= p             for every integer p>=6.
```

**Sharp instance (six sources).** For `p=6`, the alternating moduli are `(35,63)`. Exhaustive checking of every `16^2=256` two-observation word with effective odd moduli at most 31 proves that no five-bit two-heartbeat observer works. Thus

```
B_dyn(6,2,1,2)=7,   B_dyn(6,2,2,2)=6.
```

The first equality follows because no single modulus of width six has an effective odd modulus at least `2^6` for arbitrarily late times; width seven can use constant odd modulus `65`.

## 2. Exact algebraic proof of the uniform family

The gain `2^floor(t/2)` is coprime to both odd moduli, so equal transmitted residues are exactly the same as `U(x)≡U(y) (mod m_t)`. Put `n=2^p` and `M=n-1`. Since source codes lie in `[0,M]`, a collision modulo `M` consists either of identical codes or the distinct pair `(0,M)` (in either order). Since `K=2^(p-1)+3>M/2`, a collision modulo `K` between distinct codes requires their absolute numerical difference to equal `K`.

The one-bit neighbors of `0` have codes `0` or `2^i`; those of `M` have codes `M` or `M-2^j`. Therefore every pair formed by one legal step from the extreme pair `(0,M)` has numerical difference

```
|M-s|,    s in {0,2^i,2^j,2^i+2^j}, 0<=i,j<p.
```

Here `0<=s<=2^p=M+1`. A collision modulo `K` would force `|M-s|=K`, hence `s=M-K` (the alternative `s=M+K` is too large). But

```
M-K = 2^(p-1)-4 = sum_{i=2}^{p-2} 2^i
```

has `p-3>=3` nonzero binary digits, while `s` is the sum of at most two powers of two. Such a collision cannot occur.

Now consider both possible ordered observation pairs.

**(K,M).** If the final codes are distinct but congruent modulo `M`, they are `0` and `M`. Their predecessor states must each be within one bit of the corresponding extreme. Equality modulo the previous `K` reading contradicts the preceding difference argument. The final codes are therefore identical.

**(M,K).** Two predecessor states congruent modulo `M` are either identical or `0,M`. The extreme case is ruled out by the same difference argument. In the identical case, two different successor codes from that common predecessor differ by at most two signed powers of two, namely `±2^i`, `±2^i±2^j`, or zero. None has absolute value `K=2^(p-1)+3`: a difference of powers is at most `2^(p-1)-1<K`; a sum of one or two positive powers has binary Hamming weight at most two, whereas `K` has three set bits. Thus any two equal-report histories have equal final codes.

Both ordered two-reading words determine the final source exactly. Alternating them provides an all-time observer independent of the heartbeat index or hidden update history. This completes the proof.

## 3. Sharp six-source verification and finite exact arithmetic

For `p=6`, the words `(35,63)` and `(63,35)` have respectively `58` and `2` ordered distinct first-reading collision pairs, but **zero** distinct final-state pairs after applying every permitted one-coordinate update and the second residue test.

For a hypothetical five-bit observer, at each sufficiently late heartbeat `c_t=2^floor(t/2)` removes every factor of two from any modulus `m_t<=32`, so effective moduli are drawn from `{1,3,...,31}`. Every one of the 256 effective two-word combinations retains at least one pair of distinct possible final states, proving the sharp lower bound. The published JavaScript enumerates every predecessor pair and every allowed successor pair with integer arithmetic, without pruning or random sampling.

The checker also verifies the exact binary identities for the construction across `p=6..64`, a finite regression of the general symbolic argument. Its output includes the full 256-word scope and the two witness words, with `ALL_EXACT_ASSERTIONS_PASSED`.

Files:
- `research_notes/portable_direct/PREFIX851_R6_TWO_HEARTBEAT_FAMILY_CHECK.js`
- `research_notes/portable_direct/PREFIX851_R6_TWO_HEARTBEAT_FAMILY_RESULTS.json`

The exact p=6 numerical experiment was separately recomputed in Python using ordered source-state transitions. The infinite-p theorem rests on the preceding symbolic argument, not on extrapolating the 59 finite arithmetic test cases.

## 4. Comparison and next scientific frontier

PREFIX-850 proves every `p<=4` requires `p+1` bits for every finite rolling window. PREFIX-849 shows the first saving at `p=5` occurs only at length four. The present construction gives a two-heartbeat saving for every `p>=6`. Thus the earliest saving thresholds for this named binary observer are:

```
p=1,2,3,4 : no finite window yields a bit saving;
p=5       : first saving at w=4;
p>=6      : a saving already exists at w=2.
```

The open optimization is whether, for `p>=7`, two heartbeats can achieve width strictly less than `p`; the p=6 bound is exact. Further directions include wider weight alphabets, more than one hidden source update per heartbeat, and preservation of an independently specified native X6 event/port relation.

All deductions are internal to the declared named Q-only BRC observer. Publication is author evidence and carries no formal shared-task CLAIM or independent mathematical admission.
