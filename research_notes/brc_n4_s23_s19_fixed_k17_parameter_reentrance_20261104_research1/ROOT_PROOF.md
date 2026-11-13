# Certified transition root bracket at K=17

Date 2026-11-04. Parent PROOF.md establishes exact three-point optimal allocation reentrance at h=1/42, K=17, with frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Let g(s)=9 C_T(s)-17 C_B(s), where the source-retaining and Bernoulli Chernoff information functions retain their original labelled distributions; definitions and certified curvature bounds are given in PROOF.md and VERIFY.py.

**Theorem (existence).** There exists at least one real transition point s* in the following open rational interval:

s_lo = 1/9 + 9805774/10^12 = 500044125983/4500000000000;
s_hi = 1/9 + 9805775/10^12 = 40003530079/360000000000.

At s_lo the unique optimal K=17 strategy is 9 T; at s_hi the unique optimal K=17 strategy is 17 B. Their difference g has rigorous rational enclosures reported by ROOT_CERT.py, with g(s_lo)>0 and g(s_hi)<0. Because C_T and C_B are continuous on 0<s<1, the intermediate value theorem supplies at least one zero in the open interval. This is a root existence and bracket result; uniqueness of the zero remains open.

**Numerical display of strict rational enclosures:** g(s_lo) is between 3.80639e-16 and 3.83501e-16; g(s_hi) is between -2.19359e-16 and -2.16497e-16. These decimals are rounded outward for human reading; the script's assertions use exact Fraction intervals.

**Uniform finite-allocation reduction:** throughout this interval 9 T is feasible and 10 T is infeasible. For s_lo<=s<=s_hi, B(s_lo) is a Bernoulli thinning of B(s), so the Chernoff data-processing inequality gives C_B(s)>=C_B(s_lo). The explicit formula C_T(s)=-log(1-s+2s sqrt(1/4-h^2)) is increasing in s; cost c(s)=2-s is decreasing. Hence E(s)=C_T(s)-c(s)C_B(s) <= C_T(s_hi)-c(s_hi)C_B(s_lo). ROOT_CERT.py verifies with strict rational intervals that C_B(s_lo)>1/100000 and 8[C_T(s_hi)-c(s_hi)C_B(s_lo)]<C_B(s_lo)/10. For m=1,..,8, unused cost u is the fraction m/9+m(s-1/9), uniformly between 1/10 and 1 on the bracket. The bound C(m,n)<=17 C_B+mE-u C_B excludes all such m. The only competing allocations are 9 T and 17 B; they tie at any zero of g.

Run python ROOT_CERT.py in the same directory as VERIFY.py; it executes the prior exact certificate, then performs binary search over the 10^(-12) rational grid. The certificate depends on integer isqrt, Fraction arithmetic and analytical remainder/strong-concavity bounds. No floating result is used in proof assertions.

Evidence status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Next: bound g'(s) throughout the bracket, or otherwise certify the exact number of zeros; then address arithmetic budget-residue transitions for nearby rational s.
