# Hart normalized threshold: inverse square-index micro-unit

Status: EXACT CONDITIONAL ENUMERATION AND PAID-ROW BOUND / PARENT OPEN.
Auxiliary identity: UNKNOWN / DIRECTED_NONBLIND. This paper check supports the parent's declared own run RUN-02bc03dfff15c15ce7daf2f3, researcher EM-SEMIPRIME-1F8B9B, publication TP2-7BCC256B5EA65F8D5085. Those IDs are context supplied by the parent, not a claim or authority of this auxiliary. No private Native session records were read, no claims or Source writes were made, and no old experiments/checkers/correlations were rerun. A child bounded paper check independently checked the exact interval and finite-endpoint identities.

Input: OLD_SQUARE_SHELL_RETURN_FULL.md, fully read, 12,481 B, SHA256 7ec6b0647e8f1e1a41bb0dfcd4fca538b3d152f24e04cfe1f82230cdb65e27f4. Its sections 7-9 and 12 require the original normalized 4kN multiplier family and total paid cost. All statements below are in the external exact-integer model; they assert no native physical bridge, prior-art novelty, general factoring lower bound, or Foundation/Working Truth grant.

## 1. Preserve the actual score

For public integers D>=1, K>=1, define

    a_k = ceil(sqrt(Dk)),
    r_k = a_k^2-Dk,
    s_k = r_k/(2a_k-1).

The actual old mechanism is D=4N, so a_k=ceil(2sqrt(kN)), not 2ceil(sqrt(kN)). For N=15,k=2 the true row is a=11,r=1,s=1/21; the replacement a=12 gives r=24 and ratio 24/23>1. It is not the same upper-square row.

Always 0<=r_k<2a_k-1, so 0<=s_k<1. This includes square rows r_k=0. The strict upper inequality is essential: a one-too-large square index must not duplicate the previous shell.

## 2. Exact inverse square shell, all K

Set a0=ceil(sqrt(D)), amax=ceil(sqrt(DK)). For each integer a in [a0,amax], put t=2a-1 and

    lo_a = max(1, floor((a-1)^2/D)+1),
    hi_a = min(K, floor(a^2/D)).

Then

    a_k=a iff (a-1)^2<Dk<=a^2 iff lo_a<=k<=hi_a.

Each k in [1,K] lies in exactly one such interval; intervals may be empty or contain several k. For every k therein, r=a^2-Dk satisfies 0<=r<t. These formulas handle exact-square endpoints, a=1, D=1, and K>D. The clipping hi_a<=K is necessary at the final square index, and the strict previous-square bound excludes duplicate rows.

For a rational threshold theta=u/v, 0<=u<=v and v>0, accept s_k<=theta by adding the exact lower bound

    k >= ceil((v*a^2-u*t)/(vD)).

The retained interval is therefore [max(lo_a, that bound), hi_a], if nonempty. This uses integer products and division; no floating comparison or factors of N are required.

For integer bucket count B>=1 and b in [0,B-1], define b_k=floor(B*r_k/t). Bucket b is exactly

    b*t <= B*(a^2-Dk) < (b+1)*t.

Its exact local interval is obtained by intersecting [lo_a,hi_a] with

    k >= floor((B*a^2-(b+1)*t)/(BD))+1,
    k <= floor((B*a^2-b*t)/(BD)).

The lower bound records the strict upper bucket edge; equal lower edges are accepted. Scanning a upward and, within each shell, k upward emits that bucket in increasing k because the complete shell intervals occur in increasing k order. Repeating b=0,1,... gives exactly the declared (bucket,k) order, without repeats. It is not fully sorted by the rational score inside a bucket; such an additional claim would need additional ordering work.

## 3. Single floor decoding: sufficient regimes and a sharp witness

The simpler rule q=floor(a^2/D), r=a^2 mod D is correct for a retained row only if its true residual is <D. The sufficient full-prefix guarantee

    2*amax-2<D

implies this for every row. When D=4N, it is exactly equivalent to K<=N: the inequality is equivalent to amax<=2N, and hence 4NK<=(2N)^2. In this regime at most one k belongs to each shell, and it is precisely q when 1<=q<=K and r<2a-1.

Outside the regime, use the exact multi-k interval. K>N does not mean failure occurs immediately, but single floor decoding has no general guarantee. A semiprime counterexample is

    N=15, D=60, K=24, a=38, t=75,
    37^2=1369 < 60*23=1380 < 60*24=1440 <=38^2=1444.

Thus k=23 and 24 share this square shell, with residuals 64 and 4 and scores 64/75 and 4/75. Threshold theta=64/75 accepts both, whereas floor(1444/60)=24 misses k=23. The exact interval gives [23,24].

There are useful weaker subset guarantees. For an absolute residual bound 0<=R<D, single floor decoding exactly enumerates the accepted subset for every K after retaining 1<=q<=K, r<=R, and r<2a-1. This absolute residual subset must not be confused with the original normalized-score mechanism. For a normalized threshold, u*(2amax-1)<vD is sufficient to ensure all retained residuals are <D even outside K<=N. For bucket b, (b+1)*(2amax-1)<=BD is sufficient because its upper edge is strict. These are sufficient tests, not a new output-sensitive algorithm.

## 4. Explicit streaming implementation and paid row count

A complete square-index pass inspects exactly

    A = amax-a0+1
      = ceil(sqrt(DK))-ceil(sqrt(D))+1

rows, including empty shells. This is exact, with no hidden factors or residual oracle. Maintain S=a^2, q=floor(S/D), r=S-Dq. From a to a+1 update

    S' = S+2a+1,
    j = floor((r+2a+1)/D),
    q' = q+j,
    r' = r+2a+1-Dj.

All quantities are public. Initial endpoints require exact integer square roots and initialization requires exact arithmetic/divmod; every visited square row and transport is paid. In the full-prefix unique regime, 2a+1<D for each transition a<amax, so j is 0 or 1 and a single conditional subtraction suffices. Outside it, j may be larger and its computation must be charged. No bit-cost equivalence between multiplication, division, square root, square testing, and gcd is assumed.

If a productive hit is reached in a shell a*, the current pass has visited

    P=a*-a0+1

rows, not merely the number of emitted candidates. Under the declared one-pass-per-bucket implementation, if b* earlier buckets were fully scanned, the transport row count before the hit is exactly b* A+P. Within a shell, any already examined candidates also incur their own costs. With no productive hit and all B buckets exhausted, the transport count is B*A and all K multiplier candidates are eventually emitted. Bucket maintenance, modular tests, residual-square tests, gcds and emitted-candidate work remain additional paid operations. A zero residual or an eligible score is not automatically a proper factor hit.

## 5. Exact comparison with K and output H

Let H be the number of threshold-eligible multipliers, not the number of productive factorizations. In general 0<=H<=K. In the unique regime also H<=A. Outside it, H can exceed A: N=15,D=60,K=60 gives A=60-8+1=53, whereas theta=1 accepts all H=60. Thus H<=A is not a global statement.

For any D,K, write d=sqrt(D)*(sqrt(K)-1). The exact rounded count satisfies

    floor(d)+1 <= A <= ceil(d)+1,
    A=d+O(1).

An exact comparison, including finite square edges, is

    A<=K iff DK<=(a0+K-1)^2.

Equivalently, with beta=a0^2-D,

    A<=K iff beta+(K-1)*(K+2a0-1-D)>=0.

Hence “K>N” alone does not tell whether A is smaller than K in the actual D=4N model. For K=N, A=2N-ceil(2sqrt(N))+1, asymptotic to 2N; at K much larger than 4N, A/K tends to zero, but multiple k per shell and output cost must then be handled. For K proportional to N with K/N->c>0, A/K->2/sqrt(c).

In the relevant sublinear window K asymptotic to N^(1/3),

    A asymptotic to 2N^(2/3),
    A/K asymptotic to 2N^(1/3).

Thus this complete inverse scan replaces K naive ceil-square-root calls by endpoint roots and A arithmetic transports, but performs many more row visits. Eliminating a particular naive square-root call count does not prove a total-cost gain against exact-update or otherwise optimized Hart baselines.

There is no generic output-sensitive bound for this complete-pass implementation. For the old distinct-semiprime hypothesis N=pq, N is squarefree. At threshold theta=0,

    r_k=0 iff kN is square iff k=N*j^2,
    H=floor(sqrt(K/N)).

This is a proof identity, not an algorithm receiving p or q. For K<N, H=0 while A can grow as 2N^(2/3) at K asymptotic to N^(1/3). For K=N, H=1 while A is asymptotic to 2N; that sole row has a=2N,r=0 and gcd(a,N)=N, so it is not a productive proper-factor certificate. Positive output therefore also does not give a bound A=O(H). The identity would need modification for a square or nonsquarefree N.

The examples bound this specific complete a-scan and do not prove a lower bound for all threshold selectors. Indeed the zero-threshold identity itself can certify the empty set when N is promised squarefree and K<N, without scanning a. A stronger generator that jumps directly to nonempty rational-threshold or bucket intervals, with a proved total construction/retrieval cost, remains unproved here.

## 6. Pointwise first-productive-hit comparison

This strengthens the complete-pass obstruction for the declared literal a-scan; it does not compare all possible generators. Suppose the first productive proper-gcd hit in bucket order occurs at k* in [1,K], in shell a*=ceil(sqrt(4Nk*)). If g earlier buckets have each been completely scanned, the generated square-row count up to the hit is

    G_hit = g*A + P,
    P = ceil(sqrt(4Nk*))-ceil(sqrt(4N))+1.

Multiple k in one shell do not invalidate this identity: the shell must be reached before any of its candidates can be processed. Additional candidate processing within it is paid separately. For x>=y, ceil(x)-ceil(y)+1>x-y, since ceil(x)-x>=0 and ceil(y)-y<1. Hence

    P > 2sqrt(N)*(sqrt(k*)-1).

For k*>=2, use 1-1/sqrt(k*) >= 1-1/sqrt(2), yielding

    G_hit >= P >= (2-sqrt(2))*sqrt(Nk*),
    G_hit/k* >= (2-sqrt(2))*sqrt(N/k*)
              >= (2-sqrt(2))*sqrt(N/K).

The ordinary ascending-k Hart comparator with the same exact row definition, necessary QR acceptance, residual-square test, and proper-gcd termination must encounter a productive hit at some j<=k*. It therefore examines at most k* multiplier points. If the inverse mechanism rejects or fails earlier perfect-square rows because their gcd is 1 or N, both algorithms continue under the same rule. An eligible score and even a perfect-square residual are not themselves productive hits.

For K=ceil(N^(1/3)), K<=N for every positive integer N, so the full-prefix unique regime applies. Also K<=2N^(1/3), giving the finite row/point lower bound

    G_hit/k* >= (sqrt(2)-1)*N^(1/3)   (k*>=2).

This includes any 32-bit-or-larger distinct odd semiprime; the algebra does not require a 32-bit cutoff. Exact integer multiplication, division, square root, square test and gcd on O(log(NK))-bit operands admit polynomial bit-cost upper bounds in log(NK). For example, grade-school multiplication/division and binary-search integer square root already give polynomial bounds, without a sophisticated arithmetic algorithm. For a matched QR filter with a fixed or polynomial-in-log(NK) number of checks and polynomial evaluation cost per point, the comparator's variable work is at most k* poly(log(NK)). In the declared sequential exact-integer bit-cost implementation, every literally visited square row incurs at least one unit operation. Under these two explicit cost assumptions, the inverse generator's work alone exceeds the comparator's variable-work bound by N^(1/3-o(1)) as N grows. It offers no fixed polynomial total-cost gain in the stated window. The row-count inequality by itself is not an actual wall-clock benchmark comparison; no finite 32-bit timing advantage or disadvantage is inferred.

The per-point QR bound is a required comparator condition: one cannot hide arbitrarily many expensive filter checks in a common preparation term. If such a bound is absent, a direct ascending-k square/gcd comparator can omit purely necessary rejection filters and still has the polynomial-bit-cost upper bound, but it must be named as that comparator rather than described as having the same filtering implementation.

If k*=1 and g=0, both orders reach the same first multiplier; the quantitative k*>=2 bound does not apply and no ordering advantage is established. If k*=1 but g>=1, the earlier g full bucket passes still cost g*A before a hit the ordinary order sees at its first multiplier. If all B buckets fail and are exhausted, the same comparison uses G_fail=B*A versus at most K ascending-k points; for K>=2, A/K >= (2-sqrt(2))*sqrt(N/K).

Let P_common(N) denote exactly the same paid sieve/preparation work added to both algorithms. It must remain in both totals. Adding a large common term may erase the variable-work slowdown ratio, so the N^(1/3-o(1)) ratio must not be asserted for the totals without an additional bound on P_common. It cannot turn the proved disadvantage of the variable scan into a total-cost improvement. These are conditional pointwise bounds for this literal scan, not coverage guarantees, general factoring lower bounds, or a no-go for generators that provably skip empty shells.

## 7. Result boundary and next target

The micro-unit establishes exact rational threshold/bucket enumeration, finite correctness regimes, endpoint counterexamples, the accounted row cost of a concrete inverse scan, and its pointwise first-hit disadvantage in the declared K=ceil(N^(1/3)) window. It does not establish lower factorization cost, a productive-hit guarantee, general no-go, or a new Hart novelty result. The old section 12 question remains open beyond this candidate: a meaningful next rule must skip empty shells without first paying for all of them, retain the original normalized score, and count its construction, transport, filtering, retrieval, and proper-gcd verification against a matched optimized Hart comparator.
