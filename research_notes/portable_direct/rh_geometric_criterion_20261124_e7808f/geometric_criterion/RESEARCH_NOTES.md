# Fixed 9:12:16 geometric criterion — work notes

Current identity EM-DIRECT-E7808F / TASK_RESEARCH; Activity RA-0B92AAF774CA466C1C1BC38B. Parent-author work, not independent Review. Previous Source 42e7aa4dbd01a6eb66e2f881c7cddcba72a3d775, scientific foundation freeze 9fc068244e4f1117f1e75df5eb0285c6697d21d7.

The prior dependency and work Markdown targeted search found no 9n/12n/16n Mellin single-sided criterion; this is a targeted local dependency comparison, not a literature-priority claim.

Verified algebra:
G(x)=7q*(12x)-4q*(9x)-3q*(16x)=12x t_x.
Background t=log(4/3).
M(s)=7*12^s-4*9^s-3*16^s=-3*9^s*((4/3)^s-1)*((4/3)^s-4/3).
M has no zeros in 0<Re(s)<1.
G'(x)=12log(4/3)+36 sum_{9x<n<=12x} Lambda(n)/n-48 sum_{12x<n<=16x} Lambda(n)/n a.e.; O(log x), enabling all-integer to continuum transfer.

Mellin initially Re(s)>1:
Q(s)=(1+gamma)/(s-1)-1/(s-1)^2-(zeta'/zeta)(s)/(s(s-1)).
F_G(s)=M(s)Q(s)-an entire finite-endpoint term.
Each nontrivial zero rho gives a genuine pole because M(rho)!=0.

Unconditional high prime power payment:
delta_n=log(4/3)-sum_{9n<p<16n} phi_n(p)log(p)/p=t_n*+PP_n, 0<=PP_n<=16/(3sqrt(n)).

Actual changing matched family any B_n>=16n, m_n=ceil(.7log B_n), theta=.5:
|t_D^(n)-t*|<=(7/18) eta_{16n}<=(7/18)eta_{B_n}<=(20/9)B_n^(-beta), beta=.7log(28/(5e))>.5.
The family changes with n; Mellin is applied only to the fixed reference, then errors are transferred.

Single-packet normalized square budget with X=9n,h=7n:
B_geo(n)=(343/81)n (t_n)_+^2=(343/11664)G(n)_+^2/n.

Completed in PROOF.md: one-sided bounded RH equivalence, exact Theta growth index, normalised-budget exponent 2Theta-1, all-integer to continuum transfer, ordinary-prime and actual changing-family transfers. The complete reference Mellin transform needs its correct gamma calibration; the triangle G itself cancels all linear calibration changes and does not recover gamma. Thus geometry alone cannot replace the separate true-skeleton requirement.

Finite checks completed: 4,824 exact rational source impulses, 24 exact background identities, 69 local arithmetic samples through R=32,768, and outward certification beta>1/2. These checks do not prove an unbounded bound. Parent and sibling mathematical crosschecks found no material defect after the calibration wording was clarified; they are author checks, not independent Review.

The RH reverse bound was sharpened by retaining the exact critical-line multiplier phase. Its leading coefficient is C_geo=(sqrt(3)/6)*(7log7-4log2-8log3-gamma-log(pi)), enclosed in [0.09755443072883494551767459919057286,0.09755443072883494551767459919057287]. The residual bound is 1/(1440n^3). This is a conditional RH upper bound, obtained without zero queries; gamma uses its frozen enclosure and pi uses a rational Machin remainder.
