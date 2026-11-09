# PREFIX-626 — Sharp growing history-deficit theorem for the native X6-BRC four-point probe

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT MATHEMATICS / INDEPENDENT REVIEW PENDING.
Task line: RS-X6-NATIVE-ROTATION-DYNAMICS. Frozen native science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
This study uses the original 48 STAR phases, 96 two-bit ports and all 576 source/action-labelled positive BRC transitions; no ordinary propagation, classical trigonometry, matrix exponential or phase-cancellation substitute.

## 1. Problem and observer class

Let d=e4+e11+e14+e32 be the fixed native positive phase probe with its original 96-port embedding E(d). Let lambda>0 and g1,...,gn>=0 be entirely unknown. The original native terminal state is

\[
r_n=A(g_n)\cdots A(g_1)E(\lambda d).
\]

An observation supplies all 96 terminal port values plus m selected **coordinates of the fully ordered, source/action-labelled length-n native positive-path tensor**. Each additional coordinate equals one specified initial source-port mass times the product of all the typed action weights along that path. All scalar readings are exact nonnegative real numbers. Find the smallest m needed to reconstruct lambda and all n gates (hence the entire labelled tensor) uniformly. Retrospective path-coordinate queries are different from current-state-only phase or port sensors.

## 2. Theorem: exact minimum for every n>=5

\[
\boxed{m_{\rm extra}(n)=n-5 \qquad(n\ge5).}
\]

The terminal native 96-port state uniquely determines lambda, four mod-4 products of shifted gate parameters, and the last gate gn. Exactly n-5 additional labelled path coordinates suffice to reconstruct the remaining individual gates; fewer continuous scalar labelled-path readings cannot suffice on the positive open input domain. At n=5 no extra path coordinate is needed. At n=6 precisely one is needed. This is an all-finite-horizon statement for the original positive typed X6-BRC operator.

### 2a. Construct one original labelled path reading lambda*gk at every gate index

The original phase STAR triples are
(1,3,6), (1,4,5), (2,3,5), (2,4,6).
Using the frozen action rule, the unique gated edge chosen here is original source port 9 -> destination port 29, carrying the native label (i,j,u,v)=(14,4,1,1). It has weight exactly gk at step k. The other following edges have native constant weight one.

For any k>=1 write s=(k-1) mod 4. A gate-free positive seed-to-port-9 path of length s is:

s=0: 9;
s=1: 22 -> 9;
s=2: 64 -> 52 -> 9;
s=3: 28 -> 80 -> 52 -> 9.

Append (k-1-s)/4 copies of the original weight-one cycle
9 -> 28 -> 80 -> 52 -> 9.
Every listed seed port 9,22,64,28 initially holds exactly lambda under E(lambda d).

The assembled prefix ends at port 9 after k-1 actions. Take the gated action 9 -> 29 at step k, then append the first n-k edges of the second original weight-one cycle
29 -> 80 -> 52 -> 8 -> 29, repeated when necessary.
This specifies a **fully labelled genuine native length-n path W(n,k)**, containing only the one gate factor gk. Hence the exact identity

\[
\boxed{J_n[W(n,k)]=\lambda\,g_k,\quad 1\le k\le n,}
\]

including gk=0. The positive gate-free cycle from seed 28 provides, for every n, a separate labelled reference path with mass lambda. Four short seed paths, two fixed original cycles, and the explicit gated action are finite certificates establishing the identity for every finite n.

### 2b. Decode six coarse quantities from the original native endpoint

For n>=2 set t=n-2 and aggregate the final ports into native phase values v: for i!=4, v[i]=r[2i]+r[2i+1]; for phase i=4, v[4]=r[8]=r[9]. Use the original author-side PREFIX-617 eight-state identity, verified separately at commit 00cdf3bcbea94aaa623e8b3e969f2354a5bfd21e:

\[
v=H_C(2P_4)^t c_0+H_B w_t,\qquad
c_0=\lambda(0,0,4,4)^{T},\qquad
w_0=\lambda(g_2+3,g_1+3,1,1/2)^{T}.
\]

Here P4 cyclically shifts a 4-vector by one position, and each further native gate step sends w[j] to w[(j+1) mod 4], multiplying by 4(g+3) when wrapping from j=3 to j=0.

The four pure H_C phase rows, with no H_B component, are rows (2,28,38,16) for columns (0,1,2,3) respectively. Let p=(2,28,38,16). It follows that

\[
\boxed{\lambda=\frac{v[p((t+2)\bmod4)]}{4\,2^t}.}
\]

The four pure H_B rows, all H_C-free, are phases (14,40,26,4), yielding

\[
w_t=(v[14],v[40]/2,v[26]/4,v[4]/4)^{T}.
\]

Define four strictly positive products

\[
\Pi_r=\prod_{\substack{1\le k\le n\\k\equiv r\pmod4}}(g_k+3),\qquad r=0,1,2,3.
\]

Let initial token indices j0(0)=2,j0(1)=1,j0(2)=0,j0(3)=3, initial token factors b0=b1=b2=1 and b3=1/2, and h_r=#\{k:3<=k<=n, k mod4=r\}. Following the original monomial gate cycle gives

\[
\boxed{\Pi_r=
\frac{w_t[(j_0(r)+t)\bmod4]}
{\lambda\,b_r\,4^{h_r}}.}
\]

All denominators are positive for the declared input domain.

The original current-port decoder from PREFIX-622 reconstructs the final gate directly. Set
delta=r[29]-r[28] and L(v)=v[3]+v[14]+v[15]-2v[2]. For this original four-point reachable tail at n>=2,

\[
\delta=\frac{(g_n-1)L(v)}{3(g_n+3)},\qquad L(v)>0.
\]

Therefore

\[
\boxed{g_n=\frac{L(v)+9\delta}{L(v)-3\delta},}
\]

with positive denominator. These original endpoint identities give the six-scalar summary
(lambda,Pi0,Pi1,Pi2,Pi3,gn).

### 2c. Exact construction attaining n-5 extra readings

For n>=5, choose the fixed, parameter-independent list of n-5 labelled paths

\[
W(n,k),\qquad k=5,6,\ldots,n-1.
\]

Read their masses and divide by recovered lambda. The path identity yields g5,...,g(n-1). The final endpoint supplies gn. For each i=1,2,3,4 recover the one remaining gate in residue class i mod4:

\[
\boxed{g_i=
\frac{\Pi_{i\bmod4}}
{\displaystyle\prod_{\substack{5\le k\le n\\ k\equiv i\pmod4}}(g_k+3)}
-3.}
\]

No zero denominator is possible, even if one or more gates equal zero. Every gate and lambda are now uniquely recovered, so any requested labelled path mass is calculated by following the original native edges and multiplying the known weights.

### 2d. Sharp lower bound

Restrict to the open domain lambda>0 and g1,...,gn>0 in R^(n+1). The *complete* original labelled-path tensor is injective on this domain: one gate-free path reads lambda, while n paths W(n,k) read lambda*gk. The original 96-port endpoint factors continuously through the six scalars (lambda,Pi0,Pi1,Pi2,Pi3,gn), by the exact eight-state and final-port decoder identities. Any selected m labelled path-coordinate readings are also continuous real functions of the unknown inputs.

If m<n-5 and the terminal state plus those m readings sufficed to reconstruct all path masses, the combined continuous map from an open subset of R^(n+1) into R^(6+m) would have to be injective. This contradicts invariance of domain for 6+m<n+1. The argument allows even nonlinear or discontinuous **decoders**, since the measured original path coordinates themselves are continuous. Thus m>=n-5, matching the construction. It does not restrict arbitrary nonphysical encodings of a complete history into a single real.

## 3. Difference from PREFIX-625

PREFIX-625 proves 48 supplementary predecessor-port linear readings are required to restore all ordered labelled paths for an *arbitrary* nonnegative 96-port predecessor with a *known* gate sequence. Here the predecessor is the fixed original four-point input; lambda and all gates are *unknown*, and supplementary readings are retrospective *path-coordinate* measurements. The restricted input family has only six endpoint-identifiable continuous parameters, while all fully labelled histories contain n+1. The deficit therefore grows exactly as n-5, even though the endpoint's linear-state image is rank 16 under PREFIX-625's more general source class. These are separate, compatible observation questions.

## 4. Original native exact validation

Companion independent original-native checker PREFIX626_native_history_recovery_checker.py enumerates the original 48 STAR phases, all 96 ports and all 576 labelled typed native actions. Python fractions.Fraction arithmetic was used to verify every path W(n,k) against the actual original weight rule for all 1<=k<=n<=64 (2080 path positions) and the same witness under zero gate inputs, plus the gate-free reference path at every tested horizon. The full 96-port original evolution and both decoders were then tested with exact nonnegative rational inputs in 27 cases across n=5,6,7,8,9,12,16,24,32, recovering every gate and lambda exactly. All local assertions passed. Arbitrary-horizon validity follows from the native-cycle identities and exact algebraic inverse, not from extrapolating the 27 cases.

Original science frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. Earlier author-side math dependencies at PREFIX-617, PREFIX-622, PREFIX-625 remain subject to independent Driver review. This result is a new, separable author-side theorem, not a Native Result/CLAIM/Working Truth promotion.

## 5. Next exact research question

Find the minimum total-cost **online** native memory/measurement method for capturing these n-5 provenance coordinates without expanding the full length-n path tensor. Compare gate-history input recording, tagged-path access, bit complexity, preprocessing, output decoding and complexity against retaining the original gate sequence. Explore bounded retrospective lag queries where a constant-memory sufficient observer may exist.

Researcher provenance: EM-X6-A6B28D; native research activity RA-148756C3B729A3D05A529B3B. Task RS-X6-NATIVE-ROTATION-DYNAMICS is independently registered as READY/NEEDS_DISPATCH, owner taskbook/unassigned at the native query of 2026-11-09; no formal CLAIM issued in this author-side work.
