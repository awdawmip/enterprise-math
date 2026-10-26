# N=3 BRC auxiliary model: sharp universal likelihood-ratio root-masking region

2026-10-26. AUTHOR-LEVEL theorem (not independently reviewed or native Result).
GLOBAL_KNOWLEDGE_V1 source: awdawmip/chatgpt-global-knowledge@2e711e9f23ebe815597ac7b228679cdc8bcdeb63.
Enterprise Math source read: awdawmip/enterprise-math@b03d306acf9763f8db33e09d9fd434f35e4640fd.
Predecessor: research_notes/brc_lr_n3_any_kernel_root_masking_20261026_r5/PROOF.md, immutable source commit 243f8aeb68c7c24b36a0ba5775cb8f4806b70d78.

## Complete statement

In the predecessor's external finite Bayesian model, two time-1 histories a,b each have P=Q probability 1/2 and likelihood ratio 1. At time 2, exact likelihood ratio r ranges through (1/2,1,3/2). Under Q, the conditional rows are (alpha,1-2alpha,alpha) and (beta,1-2beta,beta); under P, each component is multiplied by r. Assume 0<alpha<=beta<1/2. For each r, any finite positive-support terminal Q kernel mu_r is allowed, satisfying E_mu_r[Y]=r, with P transition Y mu_r(Y)/r. Strategies can stop and decide at times 0,1,2 and must decide at 3. The four observers are (P(decide Q), Q(decide P), E_P tau, E_Q tau).

THEOREM. The full-history and (time,current exact LR)-only randomized-policy four-observer attainable sets coincide for EVERY such terminal kernel if and only if

    beta <= 3 alpha    AND    3 beta - alpha <= 1.

The boundaries are included. If either bound fails, one strictly positive mean-preserving finite terminal experiment and one signed rational linear observer objective (rational when alpha,beta are rational) yield a strictly positive minimum gap. This is a theorem about the stated external finite observer family, not about native P000/X6/Heartbeat dynamics or safe erasure for other future operations.

## All-real Bellman proof of sufficiency

Fix arbitrary real A,B,C,D, and minimize J=A e_P+B e_Q+C E_P tau+D E_Q tau. Write H(r)=min(Ar,B), m=H(1), gamma=C+D, and

    phi(r)=min(H(r), Cr+D+E_mu_r[H(Y)]),
    d0=m-phi(1)>=0,
    G=2phi(1)-phi(1/2)-phi(3/2),
    da=d0+alpha G, db=d0+beta G, dbar=(da+db)/2.

These are exact Q-mass Bellman values, using the fact that the terminal kernel depends only on current r. Because H is concave and phi<=H,

    G >= 2phi(1)-H(1/2)-H(3/2) >= -2d0.

At the root, allowing immediate stopping, exact minima are

    V_full=m+min(0,gamma-((da-gamma)_+ +(db-gamma)_+)/2),
    V_LR=m+min(0,gamma-(dbar-gamma)_+).

If G>=0, then dmin=da>=0 and
    2dmin-dbar=d0+(3alpha-beta)G/2>=0.
If G<0, then dmin=db>=(1-2beta)d0>=0 and
    2dmin-dbar=d0+(3beta-alpha)G/2 >= (1-3beta+alpha)d0>=0.
When gamma<=dmin, the positive parts are affine and the two root values coincide. When gamma>dmin>=0, the mean of the full-history positive parts is at most dbar-dmin<=dmin<gamma; the compressed positive part is no larger by convexity. Both root values equal m. Thus V_full=V_LR for EVERY real coefficient quadruple and EVERY permitted terminal kernel.

Finite randomized occupancy-flow images are compact convex polytopes. The LR-only image is included in the history image (its Q node-flow under P is r times its Q flow). If the images differed, strict convex separation would produce an all-real linear objective with unequal minima, which we just ruled out. Therefore every full-history randomized strategy has an LR-only randomized strategy with exactly the same four observers.

## Necessity I: beta>3alpha

Select alpha<gamma<beta/3, put A=B=2,C=0,D=gamma, epsilon=gamma/2. At every r set Q(Y=r-epsilon)=Q(Y=r+epsilon)=1/2. All Y and induced P probabilities are strictly positive; E_Q Y=r. Since H(r)=min(2r,2), the largest terminal information gain is epsilon<gamma (only at r=1), so phi(r)=H(r). Consequently m=2, d0=0, G=1, da=alpha, db=beta.

The full-history optimum continues from the root and at time 1 selectively continues only after b, giving
    V_full=m+(3gamma-beta)/2<m.
The LR-only optimum has
    V_LR=m+min(0,2gamma-(alpha+beta)/2).
If the LR root stops, the strict gap V_LR-V_full=(beta-3gamma)/2>0. If it continues, the strict gap is (gamma-alpha)/2>0. Hence every beta>3alpha violates universal preservation. For rational alpha,beta choose rational gamma and epsilon.

## Necessity II: 3beta-alpha>1

Because beta<1/2, select
    1-2beta < gamma < (1-2alpha)/3.
Set A=8(1+gamma), B=2A, C=0, D=gamma. H(r)=Ar for r=1/2,1,3/2. At r=1/2 and 3/2 use Q(Y=r-1/100)=Q(Y=r+1/100)=1/2; both leaves are below the H kink at Y=2, so the information gain is zero. At r=1 use Q(Y=1/2)=3/4 and Q(Y=5/2)=1/4. This is positive and mean preserving, E H(Y)=7A/8, and the information gain is A/8=1+gamma. Therefore phi(1)=H(1)-1 and phi at either endpoint equals H. Thus
    m=A, d0=1, G=-2, da=1-2alpha, db=1-2beta.
The chosen interval is exactly db<gamma<da/3. The full-history optimizer selectively continues only after a and has
    V_full=m+(3gamma-da)/2<m.
The LR-only value is
    V_LR=m+min(0,2gamma-(da+db)/2).
Its strict excess over V_full is (da-3gamma)/2>0 if its root stops, and (gamma-db)/2>0 if its root continues. Hence every 3beta-alpha>1 violates universal preservation, with rational data for rational alpha,beta.

Together the preceding sufficiency and the two constructive necessity cases prove the stated equivalence for ALL 0<alpha<=beta<1/2. The terminal kernels in both cases have positive Q support, positive induced P probabilities and correctly normalized means. No finite grid was used to infer the all-real statement.

## Exact independently recomputed rational examples

1. alpha=1/12,beta=1/3,A=B=2,C=0,D=5/48; each mu_r is equally weighted at r±1/100. d0=0,G=1,da=1/12,db=1/3. V_full=191/96,V_LR=2,gap=1/96.
2. alpha=1/4,beta=9/20,A=46/5,B=92/5,C=0,D=3/20; endpoints as above and mu_1 gives Q masses 3/4 at Y=1/2 and 1/4 at Y=5/2. d0=1,G=-2,da=1/2,db=1/10. V_full=367/40,V_LR=46/5,gap=1/40.

See VERIFY_SHARP_REGION.py and EXACT_CHECK_OUTPUT.txt: Python Fraction checks positive Q/P normalization and computes Bellman values directly for the two examples. It is a focused rational cross-check, NOT an exhaustive test over all real parameters/kernels. The universal theorem is the algebra above, at author-level, pending independent mathematical review. The observable/horizon-bound safe quotient does not discard BRC history/provenance for other observers.

Next: constructive rational occupancy-flow lifting in the safe region; determine a minimal typed path/branch repair beyond the sharp boundary.
