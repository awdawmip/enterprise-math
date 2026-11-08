# PREFIX-580-R2 — Fourth cumulant tensor of the orthogonalized native six-axis gate residual

Date 2026-11-08 Asia/Shanghai. Status AUTHOR_PROVED / EXACT_RATIONAL_COMPUTED / UNREVIEWED / NOT_ADMITTED.

## Input and observer
Frozen science awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d: the 48-phase four-STAR native X6 BRC, all 96 signed/branched native ports with 6 labeled actions per port; exact original six-axis rewards R1...R6 and gate mark K. Action count d is not physical time. The 37-state PREFIX566 quotient cannot carry all six rewards; the calculation here uses the original 96 ports. The canonical PREFIX577-R6 covariance gives the exact zero-sum correction beta=(5,-1,5,-1,-4,-4)/192. Define

    Y_d = K_d - beta·(R1,...,R6)
        = K_d - (3R1+R2+3R3+R4)/64 + d/48

at the frozen zero root, using exact sum_i R_i=d. For the native original edge e define integer M(e)=64g(e)-3q1(e)-q2(e)-3q3(e)-q4(e). Then Y_d=Σ_e M(e)/64+d/48. Cumulants of order 2 and above are unaffected by the deterministic shift d/48. The prior PREFIX577 root gauge similarity proves all nine frozen roots have the same limiting cumulant rates.

## Theorem 580.1
For every initial native port and each of the nine frozen roots, the normalized fourth cumulant converges to

    lim_(d→∞) Cum4(Y_d)/d = 87518285/21743271936 > 0.

The same exact kernel reconstruction independently reproduces lim Var(Y_d)/d=367/73728 and lim Cum3(Y_d)/d=28537/6291456 from canonical PREFIX577-R6 and PREFIX578-R6. This is a new positive fourth residual statistic after second-order orthogonalization, not an assertion of statistical independence from the six axes.

## Theorem 580.2 — Complete quartic mixed tensor of (Y,K)
For all rational a,b, write f(a,b)=lim_(d→∞)Cum4(aY_d+bK_d)/d. Then

    f(a,b)=A a^4 + B a^3b + C a^2b^2 + D ab^3 + E b^4,

    A=87518285/21743271936
    B=89759141/5435817984
    C=1656329771/65229815808
    D=35360777/2038431744
    E=434651857/97844723712.

The full symmetric five-component tensor is YYYY=87518285/21743271936, YYYK=89759141/21743271936, YYKK=1656329771/391378894848, YKKK=35360777/8153726976, KKKK=434651857/97844723712. The final pure gate term matches PREFIX577-R2; YYKK>0.

## Proof
For a rational direction (a,b), use the original 576 native labeled edges i→j with observer weight w=aM(e)+64b g(e). Define the 96×96 rational Taylor coefficient matrices T_k[i,j]=Σ_(e:i→j) w(e)^k/(6 k!), k=1,2,3,4, and P=T_0. This is a moment-generating observer of the original discrete BRC paths, not a replacement for original BRC arithmetic. The finite P is irreducible with uniform stationary π=(1/96,...,1/96). Thus Z=I-P+1π is invertible. Although the chain has period 2, the cyclic parity block decomposition gives a nonzero locally analytic leading prefactor in each parity subsequence; all fixed-order normalized log-MGF derivatives equal the derivatives of log of the simple positive Perron eigenvalue λ(t) near 0.

Normalize λ=1+Σ_(j≥1) l_j t^j and v=1+Σ_(j≥1)v_j t^j with πv_j=0. Direct coefficient comparison of T(t)v(t)=λ(t)v(t) yields exact recursion

    u_j=Σ_(k=1..j) T_k v_(j-k);
    l_j=πu_j;
    Z v_j=u_j-l_j 1-Σ_(k=1..j-1) l_k v_(j-k),   j=1..4.

Every equation is verified exactly in rational arithmetic for the selected directions. The quartic rate is

    [24l4 -24l1 l3 -12l2^2 +24l1^2 l2 -6l1^4]/64^4.

This gives six exact directional results:
f(1,0)=87518285/21743271936,
f(0,1)=434651857/97844723712,
f(1,1)=3312980315/48922361856,
f(1,-1)=-1519/48922361856,
f(1,2)=68192216129/195689447424,
f(1,-2)=952746353/195689447424.

The first five determine the degree-four homogeneous form uniquely. Let A=f(1,0), E=f(0,1), u+=f(1,1)-A-E, u-=f(1,-1)-A-E, u2=f(1,2)-A-16E. Then C=(u++u-)/2, V=(u+-u-)/2, D=(u2-4C-2V)/6, B=V-D. Substitution produces the five displayed rational coefficients. An independent sixth direction exactly verifies f(1,-2)=A-2B+4C-8D+16E. Mixed components follow by dividing B,C,D by multinomial factors 4,6,4. Exact root-gauge conjugacy from prior PREFIX577 guarantees the equal limiting cumulants for all nine frozen roots. QED.

## Reproduction and verification
The original local exact SymPy rational 96×96 perturbation program and separate full-96-port integer raw-moment DP completed with ALL_ASSERTIONS_PASS. Six rational directional calculations checked all normalized eigenvector equations. The pure Y computation checked second and third cumulants against canonical previous fractions. The integer DP independently propagated moments of degrees 0..4 through all 576 labeled edges for d=1,2,4,8,16,32,64,128; at d=128 the displayed Cum4(Y)/d is 0.004024753049. That finite-depth check tests the recurrence implementation; the spectral proof gives the limit. Executed local raw programs/results are preserved in the accompanying local research bundle; this branch also provides relative-import versions with the pinned native kernel from PREFIX579.

Provenance: canonical PREFIX577-R6 six-axis covariance and beta, canonical PREFIX578-R6 six-axis cubic tensor, PREFIX577-R2 gate fourth, PREFIX579-R2 R5/R6/K quartic on branch 6bb5b7f95295f0ebaffbdaf4301ae348db6b7a86. Native EM identity/Owner/CLAIM/Result/activity unconfirmed: status endpoint returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. GitHub author-side research persistence is not independent review or theorem admission.

## Next
Calculate the complete fourth-order (R1,...,R6,K) tensor on original 96 native ports. First demand its (R5,R6,K) principal subtensor match nine PREFIX579 rational classes; then contract the entire tensor with beta to reproduce the five (Y,K) classes. Preserve the six native axes and the original science pin.
