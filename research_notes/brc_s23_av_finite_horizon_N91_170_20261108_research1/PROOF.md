# S23/AV finite-future sign observer: exact saturation for h=91..170 and new 22-horizon plateau

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_FINITE_PROOF. Frozen scientific reference: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Extends the author-side exact results through h=90 in Draft PR #1777 at `9b5002cfe9ca4852c327f1afdca127899d5dddb3`.

## Declared experiment and observation

The two legal S23/AV parameter points are theta0=(1/2,1/2) and theta1=(5/7,7/8), with full-label single-step laws P0=(1/2,1/4,1/4) and P1=(5/7,1/4,1/28) for labels (1,3,4). Both project to the same Bernoulli z=1/4 observer. For an ordered prefix with counts (k,ell) of labels (1,4), its likelihood ratio is

`Lambda(k,ell)=7^(k+ell)/10^k`.

Label 3 pads a prefix without changing this ratio. A suffix with counts (i,j), i+j<=h, places the sign transition threshold at `T(i,j)=10^i/7^(i+j)`. Write s=i+j and order the `M_h=(h+1)(h+2)/2` thresholds `10^i/7^s`, `0<=i<=s<=h`. Distinctness follows from unique factorization. Apart from the equality class (all label-3 prefix and suffix), each minimal future-sign state is one of the M_h+1 open threshold intervals.

Define N(h) as the least n such that length-n padded prefix observations meet **every** open interval, so the minimal finite-horizon sign-state partition has saturated.

## Main exact finite theorem

For every integer h with 91<=h<=139 or 162<=h<=170,

`N(h)=n_tail(h):=min{n>=1:7^(n+h)<10^n}=floor(h*log(7)/log(10/7))+1`.

For every integer h with 140<=h<=161,

`N(h)=880`.

At the boundaries,
`N(139)=759`, `N(140)=880`, `N(161)=880`, `N(162)=884`.
In particular the second interior-gap exceptional plateau has 22 successive integer horizons, with a 121-unit increase from h=139 to h=140. At h=140, the tail bound is only `n_tail(140)=764`.

### Exact certificate and completeness

Set `T_{i,s}=10^i/7^s` and enumerate each `0<=i<=s<=h`. Sort with the exact predicate

`T_{i,s}<T_{j,t} iff 10^i * 7^t < 10^j * 7^s`.

For each total prefix count n>=1, every pair (k,ell) with k+ell=n is tested. The open interval of `Lambda=7^n/10^k` is located using exact comparisons

`Lambda<T_{i,s} iff 7^(n+s)<10^(k+i)`.

An equality is impossible for n>=1 by unique factorization. The algorithm marks the first n at which each interval is hit; the maximum first-hit count is exactly N(h). The tested prefix pairs cover all length-n ordered samples after padding with label 3. `VERIFY.py` checks every threshold, all interval hits, and the first-hit maximum for each of the 80 indicated horizons. No floating point, tolerance, probability simulation, or external numerical assumption is involved.

The leftmost threshold is `7^(-h)`; the smallest prefix likelihood ratio among lengths <=n is `(7/10)^n`, giving the universal bound `N(h)>=n_tail(h)`. For h in the stated tail-equality ranges, exact exhaustive enumeration shows the final unoccupied interval is precisely the leftmost one and is filled at n_tail(h).

### The interior gap and its exact 880-step lower certificate

For each 140<=h<=161, exhaustive exact threshold ordering identifies the same adjacent pair

`A=T(60,80)=10^60/7^140 < B=T(0,69)=7^(-69)`.

Here the first expression uses suffix coordinates (i,j)=(60,80), i+j=140. Their order follows `10^60<7^71`. They remain consecutive as h grows from 140 through 161.

For fixed ell>=0, let k_min(ell) be the smallest k>=0 satisfying `7^(k+ell+69)<10^k`, i.e. `Lambda(k,ell)<B`. As k increases, Lambda decreases, so the **first** ratio below B is the largest candidate in (A,B). Exact integer iteration yields:
- for every 0<=ell<=77, `7^(k_min(ell)+ell+140)<=10^(k_min(ell)+60)`, hence the first-below-B ratio is <=A;
- `k_min(78)=802`, and `7^(802+78+140)>10^(802+60)`, hence `Lambda(802,78)` lies strictly between A and B;
- k_min(ell) is nondecreasing in ell, so for ell>=78 the minimal prefix count k_min(ell)+ell is at least 802+78=880.

Therefore no prefix of length <=879 occupies (A,B), while length 880 does. The complete interval-occupancy test shows all other intervals have been hit by length 880 for h=140..161. Thus N(h)=880 throughout this interval.

The integer verifier independently checks all 79 rows ell=0..78, all 80 h-values, all threshold orderings, and every finite prefix occupancy needed for the theorem.

## BRC and Source interpretation

The branch carrier keeps the two **joint** counts (k,ell) and the underlying ordered three-label outcome; the declared finite-future observer reads the likelihood-difference sign under all suffixes of length <=h. The reduction to threshold cells has an exact future-operation certificate only for that horizon. This is an author-side auxiliary statistical observer result; the six-source ten-label S23 mother experiment remains a separate transfer problem. P000/Heartbeat-X6 basis and native arithmetic requirements are not modified. Mathematical admission and independent review remain pending.

## Verification boundary / next questions

The full exhaustive integer certificate covers h=91..170 (80 integers) and the fixed exact two-point S23/AV experiment. Source artifacts are `VERIFY.py` and `RUN_EVIDENCE.txt`. The plateau repeats a scaled rational gap from the h=71 phenomenon, suggesting a Diophantine/continued-fraction treatment of interior threshold gaps. Next: characterize infinite families of these plateaus or prove an effective bound on their excess `N(h)-n_tail(h)`; retain the separate four-observation full-law minimax delta4 and ten-label mother-model bridge.
