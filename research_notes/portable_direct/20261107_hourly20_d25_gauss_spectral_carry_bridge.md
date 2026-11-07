# D25: shared Gauss spectral pencil and sharp p-adic carry-port contrast (2026-11-07)

**Proven algebra / executed exact checks, author-side; UNREVIEWED, NOT_ADMITTED.** Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-hourly-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 excluded. No native Researcher execution authorization or checkpoint is asserted. Continues the exact previous D25 dual-tail note; parent objective Delta_p-R_p=0 mod p (p=13,19 mod24) remains OPEN.

## 1. A common spectral differential operator

Let A(z) = 3F2(1/2,1/3,2/3;1,1;z), B(z) = 3F2(1/4,1/2,3/4;1,1;z). The actual frozen 216 terms are [z^k]A times 2^(-k), and actual 2304 terms are [z^k]B times 9^(-k). Thus W_p is the truncated (1+6 theta)A evaluated at z=1/2, and S_p is the truncated (1+8 theta)B at z=1/9, theta=z d/dz.

Classical Clausen gives exact formal-series squares A=f² and B=g², where f=2F1(1/6,1/3;1;z) and g=2F1(1/8,3/8;1;z). Put lambda_A=1/18, lambda_B=3/64, delta=5/576. Gauss's differential equations prove that f,g share one differential expression D=z(1-z) d²/dz² + (1-3z/2) d/dz, with **Df=lambda_A f and Dg=lambda_B g**.

Define H_lambda=theta³-z(theta+1/2)(theta²+theta+4lambda). Direct coefficient recurrence gives H_lambda_A A=0, H_lambda_B B=0 and therefore the two exact forcing relations

**H_lambda_B A = (5/144) z(theta+1/2)A;  H_lambda_A B = -(5/144) z(theta+1/2)B.** (1)

Proof: for either normalized 3F2 coefficient c_k(lambda), (k+1)^3 c_(k+1)=(k+1/2)(k²+k+4lambda)c_k; subtract the two operators. These equations separate the two source labels and expose a nonzero, explicit forcing term.

## 2. A direct connection at the two actual frozen arguments

Let c=2/9, F(z)=f(z), G(z)=g(cz), J=F'G-FG'. Then z=1/2 simultaneously samples original 216 at 1/2 and original 2304 at 1/9. Exact subtraction of the two scaled Gauss equations proves

**z(1-z)(1-2z/9)J' +(1-55z/36+z²/3)J -(7z/36)(FG)'=(13/288-5z/2592)FG.** (2)

Proof: F obeys z(1-z)F''+(1-3z/2)F'=lambda_A F; chain rule gives z(1-cz)G''+(1-3cz/2)G'=c lambda_B G. Multiply J'=F''G-FG'' by z(1-z)(1-cz). With U=(1-3z/2)(1-cz), V=(1-3cz/2)(1-z), split -UF'G+VFG'=-(U+V)J/2+(V-U)(FG)'/2, and V-U=(1-c)z/2. Rearrange and substitute c=2/9 and the two lambda values. Also, for unscaled f,g the first-order exact rational identity is z(1-z)(f'g-fg')'+(1-3z/2)(f'g-fg')=(5/576)fg. These give a constructive differential bridge, not yet the finite-sum congruence W_p=S_p.

## 3. Finite polynomial transfer and exact boundary valuation

For A_N=sum_(k=0)^N a_k z^k and B_N=sum_(k=0)^N b_k z^k, coefficientwise cancellation yields, for EVERY integer N>=0,

**H_lambda_B A_N=(5/144)z(theta+1/2)A_N -(N+1/2)(N²+N+2/9)a_N z^(N+1).** (3)

**H_lambda_A B_N=-(5/144)z(theta+1/2)B_N -(N+1/2)(N²+N+3/16)b_N z^(N+1).** (4)

Legendre factorial valuation gives v_p(a_(p-1))=floor(2(p-1)/p)+floor(3(p-1)/p)=3, and v_p(b_(p-1))=floor(4(p-1)/p)=3 for every prime p>3. Argument scalings 2 and 9 are p-units. Consequently, with N=p-1 the explicit boundary term in each of (3)-(4) vanishes modulo p³, giving polynomial operator forcing laws mod p³ without discarding a finite truncation boundary.

## 4. A sharp difference in provenance carry precision

Clausen squaring must be followed by the degree-<p projection: A_<p = Pi_<p(f_<p²) and B_<p = Pi_<p(g_<p²). Label the discarded Cauchy-convolution carry ports by ordered (i,j), 0<=i,j<p, i+j>=p, with weights f_i f_j and g_i g_j. The SHARP minimum p-adic valuation over the ports on both frozen prime classes is

| Prime class | 216 port minimum | 2304 port minimum |
| --- | ---: | ---: |
| p=13 (mod24) | 2 | 0 |
| p=19 (mod24) | 2 | 2 |

**Proof for 216:** put p=6m+1. In f_i=(1/6)_i(1/3)_i/(i!)², the only p-dividing numerator factors for i<p occur at zero-based indices m and 2m. Thus v_p(f_i)=0,1,2 on i<=m, m<i<=2m, i>2m. For i+j>=p, either both indices exceed m or one has partner >=p-m=5m+1>2m. All ports have valuation >=2; port (1,p-1) attains 2.

**Proof for 2304, p=19 mod24 (p=3 mod8):** the only p-dividing numerator factors of g_i=(1/8)_i(3/8)_i/(i!)² occur at r=(p-3)/8 and s=(3p-1)/8. Hence v_p(g_i)=0,1,2 on i<=r, r<i<=s, i>s. If an index <=r appears in a carry, its partner >=p-r>s; otherwise both have valuation >=1. Every port has valuation >=2, with equality at (1,p-1).

**Proof for 2304, p=13 mod24 (p=5 mod8):** the factors occur at r=(5p-1)/8 and s=(7p-3)/8. The port i=j=(p+1)/2<=r consists of two p-units and has degree p+1>=p, so its valuation is 0. This is a labelled-port minimum and is distinct from possible cancellation after summation. For p=13 the aggregate coefficient of z^(p+1) in g_<p² is also nonzero: 6 mod13.

Therefore, on p=13 mod24 the 2304 square loses actual p^0 information if evaluated before projection; on p=19 mod24 both families' omitted ports begin at p². Precision-sensitive source retention is compulsory for any candidate transformation.

## 5. Executed evidence, provenance and next mathematical unit

An independent Python standard-library Fraction/integer script verified 24 Clausen rational coefficients per family, 23 unscaled and 20 aligned Wronskian coefficients, plus exact mod p³ operator forcing and top boundary for all 166 primes 5<=p<1000. It checked the full Gauss coefficient valuation profiles and the sharp carry witnesses for target classes. Selected 2304 aggregate coefficients at z^(p+1), reduced modp: (13,6), (19,0), (37,8), (43,0), (109,51), (373,268). General algebraic conclusions use the written proofs, not finite extrapolation.

Prior source reuses: frozen D25 216/2304 definitions and Clausen/reflection dependency; classical Clausen; p-adic factorial valuations; BRC labelled-port observer. Prior Guo–Zudilin (2019) proved 2304 p³ supercongruence remains an external target for connecting, not a premise of these lemmas. No native experiment or accepted theorem status was inferred.

**Next:** derive/test a nonlinear pullback or finite WZ/contiguous identity for the **aligned**, weighted, coefficient-projected squares at z=1/2, carrying distinct B p^0 and A/B p² omitted ports according to the residue class. Underlying Gauss local exponent-difference sets {0,1/2,1/6} and {0,1/2,1/4} differ, so a mere degree-one Möbius change plus scalar gauge cannot identify the equations; nonlinear transformations remain open. First exact witness primes: 13,19,37,43,109,373. Do not repeat frozen CM0/UR, 301-prime W/S scan, 1226-prime shifted 4F3 checks or native 373 experiment.

Control as of 2026-11-07: em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Old requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remain pending verification. Protected session/staging/claim/run UNKNOWN; preserve them. Support awdawmip/enterprise-math#1558. Author activity REGISTER_PENDING; native Source checkpoint SYNC_DEBT; review UNREVIEWED_NOT_ADMITTED.