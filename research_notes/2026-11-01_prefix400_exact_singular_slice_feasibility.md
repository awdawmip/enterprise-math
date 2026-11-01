# PREFIX-400 — Exact finite feasibility and robust singular-fiber branch separation

Date: 2026-11-01 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. This is an external static complex three-amplitude inverse model, NOT a P000 X6, native slice, or typed BRC dynamics theorem.

Frozen canonical inputs: GLOBAL_KNOWLEDGE_V1 main@9ced971d8b4a0352707cfb25bcb17977a494feb4 (bootstrap/manual, P000 projection, original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, math/BRC contracts); Enterprise Math main@993a408982a302265cb3c31f93e69e4751299500 (AGENTS, P000, joint observer rule, portable research protocol and PREFIX-399). GitHub contributor identity: awdawmip.

## Input and exact equivalence

The original complex five-Port matrix is

    A=[[4,4,0],[0,-4,4],[-5+3i,0,-3+i],
       [-2-2i,4+4i,2+2i],[-2,0,5+2i]].

Let A3 be its first three rows (det A3=-32+32i) and W=A3Y. Fix I1=1, I2=3481/3969, Cu=14884/3969; these saturate the triangle inequality and force the positive-real gauge W=(1,59/63,c+id). Fix I3=k as an EXACT rational number. I4 and I5 may have independently bounded rational errors xi4 and xi5 about measured centers J4 and J5; coherent Cv may have error eta about q. The exact complex source-feasibility problem is to decide whether at least one Y exists for all six measurements.

Set N=75154, K4=300616/3969, K5=2638189/63504, T=245c-123d, sigma=123c+245d. Direct expansion from the ORIGINAL A gives:

    I3=c^2+d^2=k
    I4=K4+16k+(16/63)T
    I5=K5+(53/8)k+(61/504)T
    T^2+sigma^2=N*k
    Cv=1+k+(2/N)(245T+123sigma)

Consequently, source feasibility is EQUIVALENT, with no singular division, to a circle and two rational closed strips:

    T^2+sigma^2=N*k,  L<=T<=U,  A<=245T+123sigma<=B

where

    L=max((63/16)(J4-xi4-K4-16k),(504/61)(J5-xi5-K5-(53/8)k))
    U=min((63/16)(J4+xi4-K4-16k),(504/61)(J5+xi5-K5-(53/8)k))
    A=(N/2)(q-eta-1-k), B=(N/2)(q+eta-1-k).

Any solution reconstructs c=(245T+123sigma)/N, d=(-123T+245sigma)/N, W=(1,59/63,c+id), and the exact source Y=A3^{-1}W.

## Theorem A (complete, finite, exact)

For arbitrary rational k,J4,J5,q and nonnegative rational xi4,xi5,eta, this exact-I1/I2/Cu/I3 slice is decidable by at most NINE quadratic-algebraic candidate points. k<0 gives NO. For k=0 test the origin; if L>U give NO. For k>0 enumerate (0,+sqrt(Nk)) and all real intersections of the circle with the four strip-boundary lines T=L, T=U, 245T+123sigma=A, 245T+123sigma=B. Four lines yield at most eight intersections.

The exact intersections of uT+v sigma=w with the circle are
    (T,sigma)=((uw ∓ v sqrt(D*N*k-w²))/D, (vw ± u sqrt(D*N*k-w²))/D),
    D=u²+v²>0,
provided D*N*k-w²>=0. Every inequality reduces to the sign of a+b*sqrt(r), determined by rational comparisons of a² and b²*r and operand signs. The supplied standard-library program emits either a YES algebraic witness (also c,d and a reconstructible Y), or a NO table of exact signs on every candidate.

Proof of completeness: the permitted subset of the positive-radius circle is closed. If it is the full circle, the fixed anchor is feasible. If nonempty but proper, connectedness of the circle implies its relative boundary is nonempty. A boundary point must saturate at least one of the four strip inequalities, and therefore belongs to the enumerated intersections. Testing all candidates is therefore necessary and sufficient. The zero-radius case is the singleton origin. Exact algebraic reconstruction proves the converse. This excludes the interval-only false-positive weakness isolated in PREFIX-398.

Scope: exact I1,I2,Cu,I3 and rational bands on I4,I5,Cv; a generic six-reading noisy five-real-variable CAD is NOT claimed.

## Theorem B (strict uniform noisy-branch separation)

Use the PREFIX-399 exact pair at k=2,T0=122,sigma0=+/-368, J4=550600/3969, J5=4417309/63504, nominal Cv+ =5, Cv- =97357/37577. Fix I1,I2,Cu,I3 exactly as above. Allow independent |I4-J4|<=1/10 and |I5-J5|<=1/10. Since the I4 constraint implies |T-122|<=delta=63/160, all allowed T have |T|<123, so |sigma|=sqrt(150308-T²)>367 and |d sigma/dT|<123/367.

Each signed branch Cv+(T), Cv-(T) differs from its respective nominal Cv by STRICTLY less than
    H=(2/75154)*(245+123²/367)*(63/160)
     =1654443/551630360 < 3/1000.

Hence across ALL allowed (possibly different) T on the positive and negative branches, the true observer separation satisfies
    inf Cv+ - sup Cv- > 90528/37577 - 2H
                         = 662821077/275815180 > 2.

Even with independent |Cv_measured-Cv_true|<=eta<=1, the two source-label observation sets remain strictly disjoint, with exact certified margin >111190717/275815180. Both labels remain realized (the nominal pair). This is branch-label identification, not pointwise uniqueness within each continuously noisy branch.

BRC observer-provenance discipline: the sigma sign identifies the two source fibers; the observer tuple (five intensities,Cu) can erase it, while Cv repairs it on the scope declared here. This is REUSE_APPLIED of the exact PREFIX-399 singular fiber; native typed BRC arithmetic was not executed.

## Actual verification and continuation

Local Python Fraction checker: PASS_PREFIX400_EXACT_CIRCLE_LINE_BOUNDARY_FEASIBILITY 8_CASES; PASS_PREFIX400_UNIFORM_NOISY_SINGULAR_TWO_BRANCH_CV_SEPARATION. The eight cases contain exact positive/negative-branch YES, exact midpoint NO, noisy-branch YES, noisy midpoint NO, incompatible intensity strips NO and k=0 YES/NO. The local independent SymPy checker re-expands the original A and returns PASS_PREFIX400_INDEPENDENT_ORIGINAL_A_MATRIX_CIRCLE_AND_CV_IDENTITIES. Finite tests check implementation, while the circle-boundary proof justifies all rational inputs in the stated slice.

Current native control: DIRECTED_RESEARCH manifest reported authority_granted=false; owner list returned CONTROL_QUOTA. Native session_start was rejected with STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No native activity/claim/Result/review/admission is implied by neutral GitHub research-note storage. Remote checker is source storage; actual test execution was on the local source, which is available in the local evidence package.

Next PREFIX-401: change I3=k from an exact rational equality to a rational interval (annulus/three-dimensional cone feasibility), then progress to complete exact QE for all five intensity intervals and noisy Cu, with reconstructible YES/NO witnesses. Analyze singular-to-regular stratification without quotienting away sigma/source identity.
