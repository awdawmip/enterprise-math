# Which arrangements change status when the two origins move?

Let \(z_i\in\mathbb R^2\) be each labeled pair of scaled readings. At a common origin \(A\in[0,1)^2\), all arms are rounded by the same coordinatewise rule \(z\mapsto\lfloor z+A\rfloor\). Let \(I_i(A)\) equal one if only label i lands in its bin, and let \(q_i=\int I_i(A)\,dA\). Write \(N=\binom c2\) and \(V(A)=N^{-1}\sum_i I_i(A)\).

## Exact individually attainable and permanent status

For each origin the unique unit cell containing \(z_i\) has a lower corner \(s\in z_i+(-1,0]^2\). As A ranges uniformly over the torus, this s ranges uniformly over the square. A second reading \(z_j\) occupies that cell exactly when \(s\in z_j+(-1,0]^2\). Translating all squares together and discarding their boundaries in the integral gives
\[
 q_i=\left|(z_i+[0,1)^2)\setminus\bigcup_{j\ne i}(z_j+[0,1)^2)\right|.
\]
The original torus is partitioned by the finitely many true coordinate breakpoints into half-open rectangles, each of positive area. Each bin status on its lower edges equals the status from the positive side. Hence \(q_i=0\) means no origin can isolate label i, \(q_i=1\) means every origin does, and \(0<q_i<1\) means that moving the origin can switch the status.

On each vertical sweep slab sort the active squares by bottom y, using the label to break ties. The exclusive vertical length of i equals
\[
 [\min(y_i+1,y_{\rm succ})-\max(y_i,y_{\rm pred}+1)]_+ .
\]
Drop a missing predecessor or successor term. Lower squares can cover through at most the predecessor top, and higher squares start no earlier than the successor bottom. All squares have the same height, so these two neighboring intervals account for every overlap with i on the slab. At an x-event flush accumulated areas for the entrant or exiting square and its two immediate neighbors, then update their lengths. Unchanged lengths may accumulate over many slabs. Sorting plus 2N events costs \(O(N\log N)\) time and \(O(N)\) space for all labeled integrals.

The true endpoint order can certify the three statuses independently of numerical area estimates. Mark a square attainable upon the first slab of positive true width on which its exclusive upper y endpoint exceeds its lower one. Mark a square changeable from permanent upon a slab of positive true width on which any positive y length is covered. Events at the same x create no slab between them. True ranks still identify positive widths when endpoints have the same rounded integer coordinate. Duplicate squares and shared boundaries are allowed by the geometry.

## Independent origins and cancellation

For two independent uniform choices A,B, the expected fraction of labels that switch status equals
\[
 S=N^{-1}\sum_i\Pr[I_i(A)\ne I_i(B)]=2N^{-1}\sum_i q_i(1-q_i).
\]
If G,L are the numbers of labels gained and lost between A and B, then \((G+L)/N\) is the fraction switching and \(|G-L|/N=|V(A)-V(B)|\). When \(S>0\), define the fraction of the *expected total number of switches* canceled in the net count by
\[
 C=\frac{\mathbb E[2\min(G,L)]}{\mathbb E[G+L]}
   =1-\frac{\mathbb E|V(A)-V(B)|}{S}
   \ \ge\ 1-\frac{\sqrt2\,\sigma}{S},\qquad
 \sigma^2=\operatorname{Var}_A V(A).
\]
The inequality uses Cauchy–Schwarz and independence of A,B. A separate comparison for the sum of covariances at one common origin is
\[
 \sum_{i\ne j}\mathrm{Cov}_A(I_i,I_j)=N^2\sigma^2-NS/2.
\]
These estimates address different quantities. At c=512 the variance ratio \(2N\sigma^2/S\) lies in \([1.86115412,1.86134580]\). The independent C81 common-origin sweep tightens the cancellation lower bound to 98.109422% at c=512 and gives 99.031829% at c=1024. The means from the two different algorithms overlap in all four shared catalogues (32, 64, 512, 1024), as recorded in common_counts.json.

## Certified results for near-critical adjacent stocks

The two original measurements are at c and c+1, each with \(p=\lfloor(9/4)\log_2 c\rfloor\) bits. The counts of never, sometimes, and always unique arrangements are exact.

| c | p | never | sometimes | always | switch rate S (rounded, %) |
|---:|---:|---:|---:|---:|---:|
| 8 | 6 | 11 | 17 | 0 | 0.753718 |
| 16 | 9 | 74 | 46 | 0 | 5.027219 |
| 24 | 10 | 159 | 114 | 3 | 4.602174 |
| 32 | 11 | 247 | 239 | 10 | 8.297761 |
| 64 | 13 | 1,097 | 742 | 177 | 7.379207 |
| 128 | 15 | 4,910 | 2,027 | 1,191 | 5.177443 |
| 256 | 18 | 18,713 | 6,573 | 7,354 | 4.942569 |
| 512 | 20 | 78,609 | 20,666 | 31,541 | 3.980659 |
| 1024 | 22 | 322,746 | 67,055 | 133,975 | 3.121052 |

The pairs (32,512) and (64,1024) have respectively identical multipliers \(2^{p-(9/4)\log_2c}=2^{-1/4}\) and \(2^{-1/2}\). At c=512 exactly 49,800 arrangements reach \(q_i\ge0.01\), 38,441 reach \(q_i\ge0.50\), and 31,824 reach \(q_i\ge0.99\). The proportion switching lies in \([0.039806587314,0.039806587329]\). These finite results permit jointly moving both origins throughout their entire torus. A critical-limit value or rate does not follow from this table.

## Error bounds and reproduction

C80's critical_bins.py encloses the two original readings by integer arithmetic with outward rounding, starting at 176 bits. Multiplying by \(2^p\) and translating all coordinates by a common integer yields true coordinate intervals and exact unit translates for the endpoints. Every distinct pair of consecutive endpoint intervals must be strictly separated. A provably equal exact rational endpoint is admitted as a tie. The driver increases working precision if true ordering cannot be resolved. It separately encloses each exact position within \(1/Q\) of its reported fixed-point coordinate, \(Q=2^{40}\). Fixed-point coordinate ties may collapse an arbitrarily short positive slab in the area approximation, while its true rank persists in both exact status flags. The sweeper computes fixed-point areas with 128-bit integer products. Its bounds on coordinate sizes, and the fact that each labeled area is at most one, prevent signed overflow.

Replacing one unit square by its translated fixed-point copy changes its membership on area at most \(4/Q\). For example, separate a horizontal and vertical move of at most \(1/Q\), each with symmetric-difference area at most \(2/Q\). At every point of this symmetric difference, toggling this single membership changes the vector of exclusive-label indicators by at most one in the \(\ell^1\) norm. Integrating and replacing all N squares gives
\[
 \sum_i|q_i-\widetilde q_i|\le4N/Q.
\]
The errors in the mean q, mean square q, and S are therefore bounded by \(4/Q,8/Q,8/Q\), respectively, using the 1-Lipschitz property of \(u(1-u)\) on the unit interval. Each single-label error is also at most \(4N/Q\), giving threshold-count brackets. The \(10^{-12}\) brackets in individual_profiles.json enclose true values. The conservation-of-count identities there refer to labeled arrangements. Independent C80 common-origin means and standard deviations are included in c80_extrema_moments.json. The variance ratios and cancellation lower bounds use their outward standard-deviation brackets. A finite check independently enumerates every offset and every label on 203 integer test catalogues with mixed signs, duplicate points, ties and unit-boundary separations. For the physical c=8 catalogue a second independent computation reads the original state transitions as exact rational numbers, checks all 28 labeled areas across all 841 origin rectangles, and verifies the reported first moment, second moment, switching fraction and threshold-count brackets.

Run, from this directory, with Python 3 and a C++17 compiler:

```sh
c++ -O3 -std=c++17 individual.cpp -o individual
python3 test_individual.py
python3 individual.py 8 16 24 32 64 128 256 512 1024 --output individual_profiles.json
python3 test_native_origins.py
python3 check_common_counts.py
```

Original measurement enclosure and comparison inputs are reproduced unchanged from enterprise-math commit 441853d82f262cceb29b631c737d67b9b79910f9, C80 grid/critical_bins.py and grid/extrema_moments.json.
