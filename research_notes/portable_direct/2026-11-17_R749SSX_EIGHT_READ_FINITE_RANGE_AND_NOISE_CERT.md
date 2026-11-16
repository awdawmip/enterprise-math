# R749SSX — Eight-read finite-range separation and explicit robust recovery floor

**Research date:** 2026-11-17. **Evidence level:** \`AUTHOR_EXACT_NOT_REVIEWED\` (finite exhaustive modular certificate and exact algebraic proof). **Research scope:** independent portable research, not a native X6 theorem or shared CLAIM.

**Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Reused results: R749SST (11-read global identifiability), R749SSU (finite inversion), R749SSV (six-phase envelopes), R749SSW (known-cutoff two-read inversion, commit \`3d64907aa39a198853132a43586b4cbc15732bb0\`). Existing review states are unchanged.

## Exact definitions and result

Keep the five *distinct labeled* nonnegative integer sources of weights \((1,1,2,3,6)\). For integers \(n\ge6\), define

\[
\Omega_n=\{(k_1,\ldots,k_5)\in\mathbf Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad
C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]

Let \(S(n)=18n^4+54n^3-345n^2+2070n-16315\), and let
\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108},\quad(e,d)\in[-2,2]^2.
\]
Within each candidate state, \((e,d)\) is *the same* across all readings. Between different candidate cutoff values independent errors are allowed. Define
\[
\mathcal O_q^{(8)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{7}.
\]

**Theorem A — finite-range eight-read exact identification.** For all distinct integers \(6\le q,p\le1000\), and all real \(e,d,E,D\in[-2,2]\),
\[
\boxed{\mathcal O_q^{(8)}(e,d)\ne\mathcal O_p^{(8)}(E,D).}
\]
The universal quantifiers over all continuous errors are settled algebraically, with an exhaustive exact modular determinant certificate for all \(\binom{995}{2}=494515\) unordered cutoff pairs. This improves the previously known uniform 11-read sufficient count on this *bounded* cutoff domain. No optimality or unbounded-cutoff eight-read theorem is asserted.

**Theorem B — explicit uniform finite-range noise separation.** Set \(A=1042\), \(C_*=C_A\), \(T_*=T_A\), \(R=A^3\),
\[
B=18A^4+54A^3+345A^2+2070A+16315,\quad D_s=2B,
\]
\[
M=216RT_*C_*+D_sC_*^2+108R(T_*+C_*+1)+D_s(C_*+1).
\]
For all candidate/error states in Theorem A,
\[
\boxed{
\|\mathcal O_q^{(8)}(e,d)-\mathcal O_p^{(8)}(E,D)\|_\infty
\ge\frac{1}{108\cdot8!\cdot(C_*+2)^2M^7}.
}
\]
Thus per-coordinate absolute measurement noise strictly below one half of this floor permits unique cutoff recovery within the specified range by testing candidate consistency. This universal numerical margin is intentionally conservative.

## Proof by integer linear lifting

For each reading index \(j=0,\ldots,7\), write \(a=q+6j\), \(b=p+6j\), \(\Delta S=S(a)-S(b)\). Multiplying the exact difference by positive denominators gives

\[
P_j=108(C_a+d)(C_b+D)\left(Y_a(e,d)-Y_b(E,D)\right).
\]

Expanding against the lifted vector \(z=(1,e,d,E,D,eD,Ed,dD)^\mathsf T\) yields a *linear* integer row

\[
\begin{aligned}
A_j=(&108(a^3T_aC_b-b^3T_bC_a)-\Delta S C_aC_b,\quad
108a^3C_b,\\
&-108b^3T_b-\Delta S C_b,\quad -108b^3C_a,\quad
108a^3T_a-\Delta S C_a,\\
&108a^3,\quad -108b^3,\quad-\Delta S).
\end{aligned}
\]

Assemble \(A\in\mathbf Z^{8\times8}\) from the eight rows, so \(Az=P\). Suppose eight readings collide. Then \(P=0\), hence \(Az=0\), where necessarily \(z_0=1\). Therefore **a nonzero determinant of \(A(q,p)\) suffices to rule out collisions for every admissible real error quadruple**. The lifted coordinates are not claimed independent physical variables; invertibility rules out the entire nonlinear state variety.

The finite exact certificate checks \(\det A(q,p)\bmod1000000007\ne0\) for every \(6\le q<p\le1000\). Since all matrix entries and determinants are integers, nonzero modular reduction proves \(\det A(q,p)\ne0\) over the integers, and hence over the reals. Swapping candidate order cannot create a collision. This proves Theorem A.

## Exhaustive provenance and reproducibility

The four labeled sources \((k_2,k_3,k_4,k_5)\), with weights \((1,2,3,6)\), have exact weight-count coefficients
\[
B_n=[z^n]\frac1{(1-z)(1-z^2)(1-z^3)(1-z^6)}.
\]
The full five-label combinatorial statistics satisfy
\[
C_q=\sum_{n=0}^{q-1}(q-n)B_n,\qquad
T_q=\sum_{n=0}^{q-1}\frac{(q-n)(q-n-1)}2 B_n.
\]
The Python 3 standard-library-only sibling certificate computes these counts by integer recurrences, forms all 8x8 matrices, and uses exact modular Gaussian elimination. It does not sample \((e,d,E,D)\), use numerical root finding, or depend on floating-point tolerances.

The full certificate returns:
- \`status=PASS\`;
- \`unordered_pairs_exhaustively_checked=494515\`;
- \`zero_mod_prime_count=0\` for prime \`1000000007\`;
- \`determinant_residue_stream_sha256=179093fbe41f7ab64af760c87f006c5b22c0bba89082e339a596435a15f76f31\`;
- minimum / maximum *nonzero* modular residue \`434\` / \`999998644\`;
- source witnesses \((C_6,T_6,C_{12},T_{12})=(41,50,380,881)\).

The checksum hashes the 494,515 sequential big-endian four-byte determinant residues, with outer loop \(q=6,\ldots,999\) and inner loop \(p=q+1,\ldots,1000\). A separate exact SymPy full-integer determinant check on \((6,7),(6,8),(7,9),(60,66),(500,501),(999,1000)\) matched the modular reductions; it is supplemental to full exhaustive coverage. To reproduce, run \`python3 R749SSX_EIGHT_READ_FINITE_RANGE_CERT.py\` and compare the reported deterministic fields to \`R749SSX_EIGHT_READ_FINITE_RANGE_RESULTS.json\`.

This is a finite, reproducible computer-assisted theorem conditional on correctly executing the inspection-ready integer code, currently \`AUTHOR_EXACT_NOT_REVIEWED\`.

## Proof of the noise floor

For all considered pairs and \(0\le j\le7\), both \(a,b\in[6,1042]\). Since \(C_n,T_n\) are nonnegative nondecreasing, \(C_n\le C_*\), \(T_n\le T_*\), \(a^3,b^3\le R\), and \(|\Delta S|\le 2B=D_s\) by a triangle bound on the signed polynomial coefficients. Every entry of the displayed \(A_j\) is bounded in absolute value by the stated \(M\).

Since \(A\) is a nonsingular integer matrix, \(|\det A|\ge1\). Every \(7\times7\) cofactor is bounded by the Leibniz estimate \(7!M^7\). For admissible errors the denominators are positive (\(C_6=41\)), and
\[
\|P\|_\infty\le108(C_*+2)^2
\|\mathcal O_q^{(8)}-\mathcal O_p^{(8)}\|_\infty.
\]
Since \(A^{-1}P=z\) and its first coordinate is exactly one,
\[
1\le\frac{8\cdot7!M^7}{|\det A|}\|P\|_\infty
\le 108\cdot8!\,(C_*+2)^2M^7\,
\|\mathcal O_q^{(8)}-\mathcal O_p^{(8)}\|_\infty.
\]
This proves Theorem B. Exact values are \(C_*=292621027685\), \(T_*=50963937031000\), \(M=7288917761105162353775610950356723274\). The denominator of the noise bound has 288 decimal digits; see the machine JSON for its full value.

## Scientific boundaries and next question

The exact counting population preserves five source labels, and the observation model preserves the within-candidate common error parameters. The lifting is an algebraic proof device, **not** a quotient of signed or provenance-sensitive BRC branch states. Neither P000/ACTIVE worldview nor canonical X6 Task/CLAIM/Review authority changes. The six-step observer is auxiliary scalar sampling, not an identified six-dimensional native physical-time increment. A native X6/BRC transfer requires an independently proved typed map preserving Cell/Link/Port, source and branch provenance, temporal order, observer fibers, residuals and the specified third coordinate of any 3D slice.

The next exact question is whether the eight-read determinant is nonzero for *every* distinct unbounded integer cutoff pair by exploiting six-phase quasipolynomial structure. A singular pair would require checking the actual nonlinear constraints before calling it a collision. Additional work: improve the coarse adjugate noise floor by exact pair-specific separation and find a constructive robust inversion procedure. Formalization is optional; mathematical independent review remains pending.
