# R284GU — Uniform conditioned-port estimate and finite-scale flexibility shift

2026-11-24. Author derivation, NOT_REVIEWED. Independent informed continuation of the auxiliary four-phase fixed binary tag model, not a native spatial or physical attribution. P000 and ACTIVE worldview unchanged. Original registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED, researcher EM-DIRECT-0C386E, activity RA-B82240E8488EF5A1DA5186C4. Previous owner inventory r1-20261124-1700-owner-read SUCCEEDED, as of 09:05:16 UTC, no LEASED entries. New read r1-20261124-1800-owner-read submitted, no shared CLAIM or formal task mutation. Current normative snapshots GK 810a12d9476c25099e5efa1995679748c85da542, EM 1e3f642c397bd02871e1a2e1739c759bcee2cdc9. Frozen science: GT c751b59823c79aac4b071d7b4b169e13ca830a7a:research_notes/portable_direct/R284GT_SUBLINEAR_OMISSION_FLEXIBILITY_TRANSITION_20261124.md and GS 66a518fef06384f130ecd16912ef5a2231ebc960:research_notes/portable_direct/R284GS_LOW_OMISSION_ASYMMETRIC_PATH_COUNTS_20261124.md, with their GL/GQ/GR dependencies as stated there. No repinning.

## 1. Uniform theorem

For integer u>=1, 0<=q<u, put H=2q+u+1, J=q+3u, N=H+J, p=H/(N-q), beta=(J-q)/(N-q)=1-p, rho=p/beta. As in GS/GT, S,P,Q are safe single-edge mode-word counts for (A,B,C)=(H,J,H),(H-1,J+1,H),(H,J+1,H-1), respectively; K=PQ(J+1)^2/(S^2 H), with K^2 the full-cycle labeled-order ratio asymmetric/symmetric.

For every fixed epsilon in (0,1), uniformly over 0<=q<=(1-epsilon)u as u tends to infinity,
  
    K = (J+1)^2 (N-q) / [H^2 (q+1/(p beta))^2] * (1+O_epsilon(log^2(u)/u)).

This strengthens GT's sublinear equivalence and extends it into the linear regime bounded away from q=u. In particular, if q/u -> lambda in (0,1), then

    u K -> (lambda+3)^2(2lambda+4)/(lambda^2(2lambda+1)^2).

Thus for each fixed linear proportion strictly between zero and one, symmetric optimal coding eventually wins labeled counts; the full-cycle relative count is asymptotically the square of this constant divided by u^2. No claim for the near-diagonal q/u -> 1 is made here.

## 2. Critical-window theorem

Uniformly for bounded real k=q-6 sqrt(u) (integer q), the preceding theorem implies

    K = 1 - (k+169/3)/(3 sqrt(u)) + O(log^2(u)/u).

Consequently, for any fixed delta>0, within any bounded k-window, eventually K>1 if k<=-169/3-delta and K<1 if k>=-169/3+delta. The continuous center of the transition is

    q_center = 6 sqrt(u) - 169/3.

This is a sign-window theorem, not an assertion that a discrete threshold is this real number plus o(1); integer rounding and possible ties must be kept. Nor does it establish uniqueness of a finite-u crossing outside the bounded window.

## 3. Proof of uniform quantitative estimate

Retain the exact GT corridor and cut. For each orientation use its own A,B,C,N'=A+B, e=A-2q, s=2u+1-(C-2q), t=e-s in {0,1}, h=B-q-s. Safety is [e-a]_+ + [b-q]_+ >= s and b<=h+[a-q]_+. Mark first A step reaching a=t+1 at b=q+l, l>=1 (e>t+1 for large u). There are binom(q+l+t,t) prefixes. Condition q prescribed B positions; the exact mass of all cut prefixes before safety is

    F binom(q+l+t,t) (A)_(t+1)(B-q)_l/(N'-q)_(t+1+l),  F=(B)_q/(N')_q.

F is retained exactly even when exponentially small. Let p'=A/(N'-q), beta'=1-p', rho'=p'/beta'. On q<= (1-epsilon)u these probabilities stay in compact subsets of (0,1), with p' bounded below and separated below 1/2 by an epsilon-dependent positive gap. Let L=m=ceil(C_epsilon log u), with constant sufficiently large. For l<=L every cut prefix is safe for large u, since q+l<=h, lower rule before cut automatic. The remaining uniformly shuffled inventory has fraction of A equal to p'+O((l+1)/u), and length at least a fixed multiple of u.

First m remaining steps and last m in reverse order are sampled without replacement at disjoint positions. Couple them sequentially to 2m independent Bernoulli(p') steps. Each conditional probability differs by O_epsilon((m+l+1)/u); by summing mismatch probabilities the joint total variation is O_epsilon(m(m+l+1)/u). In the first window the lower rule is precisely a walk of height l-1 with B up and A down, and the upper rule automatic. In the reversed last window the upper rule is precisely a walk starting at height t with B up and A down; lower rule automatic. This holds because e grows linearly, a near A is >=q, and h and B-(q+s) leave linear margins.

The omission of the middle can be bounded uniformly, rather than asserting independence of complete paths. Any lower failure after the cut implies height b-a-q+t<0; any upper failure implies the reversed height t+b'-a'<0, where a',b' are counts measured from the terminal inventory. For any remaining prefix or reverse suffix of k steps with X A steps, E[z^X] <= (1+p_rem(z-1))^k for z>1, by expanding the product of (1+(z-1)indicator_A) and using falling-factorial sampling probabilities. Choose z>1 close enough to 1 that (1+p_rem(z-1))/sqrt(z) <= eta_epsilon<1 uniformly for all l<=L and large u. A negative height requires 2X>k, so the failure probability summed over k>=m is at most eta_epsilon^m/(1-eta_epsilon). The iid walks have the same type of bound. Their infinite survival probabilities, by the GT gambler's-ruin identity, are 1-rho'^l and 1-rho'^(t+1). Thus the true conditional safe suffix probability differs from their product by O_epsilon(log^2(u)/u) uniformly for l<=L.

The falling-factorial ratio in the mass formula equals p'^(t+1) beta'^l times 1+O_epsilon((l+1)^2/u) for l<=L (expand each factor relative to its initial inventory; all inventories proportional to u). Beyond L it is bounded by beta'^l (drop conditions on the prescribed A positions); beta' bounded away from 1. Divide by (q+1)^t to bound the combinatorial prefix factor by l+2; hence omitted tail is O(u^-3) with sufficiently large C_epsilon. All estimates hold uniformly even for fixed q. Writing f=N_safe/binom(N',A), summing and using the geometric sums gives

    t=0: f/F = (1-rho')^2 * (1+O_epsilon(log^2(u)/u));
    t=1: f/F = rho'(1-rho')^2 (q+1/(p' beta')) * (1+O_epsilon(log^2(u)/u)).

Indeed sum_{l>=1}(beta'^l-p'^l)=(beta'-p')/(p' beta'), and sum l(beta'^l-p'^l) divided by this sum is 1/(p' beta')-1. Relative errors are valid since rho' and 1-rho' are bounded below and q+1/(p' beta') comparable to q+1. The orientations' p' differ from p by O(1/u) and may be replaced by p at this accuracy, without replacing F.

The exact unrestricted word ratios are H/(J+1) and (N+1)/(J+1). The exact rare-event ratios are F_P/F_S=(J+1)/(J-q+1) and F_Q/F_S=(J+1)(N-q+1)/[(J-q+1)(N+1)]. These formulas include q=0. Multiplication and cancellation therefore give

    PQ/S^2 = H(N-q+1)/[(J-q+1)^2 rho^2 (q+1/(p beta))^2] * (1+O_epsilon(log^2(u)/u)).

Multiplying by (J+1)^2/H and using rho=H/(J-q) yields the displayed theorem, because replacing (N-q+1) by N-q and (J-q)/(J-q+1) by 1 changes the relative value by O(1/u). No rare-event factor was approximated before taking ratios. This is an exact positive-branch count with retained prefix inventory and two conditional end ports, followed by a quantified approximate quotient under the labeled-count observer; no signed physical cancellation.

## 4. Critical expansion

When q=6 sqrt(u)+k, bounded k, p=1/4+O(1/sqrt(u)), so 1/(p beta)=16/3+O(1/sqrt(u)). The numerator prefactor expands as

    (J+1)^2 (N-q)/H^2
      = 36u [1-(17/6) q/u + O(1/u)].

The coefficient is 2/3 + 1/2 - 4 = -17/6 from the three factors. The denominator (q+1/(p beta))^2 equals 36u [1+(k+16/3)/(3 sqrt(u))+O(1/u)]. Combining with the uniform error gives K=1-[17+(k+16/3)/3]/sqrt(u)+O(log^2(u)/u), which is the claimed 169/3 shift. For exact q=6 sqrt(u) along square u, sqrt(u)(1-K)->169/9. The linear-limit formula follows by division by u in the same uniform theorem.

## 5. Executed exact finite evidence

Local Python integer DP using GS corridor was cross-checked against GL's original distance recurrence for all 630 orientations for u=1..20, q=0..u-1. No mismatch. Code below is the executed checker. Ratios are constructed as exact Fraction, decimal rendering only.

u,q,K,sqrt(u)(1-K) at rounded 6sqrt(u):
256,96,0.4466836637056979,8.853061380708834
576,144,0.5502936883118955,10.792951480514509
1024,192,0.6216815694031254,12.106189779099989
2048,272,0.6981129018236512,13.661850513486423

At q=u/2, u,q,uK:
128,64,53.165775744901225
256,128,57.00215033581797
512,256,59.07108292613823
Predicted limit 61.25.

The leading correction is slow at finite sizes. These observations support but do not prove the expansion or give a useful explicit finite-u error constant.

```python
from math import sqrt
from fractions import Fraction

def count(q,u,A,B,C):
    e=A-2*q;s=2*u+1-(C-2*q);t=e-s;h=B-q-s
    v=[0]*(B+1)
    for a in range(A+1):
        lo=0 if a<=t else q+min(a-t,s);hi=min(B,h+max(0,a-q))
        for b in range(lo,hi+1):
            v[b]=1 if a==b==0 else v[b]+(v[b-1] if b>lo else 0)
    return v[B]

def original(q,u,A,B,C):
    r=2*u+1;M=max(0,C-q);v=[0]*(B+1)
    for a in range(A+1):
        for b in range(B+1):
            D2=max(0,A-a-2*q)+max(0,max(0,b-q)+M-q)
            D3=max(0,C-2*q,max(0,a-q)-q,B-b+max(0,a-q)-2*q+M)
            v[b]=0 if min(D2,D3)<r else 1 if a==b==0 else v[b]+(v[b-1] if b else 0)
    return v[B]

def configs(q,u):
    H=2*q+u+1;J=q+3*u
    return [(H,J,H),(H-1,J+1,H),(H,J+1,H-1)]

def ratio(q,u):
    H=2*q+u+1;J=q+3*u
    S,P,Q=[count(q,u,*c) for c in configs(q,u)]
    return Fraction(P*Q*(J+1)**2,S*S*H)

if __name__=='__main__':
    checks=0
    for u in range(1,21):
        for q in range(u):
            for c in configs(q,u):
                assert count(q,u,*c)==original(q,u,*c)
                checks+=1
    print('exact checks',checks,flush=True)
    for u in [256,576,1024,2048]:
        q=round(6*sqrt(u))
        k=ratio(q,u)
        print('critical',u,q,float(k),float(1-k)*sqrt(u),flush=True)
    for u in [128,256,512]:
        q=u//2;k=ratio(q,u)
        print('linear half',u,q,float(k*u),flush=True)
```

DP uses monotone lo,hi: old entries left of current lo are ignored, newly exposed entries to right of old hi were never written and are zero; update in increasing b preserves north predecessor before overwriting and west predecessor after overwriting. Exact integer arithmetic; no use of approximate sign for counts.

## 6. Next

Resolve the q/u->1 near-diagonal regime, where the uniform upward drift vanishes and the two end ports no longer decouple on logarithmic windows. Seek an explicit sign-comparison/injection for P<S, and a global finite-u unique crossing theorem (or counterexample); the critical shift alone is not uniqueness. GR middle-regime optimizer and independent GP/GQ rational certificate checking remain separate open units. No repeated capacity enumeration.
