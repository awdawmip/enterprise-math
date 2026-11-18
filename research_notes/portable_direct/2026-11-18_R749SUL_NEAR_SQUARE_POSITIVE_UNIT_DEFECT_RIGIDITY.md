# R749SUL — Near-square positive-unit rigidity for the optimal labeled two-Port feedback threshold

Date: 2026-11-18 (Asia/Shanghai)
Evidence: AUTHOR_EXACT_NOT_REVIEWED. Portable independent scientific continuation; no shared X6 CLAIM asserted.

## Exact predecessor and scientific scope

Extend R749SUK, pinned at
\`awdawmip/enterprise-math@0b292a4181f3729b2bda282cf35e6df2166531e5:research_notes/portable_direct/2026-11-18_R749SUK_UNIFORM_MAXIMIZER_DEFECT_AND_DIVISOR_FIBERS.md\`.
Its frozen scientific WBRC-T30–T32 inputs are \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
This note studies an auxiliary positive-rational, *labeled* two-Port feedback observer. The native Heartbeat World X6 Cell/Link/Port event and its triadic-force, source/resource and causality permissions remain distinct. No claim about native physical admission is made.

For an integer M>=2 put

    U_M={(a,u,v,d) in {1,...,M}^4 : ad-uv=1};
    tau(a,u,v,d)=max(u,v)*a*d;
    Q(a,u,v,d)=u+v-a-d.

The canonical adjacent-diagonal family is a=d and {u,v}={a-1,a+1}; by R749SUK it is exactly the Q=0 fiber. Let T*(M) be the maximum tau over noncanonical U_M, and Opt(M) the complete labeled argmax set.

## Theorem — an infinite positive-density region forces Q=+1

For EVERY integer t>=32 and EVERY integer delta satisfying

    0 <= delta <= floor(t/8),     M=t^2-1+delta,

the maximum T*(M) exists and EACH labeled tuple in Opt(M) has

    Q=+1.

Consequently the set of positive integers M for which all noncanonical threshold-maximizers have Q=+1 contains a family of natural density exactly 1/16. This is an unconditional statement in the stated auxiliary determinant-one Port model, not a hypothesis about the unobserved X6 event layer.

### Proof

**Step A: an explicit admissible positive-unit competitor.**
Set m=t^2-1 and take

    (a,u,v,d)=(m-t, m, m-2t+1, m-t).

For t>=32 all components are positive and <=m<=M, and

    ad-uv=(m-t)^2-m(m-2t+1)=t^2-m=1;
    Q=m+(m-2t+1)-2(m-t)=1.

It is noncanonical. Its threshold is

    W=m(m-t)^2.

Let B=3delta+2t. Since m=M-delta and m-t=M-(delta+t), elementary telescoping of the product gives

    0 <= M^3-W <= B*M^2.

Thus every maximizer satisfies tau>=W>=M^3-B*M^2.

**Step B: all maximizing triples lie in a thin top cube.**
Orient the tuple by swapping u,v if necessary, so u=max(u,v). The score and Q do not change. Since u,a,d<=M and u*a*d>=W,

    u,a,d>=M-B.

Put h=M-u, r=M-a, s=M-d, S=h+r+s. Then 0<=h,r,s<=B. Exactly,

    D=M^3-u*a*d
     =M^2*S-M*(hr+hs+rs)+hrs
     >= M^2*S*(1-B/M),

because hr+hs+rs<=B*S. Combined with D<=B*M^2 this gives

    S<=B/(1-B/M),    provided B<M.

**Step C: a uniform deficit obstruction to Q outside {0,1}.**
The determinant identity from R749SUK is

    (u-a)(u-d)=u*Q+1.

Write x=u-a=r-h and y=u-d=s-h.

If Q=q>=2, xy=qu+1>0. The alternative x,y<0 would imply q=x+y+(v-u)<0, impossible. Thus x,y>0. It follows that

    S=3h+x+y >= x+y >=2*sqrt(2u+1).

If Q=-k<=-1, then for u>=2 we have xy=1-ku<0. After exchanging a,d if needed write x>0 and y=-z<0. Then x*z=ku-1>=u-1 and d=u+z<=M implies z<=h. Hence

    S=3h+x-z >=2h+x >=2*sqrt(2hx)
      >=2*sqrt(2u-2).

For u=1, tau<=M^2, which cannot match W in the present range because W> M^2 (t>=32, delta<=t/8). Equivalently the thin-cube bound u>=M-B>1 already excludes u=1. Therefore every maximizing tuple with Q not in {0,1} obeys

    S>=2*sqrt(2u-2).

**Step D: disjoint quantitative bounds.**
Here B<=19t/8 and M>=t^2-1. For every t>=32:

    B/M <= 19t/[8(t^2-1)] <= 1/12,

and the thin-cube lower bound implies

    u-1 >=t^2-2-19t/8 >=(8/9)t^2.

Both inequalities follow by multiplying through positive denominators; at t=32 their corresponding polynomial differences are positive and strictly increasing thereafter. Hence Step B gives

    S <= (12/11)*(19t/8)=57t/22,

while Step C would give

    S >=2*sqrt(2*(8/9)t^2)=8t/3.

Since 8/3>57/22, this is impossible. Therefore a maximizing tuple has Q in {0,1}; Q=0 is precisely the excluded canonical family. Thus Q=1 for every labeled maximizer. QED.

### Density corollary

The integer windows [t^2-1, t^2-1+floor(t/8)] are pairwise disjoint. Through t<=T they contain

    sum_{t=32}^T (floor(t/8)+1)=T^2/16+O(T)

scales. The largest endpoint is T^2+O(T), so this explicitly constructed set of admissible M has natural density 1/16. Therefore the set of all M with forced Q=1 has lower natural density at least 1/16; no claim of an exact global density is made.

## Executable exact certificate (independent finite support)

Companion \`R749SUL_NEAR_SQUARE_Q_CERT.cpp\` exhaustively computes the noncanonical optimum for every 2<=M<=5000 using integer congruences, not floating-point score comparisons. It orients u=max(u,v), loops over gcd(a,u)=1, enumerates all d with a*d congruent to 1 mod u and 1<=v=(a*d-1)/u<=u, and inserts each tuple at its exact maximum-entry bucket. The two u=1 configurations are added separately. A prefix maximum then yields the complete set of distinct optimal Q values for each M. Swapping u and v leaves tau and Q invariant, so the normalized orientation is complete for this proposition.

Local run: \`g++ -O2 -std=c++17 R749SUL_NEAR_SQUARE_Q_CERT.cpp -o cert && ./cert\`.

Result: \`PASS\`: 15,198,290 normalized/oriented candidate visits including canonical tuples; 271 window scales over t=32,...,70 all have optimal Q-set exactly {1}. Crosschecks reproduce R749SUJ at M=58 (T*=127890,Q=2) and M=93 (T*=579576,Q=2). Exact samples and the run scope are in \`R749SUL_NEAR_SQUARE_Q_RESULTS.json\`. The infinite theorem above rests on its written inequalities, not on extrapolation from 5000.

## What this changes and remains open

This proves infinitely many—and a positive density of—scales at which neither Q=2 nor any negative defect can attain the noncanonical global optimum, extending the universal finite observations of R749SUK with an unbounded theorem.

The missing global question is the Q-pattern on the complementary near-square gaps. In particular: can Q>=3 ever be optimal, or can the 1/16 density lower bound be raised via a stronger determinant-one competitor? A useful next step is to replace the fixed m=t^2-1 competitor with a source-preserving inverse-residue competitor at nearby u, then derive a larger guaranteed window.

The independent native X6 bridge remains: identify an actually admitted triadic Cell/Link/Port resource-and-time event, retain branch and Port provenance, and prove an observer/future-operation preserving map before transferring this auxiliary BRC feedback threshold theorem.

Provenance: prior source R749SUK@0b292a41; frozen WBRC source pin a72226e2; P000 and ACTIVE Heartbeat World current behavioral semantics read separately. No new Task publication, CLAIM, Result, Review or Foundation admission is asserted.
