# R124.2 — Three-integer relative-phase refinement (sharper than R124.1)

Date: 2026-11-13 (Asia/Shanghai). This refinement uses exactly the original directed positive half-open S23 arc from R118, including the convention that coincident endpoints define the empty arc. It improves the R124.1 four-integer lift in [PROOF.md](PROOF.md); the original result remains valid and is retained for provenance.

## Main identity: rotate the arc, not the two endpoint floors

For every real \(Y,A,C\), with \(\operatorname{frac}(x)=x-\lfloor x\rfloor\),

\[
\boxed{\quad
\operatorname{frac}(Y)\in
[\operatorname{frac}(A),\operatorname{frac}(C))_{\mathrm{directed}}
\iff
0\le\operatorname{frac}(Y-A)<\operatorname{frac}(C-A).
\quad}
\]

Proof: rotation of the oriented unit circle by \(-A\) maps the original directed arc exactly to the half-open arc starting at 0 and ending at \(\delta=\operatorname{frac}(C-A)\). The original starting point is included, ending point excluded. If the endpoints coincide, \(\delta=0\) and \([0,0)\) is empty. This handles wrapping, signed coefficients and endpoint coincidences without a case distinction.

For the S23 predicate at time \(t\), set \(Y=x+(t-j)\theta\), \(A=a\theta\), \(C=c\theta\). Thus

\[
\boxed{
M_t(\theta)=
{\bf1}\left[
\operatorname{frac}\big(x+(t-j-a)\theta\big)
<
\operatorname{frac}\big((c-a)\theta\big)
\right].
}
\]

Both sides have an implicit nonnegative fractional part. **The original six-affine-phase auxiliary observer is preserved pointwise**, not merely almost everywhere.

## Three-integer theorem

Fix any rational open \(J=(l,h)\), rational \(x\), integers \(N,j,a,c,d\) with \(d\ne0\), \(m\ge2\), and requested bits \(b_0,\ldots,b_{m-1}\) at times \(t_i=N+id\).

For \(\theta\in J\), introduce **three** integer variables

\[
n=\lfloor x+(N-j-a)\theta\rfloor,\qquad
k=\lfloor d\theta\rfloor,\qquad
p=\lfloor(c-a)\theta\rfloor.
\]

Let \(\alpha=x+(N-j-a)\theta-n\), \(\beta=d\theta-k\), \(\delta=(c-a)\theta-p\), and choose a finite mechanical word \(q=(q_i)\in P_m\), where \(q_i=\lfloor\alpha+i\beta\rfloor\). Define

\[
z_i=x+(N+id-j-a)\theta-n-ik-q_i.
\]

The prescribed pattern is attainable on \(J\) **if and only if** at least one \(q\in P_m\) makes the following single conjunction feasible with real \(\theta\) and integers \(n,k,p\):

\[
\begin{gathered}
l<\theta<h,\quad 0\le\beta<1,\quad 0\le\delta<1,\quad
0\le z_i<1\quad(\forall i),\\
z_i<\delta\quad(b_i=1),\qquad
z_i\ge\delta\quad(b_i=0).
\end{gathered}
\]

There is **no arc-order disjunction and no per-bit segment disjunction**. The expression \(z_0\in[0,1)\) enforces the floor of the shifted base phase, while all other \(z_i\) enforce the same shared \(\alpha,\beta\) mechanical lift. Conversely every feasible solution has the correct original fractions and bits. Each system consists only of rational-affine strict/weak inequalities in one real and three integer variables. Eliminate the real \(\theta\) by exact lower/upper endpoint comparisons as in R123 and R124.1, respecting weak/strict facets. A feasible three-dimensional integer point gives a rational \(\theta\) (midpoint for unequal bounds; equality when both bounds are weak).

**Cost:** For a *fixed* requested \(m\)-bit pattern, at most \(|P_m|=\Theta(m^3)\) three-integer linear feasibility calls, each with polynomially many constraints and polynomial coefficient bit growth in the binary length \(B\) of the original rational/integer input. A classical fixed-dimensional integer-programming algorithm gives total \(O(m^3\operatorname{poly}(m,B))\) bit complexity, with no factor proportional to \(|a|,|c|,|N|,|d|\). All patterns may be enumerated using an additional \(2^m\) output-related factor. Individual disconnected parameter components can be numerous and are not requested by this signature oracle.

This is a sharper dimension/branch bound than R124.1's four-integer \(3\cdot 2^m|P_m|\) feasibility alternatives. It also extends R123's two-integer specialization \(a=j=0,c=1\) to arbitrary signed \(a,j,c\) without a scan of endpoint-floor cells. For an old signature partition, run on each open old atom and test isolated rational boundary atoms directly; retain the old full provenance and ranking roots.

## Executed verification

The standard-library Python file [check_r124_relative.py](check_r124_relative.py) imports the affine, interval, exact-circle and independent phase-cut primitives from [check_r124.py](check_r124.py). It exhaustively scans the three floor variables only for *small validation instances*, checks all bit patterns, and independently compares to full six-phase point/open-gap atomization.

Executed result: \`R124_RELATIVE_3D_PASS\`; seed 1242026, 87 cases, 532 complete bit-pattern tests, 412 attained signatures, and 2,229 tested three-integer arc-conjunction candidates. Two signed huge-coefficient positive certificates check the original arc bits and the three-integer fractional identities with 101/111-digit base time and 91/106-digit spacing for \(m=4\). See [verification_r124_relative.json](verification_r124_relative.json). This check validates the finite lifting implementation, not the theoretical fixed-dimensional polynomial-time solver's practical performance.

## Next

R125: implement a genuinely large-coefficient three-integer feasibility engine and an exact projection witness extractor, benchmark against R123 floor-sum in the common domain, and test whether resonant parameters \((c-a)=\pm d\) admit a true two-integer subfamily. Preserve P000, signed branch provenance and the auxiliary-versus-native operator boundary.

Status: author-side proved exact reduction and finite exact cross-check; independent mathematical review pending. No CLAIM or native X6 event authorization follows from this note.
