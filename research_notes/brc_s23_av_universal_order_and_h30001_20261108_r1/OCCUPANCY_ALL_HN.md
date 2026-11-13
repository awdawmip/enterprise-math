# Corollary: exact prefix-cell occupancy for all finite H and n

Date 2026-11-08 Asia/Shanghai; frozen scientific input awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Independent review pending. This corollary builds on PROOF.md in this directory, Theorem A (universal certified-convergent threshold ordering).

For any integer H>=1, n>=0, define thresholds t(v,j)=r*v-j, r=ln7/ln(10/7), with v,j>=0, v+j<=H, and attainable joint-label prefix scores E(k,l)=k-r*l with k,l>=0, k+l<=n. Let left=(vL,jL), right=(vR,jR) be consecutive distinct thresholds in strict increasing t order.

Choose by the constructive rational-interval continued-fraction algorithm an integer coprime pair P,D with D>n+H and

  (n+H)*abs(r*D-P)<1.

Such a pair exists for every finite H and n. Put

  X=-P*vR+D*jR,  Y=-P*vL+D*jL.

Then X<Y and the exact number of admissible prefix count pairs with

  t(left)<E(k,l)<t(right)

is

  O_n(left,right)=C_n(Y)-C_n(X+1),

where C_n(m) is the Euclidean-floor-sum rank/count function of Theorem A applied to the prefix triangle {(l,k):l,k>=0,l+k<=n} using the same P,D. Thus O_n can be computed in logarithmically many integer/Euclidean operations, following once-per-(n+H) rational precision/key construction. For a given cell it avoids enumerating the O(n^2) prefix count pairs.

Proof: Rearrange the strict real inequalities as

  -r*vR+jR < r*l-k < -r*vL+jL.

The coefficient of r in each difference between middle and either endpoint is l+v with 0<=l+v<=n+H. If this coefficient is nonzero, the rational-key perturbation argument of Theorem A preserves the strict sign; if zero, the integer difference is exact. Multiplying by D therefore gives

  X < P*l-D*k < Y.

All keys are integers. Counting keys strictly between X and Y gives the displayed difference of rank functions. The unobserved label-3 count is n-k-l, hence every counted pair is attainable in the declared auxiliary model.

For arbitrary H, first obtain adjacent threshold pairs via the independently certified threshold order oracle (Theorem A with denominator >H). For prefix occupancy, choose the possibly larger denominator >n+H and recompute the exact integer keys. Using distinct certified convergents at these two stages preserves their respective strict threshold/symbol ordering scopes.

Validation: VERIFY_OCCUPANCY_ALL.py exhaustively checked all bounded cells at H=1..13 and n in {0,1,2,3,5,10,15} against direct prefix enumeration. Five individually certified adjacent-cell probes for H=10^12 at n=2455069 and n=10^12 were evaluated with exact integers; source and output in RUN_OCCUPANCY_ALL.txt. These are finite validation checks; the universal result follows from the above rational approximation and floor-sum proof.

This makes both threshold adjacency and any selected prefix occupancy an exact, nonenumerative random-access primitive for every finite integer horizon and prefix budget. It supplies a reusable basis for adaptive first-empty-cell search and direct algorithmic analysis of gap classes with full bit/precision-cost accounting.
