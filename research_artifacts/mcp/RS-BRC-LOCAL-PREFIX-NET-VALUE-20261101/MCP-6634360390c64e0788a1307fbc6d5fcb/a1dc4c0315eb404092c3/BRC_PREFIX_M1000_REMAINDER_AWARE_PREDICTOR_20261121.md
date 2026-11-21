# BRC prefix M=1000: native limit and a remainder-aware exact jump

Status: NOT_REVIEWED; scoped proof plus reproducible local computation; no native-code deployment, no accepted universal performance claim.
Task: RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101. Researcher: EM-X6-C7A253. Original RUN: RUN-837e867aae8d5bf5e3587401.
Input pin: awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14.
Scientific scope: odd semiprimes of 31 or 32 binary bits; multiplier m in [1,1000], complete 625-member statically irredundant m scan (residues 0,1,3,5,7 mod 8). No factors used by the scanner.

## Actual implementation compatibility gap

The pinned and 2026-11-21 current src/enterprise_math/brc_multiplier_priority_jump.py imports MAX_MULTIPLIER from brc_multiplier_transition_table.py, where MAX_MULTIPLIER=100. direct_multiplier_jump_from_one(n,m,max_multiplier=1000) explicitly raises ValueError. Thus its proven <=11 correction bound and native performance cannot be extrapolated to M=1000 by changing just an argument. Existing kernel13_prefix(max_multiplier=1000) and learned_cover_order(max_multiplier=1000) support multiplier ordering; this alone is not an M=1000 native direct-jump backend.

## Exact alternative constructed from original BRC state

Let n=j²+r, j=floor(sqrt n), 0<=r<=2j, and B=(bit_length(n)+8)//2+1, S=2^B. For positive m<=1000 define integer lower approximants

A=j S + floor(r S/(2j+1)),
T=floor(S sqrt m)=isqrt(m S²),
c=floor(A T/S²).

Then c<=floor(sqrt(m n)). Since sqrt(n)-j=alpha in [0,1), alpha=r/(2j+alpha), and r/(2j+1)<=alpha with
0<=alpha-r/(2j+1)=alpha(1-alpha)/(2j+1)<1/(2j+1),
we have 0<=sqrt(n)-A/S<1/(2j+1)+1/S.
Also 0<=sqrt(m)-T/S<1/S.

Consequently, using sqrt(m)<32 and sqrt(n)<j+1,
0<=sqrt(m n)-(A/S)(T/S)
< 32/(2j+1)+(j+33)/S.

For n of exactly 31 bits: 32768<=j<46341 and B=20, so RHS < 32/65537+46374/1048576 < 0.045. For exactly 32 bits: 46340<=j<65536 and B=21, so RHS < 32/92681+65569/2097152 < 0.032. Both are <1. It follows that c is either floor(sqrt(m n)) or one less. A single exact BRC odd-width correction suffices: set gap=m*n-c²; if gap>=2c+1, subtract 2c+1 and replace c by c+1. This reconstructs m*n=c²+gap with 0<=gap<=2c. No factor oracle, hidden labels, floating point or new unproved axiom is involved. The general M and bitlength version is subject to the explicit RHS<1 inequality, not asserted globally.

## Finite paired evidence and separate cost semantics

An independent source-aligned Python implementation extends original recurrence math to M=1000 (NOT native imported backend). Exact reconstruction asserted at each evaluated candidate for 440 fixed 31/32-bit semiprimes, 220 near-balanced and 220 moderately imbalanced, two distributional groups, four complete orders and 625 candidate fallback. Seed 20261121. All three non-skip backend modes share exact hit count and stopping-rank checksum with the isqrt reference for each group/order.

In structural order:
- Near-balanced: 150/220 hits; 55,030 probes; isqrt reference ~18.58ms for one summed pass, naive M=1000 extrapolation ~86.53ms, remainder-aware construction ~49.85ms.
- Moderately imbalanced: 178/220 hits; 48,900 probes; reference ~16.29ms, naive extrapolation ~77.98ms, remainder-aware construction ~43.25ms.
- Naive direct-jump extrapolation incurs 541,572 and 508,388 correction iterations respectively, max 31/32; 20,171 and 19,378 candidate trials respectively exceed the native 11-correction bound. The remainder-aware construction used 775 and 720 corrections respectively, maximum 1 in both groups (stronger analytical <=1 bound applies).
- Earlier complete-order comparison: structural order mean probes 250.136/222.273 versus learned20 254.855/230.636 and kernel13 275.059/241.682 (balanced/imbalanced). All orders preserve the same 150/220 and 178/220 success counts.
- Additional dynamic 2-adic skip mode is a separate experiment, not equivalent stop rank; inspect full JSON if comparing it.

Times above are unreplicated elapsed Python single-pass wall time of locally reconstructed algorithms including per-candidate exact checks and gcd, excluding native import, external setup and peak-memory certification. They show no speed advantage and cannot certify a native M=1000 net-value result. The relevant mathematical progress is a valid limited-range predictor construction and an explicit boundary preventing misuse of M<=100 theorem.

## Reproduction and unfinished task

Local reproduction in this run: BRCPREFIX_20261121_COST_PROBE.py; BRCPREFIX_20261121_COST_RESULTS.json; BRCPREFIX_20261121_SOURCE_ALIGNED_COST_EXTENSION.py; BRCPREFIX_20261121_SOURCE_ALIGNED_COST_EXTENSION.json. These local files are not, by themselves, GitHub-published materials. The script reproduces all 440 samples from seed 20261121 and asserts order/coverage and BRC reconstruction. Frozen source references: src/enterprise_math/brc_opportunistic_shortcuts.py, src/enterprise_math/brc_multiplier_priority_jump.py, src/enterprise_math/brc_multiplier_transition_table.py at pinned commit.

Next: publish/check Source, preserve valid owner; if extending the genuine native backend to M=1000, construct/validate exact semantics and include predictor generation, square testing, input selection, fallback, gcd, setup, tail and memory in a controlled paired timing study. An independent reviewer retains the NOT_REVIEWED disposition.
