# S23/AV: sharp lexicographic threshold-order extension through H=4,910,647

Date: 2026-11-08 Asia/Shanghai. Status: author-side symbolic theorem and exact-integer executable tests; independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Parent: PR #1777, preceding sharp fixed-key theorem in the same research directory at commit 34b3104cf77c4c4c7011869763fd24ee6f7dce71.
Model: two-point S23/AV auxiliary likelihood-sign observer retaining the joint label (1,4) counts and label-3 padding.

## Theorem: sharp two-coordinate integer order

Let

    r = ln(7)/ln(10/7),
    P=2074774, D=380295, n=P+D=2455069,
    u=(79,431), w=(D,P),
    epsilon=79*r-431, eta=P-D*r.

The strict rational enclosure previously established with 45 atanh-series terms certifies

    0 < eta < epsilon < 2*eta.

For every integer 0<=H<=4910647=2*n+509, define T_H={r*v-j: v,j>=0,v+j<=H}. Then *all* thresholds in T_H have exactly the strict ordering induced by the lexicographic integer key

    L(v,j)=(P*v-D*j, -v).

This order applies after the scalar first-component key starts colliding at H=n, and is sharp: at H=4910648=2*n+510, this integer lexicographic key gives an incorrect comparison for two distinct thresholds.

### Proof by unimodular coordinates

The vectors u and w form a unimodular lattice basis:

    79*P-431*D=1.

For the displacement (a,b) from a first threshold point to a second, there are unique integers A,B such that

    (a,b)=A*u+B*w,
    A=P*a-D*b,    B=79*b-431*a.

The actual real difference between the second and first thresholds is

    r*a-b=A*epsilon-B*eta.

Any two points of the nonnegative triangular domain have a displacement satisfying |a|+|b|<=H. Suppose A>0. If B<=0, the real difference is positive. If B=1, it is at least epsilon-eta>0. If B>=2, both components of A*u+B*w are positive and so

    a+b=510*A+n*B >=510+2*n=4910648>H,

contradiction. Consequently when A>0 the actual real threshold difference is positive, matching the sign of the scalar integer key difference A. When A<0, reverse the displacement and apply the same argument to -A>0.

For A=0, the displacement is B*w and the actual real difference is -B*eta. The two thresholds have the same first key component; their second lexicographic key difference is -a=-B*D. Both have the same strict sign, since D>0 and eta>0. When A=B=0 the points coincide. This proves that L is injective and gives exactly the strict order for all H<4910648.

For sharpness let

    q=u+2*w=(760669,4149979).

Its coordinate sum is 4910648; at H=4910648 it belongs to the triangle together with (0,0). Its first integer key is A=1, so L(q)>L(0,0), whereas its real threshold is epsilon-2*eta<0, hence t(q)<t(0,0). The scalar-first lexicographic order fails at that boundary. QED.

## Exact rank/select in this enlarged regime

The earlier floor-sum formula C_H(m) exactly counts points with scalar integer key K(v,j)=P*v-D*j<m. The formula counts integer points even when keys collide and is therefore unchanged.

To decode a scalar key z, put

    v0=(z*P^{-1} mod D),   0<=v0<D,
    j0=(P*v0-z)/D.

All its integer-coordinate solutions are v=v0+D*t and j=j0+P*t. A point is in the nonnegative H-triangle exactly when the integer lift parameter obeys

    t0=max(0,ceil(-j0/P)) <=t<= t1=floor((H-v0-j0)/n).

In the lexicographic threshold order, the fiber is enumerated in DESCENDING t (because the second key is -v). Thus for a valid point at lift t,

    rank_H(v,j)=C_H(K(v,j))+(t1-t).

To select the threshold at zero-based rank s, binary search for the scalar key z for which C_H(z)<=s<C_H(z+1), then choose t=t1-(s-C_H(z)). In the new fixed regime each fiber contains at most 3 points, and this rank/select procedure avoids the complete O(H^2) threshold list.

## Exact arithmetic checks and limits

The companion VERIFY_LEX_ORDER.py imports the previous VERIFY_TRIANGULAR_KEY.py implementation. It verifies the four strict rational arithmetic inequalities establishing 0<eta<epsilon<2*eta, and compares all ranks/select inverses and all real successive threshold signs at H=1..64 using exact integers; it then samples rank/select inverse queries for H=380294, 380295, 2455068, 2455069, 2455070, 4910137, 4910138, 4910647. The largest queried finite triangle has 12,057,234,345,276 thresholds, not enumerated. It also checks the exact sharp boundary counterexample (760669,4149979) at H=4910648. The executed console transcript is in RUN_LEX.txt.

The theorem is a symbolic proof for the complete claimed range. The finite program validates its precise arithmetic predicates and implementation. It is a theorem about the auxiliary two-point observer's *threshold order*, not a claim that N(H) is constant through 4910647. The pre-existing seven-plateau construction and its last unresolved horizon H=2455579 remain separate; use the lexicographic order and finite floor-sum occupancy there without equating order equivalence with all-cell capacity.

Next: H>=4910648 requires a new rational key or an extra exact integer comparison stage. Analyze the first near-resonant key inversion of u+2w, derive exact post-boundary gap-class counts and observer capacity bounds, and retain the lawful six-source/ten-label bridge and minimax delta_4 as distinct objectives. Publication is an author-side proof candidate pending independent scientific review and Source task/CLAIM verification.