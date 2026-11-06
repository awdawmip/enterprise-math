# PREFIX-534 — All 48 rooted BRC–gate series have one sharp common order-22 denominator

Date: 2026-11-06 (Asia/Shanghai). Research line: RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen **scientific** input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Current behavioral context: global canonical bootstrap and operating manual; Enterprise Math current P000/ACTIVE, research method and portable research protocol. These behavioral readings do not change the frozen science pin.
Precursors: PREFIX-525, 528 (unrooted denominator), 530 (49-dimensional lift), 532 (18 gate-only rooted laws), 533 (26 rooted joint-observer laws).
Status: AUTHOR_PROVED / EXACT_SPARSE_POLYNOMIAL_AND_MODULAR_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Mathematical question and exact scope

For the frozen four-STAR native X6 candidate, let its 48 signed directed phases be s=(STAR,previous,current), with each phase having exactly three next phases and each transition carrying two ordered and separately labeled INNER/OUTER microstep words. The gate H counts the word aAc via two successive INNER choices ending at T=(A,+L1,-L3). The BRC quantity p1=min(N_1^+,N_1^-) counts first-axis native signed-step cancellation pairs. For a fixed initial phase s set

\[
P_s(t,q,z)=\sum_{d\ge0} t^d \sum_{\substack{w:\ |w|=d\\w_0=s}}q^{p_1(w)}z^{H(w)}.
\]

The observer sums histories with multiplicity but preserves native branch/path semantics in its construction. Continuations consist of all legal paths of arbitrary macro length before the declared final histogram readout.

## Exact theorem

Let E(u,q), F(u,q) and K(u,q) be the explicit integer polynomials recorded in PREFIX-528, and define

\[
\Delta(t,q,z)=E(t^2,q)F(t^2,q)-(z-1)K(t^2,q).
\]

Then **for every one of the 48 fixed roots s** there is a polynomial N_s(t,q,z) in Z[q,z,t] such that

\[
\boxed{P_s(t,q,z)=N_s(t,q,z)/\Delta(t,q,z),\quad \deg_tN_s\le22.}
\]

Further, gcd(N_s,Delta)=1 in Q(q,z)[t] for **all** 48 roots, so every P_s has **exact generic minimal eventual linear recurrence order 22**. The even/odd subseries each have a candidate common recurrence of order 11, inherited from Delta(t)=Delta(-t). The full generic minimality assertion here concerns the total rooted sequence; parity minimality is a separately testable question.

A novel boundary effect separates the rooted numerator degrees: exactly three roots have nonzero coefficient at t^22,

\[
s\in\{(A,-L6,+L1),(B,-L4,+L1),(B,-L5,+L1)\},
\]
\[
[t^{22}]N_s=6\,879\,707\,136\,q^5(z-1).
\]

For the other 45 roots, \([t^{22}]N_s=0\), hence \(\deg_tN_s\le21\). Thus all 26 rooted joint-observer laws found in PREFIX-533 share one sharp denominator, even though their numerators differ. The three exceptional initial transients explain why a literal Berlekamp–Massey register initialized at depth zero may report length 23; the eventual denominator degree remains 22.

## Proof

(1) Use the exact 49-dimensional representation from PREFIX-530 with phase-basis W(v), target vector e_T, and rank-one correction. For v^2=q, every root is expressed using the same 49-by-49 matrix
\[
M(v,z)=\begin{pmatrix}2W(v)&(z-1)e_T\\e_T^\top W(v)^2&0\end{pmatrix}
\]
and its origin-sign-dependent endpoint row L_sigma(v). Precisely, \([t^d]P_s(t,v^2,z)=L_{\sigma_1(s)}(v)M(v,z)^d(e_s,0)\). The terminal weighting converts the original unsigned first-axis visit count K1 into the BRC cancellation count p1=(K1-|sigma1(end)-sigma1(start)|)/2.

(2) Let \(\Delta(t,v^2,z)=\sum_{j=0}^{22}\delta_j(v,z)t^j\), where the odd \(\delta_j\) vanish. Define the residue \(r_{s,d}=\sum_{j=0}^{22}\delta_j(v,z)[t^{d-j}]P_s(t,v^2,z)\), with negative depths interpreted as zero. The accompanying exact sparse-Laurent-polynomial certificate constructs every phase, each native successor and rank-one return coefficient, and computes these residues without floating-point arithmetic. It finds
\[
\boxed{r_{s,d}=0\quad \text{for every root }s\text{ and all }23\le d\le71.}
\]
These are 49 consecutive exact zero polynomial identities for each s. For d>=22 the residue equals \(L_{\sigma(s)}M^{d-22}\Delta^\vee(M)(e_s,0)\), where \(\Delta^\vee(M)=M^{22}+\delta_2M^{20}+\cdots+\delta_{22}I\). This residue sequence obeys the common degree-49 characteristic recurrence of M by Cayley–Hamilton. Hence the 49 consecutive zeros at d=23,...,71 imply every residue at d>=23 vanishes identically. Thus \(\Delta P_s\) is a polynomial of degree at most 22. Direct coefficient extraction at d=22 gives exactly the three exceptional numerator terms above.

(3) Sharpness is certified by exact finite-field coprimality. Specialize v=2 (q=4), z=3 and reduce coefficients modulo the prime 1000000007. For every one of the 48 roots the certificate computes the 23 numerator coefficients from the same native 49-state recurrence and verifies
\[
\gcd_{\mathbf F_{1000000007}[t]}(\overline{N_s},\overline{\Delta})=1,
\quad\deg_t\overline{\Delta}=22.
\]
A nonzero specialization of each resultant proves gcd(N_s,Delta)=1 over Q(q,z)[t]. The identical universal upper bound and 48 coprimality checks prove the minimal-order statement.

## Reproducible verification

Run the separately published Python 3/SymPy executable PREFIX534_exact_certificate.py from its directory. It writes PREFIX534_EXACT_EXECUTION.json and prints ALL_CHECKS_PASS. The integer dictionary basis is (v-exponent,z-exponent); the only noninteger intermediate powers v^-1 and v^-2 occur in the justified endpoint correction. The Delta polynomial has 58 nonzero monomials in (u,q,z). The exact verification covers all 48 roots at depths 23 through 71, with a maximum of 283 nonzero sparse monomials in one rooted coefficient at these depths. The independent modular coprimality check uses a second arithmetic realization at (q,z)=(4,3) modulo 1000000007.

## BRC and research continuation

BRC use: REUSE_APPLIED / REUSE_EXECUTED, namely the exact native signed-step cancellation identity from PREFIX-525 and the provenance-correct ordered INNER/OUTER transition construction from PREFIX-533. This is an all-length scalar **joint-histogram** result. The four-STAR X6 rotation candidate and its six-axis native path semantics remain the scientific object; the scalar quotient is explicitly observer-scoped.

Next smallest unit: determine whether every rooted parity subsequence attains minimum order 11, and then benchmark 22-order exact coefficient-generation time/bit-cost against the 49-coordinate linear lift, including input/output representation and endpoint BRC corrections. Continue investigating arbitrary three-axis C6 generators and full X6 rotation-selection dynamics. Canonical Result, Review, CLAIM and independent admission are governed by the current Source control and were not created by this mathematics-only publication.
