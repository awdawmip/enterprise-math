# R749SME — Finite-controller exact online Walsh-observable closure

Date: 2026-11-13 (Asia/Shanghai). Predecessor R749SMD and R749SMB/R749SMC (PR #2193). Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Author-side algebraic proof with Fraction verification; native V29/V39 event permission not asserted. Historical signed-Port/BRC source Z is time-labeled data, not a new spatial axis.

## 1. General exact theorem

Let Z∈{±1}^d be a static finite historical-source variable, M a finite controller-mode set, Σ a finite public-output alphabet and δ(m,a) the publicly determined next mode. Every output has a declared rational nonnegative likelihood q_(m,a)(z) satisfying ∑_a q_(m,a)(z)=1 for all z. Define F_(m,empty)(z)=1 and F_(m,aw)(z)=q_(m,a)(z) F_(δ(m,a),w)(z).

Define V_m^(h)=span_Q{F_(m,w): |w|≤h} in Q^({±1}^d). Then

V_m^(0)=span{1};
V_m^(h+1)=span( {1} ∪ ⋃_(a∈Σ) q_(m,a)·V_(δ(m,a))^(h) ).     (1)

**Theorem A.** This recurrence computes the exact predictive observation row spaces. The vector of all mode-spaces stabilizes after at most |M|(2^d−1) strict-growth rounds; at the first simultaneous fixed point it equals the all-finite-future row spaces. For arbitrary strictly interior priors on all 2^d histories, the minimum number of independent **affine-linear expectation** coordinates preserving every finite public word probability from mode m is dim(V_m^(∞))−1.

Proof: Every nonempty word uniquely decomposes as a first output a and a remaining suffix, giving (1). The sets of words length≤h are nested, so each V_m^(h) is monotone. Their total dimension is an integer between |M| and |M|2^d. A step with no growth is a fixed point of the full simultaneous recurrence and hence remains fixed forever; a strict-growth step increases the total dimension by ≥1. Thus finite termination and the bound hold. Given any basis containing 1, its nonconstant expectations reconstruct all likelihood functionals. Conversely, any affine statistic preserving all word expectations on the open interior of the prior simplex must have its kernel contained in the common kernel of these functionals, hence needs at least dim(V_m)−1 independent coordinates. This is a minimum for affine expectations, not a lower bound on arbitrary nonlinear real encodings.

## 2. R749SMD as a five-mode all-horizon example

Take the declared historical source Z=(X,Y,T) of three time-labeled signed-Port signs and the legal forced/nonforced public choice described in R749SMD. Define modes:

- root: query X and move to plus on public +, or minus on public −;
- plus: query Y and move to joint after either result;
- minus: query T and move to joint after either result;
- joint: query YT and move to fair;
- fair: emit independent fair ± outputs forever and remain fair.

At a query χ_v use q_(m,a)=(2+a χ_v)/4; at fair use q=1/2. Both forced and nonforced public support choices are available at each legal unsigned directed-support state (120 total). This is an explicit historical-source controller conditional on R749SF lift dynamics, not a native-event admission.

**Theorem B.** The root horizon ranks are 1,2,4,8 at H=0,1,2,3 and stabilize at 8 for all later finite H. At the fixed point the ranks are root 8, plus 4, minus 4, joint 2, fair 1.

Proof: fair's law has no dependence on Z, giving rank 1. The single joint query YT yields rank 2. From plus the two characters Y,YT form a binary basis of (Y,T); from minus the characters T,YT do likewise; their 4×4 likelihood maps are invertible B⊗B matrices, giving rank 4. The root's first X query has two independent factors (1±X/2), and each branch retains full 4-dimensional (Y,T) observability; combined rank 8. No further query can increase a rank already 8. Consequently all mode spaces stabilize by horizon 3.

## 3. Exact constructive Walsh recursion

Index the 2^d Walsh characters by masks u∈F₂^d, using χ_uχ_v=χ_(u XOR v). For coefficient vector c, multiplication by the biased query q_(v,a)=1/2+(a/4)χ_v is the sparse exact transport

(T_(v,a)c)_u=c_u/2+(a/4)c_(u XOR v).

Apply these transfers to current bases and reduce over Q via rational Gaussian elimination, iterating (1) until every mode's space stabilizes. This constructs the exact future-safe predictive carrier for a finite-mode policy without needing to enumerate every historical prior or generate exponentially many word strings. Exact algebraic termination is proved; representation-size/bit complexity and runtime must be evaluated separately when claiming engineering acceleration.

## 4. Validation and scope

The companion Python Fraction checker implements five controller modes, the Walsh-XOR coefficient transfers, exact rational basis reduction, the root-rank history [1,2,4,8], all five fixed-point ranks and stabilization at H=3; executed output reports PASS. The general finite-mode theorem holds for all finite d and finite M, while the executable coverage is the displayed d=3 five-mode controller. No physical Cell/Link/Port event is created by this calculation.

Next: read exact native V29/V39 event guard, source transport and three-force closure witness and instantiate only the permitted native output laws; compare resulting reachable row spaces with this source-prediction algorithm. If public controller modes are unbounded, study finite-horizon or bounded-controller subclasses rather than infer a universal finite carrier.
