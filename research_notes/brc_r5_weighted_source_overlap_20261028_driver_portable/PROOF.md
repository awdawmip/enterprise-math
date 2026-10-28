# R5: Sharp weighted source-overlap capacity at every LR signature

**2026-10-28 | Author-side / NONBLIND / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This contribution is not a native Driver Review, frozen Result, formal task publication, independent scientific validation, or X6 dynamical theorem.

**Immediate predecessor and authorship:** [R5 exact unweighted common-source polytope](https://github.com/awdawmip/enterprise-math/blob/6cfd90ee58e7c9c3f710afee40dc5383106acddd/research_notes/brc_r5_overlap_gluing_20261028_t1948/RESEARCH.md). Preserve its author's provenance and the exactly equal-source-weight result. Source read anchors: EM main 9a20dfa089615f6b11cc63e3c8abc5943b53e9e8; Global Knowledge main 9e8160d23b284f44f31d73b9b7e99830e8e39a5e; backend's distinct frozen Global P000 7b33f8066e9993e7c941959a9d738ed405248eb8 (blob ba8e4c75cdb3663ab3fde07e4286782344b0ed42). Project P000 V5, 6D/Heartbeat World and BRC observer/provenance typing remain binding. The present probability vectors are auxiliary finite observers, not the complete native X6 space.

## Exact all-real theorem

Let n>=3, 0<s_1<...<s_n, s_1<r<s_n. Let q,q' be nonnegative probability laws with common signature mean r, and P_i=s_i q_i/r, P'_i=s_i q'_i/r. Define

    u=(sum_i |q_i-q'_i|)/2;
    v=(sum_i s_i |q_i-q'_i|)/(2r);
    M=1-u; C=r(1-v); D=rv.

Fix a *feasible* pair (u,v), a signature index k and strictly positive first-stage source Q masses w_1,w_2. Set w_- = min(w_1,w_2), w_+ = max(w_1,w_2). With fractions for endpoints omitted when their denominators are zero, define

    G_k = min(M,
              (C-s_1 M)/(s_k-s_1)        if k>1,
              (s_n M-C)/(s_n-s_k)        if k<n),

    U_k = min(u,
              (D-s_1 u)/(s_k-s_1)        if k>1,
              (s_n u-D)/(s_n-s_k)        if k<n).

Then the exact maximum over ALL real nonnegative mean-r conditional laws is

    max_{q,q': prescribed u,v} min(w_1 q_k, w_2 q'_k)
      = min(w_- (G_k+U_k), w_+ G_k).                        (*)

The given (u,v) is feasible precisely when

    0<=u<=1,  s_2 u<=rv<=s_(n-1) u,
    s_1(1-u)<=r(1-v)<=s_n(1-u).

A rational feasible tuple has a rational maximizing witness. With equal source weights w_1=w_2=w, (*) reduces to w G_k and recovers the predecessor's overlap-coordinate bound. The weighted optimum can be strictly larger than min(w_1,w_2) G_k.

If strictly positive conditional laws exist for these fixed u,v (equivalently M>0, s_1 M<C<s_n M along with the feasibility constraints), (*) is their sharp SUPREMUM, approached by positive laws with identical u,v; the boundary maximum generally requires zero common mass at some signature.

## Proof

Decompose q=c+a and q'=c+b, where c_i=min(q_i,q'_i), a_i=(q_i-q'_i)_+, b_i=(q'_i-q_i)_+, so a_i b_i=0. Common part c has mass M and signature moment C. Each residual a,b has mass u and moment D. For any vector x of mass X and moment Y, its k-coordinate satisfies

    0<=x_k<=min(X,
                  (Y-s_1 X)/(s_k-s_1)  if k>1,
                  (s_n X-Y)/(s_n-s_k)  if k<n).

Consequently c_k<=G_k and a_k,b_k<=U_k. If the lower-weight source carries the residual at k, the overlap is at most min(w_- (G_k+U_k),w_+ G_k); if the higher-weight source carries it, the overlap is at most w_- G_k, which is never larger. This proves the upper bound.

For attainment, choose c_k=G_k and distribute M-G_k mass with moment C-s_k G_k over the smallest and largest signatures *other than k*. The constraints defining G_k force nonnegative interpolation weights. If u=0, set a=b=0. Otherwise let m=D/u, so s_2<=m<=s_(n-1), and allocate a to the lower-weight source:

- m>s_k: a is the mass-u, mean-m interpolation on {s_k,s_n}. Take b on {s_1,s_(n-1)} if k>1, or {s_2,s_(n-1)} if k=1.
- m<s_k: a is the interpolation on {s_1,s_k}. Take b on {s_2,s_n} if k<n, or {s_2,s_(n-1)} if k=n.
- m=s_k: take a=u at k; b is the mass-u, mean-m interpolation on {s_1,s_n}.

All interpolation weights are nonnegative by the TV wedge, and a and b are disjoint. At n=3 the repeated support {s_2,s_(n-1)} is simply the point s_2; the wedge forces m=s_2. The k-th residual of a is exactly U_k, the k-th residual of b is zero. Thus q=c+a, q'=c+b realize the same u,v and attain (*) simultaneously. All operations are rational for rational data.

For strict positivity, choose any full-support c^+ of mass M and moment C. It exists when M>0 and s_1M<C<s_nM. Replace c by (1-epsilon)c+epsilon c^+ and keep a,b fixed; then q and q' are strictly positive and preserve u,v exactly. Their overlaps converge to (*). **QED.**

## Exact rational countertransfer: equal vs unequal source weights

At signatures (1/2,1,2,3), r=3/2 and u=v=3/5, the top k=4 has G_4=4/25 and U_4=6/25. Equal source masses (1/4,1/4) force overlap <=1/25, strictly below 1/20. Different source masses (1/6,1/3), whose total remains 1/2 and whose two source histories still have LR 3/2, yield the sharp nonnegative maximum 4/75 >1/20.

Indeed the predecessor's strictly positive rational laws

    q  =(147/250,1/100,1/100,49/125);
    q' =( 57/250,31/100,31/100,19/125)

have the same u=v=3/5. With Q(A,B,O)=(1/6,1/3,1/2) and P(A,B,O)=(1/4,1/2,1/4), all initial source masses are positive, sum to one under each law, A/B have LR 3/2 and O LR 1/2. Their top-branch shared weighted Q mass is

    min( (1/6)(49/125), (1/3)(19/125) )
      =19/375 >1/20 >1/25.

The predecessor's positive second-stage kernels at LR=3 can be retained unchanged, giving a normalized two-stage weighted-occupancy witness. This DOES NOT contradict the predecessor's fixed-equal-weight obstruction; it proves that the assumption w_1=w_2 is indispensable when transferring the 1/25 bound.

## Proof boundaries, verification, and next unit

VERIFY.py performs exact Fraction-only checks, including the displayed strict-positive witness and 4,875 rational (n,k,source-weight) sharp constructions and upper-bound instances, n=3..7. Universal validity is proved by interpolation above, not extrapolated from checks. This is a source-exposed author-level extension, not independent review/admission, signed Bellman separation, the all-directions convex-hull equality, the original four-observer actual-image separation, or native X6 physics.

Next mathematical unit: keep source Q weights along with the TV/common-part/residual-capacity coordinates through TWO nonterminal stop/continue decisions. Derive exact four-observer signed Bellman supports with separate P/Q occupancies; eliminate any candidate with signed-support inequality before testing true-image inequality. Existing R5 mother objective and formal Task/Result provenance remain unchanged; do not duplicate formal publications without current native Driver authority.
