# R5 — terminal-observer compatibility: an exact necessary condition and a rank-four counterexample

Date: 2026-10-31 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. All-real statements below are analytic claims, not extrapolations from the finite checks. This is an **auxiliary finite two-law stopping model**, not an indigenous X6 theorem or a solution to the original four-observer mother question.

## Frozen scientific sources and authority

GLOBAL_KNOWLEDGE_V1 `main@4c34fe83fdfbdb42e83dc154a17a1e5460716ac4`; Enterprise Math `main@fa56bd5ca2e741971266ccd81244dbb11e4daf51`; current P000 and ACTIVE residual-faithful worldview read and preserved. Principal predecessor: `be7642cd9ac9d6dfe31c7346d6d606ea02774cd5:research_notes/brc_r5_sourceblind_terminal_fourrank_20261031_t1953/RESEARCH.md`; its all-real result assumes a particular indicator error response. Native gateway reported `research_authority_granted=false`, `executor_binding_configured=false`, `CODE_REVIEW_REQUIRED`, and quota 5/5; an Owner-list query returned `CONTROL_QUOTA`. No native CLAIM, Result or independent Driver acceptance is inferred.

BRC meaning here: individual **positive** Q cylinder masses retain origin and route labels, and each terminal cylinder carries its exact likelihood-ratio conversion `P(cylinder)=lambda*Q(cylinder)`. Signed four-observer linear functionals are readouts of distributions, not signed BRC path masses. No claim is made about physical clocks or a native 3D slice/6D embedding.

## Model and exact support reduction

Two hidden origins `i=0,1`, each having initial P=Q mass `1/2`, start at common observable key A=(time 1, LR 1). At A choose STOP or CONTINUE. After CONTINUE, origin-i nature selects D,C,Y with conditional Q probabilities `(a_i, 1-2a_i, a_i)` and likelihoods `(1/2,1,3/2)`. D and Y can STOP at time 2, or CONTINUE: D splits Q `(2/3,1/3)` into terminal DH=(time 3, LR 1/4) and common L=(time 3, LR 1); Y splits Q `(1/2,1/2)` into terminal YH=(time 3, LR 2) and L. C has no policy decision: nature terminates at C=(time 2, LR 1) with probability `1-k_i`, or proceeds to L with probability `k_i`. At L choose STOP (time 3, LR 1) or CONTINUE (time 4, LR 1). Every terminal P mass is terminal LR multiplied by Q mass. For `0<a_i<1/2, 0<k_i<1`, all natural transition masses are strictly positive, and every policy has total P=Q mass 1.

FULL sees origin and full route history and may choose separately at origin-specific A,D,Y and L entries (12 binary deterministic controls); seedless LR sees only the four current keys A,D,Y,L (4 binary controls), with independent local real behavioural stop probabilities and no persistent random seed. No key is revisited in one history. The shared terminal Bernoulli error probability `r(t,lambda)` is in `[0,1]` (strictly `(0,1)` in the example), is identical for P and Q conditional on the terminal key, and cannot use origin, action history, or policy identity. The four observer is `O=(e_P,e_Q,T_P,T_Q)` with `e_S=E_S[r]`, `T_S=E_S[time]`.

Assume the exact compensated-source relation `theta=(1+k_0(1-2a_0))/a_0=(1+k_1(1-2a_1))/a_1`. Set `b_i=(1-2a_i)(1-k_i)=2-a_i(theta+2)>0` and `c_i=(1-2a_i)k_i=a_i*theta-1>0`; in particular `theta>2`.

For **any signed** observer direction `H=(p,q,u,v)`, give each terminal key x=(t,lambda) the Q-weighted leaf score `h_x=(p*lambda+q)*r(x)+(u*lambda+v)*t`. With terminal labels A,D,Y,C,DH,YH,L,L4, define

```
Lstar = max(h_L, h_L4)
Dstar = max(h_D, (2*h_DH+h_Lstar)/3)
Ystar = max(h_Y, (h_YH+h_Lstar)/2)
F_i   = a_i*(Dstar+Ystar)+b_i*h_C+c_i*Lstar-h_A
      = g(H)+a_i*k(H)
g(H)  = 2*h_C-Lstar-h_A
k(H)  = Dstar+Ystar-(theta+2)*h_C+theta*Lstar.
```

Backward induction proves that common downstream optimal choices maximize both origin subtrees: at D,Y,L, their conditional descendants are origin-independent; C has no choice. FULL may choose A separately by origin, whereas seedless LR makes a common A choice. The exact support values are

```
sup_FULL H.O = h_A + [max(0,F_0)+max(0,F_1)]/2
sup_LR   H.O = h_A + max(0,F_0+F_1)/2
Delta(H) = (|F_0|+|F_1|-|F_0+F_1|)/4.
```

The expected signed score is multi-affine in each behavioural decision probability, hence a maximum over all real behavioural policies occurs at a deterministic endpoint. It follows that **the full four-dimensional convex hulls are equal if and only if `(g+a_0*k)*(g+a_1*k)>=0` for every `H`**, with g,k evaluated by the finite maxima above. This is an exact, all-signed, piecewise-linear support criterion, not a sampled-direction test.

## Theorem A — terminal interpolation is necessary

Let `a_0 != a_1` and the above compensated source relation hold. For any shared legal terminal response, define

```
gamma = 2*r_C-r_A-r_L
xi    = r_D + r_YH/2 - 3*r_L/2 - (theta+2)*(r_C-r_L)
Abar  = a_0+a_1
B     = theta+7/2+4/Abar.
```

For any real `0<s<min(1/2,theta/(2*B))`, put

```
t = theta-s*(xi+2*gamma/Abar)
H_s = (0,s,2*(t+1),-(2*t+3)).
```

Then **the exact all-real signed four-observer support gap** is

```
Delta(H_s)=s*abs(gamma)*abs(a_0-a_1)/(2*Abar).
```

Consequently, equality of the full four-observer convex hulls **requires** the source-blind terminal interpolation equation `2*r_C=r_A+r_L`. This condition involves only the three LR-1 terminal-time classes (t=1,2,3), regardless of all other terminal responses.

**Proof.** The stated bound and `0<=r<=1` imply `t>theta/2>1`. The time increment for L CONTINUE minus STOP is `-1`, while its Q-error increment is in `[-s,s]`: L STOP uniquely maximizes. For D, CONTINUE minus STOP has time increment `-(t+2)` and Q-error increment in `[-s,s]`, hence D STOP uniquely maximizes. For Y, CONTINUE minus STOP has time increment `t` and Q-error increment in `[-s,s]`, hence Y CONTINUE uniquely maximizes. The changes at these keys are computed under Q and account for both terminal branches. For this fixed downstream regime, direct substitution of P=lambda*Q and the b_i,c_i identities gives

```
F_i(H_s)=a_i*(t-theta)+s*(gamma+a_i*xi).
```

Our choice of t makes `F_0+F_1=0` and `F_0=s*gamma*(a_1-a_0)/Abar=-F_1`. Substitute into the exact support-gap identity to obtain the formula. When `gamma!=0` and `a_0!=a_1`, this single signed direction strictly separates the convex hulls. This proof applies to every legal real terminal response and all real behavioural strategies. QED.

## Theorem B — the necessary equation is not sufficient, even at full rank

Fix strictly positive rational kernels

```
(a_0,k_0)=(1/4,3/4), (a_1,k_1)=(1/5,1/6), theta=11/2.
```

Take a shared, strictly interior, source-blind terminal response `r_x=1/2` on all keys except `r_DH=1/2+v` and `r_L4=1/2+w`, with `0<v,w<1/2`. Thus `gamma=0` identically. The seedless LR four-observer convex hull has **full affine rank four** for every such v,w. For five LR deterministic controls `(A,D,Y,L)` equal to `(0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0)`, subtracting the first observed four-vector from the other four gives the exact determinant

```
det = 152361*v*w/40960000 != 0.
```

More strongly, for the fixed signed direction `H=(10,9,1,-2)`, when

```
w>2/19;   23*v+19*w>11/2;
F_0=1-19*w + (-83+46*v+722*w)/24 > 0;
F_1=1-19*w + (-83+46*v+722*w)/30 < 0,
```

backward induction gives L,D,Y all CONTINUE and the strict support gap `Delta(H)=min(F_0,-F_1)/2>0`. These are open inequalities and define an open set of valid rank-four negative candidates.

At the exact instance `v=1/8,w=1/4`, direct Q/P enumeration yields

```
F_0=53/96, F_1=-37/120;
sup_FULL H.O=1685/192,  sup_LR H.O=2759/320;
Delta(H)=37/240;
det=152361/1310720000.
```

A FULL strategy CONTINUEs at A for origin 0, STOPs at A for origin 1, and CONTINUEs at all reached D,Y,L keys. Its exact observer is

```
O_FULL=(221/384, 7/12, 107/48, 107/48).
```

Since `||H||_1=22`, every point of the entire LR four-hull is at least `(37/240)/22=37/5280` away from this FULL observer in the infinity norm. This is a four-hull separator, not merely a nonmembership statement for actual LR behavioural images. All natural P/Q path probabilities remain strictly positive, with both laws normalized.

**Why this is an advance.** In the predecessor's example a perturbation at C violated the three-time interpolation equation. Theorem A identifies that equation as a universal first necessary condition for source compensation with any source-blind response. Theorem B then supplies a genuinely different obstruction beyond it, already on an open full-rank family: L's time-4 error creates a distinct A-source advantage even when its time-1/2/3 LR-1 errors interpolate exactly.

## Verification and limits

`VERIFY.py` uses Python standard-library `Fraction` only. It explicitly computes all 4096 FULL and 16 seedless LR deterministic observations, checks terminal P/Q normalization, all legal error probabilities, Bellman supports, the rank-four determinant, the exact FULL witness and support gap, plus two rational instances of Theorem A's small-s separator. `EXACT_OUTPUT.txt` is the actual execution output. The symbolic v,w determinant and the all-real/semi-infinite H support statements are proven algebraically above; finite tests do not constitute those general proofs.

No theorem acceptance, formal proof checker, independent review, novelty priority or native X6 correspondence is claimed. The mother question (full four-hulls equal but actual seedless-LR behavioural four-images unequal) remains open. Existing protected P000 and ACTIVE worldview unchanged.

## Next discriminating question

Under `gamma=0`, classify the **additional** terminal-event relations that force `(g+a_0*k)*(g+a_1*k)>=0` on every polyhedral sign chamber in H-space, while retaining four-rank. Start by eliminating L4 effects with exact rational chamber/LP calculations. Demand either (i) all FULL deterministic four-observer vectors represented by <=5 LR deterministic points with exact rational weights for a genuinely new candidate, or (ii) one exact rational signed separation direction. Only after (i) should actual four-image nonmembership be examined using semialgebraic methods. See `NEXT_TASK.md`.
