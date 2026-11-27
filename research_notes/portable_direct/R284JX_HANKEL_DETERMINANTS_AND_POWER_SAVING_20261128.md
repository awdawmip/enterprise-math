# R284JX — Reciprocal Hankel determinants and a stronger power saving for integer roots

2026-11-28. Author proof and executed outward-rounded rational interval certificate; NOT_REVIEWED. Own recovered metadata EM-DIRECT-0C386E / TASK_RESEARCH, MCP-8cd6c4fa26b9459d923ff73ba0082220; no own formal RUN. Owner request r1-20261128-0201-leased SUCCEEDED: INV-4225921250d66b71ed2a93b631d63c06, as of 2026-11-27T18:03:17.222241Z, LEASED filter empty. Snapshot, not live write authority. No shared task mutation. Ordinary auxiliary arithmetic observer, not native spatial attribution.

Current global normative snapshot 508cc399147616bfad15ea13384acb850cb74db4: both canonical entries verified; P000 V4/V5, ACTIVE worldview, TASK route, portable/continuation, joint and residual contracts read. Frozen scientific inputs: JW c1c6493695d6591efc5811455c4a2aaf9df320fa:research_notes/portable_direct/R284JW_FOURTH_ROOT_COEFFICIENT_AND_SPARSE_INTEGER_ROOTS_20261128.md and JV b19f621164a985ba2b4d7c59a157a34cbebe7b71:research_notes/portable_direct/R284JV_TRANSCENDENTAL_SCALE_AND_DENSITY_ONE_SEPARATION_20261128.md (both full text read). Same C, full endpoint E and eventual unique legal real root q_d; reuse JV's all-fixed-order asymptotics and global residual comparison, not an independent review of those results.

## 1. General reciprocal Hankel determinant theorem

Suppose a real sequence defined for sufficiently large positive integers d has, for every fixed M, an asymptotic expansion
q_d=P_2(d)+sum_{k=1}^M c_k d^(-k)+O(d^(-M-1)),
with P_2 a fixed real polynomial of degree at most two. Constants may depend on M. For fixed m>=1 put n=2m+2, K=n(n-1)/2=(m+1)(2m+1), H_m=det(c_{i+j-1})_{1<=i,j<=m}. Assume H_m !=0.

For distinct integer arguments D<=d_1<...<d_n<=2D define the integer-coordinate observer
B_m=det rows (1,d_i,...,d_i^(m+1), q_di,d_i q_di,...,d_i^(m-1) q_di).
The exact determinant asymptotic is
B_m/V(d_1,...,d_n)= sigma_m H_m / prod_i d_i^m + O(D^(-mn-1)),
where V=prod_{i<j}(d_j-d_i) and sigma_m=(-1)^(m(m+2)+m(m-1)/2). The error is uniform over all distinct integer arguments, including adjacent ones.

Proof. For column j=0,...,m-1 subtract the polynomial part of d^j q_d:
d^j P_2(d)+sum_{k=1}^j c_k d^(j-k).
The degree is at most m+1, so these are exact determinant-preserving column operations. The remaining column has expansion sum_{k>=1} c_{j+k}d^(-k). The matrix of the first m reciprocal coefficients is precisely the Hankel matrix A=(c_{k+j}) with k=1,...,m and j=0,...,m-1. Right-multiply the residual block by A^(-1). The determinant of the original block is H_m times that of the transformed block. The transformed columns now have expansions d^(-k)+O(d^(-m-1)), k=1,...,m, with higher terms supplied by the all-order hypothesis.

For t_i=d_i/D, factor D^j from polynomial column j and D^(-k) from transformed residual column k. The total power is D^(m+1). The scaled columns are 1,t,...,t^(m+1), t^(-1),...,t^(-m) plus fixed smooth inverse-power corrections of order O(D^-1) or smaller. To control arbitrary adjacent arguments rigorously, take the q expansion through d^(-4m) with remainder O(d^(-4m-1)). Multiplication by d^j (j<=m-1), by fixed A^(-1), and by D^k (k<=m) leaves a scaled remainder O(D^(-2m-2)). Apply the Newton divided-difference row transform of orders 0,...,n-1, whose determinant equals 1/V(t). Every fixed smooth correction stays O(D^-1) by the divided-difference mean-value formula. For the discrete remainder, the explicit divided-difference sum has at most n terms, with each inverse denominator at most D^(n-1) because |t_i-t_j|>=1/D. Hence even the largest-order discrete contribution is O(D^-1). The divided-difference entries of the leading functions are bounded on [1,2], so determinant multilinearity gives a uniform O(D^-1) error in the normalized determinant. This proof requires no smooth extension of the remainder in integer d.

The leading determinant is evaluated exactly: multiplying each row by t_i^m changes the exponents to m,m+1,...,2m+1,m-1,...,0. Sorting them to 0,...,2m+1 gives sigma_m times the Vandermonde. Thus the normalized leading determinant is sigma_m/prod_i t_i^m. Since V(t)=D^(-K)V(d) and K-(m+1)=mn, restoration of factors proves the displayed formula. QED.

Corollary. E(X)=#{d<=X:q_d is an integer}=O(X^(1/(2m+1))) for each fixed m with H_m!=0. Indeed for sufficiently large D, |B_m|/V is between positive constants times D^(-mn). Choose a fixed b_m>0 small enough that the upper constant times b_m^K is <1. In a block of length H=floor(b_m D^(mn/K))=floor(b_m D^(2m/(2m+1))), if n distinct q_di are integers, B_m is an integer but 0<|B_m|<1, contradiction. At most n-1 arguments per block. Partition each dyadic interval and sum the resulting O(D^(1/(2m+1))) counts. Finite initial range absorbed. m=1 recovers JW exactly; m>=2 requires new Hankel nonvanishing, not merely c_1!=0.

## 2. Certified R284 reciprocal coefficients and nonvanishing

Use JW's exact full observer with h=1/d, s=d^2/q:
f_d=h^-1{3[4+s(3h+h^2)]^2(a+e)b-32[3+s(h+h^2)][a+s h^2(v+b)]^2}.
The normalised v,b,a,e and full endpoint are exactly those in frozen JW/JV. The executed extension computes the braces through h^8 with symbolic QQ coefficient polynomials. It uses the same log-product/Faulhaber identity as JW (omits the cancelled lower endpoint Bernoulli term); Euler-Maclaurin includes orders 2,4,6,8, both endpoints and the full e. Differentiate the smooth exponential-weighted integrands via polynomial operators. This yields f_d to order 7. Existence and remainder are supplied by JV; no effective bound for the remainder is claimed.

Use triangular Taylor jets in (h,s-s_*) with total degree <=8 before the h^0 cancellation. If s_d=s_*+sum_{j=1}^7 a_j h^j+O(h^8), determine a_j successively by setting the h^j coefficient of f_d(h,s_d) to zero: the coefficient of a_j is L'(s_*), and all other terms involve the previously determined a_i. Invert s_d using the reciprocal power-series recurrence. The exact interval operations use outward-rounded rational multiples of 10^-80; all multiplication/division enclosures follow the four endpoint rule and reciprocal rule. The bracket for s_* is (937181823342286298624673,937181823342286298624674)/10^24; both signs independently recomputed via exact moment enclosures. Taylor degrees 31/32 of exp(-s phi) bound every positive moment since 0<=s phi<=1. All symbolic polynomial coefficients and exact integrals of polynomial moments are rational. Derivative and root recurrences use interval arithmetic with no floating-point decisions. Displayed decimals are approximations only.

Result:
q_d=alpha*d^2+beta*d+gamma+c1/d+c2/d^2+c3/d^3+c4/d^4+c5/d^5+O(d^-6).
alpha approx 1.0670288039024105; beta approx -4.404699500829311; gamma approx -12.53363505603851.
c1 approx 10.255919898762528; c2 approx 26.886149082395104; c3 approx 15.866774024084763; c4 approx -167.233866633183; c5 approx -2640.50008128147.
H_1=c1>0 (JW reproduced);
H_2=c1*c3-c2^2 approx -560.1366490379958;
H_3=c1*(c3*c5-c4^2)-c2*(c2*c5-c3*c4)+c3*(c2*c4-c3^2) approx 1045534.571171761.
Exact scaled interval endpoints (denominator 10^80), as printed by the executed certificate:
H_2:
-56013664903799581449246950504483727201352999968948400725847962150806349801029339177
-56013664903799579368914681529457578722999820600469529334067977027664519317234091578
H_3:
104553457117176048452817912583409208952759223505323926063001423176964038371368611504470
104553457117176131789610311716502731873813372667520610714152345152537516608912095510102
In particular -561<H_2<-559 and 1045534<H_3<1045535; all sign assertions passed.

Executed certificate (full readback and Git blob match to local actual executed file):
9f683d9b489181ab756307b4cc50451540cf3343:research_notes/portable_direct/R284JX_hankel3_certificate.py
blob e752cdee18ca3455b9c8a4f166fb683031d33c01; SHA256 d77b49e4795e256acf2363c44a405b9c55e709fee453b03fe0427245ee3dd009.
Earlier independent-order truncation check (same recurrence, not independent review):
e4a95aa357eea5d57c3e5ad4b9d3429e0253eacb:research_notes/portable_direct/R284JX_hankel_certificate.py
blob cb00bf2f71c57522b94d11b231aaa6c4a03d1ab4; SHA256 c054296bc691f6e7670a92f1f3f3c3580dd147f979d6ace29c0a2f347eda6800.
Both runs reproduced JW gamma and delta intervals; H2 interval exactly matched across the two truncation orders. No numerical finite-d root computation is needed for this proof.

## 3. Stronger unconditional power count relative to the frozen JV/JW results

m=2 yields E(X)=O(X^(1/5)); m=3 yields the stronger
E(X)=O(X^(1/7)).
For m=3 use rows (1,d,d^2,d^3,d^4,q_d,d q_d,d^2 q_d) and
B_3/V=H_3/prod_i d_i^3+O(D^-25).
There are 28 Vandermonde factors. For sufficiently large D the upper bound for |B_3|/V is 1100000 D^-24; in each block of length floor(D^(6/7)/2), the determinant magnitude is at most 1100000/2^28<1 and is nonzero. At most 7 exceptional d per block. This bounds all legal integer zeros of the complete C, hence all target equality qK=32/3, since eventual uniqueness comes from frozen JS/JV. The d count is not a q count. The asymptotic onset remains unevaluated.

## 4. Shrinking targets, using the same joint determinant

For fixed A>2m and C0>0 count d<=X with dist(q_d,Z)<=C0*d^-A. Let integer n_i be a nearest integer for each chosen d_i, and apply the same polynomial subtraction, Hankel block transformation, and scaling to the integer observer with n_i replacing q_di. Each transformed scaled residual column changes by O(D^(2m-1-A)), because its linear combination uses d_i^j with j<=m-1 and scaling D^k with k<=m. Suppose successive d gaps are at least T>=1. In the divided-difference row transform the perturbation of order k is O(D^(2m-1-A)*(D/T)^k) for k<=2m+1. With T<=D this is bounded uniformly by O(D^(4m-A)/T^(2m+1)). Choose T=ceil(K0*max(1,D^((4m-A)/(2m+1)))) with sufficiently large fixed K0 (depending on m,A,C0 and coefficient matrices) to make this error smaller than a fixed fraction of the leading normalized determinant, whose absolute value on [1,2]^n is bounded below after normalization. The determinant is Lipschitz on the bounded divided-difference entries, so it remains nonzero and bounded above by a constant times V(d)D^-mn. Take a sufficiently small fixed block-length factor b_m for this upper constant, ensuring magnitude <1. Since A>2m the exponent for T is strictly less than mn/K, so the selection is feasible in sufficiently large blocks. Greedy selection with successive gaps >=T gives at most (n-1)T exceptional d per block (otherwise n distinct arguments can be selected). Therefore
E_A(X)=O(X^[1/(2m+1)+max(0,(4m-A)/(2m+1))]).
For m=3: A>=12 gives O(X^(1/7)), 6<A<12 gives O(X^((13-A)/7)); for m=2: A>=8 gives O(X^(1/5)), 4<A<8 gives O(X^((9-A)/5)). Combine with JW m=1 when that bound is stronger. By JV's two-sided residual-distance comparison this applies to g_d<=d^-A (adjust C0). This is not an all-d inverse-polynomial lower bound. Constants and effective onset remain open.

## 5. Next scientific question

Can nonzero reciprocal Hankel minors be shown at infinitely many orders by a structural property of the joint asymptotic sequence? The theorem would then give E(X)=O_epsilon(X^epsilon) for every epsilon>0. Nonvanishing beyond the third minor is not proved here; transcendence of alpha alone cannot imply it. Even such a subpower bound would not rule out individual integer zeros. The other high-value route is to use exact C congruences / JQ root-distance certification on the remaining sparse d, and to make the asymptotic onset effective. No formal Result, independent Review, canonical theorem admission or task closure claimed.
