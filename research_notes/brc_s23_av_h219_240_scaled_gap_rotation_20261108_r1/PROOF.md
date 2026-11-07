# S23/AV: third exact interior-gap plateau and rotation return-time formula
Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_EXACT_FINITE_PROOF; independent review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continuation of Draft PR #1777 at e02f5504983f9cc5784c49cc86aa54c3cff89491.

## Exact model
For lawful S23/AV parameters theta0=(1/2,1/2), theta1=(5/7,7/8), the full three-label laws (labels 1,3,4) are P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). Their compressed Bernoulli label-3 laws coincide at z=1/4. For an ordered prefix with k label-1 and ell label-4 outcomes, Lambda(k,ell)=7^(k+ell)/10^k. Label 3 can pad to any n>=k+ell.

With future suffix length <=h, the distinct sign thresholds are T(i,s)=10^i/7^s (0<=i<=s<=h); M_h=(h+1)(h+2)/2 thresholds partition positive ratios into M_h+1 open cells. The equality-at-1 state is retained separately. Let N(h) be the least padded prefix length n needed to realize every open cell.

## New exact theorem
For ALL INTEGERS h=219,...,240, N(h)=1311. Boundary results: N(218)=1190, N(241)=1315. Thus N(219)-N(218)=121 and the constant region spans 22 consecutive horizons. The tail bound n_tail(h)=min{n>=1:7^(n+h)<10^n} rises from 1195 at h=219 to 1310 at h=240, so the internal gap causes a positive excess throughout this interval.

For each 219<=h<=240, the unique final cell is the open interval
A=10^60/7^219 < Lambda < B=7^(-148)
between adjacent thresholds T(60,219) and T(0,148). Its first prefix witness is (k,ell)=(1233,78), total 1311.

## Gap lower-bound proof (exact integers)
At fixed ell, Lambda(k,ell)=7^ell(7/10)^k decreases strictly with k. Let k_min(ell) be the smallest k>=0 with Lambda(k,ell)<B; equivalently 7^(k+ell+148)<10^k. This first sub-B value is the highest possible candidate in the interval (A,B) for that ell.

VERIFY.py checks k_min(ell) is minimal, and proves for each ell=0,...,77:
7^(k_min(ell)+ell+219) <= 10^(k_min(ell)+60).
Thus Lambda(k_min(ell),ell)<=A; no k at that ell can enter (A,B). At ell=78, it checks k_min(78)=1233 and the strict comparisons
7^(1311+148)<10^1233, 7^(1311+219)>10^(1233+60).
Therefore Lambda(1233,78) lies in (A,B). Since k_min is nondecreasing in ell, all ell>=78 with Lambda<B satisfy k+ell>=1233+78=1311. No shorter prefix hits the gap. Padding by label 3 permits length 1311.

## New reusable irrational-rotation reduction
Let r=ln(7)/ln(10/7) (irrational by unique prime factorization) and d=11r-60. The exact integer inequalities 10^60<7^71 and 7^72<10^61 establish 0<d<1. For every integer t>=0, define I_t=(10^60/7^(71+t), 7^(-t)). At each ell>=0, the first k for Lambda(k,ell)<7^(-t) is
k_min(ell;t)=floor(r(ell+t))+1.
The further condition Lambda(k_min,ell)>10^60/7^(71+t) holds iff
{r(ell+t)}>1-d.
Write v_t=min{v>=t: {rv}>1-d}. Since k_min(ell;t)+ell strictly increases with ell, the least prefix length entering I_t is EXACTLY
F(t)=(v_t-t)+floor(rv_t)+1.
This proves the scaled-gap first-hit problem reduces to a return time of a one-dimensional irrational rotation. For t=148, v_t=226 and F(148)=78+1233=1311. The earlier t=0,69 cases are the predecessors. For N(h), I_t must additionally be adjacent in the threshold set; that adjacency is separately proved here for h=219..240.

Derivation: Lambda(k,ell)<7^-t iff k>r(ell+t), and Lambda(k,ell)>10^60/7^(71+t) iff k<r(ell+t+11)-60. Substituting k=floor(rv)+1 gives 1-{rv}<11r-60=d.

## Completeness of finite exact proof
VERIFY.py enumerates every T(i,s) for h=218..241. Floating logs are used ONLY to propose an ordering/lookup position. The complete threshold ordering is verified with adjacent exact integer comparisons 10^i*7^t<10^j*7^s. Every tentative prefix assignment is corrected and checked against its exact neighboring thresholds using 7^(n+s)<10^(k+i). All k=0,...,n and successive n are covered to full interval occupancy. It checks every first-hit maximum, the unique final gap and the two boundary horizons. The numerical certificate is integer-only; no tolerance or probabilistic sampling is used to decide results.

BRC semantics: this construction retains the joint branch counts (k,ell) and three-label source, whereas the compressed Bernoulli observer loses that joint information. This is an exact fixed-two-point auxiliary result for a declared finite future-sign horizon. P000/Heartbeat X6 remains unchanged. The separate six-source/ten-label mother-model transfer, native task CLAIM and independent theorem review remain open.
