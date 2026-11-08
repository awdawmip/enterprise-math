# PREFIX-620-R6 — Balanced signed-label parameters uniquely maximize BRC first-passage stopping cost

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs, population and observer

Science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`; reuse PREFIX-610 native-derived signed-label observation, PREFIX-613 anytime confidence, PREFIX-615 neutral thinning, PREFIX-617 stopping rule, PREFIX-618 exact balanced cost, PREFIX-619 asymmetric rational polynomial. Preserve native BRC port and branch provenance; signed-label compression is sufficient only for this declared confidence-width and stopping-cost decision, not arbitrary future BRC updates.

There are two distinguishable information directions `ell=1,2`. An original one-step trial yields positive or negative label for direction ell with probabilities `p_ell/q` and `(1-p_ell)/q`, respectively, `q=12` for Boolean slot 0 and `q=24` for Boolean slot 1 or 2, or yields neutral otherwise. The statistical interior has `0<p_ell<1`; we include `p_ell=0,1` as limit-probability endpoints. Fix `beta=1/40` and target p-confidence diameter `delta=1/4`.

The accepted anytime confidence set after m informative signs, k positive, is
```
C(m,k)={p in (0,1):40(m+1)*binom(m,k)*p^k*(1-p)^(m-k)>1}.
D(m,k)=diameter(C(m,k)).
```
For each direction, `J` is the **first-passage time** when `D(m,k)<=1/4`. For the full original trial stream, `T_q(p1,p2)` is the number of original BRC trials until both directionwise first-passage conditions have been reached.

## Theorem: globally sharp expected native action cost

For all `(p1,p2)∈[0,1]^2`,
```
E_[p1,p2] T_12 <= E_[1/2,1/2] T_12
                  = 2350.8871013999329674336846958203177...,
E_[p1,p2] T_24 <= E_[1/2,1/2] T_24
                  = 4701.7742027998659348673693916406354... .
```
In either case, equality holds **only** at `p1=p2=1/2`. The exact rational maximum and reproducible formula are in PREFIX-618/619; the decimal shown here is a display approximation.

### Lemma 1: first-passage survivor Bernstein coefficients are symmetric and centrally unimodal

Construct integers `A_m(k)` by
```
A_0(0)=1,
A_m(k)=1{D(m,k)>1/4}*(A_(m-1)(k)+A_(m-1)(k-1)),
```
zero outside `0<=k<=m`. These count the length-m binary sign strings with k positives that **have not previously stopped**. The recurrence uses the actual path history; it is not just the instantaneous width indicator.

A necessary correction to an initial shorthand is witnessed exactly by
`D(25,25)<=1/4` but `D(26,25)>1/4`.
Appending a negative sign can increase the current confidence width, so an already stopped history must **not** be reintroduced among survivors. The A-recurrence handles this correctly.

For every integer `1<=m<=189`, define the rational Bernstein coefficient
`c_m(k)=A_m(k)/binom(m,k)`.
The exact finite certificate establishes
```
c_m(k)=c_m(m-k),
c_m(k)<=c_m(k+1)  for 0<=k< m/2.
```
It additionally checks that `A_189(k)=0` for every k, while at m=25, `A_25(0)=A_25(25)=0` and `A_25(1)>0`. Thus the sequence is centrally symmetric and nondecreasing to the midpoint for every relevant finite m and strictly nonconstant by m=25.

**Exact finite verification.** The companion script replays PREFIX-618's strict integer dyadic-root predicate for width events, then performs the **pathwise** A-recurrence to m=189. It exhaustively checks all 18,144 pairs `(m,k)`, 18,144 symmetry equalities and 9,025 central monotonicity inequalities by integer cross-multiplication:
```
A_m(k)*binom(m,k+1) <= A_m(k+1)*binom(m,k).
```
The result was `ALL_CHECKS_PASS`; source root computations performed 721,445 integer comparisons in that certificate execution. A failure of the finite statement aborts the program. This exact exhaustive finite-domain certificate is the substantive premise of the analytic all-parameter theorem below. It is an **algorithmically enumerated finite lemma**, not a closed-form claim that central unimodality automatically holds for all beta/delta values.

### Lemma 2: each first-passage survival probability is maximal at p=1/2

For each `m=0,...,188`, the genuine first-passage survival probability is
```
s_m(p)=Pr_p(J>m)
      =sum_(k=0)^m A_m(k)*p^k*(1-p)^(m-k)
      =sum_(k=0)^m binom(m,k)*c_m(k)*p^k*(1-p)^(m-k).
```
The **Bernstein derivative identity** gives exactly
```
s_m'(p)=m * sum_(k=0)^(m-1)
   binom(m-1,k)*(c_m(k+1)-c_m(k))*p^k*(1-p)^(m-1-k).
```
By coefficient symmetry, the k-th difference `c_m(k+1)-c_m(k)` is the negative of the `(m-1-k)`-th difference. By coefficient central unimodality, the difference is nonnegative for `k<(m-1)/2`. For `0<p<1/2`, the lower-index binomial mass at k is at least the reflected mass at `m-1-k`, because
```
binom(m-1,k)=binom(m-1,m-1-k),
(p/(1-p))^(m-1-2k) <= 1.
```
Thus the paired derivative terms are nonnegative and `s_m'(p)>=0` on `0<p<=1/2`; symmetry implies `s_m'(p)<=0` on `1/2<=p<1`. Therefore
```
s_m(p)<=s_m(1/2) for every p∈[0,1].
```
Since `c_25(0)=0` and `c_25(1)>0`, the derivative is strictly positive on `0<p<1/2` for m=25, and strictly negative on `1/2<p<1`, so `s_25(p)<s_25(1/2)` whenever `p!=1/2`. Hence the fair parameter has a strictly largest first-passage survival distribution.

### Lemma 3: native-trial expectation and uniqueness

Poissonize the original native one-step trial stream at unit rate. The two informative direction clocks are independent rate-`1/q` Poisson processes. In scaled time `u=t/q`, the probability that a direction with sign parameter p remains unfinished is the **nonnegative** Poisson mixture
```
F_p(u)=e^(-u)*sum_(m=0)^188 s_m(p)*u^m/m!.
```
By Lemma 2, `F_p(u)<=F_(1/2)(u)` for all `u>=0`, strictly for `u>0` when p is not fair. The probability that at least one of two independent directions is unfinished is
```
F_p1(u)+F_p2(u)-F_p1(u)*F_p2(u)
 =1-(1-F_p1(u))*(1-F_p2(u)).
```
It is coordinatewise increasing in the two F values and strictly increasing wherever the other direction has nonzero probability of having finished, as holds for all u>0. Therefore its integral, multiplied by q, is uniquely largest at `p1=p2=1/2`. The Poisson compensation identity equates this integral with the expected **discrete** number of original one-step trials. PREFIX-618 computed the exact rational value there; PREFIX-615 supplies the same slot0 versus slot1/2 factor of two. QED.

## Verification status and next unit

Executable file `PREFIX620_R6_global_worst_parameter_certificate.py` uses Python standard library exact integers and imports the unchanged PREFIX-618 root-checking certificate. Machine output is `PREFIX620_R6_RESULTS.json`, with actual `ALL_CHECKS_PASS` and the finite coverage values above. No original PREFIX-565 96-port graph rerun or independent review took place this turn. The 95% anytime joint confidence property is inherited from PREFIX-613/617; this theorem adds a sharp global expected **cost** result under its exact observer and target.

This research is a project-specific application of Bernoulli first-passage and binomial Bernstein techniques; it makes no priority claim over classical sequential inference. The real novel unit within this frozen BRC frontier is the finite checked survivor-coefficient shape that makes the global parameter comparison exact.

**Next:** extend one-direction stochastic domination into a constructive coupling of the full two-direction total original-trial stopping distribution; obtain a sharp all-parameter tail / quantile bound and determine whether variance, unlike the full stochastic order, is maximized at balance. Preserve native port/branch provenance and the observer/future-operation scope. Do not assume a variance ordering from a mean ordering.

BRC reuse resolution: `COMPOSE_APPLIED` (PREFIX-610, 613, 615, 618, 619); `EXTEND_EXISTING_TOOL` exact pathwise Bernstein survivor certificate.
