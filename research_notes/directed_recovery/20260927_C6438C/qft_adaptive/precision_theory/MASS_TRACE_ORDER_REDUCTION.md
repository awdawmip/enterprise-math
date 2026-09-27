# One exact raw prefix mass is already order-finding powerful

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
No new scientific execution. This extends the previously executed exact-row reduction at EM `951cc16cb09635fae9f93230d96030fdaa2035b3`; it is not an oracle implementation or a sampling lower bound.

Let N>=3, gcd(a,N)=1, n=ceil(log2 N), t=2n, i=t-1 and Q=2^i. In the actual native instrument at h=0^i all feedback words are identities, independently of the certified phase-bank precisions. Put s=ord_N(a^2). The complete raw row is

    u_h(w) = Q^-1 #{0<=j<Q : a^(2j)=w mod N} e0.

Write Q=k s+r with 0<=r<s. Exactly r subgroup labels occur k+1 times and the other s-r occur k times. Therefore the **scalar** raw mass is

    M_h = trace Gamma_h(1)
        = [(s-r)k^2+r(k+1)^2]/Q^2
        = 1/s + r(s-r)/(s Q^2).

It follows that

    1/s <= M_h <= 1/s+s/(4Q^2).

The group of units has even order for N>=3. If ord(a) is even, squaring halves it; if odd, that odd order divides half the even group order. Hence s<=phi(N)/2<2^(n-1), without computing phi(N) or any factor. In particular Q>s^2.

If s=1, M_h=1. If s>=2, Q>s^2 implies

    s/(4Q^2) < 1/[s(s-1)],
    1/s <= M_h < 1/(s-1),
    s = ceil(1/M_h).

One subsequent actual modular-power test determines ord(a): it is s if a^s=1 modulo N, and 2s otherwise. The ceiling and modular power must use the typed arithmetic interface if executed. Exact rational output bit lengths in this reduction are polynomial: the displayed mass has denominator dividing Q^2. The proof does not give a method to obtain the mass cheaply.

A uniform polynomial-cost exact oracle for trace Gamma_h(1) on every legal prefix would therefore already solve modular order finding in polynomial cost. Replacing a matrix oracle by this scalar observable does not automatically remove the central difficulty. The formula takes the raw prefix mass; the trace of a normalized conditional covariance is always one and contains none of this information.

This statement does not prove classical order finding impossible, rule out cheap typical-prefix masses, or show that a sampler must visit this prefix. Its probability can be small, and an error-budgeted policy may never require the exact answer here. An arbitrary additive or relative approximation cannot be inserted into the ceiling formula without a separate precision/rounding analysis. No new assumption about a known order, factor, or full output law is made.

The algebra was cross-checked by another shared-context author. N=2 is a trivial separate unit-group boundary and is not needed for the reduction above.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1.
