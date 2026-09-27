# Closing the unit-slope mixed kernel when the reduced slope is plus or minus one

Status: SYMBOLIC / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED. This is a new proof note, not a modification of the frozen mixed-reciprocity source. No scientific import, host numerical test, external query, or remote write was performed.

## 1. Exact problem and sources

The remaining kernel in `../sep27-qft-two-bit-mixed-recurrence/MIXED_THRESHOLD_RECIPROCITY.md`, SHA256 `2f2f90d23324c3a672aec67e8ff7783ebfcb511fef6cdfae774e06a106a0949a`, is

    Q[alpha,beta,gamma](N;m,c;R,p,B)
      = sum_(0<=j<N) j^alpha floor((j+c)/m)^beta
                            floor((p*j+B)/R)^gamma,                 (1)

where N>=0, m,R,p>=1, c and B are signed integers, and alpha+beta+gamma<=D<=5. The convention x^0=1 includes x=0. The original application has p=2V, m=P/p, V=2^ell and P=2^(k+1), with ell<k. Its active fine-knot reduction calls at most four parameter families (1) per modular orientation. General (1) was not closed by the preceding note.

We use the prospective ordinary single-floor contract proved in `../sep27-qft-floor-degree-five/DEGREE_FIVE_RECIPROCITY.md`, SHA256 `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`:

    F[u,e](n,d,a,b)=sum_(0<=j<n) j^u floor((a*j+b)/d)^e,
    u+e<=5, n>=0, d>=1, a,b signed.                              (2)

That proof has one Euclidean child per parameter state. It is a separate dependency, not a claim that the frozen degree-three API supports degree five. No backend is run here.

## 2. Two exact preliminary reductions

### Removing a common factor of the slope and denominator

Let g=gcd(p,R), p=g*p0, R=g*r, and write B=g*B0+b0 with 0<=b0<g. Then

    floor((p*j+B)/R)=floor((p0*j+B0)/r).                           (3)

Indeed p0*j+B0 is an integer, and adding b0/g in [0,1) before division by the positive integer r cannot cross the next multiple of r. This proof includes signed B. Gcd, all divisions, and the range assertion on b0 are paid operations in a future typed implementation. Equation (3) does not mean that B is divisible by g.

If r=1, the remaining floor is affine, and fixed-degree expansion reduces (1) directly to (2). Assume r>1 below.

### A signed unit residual

Suppose the reduced slope has one of the source-verifiable forms

    p0=A*r+1  or  p0=A*r-1.                                      (4)

For the plus sign,

    floor((p0*j+B0)/r)=A*j+floor((j+B0)/r).

For the minus sign, the exact integer identity is

    floor((p0*j+B0)/r)=A*j-floor((j+r-1-B0)/r).                    (5)

The latter follows from floor(-x/r)=-floor((x+r-1)/r) for integer x, including negative x. After the binomial expansion of the gamma-th power, each term therefore has the form

    j^a floor((j+c)/m)^b floor((j+d)/r)^e,
    a+b+e<=D,                                                    (6)

where d=B0 in the plus case and d=r-1-B0 in the minus case. The coefficient includes the appropriate power of A and sign. In particular, the minus case is not replaced by a positive floor with the original offset. All expansions preserve total degree. Fixed exponents give a fixed number of terms, regardless of A or any scale.

The route is selected from (3)-(4), before computing an answer. Equivalently, for r>1 the canonical reduced slope remainder is 1 or r-1. When both descriptions apply either fixed convention is valid; choosing one consistently avoids duplicate work. All eligibility calculations must be typed and recorded.

## 3. Two unit-slope floors terminate in two ordinary tables

This section closes (6) for arbitrary m,r>=1 and signed c,d. Set

    A_j=floor((j+c)/m), B_j=floor((j+d)/r),
    Delta_b(k)=k^b-(k-1)^b,
    S_a(t)=sum_(0<=j<t) j^a.

Return the empty sum when N=0. For N>=1, the A jumps within the observed range occur at integer locations

    J_A(k)=m*k-c,   k=A_0+1,...,A_(N-1),

and the B jumps at

    J_B(l)=r*l-d,   l=B_0+1,...,B_(N-1).

Both locations lie in [1,N-1]. Empty ranges contribute zero. There is no loop over these potentially long ranges in the algorithm below.

At a coincident jump, update A first and B second. Immediately before an A jump the B value is

    B_A^-(k)=floor((m*k-c+d-1)/r).

At a B jump the updated A value is

    A_B^+(l)=floor((r*l-d+c)/m).

The minus one in the first formula is essential, including when m and r have a nontrivial gcd. The corresponding increments of A^b B^e are

    Delta_b(k) [B_A^-(k)]^e,
    [A_B^+(l)]^b Delta_e(l).

At a tie their sum equals the full product increment, with no commutativity assumption beyond these scalar integer factors. Interchanging the finite jump sums with the original sample sum yields

    sum_(0<=j<N) j^a A_j^b B_j^e
      = S_a(N) A_(N-1)^b B_(N-1)^e
        - sum_k Delta_b(k) [B_A^-(k)]^e S_a(m*k-c)
        - sum_l [A_B^+(l)]^b Delta_e(l) S_a(r*l-d).                (7)

Each jump affects precisely the indices j>=J. Thus its omitted initial weight is S_a(J), which proves (7). This is a terminal algebraic reduction to ordinary floors, not a recursive mixed transpose. It remains valid for negative quotient values, N=1, b=0, e=0, and ties at the last observed index. Delta_0=0 suppresses the corresponding entire correction; zero powers are not suppressed.

For an explicit API mapping, let

    k0=A_0+1, nA=A_(N-1)-A_0,
    l0=B_0+1, nB=B_(N-1)-B_0.

After k=k0+x and l=l0+x the two ordinary table parameter tuples are

    TA=(nA, r, m, m*k0-c+d-1),
    TB=(nB, m, r, r*l0-d+c).                                    (8)

Only nonempty required tables are called. In the first correction the polynomial multiplying the floor has degree at most (b-1)+(a+1)=a+b. Adding its floor exponent e gives at most D. In the second correction the bound is a+e+b<=D. Shifts to zero origin preserve it. The same two table tuples work for every fixed-degree triple (a,b,e) with the given N,m,r,c,d, so the binomial terms from (5) reuse the same tables rather than generating a new family for every exponent.

The coefficients of S_a are rational in their expanded form. A typed implementation should form the combined integer numerator using the degree-five source's declared Faulhaber denominator and perform the exact final division; it must not round or separately divide nonintegral monomials. In a nonzero jump correction, a<=D-1; the standalone endpoint S_D(N) is handled by the ordinary contract's exact degree-(D+1) power sum.

## 4. The closed input family and cost

Combining (3), (5), and (7) proves:

> For every fixed D<=5, (1) is computable from at most two ordinary degree-D parameter tables whenever r=R/gcd(p,R) is one or the reduced slope p/gcd(p,R) is congruent to plus or minus one modulo r. The r=1 case needs at most one ordinary table. All remaining work is a fixed-degree coefficient expansion and paid integer endpoint/eligibility arithmetic.

This supplies a genuine terminating route for this subfamily. Its only nontrivial recursive backend is the already stated single-floor Euclidean recurrence. It neither enumerates m nor scans p, R, or the observed range. Fixed-degree expansions and two Euclidean chains have polynomial bit cost under the exact typed arithmetic contract; this is a mathematical cost statement, not a measured runtime or a claim that all evidence serialization is free.

A concrete new non-top two-bit family is

    p=2V, R=2V-1 or R=2V+1, arbitrary ell<k<g-1.                 (9)

For R=p-1, p=R+1; R=1 is the separately handled affine case. For R=p+1, p=R-1. Thus both routes satisfy the theorem without any restriction on the potentially large gap k-ell or on H=L/P. This includes a subfamily of the earlier p<R<P obstruction: signed normalization, not another unproved transpose, is what resolves it.

For the particular spline combination in the source note, a conservative count per nonempty original orientation is: at most two ordinary degree-three tables for the coarse active correction, four degree-four/five tables for the fine prefix, and four active mixed families each reduced to two degree-five tables by this note. Therefore at most fourteen ordinary degree-five-capable table calls per orientation, or twenty-eight for the two modular orientations, suffice symbolically. This is a safe parameter-table count, not a minimal design, a primitive-call count, or a benchmark. Exact range emptiness and shared tuples can reduce it. Endpoint polynomials, scale construction, signs, gcds, all normalizations and exact divisions remain separately paid.

The scalar query retains the original heads r_query and R-r_query (0 and R at residue zero), keeps both coincident half-modulus orientations, and uses the original 4^-g normalization. The r used in sections 2-3 is a reduced denominator, not the requested modular residue. Supplied order/address information remains an external paid dependency. No method to discover an unknown modular order or group logarithm is obtained by selecting (9).

## 5. Relation to other small domains and the unresolved case

A separate elementary closure, not needed for (9), follows when m is bounded: split j=m*t+tau, 0<=tau<m. Then the first floor is t+floor((tau+c)/m), while the second is floor((p*m*t+p*tau+B)/R). Each nonempty class gives one ordinary degree-D table after polynomial expansion. This costs up to m classes. At m=2 it is a legitimate fixed two-class reduction; with general m=2^(k-ell), calling it a bit-polynomial algorithm would hide exponential work.

The coordinator's separate adjacent-bit shift proof gives a substantially lighter route for m=2 and should be preferred to this generic degree-five detour. The contribution of (9) is arbitrary bit separation in a distinct modulus family, not an improvement claim over the adjacent construction.

For the general case, let a be the canonical remainder of p0 modulo r. The representative a-r is another exact choice, and either sign can reduce the absolute slope to min(a,r-a). If that absolute residual is one, section 3 closes the problem. For larger residuals, signed normalization alone does not turn the second floor into a unit-slope floor. Transposing can again produce a denominator multiplied by m; neither an acyclic global parameter measure nor a polynomial bound on the aggregate state count has been proved here. Detecting an ineligible input must return an explicit unsupported-route status in a restricted implementation, rather than silently enumerating a scale or claiming a general zero answer.

This is a strict sufficient family, not a necessity theorem or a hardness result. It does not settle arbitrary mixed floors, growing sign masks, noncommuting matrix weights, or full Shor dequantization.

## 6. Minimal future typed interface

A separately versioned implementation can expose a complete degree-D family request for (1), or just the fixed indices required by the spline caller. Its certificate should bind the source and ordinary backend and record:

- original parameters and empty N disposition;
- the typed gcd, B division, reduced slope division, selected plus/minus/affine route and offset transformation;
- endpoint quotient values, k/l ranges, complete table tuples (8), and proven empty or Delta_0 omissions;
- coefficient expansions, exact common denominators, actual signed operation references, and final reconstruction;
- actual ordinary table evidence and all reused-table links, with no fabricated zero-table record;
- fresh strict replay, failed work, terminal failure/reuse rules, and separate production/validation accounting.

The positive mathematical result is ready for source implementation, but this note contains no implementation or actual arithmetic evidence. Any future bounded execution must distinguish this new modulus-family admission from the older aligned V|R admission and retain rejected inputs with their actual paid work.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
