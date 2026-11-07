# D25 hourly20 — A-stream exact short carry and A/B second-digit source split

2026-11-07 · portable, author-side TASK_RESEARCH · finite-field derivation with executed exact checks · UNREVIEWED / NOT_ADMITTED.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Preserve scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Reported lane: chatgpt-research-hourly-enterprise-math-20260923 (maintenance ID excluded). Native role/CLAIM/run not verified.

## Unit 1. The missing A-stream short carry (exact theorem)

Let p=6m+1 be prime and work in F_p[z], p>3. Let
Q(z)=sum_{i=0}^m q_i z^i, q_i=binom(m,i)binom(2m,i),
R(z)=sum_{j=0}^{4m-1}r_j z^{p-1-j},
r_0=1/[18(m+1)(2m+1)],
r_{j+1}/r_j=(j+1)^2/[(m+j+2)(2m+j+2)].
These are the already established low Gauss and normalized valuation-two tail sources (prior exact input: research_notes/portable_direct/20261107_onhour_d25_reflected_frobenius_prefix_ports.md; forced Gauss-Wronskian source: research_notes/portable_direct/20261107_onhour_d25_cartier_one_constant.md). Every denominator appearing in the indicated finite ranges is a unit.

Set P=pi_<p(QR), where pi_<p truncates powers >=p. Then uniquely
QR=P+z^p H_A, with
[z^ell]H_A=sum_{j=0}^{m-ell-1} q_{j+ell+1} r_j  (0<=ell<m).
In particular,
deg H_A=m-1, [z^{m-1}]H_A=binom(2m,m)/[18(m+1)(2m+1)] !=0 in F_p.
The *entire* carry port uses only the first m reflected tail coefficients r_0,...,r_{m-1}, not its full 4m-coefficient tail. Proof: the exponent of q_i r_j is p-1+i-j; it crosses the cutoff precisely when i>=j+1. At exponent p+ell this requires i=j+ell+1. The top coefficient occurs only at i=m,j=0, hence is nonzero.

Define D=z*d/dz. For any x in F_p^\{0,1} with Q(x)=0, the full weighted projected source observer is exactly
E_A(x):=2(1+6D)P(x)
      =12(DQ)(x)R(x)-2x(H_A(x)+6(DH_A)(x)).
Indeed D(z^pH_A)=z^p DH_A and x^p=x. Using the earlier exact Cartier-Wronskian identity, with r=(p+1)/2 and source-preserved integration constant c_A:
(DQ)(x)R(x)= -[I_A(x)+c_A x]/(1-x)^r,
the same observer has the **compact Cartier port**
E_A(x)= -12[I_A(x)+c_A x]/(1-x)^r -2x(H_A+6DH_A)(x).
This is the A analogue of the prior B3/B5 port, with its own source exponent, weight 6 and nonzero leading carry. No A/B origin tags are identified merely because the terminal Frobenius charges coincide.

## Unit 2. Exact second-digit difference with *both* carry ports

Let F_A(z) be the Gauss series 2F1(1/6,1/3;1;z), and F_B(z) be 2F1(1/8,3/8;1;z) for B3, or 2F1(5/8,7/8;1;z) for B5. Put C_B=1 (B3), 1-z (B5). Clausen and Euler give the formal identities
3F2_A=F_A^2,  3F2_B=C_B F_B^2.
Truncate each F at n<p, splitting it into its exact p-adic lower part L (n<2m+1 for A, n<3k+2 for B) and upper part p^2 R (normalized valuation-two tail). The upper-square term vanishes mod p^3; the lower-upper term is 2p^2LR. Apply respectively 1+6D and 1+8D followed by pi_<p and evaluations alpha=1/2, beta=1/9.

Define the exact, source-labelled low-jet terms
G_A=(1+6D)pi_<p(L_A^2)(alpha), G_B=(1+8D)pi_<p(C_B L_B^2)(beta)
mod p^3 and W,V as the corresponding original weighted 3F2 sums to n=p-1.
The p^3 lifting identity is
W-V == G_A-G_B + p^2(E_A-E_B) (mod p^3).
At the frozen target classes p=13,19 (mod 24), the cited CM root inputs give Q_A(alpha)=Q_B(beta)=0 and the new A and prior B compact ports apply. When G_A=G_B (mod p^2), set Gamma_p=(G_A-G_B)/p^2 (mod p). Then the **single exact remaining local cancellation** is
Gamma_p + E_A - E_B == 0 (mod p).
This is an exact reduction, *not* a universal proof of this last equality. The first quotient is a lower-jet p-adic source; E_A and E_B are separate high-tail Cartier/carry sources.

B has E_B= -16 C_B(beta)(I_B(beta)+c_B beta)/(1-beta)^r_B - 2beta(H_B+8DH_B)(beta) with r_B=(p+1)/2 for B3 and (p+3)/2 for B5. The B5 Euler diagonal is the independently established nonzero Dixon term (k!)^2((3k+1)!)^2/192 (mod p); its source label is retained.

## Executed exact checks and discrimination

Program d25_a_short_overflow_20261107.py verifies the A carry coefficients/leading unit at all 178 primes p<2500, p=1 (mod6), and compares the independently iterated full weighted double convolution against the compact A expression at all 94 target primes p<2500. PASS 178/178, 94/94.

Program d25_compact_fricke_defect_20261107.py computes original 3F2 coefficients modulo p^3 and separate lower Gauss squares, then verifies both source splittings and the compact cancellation for all 94 target primes p<2500. PASS 94/94. Representative p:(Gamma,E_A,E_B) are
13:(4,9,0), 19:(14,13,8), 43:(2,31,33), 67:(16,30,46), 373:(219,1,220), 997:(644,458,105), all modulo p. In the tested range W=V=p (mod p^3). These exact finite computations verify the coding and the bounded family; the mother supercongruence remains OPEN.

The p=373 check here is modular arithmetic on a portable finite-ring reconstruction, **not** the original native H0/B0 p=373 experiment (#1559).

## Next smallest unfinished unit

Find and prove, using the *actual* Fricke pullbacks t_\pm=±6sqrt(2) and the lower Gauss inputs, a source-aware identity that computes Gamma_p from the two separate Cartier constants and short overflow ports. First test a proposed transformation at p=13,19,43,67,373; use the six triples above as a regression witness. A proposed identity matching only common terminal -z^p fails to account for the already proved lower injection and B5 Dixon diagonal. Do not repeat the proven B carry or the native H0/B0 replication.

Transport status checked 2026-11-07T14:18:37Z: em_sites_connection_status was CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; em_status failed BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Historic requests em-h20-20261106-1324-d25-task-r13, em-h20-20261106-1324-d25-cont-r13 are preserved as UNKNOWN_PRESERVE. Author-side publication is distinct from a native Source checkpoint, Result or review. Support path #1558.
