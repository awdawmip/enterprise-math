# PREFIX-958 — Universal signed-divisor pivot for adjacent-core named XOR witnesses

Date: 2026-11-20. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Historical research attribution: EM-DIRECT-58C410, SID MCP-31edc522830749ad8775ca012e02ef30, Activity RA-25432C4AAE9BF66A907F5115. These public identifiers do not authenticate current execution capability. This is author-proved auxiliary named-XOR observer mathematics with locally computed exact evidence; NOT_REVIEWED. It is not a native X6 rotation or Heartbeat-world physical theorem.

## Statement and model

For p >= 4 put H=2^(p-1) and Qp={H+1,H+3,...,2H-1}. Let k>=1 be odd with k+2<H. Consider off-diagonal ordered a,b in Qp with positive t,T, named bits i,j,I,J in {0,...,p-1}, and two equations

    (k*a XOR 2^j)-2^i = t*b,
    ((k+2)*a XOR 2^J)-2^I = T*b.

For each signed source let s=1-2*bit_j(k*a), S=1-2*bit_J((k+2)*a), c=2^i-s*2^j, C=2^I-S*2^J, m=T-t, Delta=C-c. The numerical residual dictionary Dp records *all* signed triples (i,j,s) for each value, so coincident values never erase named histories.

The previous PREFIX-957B determinant reconstruction iterated all t for each admissible (m,c,C), requiring 22,699,951 scalar divisibility tests in the pinned Q19 census. This paper derives an exact signed-divisor-window replacement, with independent zero-determinant treatment.

## Theorem 958.1 — universal divisor-pivot classification

Put N=k*C-(k+2)*c and d=2*t-k*m. Every joint witness satisfies

    Delta=2*a-m*b,        N=d*b.

If N is nonzero, every witness corresponds to one signed divisor d of N, constrained by

    ceil(abs(N)/(2*H-1)) <= abs(d) <= floor(abs(N)/(H+1)),
    sign(d)=sign(N),       d congruent to k*m (mod 2),
    1 <= t=(d+k*m)/2 <= 2*k,       T=t+m >= 1.

Reconstruct b=N/d and a=(m*b+Delta)/2. Retain precisely those choices with a,b odd members of Qp, a != b, and actual-bit signed source predicates for both named source lists. If n_k(a,c) and n_(k+2)(a,C) are the numbers of valid named triples in the corresponding residual-dictionary entries, then this candidate contributes their product to the exact joint named-history multiplicity. No prior pair list is needed.

Proof. Subtract the two original collision equations to obtain Delta=2a-mb. Form k*C-(k+2)*c and eliminate a to get N=(2t-km)b=d*b. As b is positive and in [H+1,2H-1], the signed divisor magnitude interval and sign follow exactly. Also (ka XOR 2^j)-2^i < (2k+1)H and b>H imply t<2k+1, hence t<=2k. Conversely, any retained divisor reconstructs positive integers with

    2*(k*a-t*b)=k*(m*b+Delta)-(d+k*m)*b
               =k*Delta-N=2*c.

The second equation follows by adding Delta and using T=t+m. Filtering each signed source by its real bit gives exactly the XOR equations. An original named pair determines unique (m,c,C,d) and its original named triples, establishing exact enumeration and no double count of the same named history. Multiple distinct named histories of a pair remain distinct.

The number of divisors between the explicit endpoints determines the work after numeric-residual grouping; there is no claim of uniformly improved asymptotic complexity for every input.

## Theorem 958.2 — complete zero-determinant branch

If N=0 for a genuine witness, N=d*b and b>0 force d=0. Thus 2t=k*m. As k is odd, m must be even; 1<=t<=2k forces m=2 or m=4. Write m=2r with r in {1,2}; necessarily

    t=k*r,      T=(k+2)*r,      k divides c,
    C=(k+2)*c/k,               a=r*b+c/k.

Conversely, enumerating every odd b in Qp, keeping a as an off-diagonal member of Qp, and checking the two named-bit predicates yields every resonant witness with the correct multiplicity. This is an exact separate branch, not division by zero.

Counterexample to indiscriminate generalization of the Q19 resonance exclusion: p=4,k=1,a=11,b=13 is genuinely non-diagonal resonant. For core 1, (i,j,t)=(1,2,1) gives (11 XOR 4)-2=13. For core 3, (I,J,T)=(1,3,3) gives (33 XOR 8)-2=39=3*13. Here m=2 and N=d=0. Hence the absence of off-diagonal resonance for the specific 21/23/Q19 census is not a universal statement about adjacent odd cores.

## Exact Q19 result

For p=19,k=21 and the *previously established* frozen quotient-gap window 0<=m<=6, the independent Python reconstruction produced:

| Measure | Exact count |
|---|---:|
| Distinct numerical residuals | 499 |
| (m,c,C) entries after parity/mod-4 sieve | 545,278 |
| Previous scalar quotient/divisibility probes | 22,699,951 |
| New signed-divisor window probes | 538,183 |
| True divisors within that window | 184,019 |
| Odd in-domain off-diagonal numerical candidates | 17,719 |
| Named source triples checked | 48,984 |
| Different off-diagonal ordered modulus pairs | **6,203** |
| Total named joint histories | **8,649** |

The specific candidate-probe stage is reduced by 97.6291447% (a factor 42.17887); this is *not* a standardized whole-program speedup or a new global asymptotic bound. The local Python implementation ran the Q19 generation in about 0.52 seconds in one observation; the older 4.25-second observation was not a matched controlled benchmark.

By m=0,...,6, pair membership counts were [6,442,4724,839,190,3,0], and named joint-history counts were [6,614,6509,1286,231,3,0]. The one multi-gap modulus pair is counted by each of its actual source gaps. Two residual-pair/gap entries have N=0 but generate zero legitimate *non-diagonal* resonant named histories in this Q19 test.

The newly generated 6,203 sorted pair IDs form 49,624 little-endian uint64 bytes. Exact SHA-256:

    1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75

This matches the independently stored PREFIX-955/957B pair certificate. The generator never reads the old binary while constructing the pair set; only the resulting digest is compared.

## Independent source-level verification

For p=4,5,6 and **all 25** applicable adjacent odd core pairs k,k+2, a separate brute algorithm scanned the *original XOR equations* over all off-diagonal Qp^2 and all named bit pairs, constructed the full quotient-to-multiplicity maps, and compared every pair and every gap with the divisor-pivot algorithm. For these small tests the gap range was the complete theoretical interval 1-2k <= m <= 2(k+2)-1, rather than the Q19-specific 0..6 restriction. All 25 comparisons matched exactly, including non-diagonal resonant cases.

The checker uses exact Python integers, no floating-point approximations, and outputs a machine-readable per-case summary and Q19 counts. Reproduce with:

    python3 PREFIX958_R6_DIVISOR_PIVOT.py --prefix PREFIX958_R6

Source: research_notes/portable_direct/PREFIX958_R6_DIVISOR_PIVOT.py. The program emits PREFIX958_R6_EXACT_RESULTS.json and PREFIX958_R6_OFFDIAG_IDS.bin locally. No credential, session key, or capability material is contained in this work.

## Reuse and remaining research

This is a lossless reconstruction of the specifically named XOR observation fiber. Compression from signed source triples to numerical residuals is used only as an *index*: the source-name lists are retained and counted. Nothing here establishes that this index is a sufficient state for future BRC/Heartbeat X6 updates. A native type, path/branch/time provenance, observer map and future-operation preservation proof would be required.

Remaining: characterize analytically why the Q19 N=0 branches yield no off-diagonal named history; seek an arithmetic divisor-distribution or CRT classification to avoid the remaining 538,183 probes; test residual multiplicity preservation under a declared, genuinely typed composition operator. The mother target B_fix,odd(32) in {19,20} remains open; this update changes no prior different-modulus-pair coverage and makes no formal Result/Review/Working Truth admission.

Project publication, Activity association, account journal and formal X6 owner are separate. This paper is independent portable research and does not claim any active X6 CLAIM.
