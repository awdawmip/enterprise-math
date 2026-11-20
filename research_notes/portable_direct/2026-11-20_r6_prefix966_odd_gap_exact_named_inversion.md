# PREFIX-966 — Odd-gap parity fibers and exact named-XOR reconstruction

Date: 2026-11-20. Scientific status: **AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED**. Frozen input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Historical author provenance EM-DIRECT-58C410; this label does not authenticate the present conversation. This is an auxiliary integer observer, not a native P000/X6/BRC event, formal CLAIM, Result or independent Review.

## Domain and original equations

Let p>=4, H=2^(p-1), Q_p={H+1,H+3,...,2H-1}, and k>=1 odd with k+2<H. For a,b in Q_p, source indices 0<=i,j,I,J<p and positive integers t,T, investigate

    ((k*a) XOR 2^j)-2^i = t*b
    (((k+2)*a) XOR 2^J)-2^I = T*b.

Set m=T-t. Actual source-bit signs are s=1-2*bit_j(k*a) and S=1-2*bit_J((k+2)*a). Define numerical residuals c=2^i-s*2^j, C=2^I-S*2^J, and D_p={2^u +/- 2^v:0<=u,v<p} as a set of **different integer values** (each retains all its signed source slot representations). Subtraction and elimination give

    C-c=2*a-m*b,
    N=k*C-(k+2)*c=(2*t-k*m)*b.

This note treats positive odd gaps m.

## Theorem 966.1 — Exact parity-filter count

For every p>=3 the odd members of D_p are exactly the union of

    {1-2^r:1<=r<p}, {1+2^r:1<=r<p}, {2^r-1:1<=r<p}.

Only the latter two sets overlap, at 3=1+2=4-1. Hence |D_p odd|=3p-4. Using the already established |D_p|=(3p^2-5p+10)/2, |D_p even|=(3p^2-11p+18)/2.

Since a,b,m are odd, C-c=2a-mb is odd. Therefore c,C are of opposite parity. **The exact number of parity-eligible ordered numerical residual pairs** is

    P_odd(p)=(3p-4)(3p^2-11p+18).

At p=19, |D_p|=499, |D_p odd|=53 and |D_p even|=446. Exactly 47,276 ordered numerical pairs survive, versus 249,001 before parity screening. These are numerical candidates, not actual named XOR witnesses.

Proof: a sum/difference of powers of two is odd iff exactly one term has exponent zero. The three families enumerate every possible ordered position and sign. If 1+2^r=2^s-1, then 2^r(2^(s-r)-1)=2, forcing r=1,s=2, yielding the unique overlap. By parity of 2a-mb, each admissible (c,C) is odd/even or even/odd. Count both orientations. QED.

## Theorem 966.2 — No odd-gap resonance, complete quotient inversion

For any odd k,m, the identity N=(2t-km)b forces **N odd, d=2t-km odd, N!=0 and d!=0**. For every actual witness 1<=t<=2k.

All named witnesses at fixed odd gap m are obtained by the following finite, source-faithful construction:

1. Enumerate all opposite-parity value pairs (c,C) of D_p, retaining their complete lists of source slots (i,j,s) and (I,J,S).
2. For each t=1,...,2k form d=2t-km and N=kC-(k+2)c. If d divides N, test b=N/d in Q_p; then test a=(mb+C-c)/2 in Q_p. Exclude a=b only for a non-diagonal census.
3. For every pair of source slot representations, require s=1-2*bit_j(k*a) and S=1-2*bit_J((k+2)*a); retain each passing tuple (a,b,t,t+m,i,j,I,J) with its own multiplicity.

Proof: parity of C-c forces N odd because k and k+2 are odd. Hence d is odd/nonzero. Also c>=1-H, a<=2H-1 and b>=H+1 imply

    t*b=k*a-c <=k*(2H-1)+H-1 <(2k+1)*(H+1),

so the positive integer t<=2k. Every genuine witness must occur in the enumerated (c,C,t). Conversely, the construction implies k*a-t*b=c and (k+2)*a-(t+m)*b=C; the real-bit sign predicates turn both into the original XOR equations. No named history is deleted by deduplicating the *value* dictionary because each numerical value retains its full original slot list. QED.

For adjacent cores the earlier PREFIX-960 bound m in {0,...,6} identifies odd branches precisely as m=1,3,5. This specialized route uses bounded integer divisibility by d rather than factorizing N to extract candidate divisors. For fixed small k, it uses O(k*p^3) arithmetic quotient tests; actual bit complexity and source recovery are accounted for separately.

## Independent verification

Program: PREFIX966_R6_ODD_GAP_RECONSTRUCT.py in this directory. It directly generates candidate (c,C,t), recovers each original named source tuple and checks **both raw XOR equalities**. A separate direct enumerator scans original XOR source terms and strict odd modulus b, joining endpoint outputs only when y=x+m*b, without importing the numeric residual inversion. Exact equality of per-pair named multiplicities was checked for all p=4..7, all odd k satisfying k+2<H, and m=1,3,5: **168 exhaustive (p,k,m) tests**.

For p=19,k=21, with a!=b:

| m | distinct ordered (a,b) | complete named joint histories | division tests | arithmetic domain candidates |
|---:|---:|---:|---:|---:|
| 1 | 442 | 614 | 1,985,592 | 1,419 |
| 3 | 839 | 1,286 | 1,985,592 | 2,825 |
| 5 | 3 | 3 | 1,985,592 | 15 |

The three pair sets are disjoint: **1,284 ordered pairs and 1,903 named joint histories** in their union. Their counts match earlier PREFIX-957B results; the present generator did not import the previous pair certificates. The full tuple-level checks are explicit assertions in the accompanying Python program.

SHA-256 of sorted comma-separated (a,b,t,T,i,j,I,J) tuple data lines joined by newline with a final newline (CSV header omitted):

- m=1: ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71
- m=3: 1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3
- m=5: c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b

Local test elapsed about 0.30–0.32 seconds per gap for the p19 reconstruction; not a comparative full end-to-end benchmark. An additional local reproducibility package retains the full 168-case JSON, complete 1,903 named tuples, stdout and file hashes; running the source regenerates all files. The algorithm does not claim a polynomial-time solution when k scales exponentially with p.

## Scientific boundary and next direction

Only the explicitly defined **auxiliary named integer observer** is proved. The stronger native BRC/X6 path equivalence, typed provenance compression and physical interpretations are unproved. For further study, combine quotient inversion for odd gaps with even-gap divisor/resonance handling and measure end-to-end preprocessing, source reconstruction and verification. Determine which source-signature quotient, if any, remains sufficient under downstream BRC composition. The overarching B_fix,odd(32) in {19,20} remains open.
