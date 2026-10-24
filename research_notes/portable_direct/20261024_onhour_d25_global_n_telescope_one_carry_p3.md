# D25/LIFT — original-summand n-telescope and one-carry p³ certificate

2026-10-24 | TASK_RESEARCH author-side exact algebra, two independent integer arithmetic checks | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is NOT a formal Source checkpoint, frozen Result, native CM/divided-power benchmark, Lean proof, or independent review.

Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; historical task publication TP2-B6F4FC938FF94941C1B7; frozen *scientific* Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical conversation \`chatgpt-research-onhour-enterprise-math-20260923\` is **not** CONTROL_PLANE_MAINTENANCE \`chatgpt-hourly-enterprise-math-20260921\`. No service session/claim/run ownership is inferred.

## 1. Fixed original object and a new exact n-direction certificate

For any positive integer m put p=6m+1, N=4m, and retain the unchanged original source:
\[
A_m=\frac{(6m)!}{3^{6m}((2m)!)^3},\quad R_{m,0}=1,\quad
\frac{R_{m,n+1}}{R_{m,n}}=
\frac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},\quad
S_m=A_m\sum_{n=0}^{N}(6n+2p-1)R_{m,n}.
\]
Here p is a positive integer in the **exact rational** statements; impose primality only for valuation/modular claims.

Set
\[
K_p(n)=\frac{(2p+1-3n)(2p+3+6n)}
{(3n+p+2)(3n+2p+1)}.
\]
**Exact identity over Q**, for each n≥0:
\[
\boxed{(6n+2p-1)R_{m,n}
=12\{nR_{m,n}-(n+1)R_{m,n+1}\}+pK_p(n)R_{m,n}.}\tag{1}
\]
Proof: substitute the displayed original ratio, put over the common denominator \((3n+p+2)(3n+2p+1)\), and factor the numerator of the residual as \(p(2p+1-3n)(2p+3+6n)\). This is an identity of rational functions, not an empirical induction.

Summing all **original** n gives
\[
\boxed{\frac{S_m}{pA_m}=\sum_{n=0}^{4m}K_p(n)R_{m,n}
-\frac{12(4m+1)}pR_{m,4m+1}.}\tag{2}
\]
Thus the previous *m-direction* five-tail WZ proof is not invoked or recredited: (1) is an independent, original-*n*-direction finite telescoper. The moving endpoint and its provenance remain explicit.

## 2. Two actual singular points, and exact compression to one p-unit

Now take prime p=6m+1≥7. The exact factorial representation already in the original evidence shows \(v_p(R_{m,n})=0\) for \(0\le n\le m\), and \(=1\) for \(m<n\le4m+1\). Within \(0\le n\le4m\), \(K_p(n)\) has a p-denominator **only** at n=2m and n=4m. Write \(u_n=R_{m,n}/p\) for \(n>m\), a p-adic unit.

At n=2m the legitimate cancelled coefficient is
\[
\alpha_2=pK_p(2m)=\frac{(p+2)(4p+1)}{3(2p+1)}.
\]
At n=4m the same cancellation gives \(pK_p(4m)=(6p-1)/(4p-1)\). The untouched final recurrence is
\[
\frac{R_{m,4m+1}}{R_{m,4m}}
=\frac{(2p-1)^2}{2(2p+1)(4p-1)}.
\]
Therefore the combined **special n=4m plus explicitly sourced original terminal** coefficient is
\[
C_4=\frac{6p-1}{4p-1}-12(4m+1)
\frac{(2p-1)^2}{2(2p+1)(4p-1)}
=\frac{-8p^2+14p-3}{4p-1}.
\]
No forbidden inverse of p or deletion of an original boundary occurs.

Exact factorial cancellation gives
\[
\boxed{\frac{R_{m,4m}}{R_{m,2m}}=q_m^2,\quad
q_m=\frac{(12m)!(2m)!}{216^m(6m)!(8m)!}
=\frac1{3\cdot216^m}\prod_{a=2m}^{p-2}\left(1+\frac pa\right).}\tag{3}
\]
The last product identity follows exactly by writing \(8m=p+2m-1\), \(12m=2p-2\), then cancelling ordinary factorials. Consequently, with \(C=\alpha_2+C_4q_m^2\),
\[
\boxed{\frac{S_m}{pA_m}=
\sum_{n=0}^{m}K_p(n)R_{m,n}
+p\!\!\sum_{\substack{m<n<4m\\n\ne2m}}\!\! K_p(n)u_n
+C\,u_{2m}.}\tag{4}
\]
This is an **exact rational equality** for every m≥1. It retains the three original exceptional/endpoint contributions in the explicitly proved \(C\), while only one high unit \(u_{2m}\) has to be carried. It is not an assertion that their separate source states are globally identical under unrelated future observers.

## 3. Explicit p²-normalized jet = original p³ endpoint

Define \(H_s=\sum_{a=1}^{s}1/a\), \(H_0=0\), and the integer Fermat quotient \(q_p(6)=(6^{p-1}-1)/p\). As \(216^{2m}=6^{p-1}\), (3) implies
\[
q_m^2\equiv\frac19\{1+p[2(H_{p-2}-H_{2m-1})-q_p(6)]\}\pmod{p^2}.
\]
Since \(H_{p-1}\equiv0\) and \(H_{p-2}\equiv1\pmod p\), expansion of \(\alpha_2+C_4q_m^2\) gives
\[
\boxed{C\equiv1+p\eta_m\pmod{p^2},\quad
\eta_m=\frac{19}{9}-\frac23H_{2m-1}-\frac13q_p(6).}\tag{5}
\]

For \(0\le n\le m\), put
\[
b_n=\frac{(-1)^n\binom mn}{2^n},\quad
K_0(n)=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},
\]
\[
D_n=\sum_{j=0}^{n-1}\left[\frac1{2(j-m)}-\frac1{3j+2}-\frac2{3j+1}\right],
\quad
L_n=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1}.
\]
All displayed denominators in these **LOW** jets are p-units. The exact Pochhammer ratio, with numerator parameter \(-m+p/2\), yields \(R_{m,n}\equiv b_n(1+pD_n)\pmod{p^2}\); direct differentiation of \(K_p\) at zero gives \(K_p(n)\equiv K_0(n)(1+pL_n)\pmod{p^2}\).

For the regular HIGH indices in (4), only \(u_n\bmod p\) is needed, and the original p-free factorials determine them without inverting a p-divisible factor. At the one carried exceptional index,
\[
\boxed{u_{2m}=
\frac{(p-1)!(2m-1)!}{216^{2m}((4m)!)^2}
\prod_{a=1}^{2m-1}\left(1+\frac pa\right),}\tag{6}
\]
an **exact** rational identity giving its two p-adic unit digits.

Combining (4)–(6) gives, for every prime p=6m+1≥7,
\[
\boxed{
\begin{aligned}
\frac{S_m}{pA_m}\equiv{}&
\sum_{n=0}^{m}b_nK_0(n)[1+p(D_n+L_n)]\\
&+p\!\!\sum_{\substack{m<n<4m\\ n\ne2m}}\!\! K_0(n)u_n
+u_{2m}(1+p\eta_m)\pmod{p^2}.
\end{aligned}}\tag{ONE-CARRY}
\]
This is an **all-prime algebraically proved normalization** at the original third-digit precision. It does **not** prove that the normalized sum equals the claimed target.

A useful exactly scoped first-digit shadow follows by partial fractions \(K_0=-2+2/(3n+1)+3/(3n+2)\). If \(I_a=\sum_{n=0}^m b_n/(3n+a)\),
\[
\frac{S_m}{pA_m}\equiv -2^{1-m}+2I_1+3I_2+u_{2m}\pmod p.
\]
The one-port compression is valid for this declared scalar endpoint observer. Keep the original LOW/HIGH provenance and \(q_m\) for any other future operations.

## 4. Exact hard-target equivalence and actual remaining gap

The unchanged original task is \(S_m\stackrel{?}{\equiv}p(4/3)^{p-1}\pmod{p^3}\) for p mod24 in {13,19}. Since \(A_m=(p-1)!/[3^{p-1}((2m)!)^3]\) is a p-unit, **the hard target is equivalent** to the following concrete same-prime arithmetic obligation:
\[
\boxed{\text{RHS(ONE-CARRY)}
\stackrel{?}{\equiv}
\frac{4^{p-1}((2m)!)^3}{(p-1)!}\pmod{p^2}.}\tag{CM/DP-BRIDGE}
\]
The right side contains the original normalized factorial target, with no moved rank or different-prime induction. Thus a same-class CM/divided-power argument could be aimed directly at the regular two-jet sums and the one retained carry \(u_{2m}\). This final equality is **UNPROVED** for all target primes and is not a renamed axiom.

## 5. Executed independent arithmetic, BRC and continuation

Executed the accompanying standard-library checker \`20261024_onhour_d25_global_n_telescope_one_carry_check.py\`: exact rational (1)–(4) checked at m=1,...,8 (including composite 6m+1, where only rational identities were claimed); for **207/207** primes p≤3000 with p≡1 mod6 (including **107/107** primes in the two frozen target classes), the p-adic original three-factor recurrence reconstructed \(S_m\bmod p^3\), while a separate factorial/unit and low harmonic implementation reconstructed ONE-CARRY\bmod p². Original and new normalizations and their first-digit projections matched in every case. The original hard-target equality also held in this finite sample; this is not a proof. The full per-prime JSON is retained with the executed local checker; no native experiment was run. Author-side SHA256 checker \`e24601ab450afc3441b0ca388250e32ce6d8d22a6215dfe21ed12ba12c0f315d\`, 207-prime record SHA256 \`420c228e6a2641aca67605f9764714ee618c23ad686ecc84bfe8eb14dadb8714\`.

BRC **COMPOSE_APPLIED / REUSE_APPLIED**: the integer/valuation carrier preserves p, m, n, all original source positions, p-free factorial units and rational boundary transitions. The explicit equality (3) licenses precisely the compression of n=2m, n=4m and the original terminal under the declared scalar modulo-p³ endpoint observer; it does not assert equality under native X6 evolution. P000 and ACTIVE residual-fidelity world model are not changed.

**Already consumed, not recredited:** D24 frozen RR-AC9B3BA5BD277CE043F5; exact original-rank WZ \`c7fb90fd\`; same-prime FIVE \`7724e73f\`; LOW odd/even seed jets \`6f14c39f\`/\`5404753a\`; direct original 575-prime p≤20000 sweep \`c6ba00a0\`. **New science here:** independent original-*n* telescoper and p³ one-carry collapse, plus the exact explicit CM/DP-BRIDGE obstruction.

**Next smallest mathematical unit:** prove or refute CM/DP-BRIDGE, preferably derive the same-class normalized Jacobi/Gauss relation that cancels the low two-jet, HIGH regular jet and Wilson/Fermat factors while preserving the one carry. Separately the Source-fixed, **unmodified native benchmark** is still NOT RUN; no substitution by this Python arithmetic is permissible. No benchmark executor is currently verified (NATIVE_EXECUTOR_UNASSIGNED). Source case \`awdawmip/enterprise-math#1539\` (OPEN at last read, 2026-10-24) owns the onhour session inconsistency and restoration. Fresh Sites reports \`research_authority_granted=false\`; exact \`em_control_continuation\` returned \`CONTROL_QUOTA\` and local checkpoint listing \`ACCESS_DENIED\`. Neither a valid current winning CLAIM nor formal session/run was obtained; no unknown mutation was retried. The unrelated old three neutral UR staging sources remain separate.

**Recovery packet:** parent and publication above; immutable science pin above; preserve original unknown/denied requests and Source-side continuation; no legitimate session_id/claim_id/run_id/target_request_id freshly issued this turn. Research artifact is **author-only UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT** until formally registered and reviewed. Unmodified research scheduling, activation and notifications, with no new scheduler or Actions.
