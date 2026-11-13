# Stage379-B | Exact narrower two-sided cusp localization

2026-11-02, Asia/Shanghai. Author-side exact continuous-real theorem, independently unreviewed. Original frozen scientific pins: GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 Git Blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Scientific predecessor: Stage378-B commit c139cf4af6f3f5a954434139468127a3521ce85f in Draft PR #1736.

## Model and exact theorem

Let k=0,1,2,3, B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160. All four residual channels and all sixteen individually weighted audit comparisons remain separate. Define b(x,y)=(5/32)sum_k w_k |r_k(x,y)|; D(a,z)=(1/2)sum_k w_k|B_k(a)-B_k(z)|; c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256. Minimize 33/1024+c(P)+c(Q) over [0,1]^4 subject to b(P)+b(Q)<=2beta_*+11/5000, where beta_*=b(q_*) for the inherited isolated simultaneous r_0=r_1=0 root.

**Theorem.** Every global minimizer, after interchange of P and Q as needed, satisfies P in (0.2308,0.2345) x (0.55,0.56), and Q in (0.2365,0.239] x (0.57566,0.57574). For alpha=(1+sqrt(13))/8, |y_Q-alpha|<47/1000000.

## Full exact proof and certificate

Stage378-B established the inherited P band and Q_y in (0.57565,0.57575). Opposing exact rational r0/r1 face signs isolate q_* within x in (231083940,231083942)/10^9, y in (555508852,555508864)/10^9. There sum_k w_k r_k=0 and signs r2>0>r3 imply beta_*=(15/16)r2(q_*), and monotonicity of B2 on this box yields the strict budget bound B_UP=97582683/10^10 >2beta_*+11/5000.

The exact feasible rational comparator P_ref=(23113910/10^8,55568442/10^8), Q_ref=(23780690/10^8,57569391/10^8) has variable cost C_ref=16174336378406867755705673/256000000000000000000000000. Feasibility follows from its exact b sum being below the root-enclosure lower budget.

Set lambda=483/400 and L=c+lambda b. On each closed subrectangle choose signs s_r,s_xa,s_xb,s_ya,s_yb in {-1,0,1}, independently for each k, at the midpoint. The inequality |u|>=s*u holds throughout the box, including sign changes, and gives the separable cubic lower support
L>=K+sum_k A_k B_k(x)+sum_k H_k B_k(y),
A_k=w_k[lambda*s_r/8-(63*s_xa+s_xb)/512],
H_k=w_k[lambda*s_r/32-(9*s_ya+7*s_yb)/512],
K=sum_k w_k[((63*s_xa+9*s_ya)*B_k(1/4)+(s_xb+7*s_yb)*B_k(3/4))/512-lambda*m_k*s_r/1024].
For any cubic f on [a,b], every f(t) is at least the minimum of its four Bernstein–Bezier control ordinates f(a), f(a)+(b-a)f'(a)/3, f(b)-(b-a)f'(b)/3, f(b). Apply this to each signed x and y cubic, then bisect the longer side recursively at exact rational midpoints. The complete binary leaf-cover checker verifies all interval paths, strict inequalities, and exact domain-volume coverage.

The resulting strict region-wide lower bounds are:
* Closed P=[0.2308,0.2345]x[0.55,0.56]: L>37517335/10^9; 1344 leaves, depth at most 35.
* Closed Q_LO=[0.2365,0.239]x[0.57565,0.57566]: L>37446850/10^9; 37 leaves, depth at most 18.
* Closed Q_HI=[0.2365,0.239]x[0.57574,0.57575]: L>37446805/10^9; 72 leaves, depth at most 22.

Define the above three lower thresholds T_P, T_QLO, T_QHI. The **exact positive dual margins** are
T_P+T_QLO-(C_ref+lambda*B_UP)=19084697132244294327/256000000000000000000000000>0,
T_P+T_QHI-(C_ref+lambda*B_UP)=7564697132244294327/256000000000000000000000000>0.
Thus a feasible pair whose Q is in either excluded closed strip has c(P)+c(Q)=L(P)+L(Q)-lambda[b(P)+b(Q)]>T_P+T_Q-lambda*B_UP>C_ref. Since the comparator is feasible, neither closed strip can contain a global minimizer. Inherited containment gives the strict new band, including boundary exclusion. The polynomial 16t²-4t-3 has opposite signs at 575693/10^6 and 575694/10^6, isolating alpha and proving the stated 47/10^6 distance bound.

## Executed verification, provenance and open questions

Actual self-contained standard-library Python Fraction source was executed and independently replayed against its deterministic complete CSV; both standard outputs were byte-identical. Total 1453 closed leaves, zero unresolved. Normalized CSV 182434 bytes, SHA256 aa48034a214df51a493d387862e12d05eed5b18681299574f41264656262d828; result marker STAGE379B_EXACT_NARROWER_CUSP_QY_PASS. The repository adapter reuses the immutable Stage377-B signed-Bernstein proof kernel with Git Blob 9b54a83059ff965e4807577448c3828cc64e8f04; it applies the new exact constants and verifies/regenerates the same normalized CSV hash. The standalone run is actual executed evidence; adapter execution from a new checkout remains available for separate replication.

This is a continuous-real auxiliary Bernoulli/BRC theorem, not a native P000/X6 theorem. Complete four-parameter optimality, exact global cusp candidate evaluation, Source Result/CLAIM, independent review and the native observer-preserving three-dimensional slice/third-coordinate mapping remain open. Next Stage380-B studies the exact polynomial critical chambers and cusp boundary rather than simply repeating narrower-band certificates.
