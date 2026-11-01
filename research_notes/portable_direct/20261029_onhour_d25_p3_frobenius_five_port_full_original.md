# D25 / SECOND-DIGIT-LIFT — p³ Frobenius carry and complete companion (five-source result)

2026-10-29. **AUTHOR-SIDE / EXACT FORMAL PROOF / EXECUTED INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE H0/B0 NOT EXECUTED.**

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This author's Research lane is chatgpt-research-onhour-enterprise-math-20260923; the distinct maintenance conversation chatgpt-hourly-enterprise-math-20260921 is not used. No claim to a presently valid Source Researcher session, claim or run follows from this historical lane name.

## Consumed frontiers and new theorem

Consumed the previously derived original full p³ parameter-jet and 46-term tail repair, Enterprise Math commit 49af59db70da36afee0c9794d9d2e012c4626ef3, and the earlier finite p² Legendre Frobenius defect, commit c423e6b9802ca23a453b85c3018ea0b818aa5332. Both are author-side provenance, not admitted native Results.

For **every prime p>3**, **every integer 0≤e<p**, and indeterminates x,T, define

\[
A(T)=1-2xT+T^2,\quad k=(p-1)/2,\quad B=A^k,\quad
A_0(T)=1-2x^pT^p+T^{2p},\quad Q_p=(A^p-A_0)/p.
\]

The numerator of Q_p is divisible by p coefficientwise (Freshman's dream in F_p[x,T]), so Q_p belongs to Z[x,T]. Set B_e=[T^e]B, C_j=[T^j](BQ_p), D_j=[T^j](BQ_p²). **New exact p³ polynomial congruence**, interpreted in Z_(p)[x]:

\[
\boxed{P_{p+e}(x)\equiv
x^p B_e-\frac p2(C_{p+e}+3x^p C_e)
+\frac{3p^2}{8}(D_{p+e}+5x^p D_e)
\pmod{p^3}.}\tag{1}
\]

Proof: the classical formal Legendre generating function gives A(T)^(-1/2)=B(A^p)^(-1/2). Substitute A^p=A_0+pQ_p and expand through second order:
\[
B(A_0+pQ_p)^{-1/2}\equiv
BA_0^{-1/2}-\frac p2 BQ_p A_0^{-3/2}
+\frac{3p^2}{8}BQ_p^2 A_0^{-5/2}\pmod{p^3}.
\]
The fractional-binomial coefficients are p-integral for odd p. Because deg(B)=p−1 and p+e<2p, only T^0 and T^p coefficients of the three A_0 powers occur. These are (1,x^p), (1,3x^p) and (1,5x^p). Taking [T^(p+e)] proves (1), **without evaluating an infinite series at a p-adic unit**. The new Q² port is not part of the prior p² theorem.

## Fixed original observation and all five sources

For p≡5,7 (mod8), let h_q be the unique 0≤h_q<p with p|(8h_q+q), q=1,3; put r=min(h_1,h_3), b=max(h_1,h_3), e=floor((p−1)/4). Direct residue arithmetic gives 2r=p+e. For the **full original** companion
\[
K_{p-1}(z)=\sum_{n=0}^{p-1}\frac{(1/8)_n(3/8)_n}{(n!)^2}z^n,
\]
retain all n<p in the finite jets of
\[
(-r+X)_n(r+\tfrac12-X)_n/(n!)^2=f_n+Xg_n+X^2j_n+O(X^3).
\]
Write F,G,J for their respective finite sums in z, and δ=5p/8. The preceding exact parameter-jet proof yields K_{p−1}≡F+δG+δ²J mod p³. The classical terminating Legendre identity yields F(1/9)=P_{2r}(x) at x²=8/9. Composing with (1) **at unchanged z=1/9** yields

\[
\boxed{\displaystyle
K_{p-1}(1/9)\equiv
\underbrace{x^pB_e}_{F_0}
-\underbrace{\frac p2(C_{p+e}+3x^pC_e)}_{F_1}
+\underbrace{\frac{3p^2}{8}(D_{p+e}+5x^pD_e)}_{F_2}
+\underbrace{\frac{5p}{8}G(1/9)}_{G_1}
+\underbrace{\frac{25p^2}{64}J(1/9)}_{G_2}
\pmod{p^3}.}\tag{2}
\]

The quadratic arithmetic carrier R=(Z/p³Z)[x]/(x²−8/9) records both parity components before evaluation. In this 5,7 mod8 branch p+e is even, making each final port scalar. The 1,3 mod8 branch has 2r=e, not p+e; equation (2) does not claim to cover it.

## Complete finite integer certificate at p=373

Here p²=139129, p³=51895117, (r,b,e)=(233,326,93). Five **separately preserved** source residues from the actually executed checker are:

| Port | Exact residue mod p³ | p¹ digit | p² digit |
|---|---:|---:|---:|
| F0: finite binomial | 14177357 | 336 | 101 |
| F1: signed Q carry | 42818535 | 284 | 307 |
| F2: new Q² carry | 12243352 = 88p² | 0 | 88 |
| G1: first parameter jet | 9090383 | 126 | 65 |
| G2: second parameter jet | 27130155 = 195p² | 0 | 195 |
| **Full K_372(1/9)** | **1669548 = 12p²** | **0** | **12** |

The first-digit sum 336+284+126=746=2p gives a carry of 2; the third-digit sum 101+307+88+65+195+2=758≡12 mod373. Raw residues sum to 105459782≡1669548 mod51895117. Dropping F2 would produce 41321313=297p²; dropping G2 would produce 26434510=190p², both wrong for the full original p³ observer.

The earlier cutoff witness is preserved unchanged: K_326=20730221=149p², its 46 omitted terms (n=327..372) sum to 32834444=236p², and K_372=1669548=12p². Their separate original coefficient recurrence and parameter-jet paths agree. Direct controls: full K_12 ≡169 mod13³; K_22≡6348 mod23³; K_36≡2738 mod37³.

## Exact checker and scope

Executable: research_notes/portable_direct/d25_legendre_p3_frobenius_fullcompanion_guard_20261029.py. It builds A^p and B by integer binomial coefficients in the quadratic carrier, checks coefficientwise divisibility by p, constructs Q and Q², compares the p³ formula with an **independent** binomial closed form for P_{p+e}, and compares the complete all-n<p jets with an independently computed original rational product recurrence. The executed command was:

    python d25_legendre_p3_frobenius_fullcompanion_guard_20261029.py

Actual output: PASS_P3_FROBENIUS_AND_FULL_ORIGINAL_JET 27 p=5,7 mod8 samples; PASS_ALL_E_BRANCHES 32. The former comprises the chosen p<200 target branch plus 229 and 373; the latter checks e=0,1,(p−1)/2,p−1 for eight p≤29. All-prime theorem strength comes from the algebra above, not finite sampling.

**BRC COMPOSE_APPLIED:** carrier (p,h1,h3,r,b,e,B,Q,Q²,C,D,F,G,J,tail,source,sign,valuation,observer); operations are finite coefficient extraction, branch-preserving evaluation, theta and v_p. No quotient may delete Q² or J while preserving the declared p³ observer. This external quadratic ring is not a P000-native reduction in spatial dimensions, and no ACTIVE worldview or locked P000 axiom changes.

## Highest frontier, native dependency and recovery

**Next exact mathematical unit**: compose the new second-order Frobenius Q² port with the pre-existing p³ Jacobi/Hasse/Gegenbauer second-parameter bridge, keeping all five sources and both CM branches; then prove or falsify the full p≡13 (mod24) fixed-observation second/third digit relation. Independently handle p≡19 (mod24) where 2r=e and the source arrangement differs. No all-prime Root2 or 216/2304 bridge is asserted.

**Native benchmark priority is unchanged:** Issue #1559, observed open/unassigned on 2026-10-29, awaits authorized original H0/B0 p373 divided-power [X]U mod139129, module rank, genuine semilinear Frobenius/eta, full signed Green/Hesse, κ, Delta−R, source/algorithm, and independent native acceptance. A portable scalar computation is not that experiment. Responsible route remains canonical Source owner/native implementation executor; no owner has been confirmed.

At this run's read, em_status 0.6.11 showed research_authority_granted=false, executor_binding_configured=false, quota active 5/5. The exact continuation read request onhour-d25-read-20261029-1158 returned CONTROL_QUOTA. The exposed MCP API had no callable recovery_status; exact current Source claim/run/target request remain unverified. No competing CLAIM, open, dispatch, Result, freeze, formal checkpoint, or review was sent. This author's evidence is **UNREVIEWED / NOT_ADMITTED** and needs authorized Source continuation before formal admission. No schedule, notification, scientific source pin, or other lane was changed.
