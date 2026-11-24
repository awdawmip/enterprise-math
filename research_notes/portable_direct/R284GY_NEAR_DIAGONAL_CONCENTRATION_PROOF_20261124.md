# R284GY — Uniform growing-gap concentration and ratio proof (GW recovery)

2026-11-24. Author proof, NOT_REVIEWED; independent auxiliary four-phase binary-tag model, not native physical attribution or P000 modification. Fixed sources: R284GV cc7c920e534ed7898177b272d834564bf03b3721:research_notes/portable_direct/R284GV_TWO_CUT_COUNT_AND_FIXED_DIAGONAL_GAP_20261124.md (blob e3b1e1787b5fa5fb53a3f9078cc10affde20ce86); R284GX dff580f539319ddcfd5f521a2cb65bd0f783c4c0:research_notes/portable_direct/R284GX_STRICT_JOINT_MODE_DOMINANCE_AND_FINITE_TRANSITION_20261124.md (blob 681b2f41eb4df9f633f01dc1dccecd06f66e140c). These preserve original GL/GS science pins. GX explicitly recorded GW's uniform proof as missing; this note supplies a reconstruction rather than counting the same claim as a new theorem. Current gateway em_status(identity_only=true) returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Historical identity EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4 is provenance only. No owner verification or CLAIM, no protected-state update. Independent non-overwriting science preservation under docs/RESEARCH_CONSOLE_FALLBACK.md. Current GitHub entry files, P000, ACTIVE worldview and joint observer contract read; no changes to them.

## 1. Theorem

Let u tend to infinity through integers, d=u-q>=1, d->infinity and d/u->0. Use H=2q+u+1, J=q+3u, m=q+u. Let S,P,Q denote GV single-edge safe mode-word counts for (H,J,H), (H-1,J+1,H), (H,J+1,H-1). Let K=PQ(J+1)^2/(S^2 H).

Then uP/S->1, uQ/S->2 and uK->32/3. The labeled full-cycle count ratio K^2 is asymptotic to 1024/(9u^2). This recovers the previously reported GW result with a full proof valid for all growing sublinear d, including d much larger than sqrt(u).

Moreover for each of the three counting measures, let Z be the sum of the two deficit ports I,J0 as defined below, normalized by its own total count. For each fixed epsilon>0 there is c_epsilon>0 such that
Pr(|Z/d-2|>epsilon) <= exp(-c_epsilon*d+O_epsilon(d^2/u+log(d+2)))
for all sufficiently large u along the stated regime. Thus Z/d->2 in probability simultaneously for all three orientations. The estimate is a marginal count observer, not an independent-port assertion.

## 2. Exact common coordinates

Write C(n,k)=0 outside 0<=k<=n. For n>=1 and x>=0 define cumulative kernel U_n(x)=C(2n-x,n-x)-C(2n-x,n-x-1) for 0<=x<=n, zero otherwise; primitive kernel l_n(x)=C(2n-2-x,n-1-x)-C(2n-2-x,n-2-x) for 0<=x<n, zero otherwise.

Take U=U_u, l=l_u, V=U_m, r=l_m. In S use deficit I=u-i,J0=m-j; in P use I=u-1-i,J0=m-1-j; in Q use I=u-i,J0=m-j. GV and GX yield exact weights for each I,J0>=0, z=I+J0:
w_S=(U(I)+q*l(I))*V(J0)*C(z+1,d)
w_P=l(I)*r(J0)*C(z+3,d+1)
w_Q=U(I)*V(J0)*C(z,d-1).
The sums are respectively S,P,Q. The z shifts retain the actual different middle inventories; they must not be erased. The positive kernel sums follow from GV's unique two-cut decomposition and the GX cumulative reflection identity.

## 3. Exponential concentration without d^2/u->0

Normalize each endpoint kernel by its value at deficit zero. For n>=2 the two exact formulas are
U_n(x)/U_n(0)=(x+1)*C(2n-x,n-x)/C(2n,n),
l_n(x)/l_n(0)=(x+1)*C(2n-2-x,n-1-x)/C(2n-2,n-1).
These follow by factoring each binomial difference, with factors (x+1)/(n+1) and (x+1)/n respectively. For k=n or n-1, the remaining ratio equals
product_{j=0}^{x-1} (k-j)/(2k-j).
Each factor <=1/2. For 0<=x<=k/2, logarithms of its ratio to 1/2 are bounded below by -C*j/k (absolute C), from log(1-j/k)-log(1-j/(2k)). Consequently the normalized kernel is at most (x+1)2^(-x) everywhere (including zero extension), and at least (x+1)2^(-x)*exp(-C*x^2/k) on that smaller domain. The S left kernel U+q*l, after normalization, is a convex combination of the two normalized kernels, so it satisfies the same inequalities with k=u-1. Since m/u->2, all normalized pairs have the upper bound (I+1)(J0+1)2^(-z) and lower bound given by this expression times exp(-C' z^2/u) whenever z<=C0*d for any fixed C0, for sufficiently large u. The constants in the endpoint bounds are uniform across orientations.

Sum over I+J0=z; sum (I+1)(J0+1)=C(z+3,3). After removing the two orientation-specific zero-deficit kernel constants, the true marginal weight is bounded above by
W(z)=C(z+3,3)*2^(-z)*C(z+a,g),
where (a,g)=(1,d),(3,d+1),(0,d-1), and bounded below by W(z)*exp(-C' z^2/u) for z<=C0*d. All integer pairs in that latter range are within the common nonzero kernel support since d=o(u). The case z+a<g has zero weight.

To analyze W, put k=z+a-g>=0. Up to a constant independent of k, W is the probability mass of the sum of g+1 independent geometric variables on {0,1,...} with success probability 1/2, multiplied by C(k+g-a+3,3). Indeed its mass is C(k+g,g)2^(-k-g-1). Its mean is g+1 and the mgf of one geometric variable is 1/(2-exp(t)), finite around t=0. Exponential Markov bounds with a fixed small positive or negative t give exponentially small probabilities for |k/d-1|>eta, for each fixed eta>0; this follows directly by expanding log(1/(2-exp(t)))=t+O(t^2) at zero and using g+1=d+O(1). The polynomial weight cannot remove the exponential tail: for the upper tail choose a smaller positive exponential tilt to bound the polynomial times the indicator, or expand the first three derivatives of the mgf. For the lower tail k=O(d), the polynomial is O(d^3). The tilted expectation bound is O((d+2)^3 exp(-c_eta*d)). On the interval |k/d-1|<=1/4, the polynomial is bounded below by c*d^3 for large d, and the probability tends to one. This interval lies in z<=3d. It supplies a lower bound for the total true normalized marginal, relative to the unweighted geometric normalization, of c*d^3 exp(-C'' d^2/u). Thus dividing the tail upper bound by this denominator proves the stated exponential concentration (allowing the harmless O(log(d+2)) term). In particular d^2/u=o(d) suffices. No Taylor approximation requiring d^2/u=o(1) has been made.

## 4. Recover the two orientation ratios without a tail-uniform-integrability assumption

For z in [(2-epsilon)d,(2+epsilon)d], 0<epsilon<1/2, both deficits are o(u) uniformly, and every weight is positive for large u. Exact cancellation gives
U(I)/l(I) = (2u-I)(2u-I-1)/[(u-I)(u+1)] ->4,
V(J0)/r(J0) ->4 by replacing u,I with m,J0.
Then
u*w_P/w_S = [u/(q+U/l)]*[r/V]*[(z+3)(z+2)/((d+1)(z+2-d))],
u*w_Q/w_S = [u*(U/l)/(q+U/l)]*[d/(z+1)].
As u->infinity, the first factors tend uniformly to 1 and 1/4 in the P expression, and to 4 in the Q expression, since q/u->1. The remaining z-dependent factors are uniformly close to 4 and 1/2 when epsilon is small: the limiting functions of y=z/d are y^2/(y-1) and 1/y, continuous at y=2.

For each fixed epsilon, concentration in section 3 holds separately under S, P and Q. Their full sums equal their central-window sums times 1+o(1). Hence the ratio of full sums is asymptotically the ratio of their central sums, even after scaling by u. On the central window the preceding pointwise ratios bound the ratio of the sums by their infimum and supremum. First take u->infinity, then epsilon->0 to obtain uP/S->1 and uQ/S->2. This argument needs no bound on u times a tail probability and remains valid when d grows arbitrarily slowly (e.g. log log u). Finally (J+1)^2/(uH)->16/3, hence uK->32/3. QED.

This proof uses the BRC positive branch observer retaining both port deficits, and a marginal bound only for the specified count ratios. It preserves all different middle residual capacities in the exact weights.

## 5. Executed finite evidence and reproduction

Exact integers, not floating point in counting or comparisons. A new checker constructed common-coordinate weights by packed exact convolution and cross-checked their total against the frozen GL residual-distance DP reproduced in GX: all 513 orientation cases u=1..18, d=1..u, zero mismatches. Eight additional full parameter rows were computed and each orientation total independently matched GX's original GV packed count. The ninth row (u=1024,d=181) did not finish within the local command timeout and is not included. Selected actual outputs, rounded only for presentation:
u,d | uP/S | uQ/S | uK | mean Z/d (S,P,Q) | Pr(|Z/d-2|>1/2) (S,P,Q)
64,8 | 1.0761625 | 1.8998861 | 11.1905356 | 2.20283,2.22171,2.08441 | .290125,.313494,.258444
256,16 | 1.0519123 | 1.9714968 | 11.1905264 | 2.11863,2.12506,2.05661 | .159093,.170478,.137130
1024,32 | 1.0288641 | 1.9909616 | 10.9855010 | 2.06319,2.06503,2.03190 | .053370,.056607,.044364
256,64 | 1.3059901 | 2.8251297 | 20.7647667 | 1.85447,1.85222,1.84266 | .004170,.004708,.005218

Reproduction: use counts, dp, configs and C from the Python block of the frozen GX source. New code below is the executed common-coordinate core and crosscheck (the test also printed the means and tails shown above). Each packed integer digit is wide enough for the maximum possible convolution coefficient.

```python
def kernels(n):
    U=[C(2*n-x,n-x)-C(2*n-x,n-x-1) for x in range(n+1)]
    l=[C(2*n-2-x,n-1-x)-C(2*n-2-x,n-2-x) for x in range(n)]+[0]
    return U,l

def weights(u,d):
    q=u-d;m=q+u
    U,l=kernels(u);V,r=kernels(m)
    out=[]
    for L,R,shift,g in [([v+q*w for v,w in zip(U,l)],V,1,d),(l,r,3,d+1),(U,V,0,d-1)]:
        width=(max(L).bit_length()+max(R).bit_length()+min(len(L),len(R)).bit_length()+7)//8
        pack=lambda s:int.from_bytes(b''.join(x.to_bytes(width,'little') for x in s),'little')
        raw=(pack(L)*pack(R)).to_bytes(width*(len(L)+len(R)-1),'little')
        out.append([int.from_bytes(raw[z*width:(z+1)*width],'little')*C(z+shift,g) for z in range(len(L)+len(R)-1)])
    return out

n=0
for u in range(1,19):
    for d in range(1,u+1):
        q=u-d
        for w,c in zip(weights(u,d),configs(q,u)):
            assert sum(w)==dp(q,u,*c),(u,d,c)
            n+=1
print('DP count crosschecks',n)
# Exact diagnostic on any completed parameter pair:
# W=weights(u,d); S,P,Q=map(sum,W); q=u-d; H=2*q+u+1; J=q+3*u
# assert [S,P,Q]==[counts(q,u,*c) for c in configs(q,u)]
# mean=[Fraction(sum(z*v for z,v in enumerate(w)),d*sum(w)) for w in W]
# tail=[Fraction(sum(v for z,v in enumerate(w) if 2*abs(z-2*d)>d),sum(w)) for w in W]
```

## 6. Next questions

Finite strict monotonicity of K(q,u) remains unproved. A possible route is sharper likelihood-ratio comparison in common deficit coordinates under adjacent q (including shifted middle binomial). The new uniform proof closes the missing GW proof material independently of that monotonicity. No formal Task completion, Result or Review asserted; Activity association still awaits authenticated reconciliation.
