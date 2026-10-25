# R4-EC13 — Binomial grade law and a square-root provenance crossover in positive BRC

**2026-10-25. Author-side exact mathematical draft, NOT native Source Result or independently admitted.**

Parent: R4-EC12 positive Laurent minimal realization at immutable commit fed35782b51e671bd2045c004c67d9ce55a8ae10. Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@c8191daa0c167af40c86972ac9fe45dc3569e06c; Enterprise Math main@db3a1f965272aff77b89983f35045d4458098a51. P000 is ACTIVE_LOCKED. This is the *auxiliary* unit-positive-mass binary affine BRC, not native P000 six-dimensional X6 dynamics.

## Definitions and observation scope

Start at (q,r,e,t)=(0,0,+1,0), with q in {0,1,2}; r=0 means no 00 and no trailing 0, r=1 means no 00 and trailing 0, r=2 means 00 has appeared. Orientation e=±1 and grade t=e*k for affine displacement k. At each bit a in {0,1}, use (q',eta,b) according to:

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

Update e'=eta*e, t'=t+e'*b. If r=2 keep r=2; otherwise bit 1 resets r=0, bit 0 sets r=1 if r was 0 and sets r=2 if r was 1. Every ordered bit word has positive mass 1.

Let j=(n-t)/2 count the **negative grade increments** in an n-step word. Let C[n,j] count source-clean (r≠2) words, D[n,j] source-dirty (r=2) words. The stated observer conditions on (n,t) and queries source cleanliness. It does not assert word-resolved recovery, full-effect classification, or P000 transport.

## Theorem 1. Exact binomial effect-grade law

For every q and either bit the edge table gives the universal identity

    t' - t = e*(1-2a).

Thus the grade sign sigma_i=t_i-t_(i-1) and previous orientation e_(i-1) uniquely recover the bit

    a_i = (1-e_(i-1)*sigma_i)/2.

This is a triangular bijection between length-n input words and length-n words of signs sigma_i=±1; it holds for each n, without any independence assumption on the source labels. The number with j negative signs is exactly binom(n,j). Therefore

    C[n,j]+D[n,j] = binom(n,j)
    T(x,u) = sum_{n,j} binom(n,j)*x^n*u^j = 1/(1-(1+u)*x).

This is a binomial law for t=e*k, not for k alone.

## Theorem 2. Exact rational bivariate clean-source series

Retain the eight source-clean fine states, ordered

    (0,0,-), (0,0,+), (1,1,-), (1,1,+),
    (2,0,-), (2,0,+), (2,1,-), (2,1,+).

Let M(u) be the 8x8 matrix of transitions remaining clean, each positive-grade step having coefficient 1 and each negative-grade step coefficient u. Let v be the initial (0,0,+) basis vector and 1 the row of eight ones. Then the formal series C(x,u)=1^T (I-xM(u))^(-1) v satisfies

    Delta(x,u) = 1-(1+u)*x+2*u^2*x^4-u^3*x^6
    N(x,u) = (1-u*x^2)*(1-u*x^3)
    C(x,u) = N(x,u)/Delta(x,u)
    D(x,u) = 1/(1-(1+u)*x)-N(x,u)/Delta(x,u).

An explicit finite polynomial certificate makes the identity auditable without trusting a black-box inverse. Put K=1+u*x^2, A=u*x-1, B=u*x^3+x-1, E=u^2*x^5-u*x^3-x+1 and define the eight-component polynomial column

    H=(-u*x^4*A, A*B, -u*x^3*A, u*x^2*E,
       -x^2*A, u*x*E, x*A*B, -u^2*x^5*A)^T.

Entry-by-entry polynomial multiplication verifies

    (I-x*M(u))*H = K*Delta*v
    1^T*H = K*N.

Both I-xM and K have invertible constant terms, proving the exact formal-series quotient for **all** n,j. The minus signs in H are algebraic certificate coefficients; physical path weights remain positive. At u=1 this simplifies to (1+x)/(1-x-x^2), giving Fibonacci F_(n+2) clean paths. At u=0 the clean series is 1/(1-x).

A further exact scalar recurrence, defining out-of-range indices to be zero, is

    C[n,j] = C[n-1,j]+C[n-1,j-1]-2*C[n-4,j-2]+C[n-6,j-3]+s[n,j],

where s[0,0]=1, s[2,1]=s[3,1]=-1, s[5,2]=1, and all other s=0. This can calculate every grade fibre without propagating the original 14 fine states.

## Theorem 3. Fixed-grade source reversal

For each fixed integer j>=1, the dirty-source grade generating function [u^j]D(x,u) has no poles other than x=1, and the pole of order j has coefficient 2j:

    lim_(x→1) (1-x)^j * [u^j]D(x,u) = 2j.

To prove this write A0=1-x-u*x and delta=2*u^2*x^4-u^3*x^6. Since Delta=A0+delta,

    D=(1-N)/A0 + N*delta/(A0*(A0+delta)).

Expand in the formal variable u over Q(x). For [u^j], the only terms of pole order j arise from u*(x^2+x^3)/A0, contributing 2, and from 2*u^2*x^4/A0^2, contributing 2(j-1). The other terms have pole order at most j-1. No other x poles arise after taking a fixed u coefficient. Therefore, for fixed j>=1,

    D[n,j] = (2j/(j-1)!)*n^(j-1)+O_j(n^(j-2))
    P(dirty | t=n-2j) = D[n,j]/binom(n,j)
                      = 2*j^2/n+O_j(n^(-2)).

So each fixed-defect near-frontier grade shell becomes **asymptotically clean**, while the unconditional clean mass F_(n+2)/2^n tends to zero. No contradiction: fixed-j shells are rare within all 2^n words. Two exact subfamilies:

    D[n,1]=2 for every n>=3;
    D[n,2]=4*n-12 for every n>=5.

A finer concentration follows without generating functions. The initial state reaches s*=(2,0,-) after two positive grade increments. One negative increment at s* followed by two positives returns to s* without source pollution. Requiring two initial positives, two positives between successive negatives, and two final positives gives exactly binom(n-2j-2,j) such sign words for n>=3j+2, each ending in the *same* fine state (2,0,-), with k=-(n-2j). Consequently

    P[n,j](q=2,r=0,e=-) >= binom(n-2j-2,j),

and this one fine-state mass divided by binom(n,j) tends to 1 for fixed j.

## Theorem 4. Exact square-root crossover, with a finite error certificate

Let E be the event that j negative-grade positions chosen uniformly from {1,...,n} are never separated by only one or two positions. Compress ordered positions b_i to b_i-2(i-1). This counts

    P(E | j) = binom(n-2j+2,j)/binom(n,j),

using zero for an inadmissible binomial numerator.

Let B mean that a negative lies in one of the first or last two positions, or that some three negatives have total span <=4. **Outside B, a word is clean if and only if E holds.** If E holds, every negative begins at the clean reference s*, which is restored by the subsequent two positives. If E fails outside B, take the first close pair. Its predecessor is s* and no third negative interrupts the local consequence:

    distance 1: (2,0,-) -> (1,1,-) -> (0,2,+) [dirty];
    distance 2: (2,0,-) -> (1,1,-) -> (0,0,-)
                          -> (2,1,+) -> (1,2,+) [dirty].

The boundary of length two guarantees room for these transitions. Under the uniformly sampled j-subset, the boundary event has probability <=4j/n. There are at most 6n triples with span <=4, and each specific triple has probability (j)_3/(n)_3. Hence **for all n>=5**,

    |P(clean | j)-binom(n-2j+2,j)/binom(n,j)|
       <= 4j/n + 6n*(j)_3/(n)_3,

where (j)_3=0 for j<3. This is a rigorous finite-domain discrepancy bound, not a numerical approximation.

If j=j(n) obeys j/sqrt(n)->c with c finite and nonnegative, this discrepancy tends to zero and

    binom(n-2j+2,j)/binom(n,j)
      = product_{i=0}^{j-1}(n-2j+2-i)/(n-i) -> exp(-2c^2).

Thus the **exact crossover limit** is

    lim P(clean | t=n-2j) = exp(-2c^2)
    lim P(dirty | t=n-2j) = 1-exp(-2c^2).

In particular j=o(sqrt(n)) yields clean fraction ->1, while sqrt(n)<<j<<n^(2/3) yields clean fraction ->0. The square-root theorem is *not* obtained by plugging a growing j into the fixed-j expansion.

Exact recurrence illustrations: for (n,j)=(100,5),(400,10),(900,15), the clean fractions are approximately 0.5871514, 0.5960066, 0.5993249, approaching exp(-0.5)=0.6065307. For (100,10),(400,20),(900,30), the fractions are about 0.1007277, 0.1162979, 0.1223324, approaching exp(-2)=0.1353353. These decimals illustrate, but do not prove, the limit.

## Validation and controlled status

The fully executed accompanying local reproducibility source (included in the downloadable evidence archive for this run) checks: both finite polynomial certificate identities exactly; 14-state grade sign bijection; the coefficient recurrence against all-grade integer path DP through n=96; all 8191 raw bit words through depth 12; all 65528 sign words for lengths 3..15 against the equivalence outside B; exact j=1,2 formulas and finite fine-channel bounds; scaling illustrations by an independent recurrence through n=900, j<=30. No floating-point arithmetic is needed for the proofs. A smaller repository verification script accompanies this note as an additional symbolic checker; it is not misrepresented as byte-identical to the locally executed complete program.

GitHub authenticated identity: awdawmip. Native task listing returned CONTROL_QUOTA. Native researcher session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. This **does not** imply no available Task; it means a live active owner and valid CLAIM could not be determined here. This draft has no service-issued researcher identity, official Result, independent Driver review, Working Truth promotion or P000 change.

**R4-EC14 next unit:** extend the source-contamination bounds into j>>n^(2/3), especially positive-density j=alpha*n, using rigorous automaton large deviations; separately retain fixed effect-blind six-control-state versus seven-control-state precision as an open question. Source-port timing from R193 and actual native X6 correspondence remain unverified and must not be silently inferred from the auxiliary model.
