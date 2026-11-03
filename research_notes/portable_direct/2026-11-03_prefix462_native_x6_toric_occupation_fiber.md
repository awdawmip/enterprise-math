# PREFIX-462 — X6 BRC toric occupation fibers and exact weight quotient criterion

2026-11-03 Asia/Shanghai. AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Successor to PREFIX-461 (main commit b6ac82b5c891624a4bcd289eacf2a539efc3cb2b). Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d. The current global/Enterprise Math norms, P000, ACTIVE X6/Heartbeat and joint-residual-preservation rules were read separately.

## Question and typed model

Following PREFIX-461, for terminal historical residue q−1 at word length N=q+m−1, q>=m+1, exactly q−1 steps are −e1; the other m steps lie in the eleven-letter native X6 alphabet D={+e1,±e2,...,±e6}. Remove the fixed −e1 translation and distinguish: ordered native words; unordered counts of each of the eleven letters (occupation); terminal endpoint (s,y2,...,y6); and the historical residue port. Each has different information content. Coordinates are signed X6 chart displacements, not final Cell addresses. Positive branch weights may be added/multiplied exactly using the frozen BRC positive histogram semantics, without replacing positive mass with signed amplitude.

We determine a universal algebraic presentation of the occupation-to-endpoint quotient, its exact fibers, and when an *individual occupation product weight* can descend to the endpoint.

## Theorem A: toric complete intersection, for every number of pairs and every length

Let k>=1 and let S=Q[Z,U1,V1,...,Uk,Vk], with all 2k+1 variables of degree one. Define phi:S -> Q[t,x,x1^±1,...,xk^±1] by Z↦tx, Ui↦t xi, Vi↦t xi^-1. The exponent image of a degree-m monomial records (m,s,y1,...,yk), where s counts the unilateral Z letter and yi counts Ui minus Vi. The full toric kernel is

ker(phi) = (Ui Vi − U1 V1 : i=2,...,k).

These k−1 quadratic relations form a Gröbner basis with leading monomials Ui Vi (i>=2), a homogeneous regular sequence, and the quotient is a domain. Its Hilbert series is

H(z)=(1-z²)^(k−1)/(1-z)^(2k+1)=(1+z)^(k−1)/(1-z)^(k+2).

For native six-axis residual D, k=5, so H(z)=(1+z)^4/(1-z)^7. In particular dim_Q (S/ker phi)_m = sum_{j=0}^4 binom(4,j)binom(m-j+6,6) (with out-of-range binomial coefficients zero), exactly the PREFIX-461 support enumerator.

Proof: Orient every UiVi -> U1V1 for i>=2. The initial monomials are mutually coprime, so Buchberger S-pairs reduce to zero. Given a monomial with counts (s,c_i^+,c_i^-), define yi=c_i^+−c_i^-, pi=min(c_i^+,c_i^-), and p=sum_i pi=(m−s−sum|yi|)/2. The unique irreducible normal form is Z^s (U1V1)^p prod_i Ui^max(yi,0) Vi^max(−yi,0). It is completely determined by (m,s,y), and different normal monomials have different Laurent images; hence the proposed Gröbner ideal is precisely ker(phi). Pairwise coprime leading terms imply that the quadrics form a regular sequence, yielding the displayed Hilbert series. QED.

## Theorem B: exact occupation fiber and four-integer repair

For any supported (m,s,y), let p=(m−s−sum|yi|)/2. The occupation vectors in that endpoint fiber are in bijection with nonnegative integer k-tuples (p1,...,pk) with sum pi=p:

c_i^+=max(yi,0)+pi, c_i^-=max(−yi,0)+pi, c0=s.

Therefore the fiber contains exactly binom(p+k−1,k−1) *unordered occupations*. For the native k=5 carrier this is binom(p+4,4); keeping four pi values repairs the exact occupation label, as the fifth is p minus their sum. The corresponding ordered-word multiplicity for one occupation is m!/(s! prod_i c_i^+! c_i^-!). The endpoint quotient cannot recover the order of the word.

The bijection also yields the exact, all-m identity:

sum_{(s,y) in W_m} binom((m−s−sum|yi|)/2+4,4) = binom(m+10,10),

where W_m has s>=0, s+sum|yi|<=m and the requisite even slack. The right side counts all weak compositions of m into eleven bins. The four primitive pair-exchange relations connect each entire occupation fiber. QED.

## Theorem C: exact sharp scalar product-weight descent

Assign fixed strictly positive rational weights w0,wi^+,wi^- to the eleven letters, and set rho_i=wi^+ wi^-. For an occupation vector the product of its letter weights is an endpoint-only function for *all lengths and supported endpoints* if and only if rho_1=...=rho_k.

Necessity: all length-two opposite pairs UiVi end at the same displacement and have weights rho_i. Sufficiency: Theorem A connects any two occupations with a common endpoint by swapping UiVi with U1V1; equality of all rho makes each exchange weight-preserving. The common product is

w0^s prod_i (wi^+)^max(yi,0) (wi^-)^max(−yi,0) rho^p.

For arbitrary weights the source-sensitive factor prod_i rho_i^pi survives. Treating the rho_i as algebraically independent indeterminates makes distinct pi-tuples distinguishable formal monomials, and hence the occupation fiber is precisely the generic product-weight distinction. The criterion is for *individual word product weight*. An endpoint-only BRC future can still use the sum of all positive masses over this fiber. An occupation/branch-history-sensitive future must retain the relevant pi allocation or its equivalent.

Concrete native witness: (w2^+,w2^-)=(3,5), (w3^+,w3^-)=(7,11). The two ordered orientations of the ±e2 return have total mass 2×3×5=30; the two orientations of ±e3 have 2×7×11=154. Their raw X6 endpoint is zero in each case, yet branch origin distinguishes the positive-mass contributions.

## Exact endpoint mass formula and validation

For positive rational weights, the full weighted mass of all length-m ordered residual words reaching (s,y) is exactly

M_m(s,y) = sum_{p1+...+pk=p} [m!/(s! prod_i(max(yi,0)+pi)!(max(−yi,0)+pi)!)] w0^s prod_i (wi^+)^(max(yi,0)+pi) (wi^-)^(max(−yi,0)+pi).

This is a purely finite positive-branch multinomial identity, compatible with PREFIX-461's Laurent generator. For a fixed last-history-sector of N=q+m−1 words with per-letter independent weights, also multiply by binom(N,q−1) times the (−e1 weight)^(q−1). A future that accesses intermediate order needs its original path identity.

Exact independent integer certificate: prefix462_toric_brc_certificate.py (stdlib Python, no approximate arithmetic) completely enumerates all eleven-bin occupation vectors m=0..8, checks canonical normal-form invariance, support Hilbert coefficients and every fiber size, then compares the multinomial weighted formula to independent ordered-step dynamic programming for m=0..6 using weights (2,3,5,7,11,13,17,19,23,29,31). m=8 has 43,758 occupation vectors and 17,469 endpoints. All checks returned PASS. Theorem scope is all k>=1,m>=0 for A and B, and strictly positive rational weights for C; the executed checks are finite regressions.

## Status, relation to open frontier, next

BRC reuse: REUSE_APPLIED of the pinned positive exact branch histogram and endpoint observer semantics; frozen source modules brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1 and brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8, read from scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d. The code is an independent exact combinatorial verification, not a newly executed native ControlPacket experiment. The algebraic quotient is a structured way to retain/repair source information; no phase/amplitude or physical heartbeat claim follows.

The mother all-degree X6 degree-(m+1) polynomial-moment rank conjecture remains: each sign-character block t=0,...,5 of the evaluation map on W_m has nullity max(0,floor((m−t+3)/2)) for all m>=2. The present graded toric Hilbert series counts support *locations*, not that polynomial-evaluation rank; the two distinct Hilbert problems need a connecting argument. Next PREFIX-463: build a parity-simplex Newton/border interpolation basis using the four quadratic exchanges and try to prove the exact evaluation-kernel recurrence; alternatively test the four-integer occupation-repair carrier against native BRC affine futures and bit-complexity metrics.

Provenance: prior PREFIX-461 report blob 03327c2684dbdb39bf3f20637be4; this run's executable, log and proof; current controlled sources per docs/RESEARCH_CONTINUATION_PROTOCOL.md, P000 and ACTIVE world definitions. Actual GitHub login awdawmip, repo permission admin/push. Current native task query returned CONTROL_QUOTA and session start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); active Owner/Researcher-ID unconfirmed. This is author-side preservation, not CLAIM, independent review or admission.
