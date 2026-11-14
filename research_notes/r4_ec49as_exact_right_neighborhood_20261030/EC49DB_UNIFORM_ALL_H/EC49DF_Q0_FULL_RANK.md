# EC49DF — Full three-channel positive-BRC rank on EC49DC's Q=0 certificate locus

**2026-11-01, author-side analytic theorem and exact finite native check.** Status: PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Frozen science inputs: GLOBAL_KNOWLEDGE_V1 main 176e1691b5401cba0e81da0b28574b2c9624d406, Enterprise Math main e5f31bafe2c7dd421430023f4d717013c424525f, predecessor EC49DD commit 6cb32857e7e0d1433297e7b40497da2136a56222. P000 and ACTIVE worldview not changed. Gateway 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, new job quota 5/5; active Source owner not verified. GitHub text is durable author-side evidence, not a native CLAIM, Result or independent mathematical review.

## Exact observer

Genuine ordered signed native X6 primitive-step prefixes have fixed length n and displacement D=(2s,2v,0,0,0,0), s integer, v>=0, |s|+v<=h. Adjacent ordered positive tags A=(+E1,+E2) and B=(+E2,+E1) are tracked jointly, including boundary into the future. Complete future operations are a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3). Futures have exactly h, or 1 through h, complete operations and return to the chosen Cell. Rows for a complete future/tag combine positive BRC channel products Wx, Wy (weights x_i,y_i>0 on positive step Ei, weight 1 on negative step) and independent branch count. Observation dimension is the rational-linear rank for rational weights, real-linear rank for positive real weights. No signed-amplitude, physical-propagation or variable-prefix-length inference is made.

## Theorem (new universal sufficient condition)

For two strictly positive six-vectors x,y put

    H(x,y) = det([[x3,x4,x5], [y3,y4,y5], [1,1,1]]).

If H(x,y) != 0, then for **every integer h>=2**, and in **every returning fiber**, the observer at literal prefix length n=2h+8 achieves the full three-channel ranks. Let defect delta=h-|s|-v. The exact/cumulative ranks are delta=0: (12,12); positive odd: (15,18); positive even: (18,18). Global dimensions are exact 3*(11h^2+15h+8)/2, cumulative 18h^2+24h+12. **The earliest simultaneous saturation length is n_sat(h)=2h+8.** The statement holds over Q for positive rational weights and over R for arbitrary strictly positive real weights with H!=0.

A concrete point on the old EC49DC certificate-zero locus:

    x = (2,3,5,2,4,1)
    y = (4,5,7,3,9,1).

These positive vectors are nonuniform and nonproportional. Yet EC49DC's factor Q=(x1-x3)*(y2-y3)-(x2-x3)*(y1-y3) equals (-3)*(-2)-(-2)*(-3)=0, whereas H=det([[5,2,4],[7,3,9],[1,1,1]])=-10 != 0. Consequently P=0 because P contains factor Q, but all three BRC channels **retain full observable rank** at the stated length for every h>=2. This proves EC49DC's certificate-zero locus is not a necessary rank-degeneracy locus. It neither contradicts EC49DC's proper sufficient theorem on P!=0 nor classifies all exceptional weights.

## Analytic proof: amplify literal tag-only witnesses using three neutral X6 axes

EC49DE provides, **for all h>=2 and all fibers**, literal length-(2h+6) prefixes p_1,...,p_r and legal complete returning suffix/tag rows (w_a,t_a) so that the count-only r-by-r matrix

    T[a,i] = 1[final_tag(p_i concatenated w_a)==t_a]

has nonzero determinant (r is the exact/cumulative tag rank 4, 5 or 6). This follows from EC49DE's six explicit neutral six-step primitive motifs with integer feature determinant -1, plus its four genuine positive mixed-boundary paths. These are real ordered signed-X6 paths, not semantic placement simulators.

For each i create three length-(2h+8) literal signed-X6 prefixes

    P(i,3)=(-E3,+E3)+p_i,
    P(i,4)=(-E4,+E4)+p_i,
    P(i,5)=(-E5,+E5)+p_i.

Each inserted gate has zero endpoint and no A/B adjacent-positive pair. Its final step is neither +E1 nor +E2, so it produces no seam tag; the final prefix step and all A/B history used by the full nine-state process are unchanged. Every complete future/tag thus takes the same Boolean T[a,i] on P(i,3), P(i,4), P(i,5). The positive BRC gate contributes factors (x_j,y_j,1), j=3,4,5, without discarding branch provenance.

Let Ax_i=Wx(p_i), Ay_i=Wy(p_i), Bx_a=Wx(w_a), By_a=Wy(w_a), all >0. The genuine 3r-by-3r observation matrix on selected suffix/tag rows and these 3r prefixes is exactly

    M[(a,Wx),(i,j)] = Bx_a * Ax_i * T[a,i] * x_j
    M[(a,Wy),(i,j)] = By_a * Ay_i * T[a,i] * y_j
    M[(a,C ),(i,j)] = T[a,i].

In each i-block of three prefix columns, right-multiply by the inverse of the 3-by-3 matrix G with rows (x3,x4,x5),(y3,y4,y5),(1,1,1). Regrouping channel rows/columns gives three independent r-by-r blocks:
    
    diag(Bx_a) * T * diag(Ax_i),
    diag(By_a) * T * diag(Ay_i),
    T.

All are invertible since T is invertible and all products are positive. Thus, up to the row/column permutation sign,

    det M = ± (det G)^r * (det T)^3
            * product_a(Bx_a * By_a) * product_i(Ax_i * Ay_i) != 0.

The observer's six-feature future-safe quotient implies the matching formal upper bound 3r. Hence rank exactly 3r at n=2h+8 for every h, on ALL fibers, provided H!=0. This sufficiency is independent of Q, and the proof uses only exact native signed paths and BRC products.

## Uniform sharp lower bound

Consider D=(-2h,0,0,0,0,0): its only returning complete suffix is e^h, tag-preserving and beginning +E3. For n<=2h+4 the prefix contains at most two positive primitive steps, so cannot exhibit both ordered tags A and B; the corresponding tag block vanishes and total 3-channel rank is at most 9<12. At n=2h+6 the prefix has exactly three positive steps; the only positive-step patterns that contain BOTH ordered adjacent pairs are 121 and 212. Since negative-step weights are 1, the triples (Wx,Wy,count) on that tag block take at most TWO distinct values. This block therefore has rank at most two, while the other three tag blocks contribute at most three each: whole fiber rank is at most 2+3*3=11<12 for **every** positive x,y. Odd prefix lengths cannot reach even D. At n=2h+8 our explicit gate proof achieves rank 12 in this fiber; every larger even length preserves a rank witness by prepending additional neutral (-E3,+E3) pairs, which add nonzero common weight factors without affecting the tag or boundary feature. Therefore n_sat(h)=2h+8 exactly.

## Actually executed finite evidence

The adjacent **VERIFY_EC49DF_Q0.py** imports the preexisting **VERIFY_EC49DD.py** and this same PR's **VERIFY_EC49DE_COMPACT.py**. It checks real signed-X6 endpoints, complete returning suffixes, actual ordered A/B history, exact integer positive weight products and modular determinants at prime 1000003. It uses the explicit rational example above. For h=2..7 it tests **398 nonzero genuine 3r-by-3r modular determinants** across **199 target fibers** and both exact/cumulative returning languages. It enumerates all **97655 complete operation words of lengths 1..7** and reconstructs all 398 witness minors from the actual primitive paths. Output is PASS and includes the computed exact/cumulative total dimensions. The finite check validates witness generation and arithmetic in that declared finite domain; all-h claims derive from the analytic 3-by-3 gate factorization plus sharp extreme-fiber obstruction, not numerical extrapolation.

**Next EC49DG:** enlarge the tag-safe neutral-gate criterion (e.g. choose any three positive axes among E3..E6), classify true low-rank strata when all such minors vanish, obtain compact universal certificate complexity bounds and independent formal checking. Preserve P000, Source owner and the existing independent-review requirements.
