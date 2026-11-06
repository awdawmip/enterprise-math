# D25: Original-216 first-digit Gauss flux and two-port diagnostics

Date: 2026-11-07. TASK_RESEARCH, author-side portable arithmetic. Research lane: chatgpt-research-onhour-enterprise-math-20260923; do not borrow the maintenance lane chatgpt-hourly-enterprise-math-20260921. Task publication TP2-B6F4FC938FF94941C1B7, frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Classification: finite-characteristic reduction PROVED (from previously proven Clausen identity); character-splitting pattern and second-digit unit balance FINITE-VERIFIED only; UNREVIEWED / NOT_ADMITTED.

## Smallest original-scalar question

For a prime p=6m+1>3, let a_n=(2n)!(3n)!/[216^n(n!)^5], W_p=sum_(0<=n<p)(6n+1)a_n. Consume the original parameter polynomial (see prior report a953484013a1c1297f006b86a721869fab29f6ef):
A_n(t)=(-3m+t/2)_n(-2m+t/3)_n(-4m+2t/3)_n/[2^n(n!)^3].
Define its unperturbed **original-216** port (distinct from the signed Clausen triangular J_p):
U_(0,p)=sum_(n=0)^(2m)(6n+1)A_n(0), an element of Z_(p).
Define a finite Gauss polynomial
D_m(z)=sum_(k=0)^m binom(m,k)binom(2m,k)z^k,
and the differentiated flux F_m(z)=D_m(z)+12z D_m'(z).

## Exact finite-characteristic reduction

THEOREM. For every such prime:
  W_p == U_(0,p) == D_m(1/2) F_m(1/2) (mod p),
where F_m(1/2)=D_m(1/2)+6D_m'(1/2).

Proof. By the previously verified original-216 valuation stratification, a_n is p-divisible for n>=2m+1, hence W_p=U_(0,p) modulo p. The finite Pochhammer parameters at t=0 reduce as (-3m,-2m,-4m)=(1/2,1/3,2/3) in F_p. Let H(x)=sum_(n=0)^(2m)A_n(0)x^n. The formal Clausen symmetric-square identity, coefficientwise for degree <=2m and with the remaining coefficients vanishing in F_p, gives H(x)=D_m(x/2)^2 in F_p[x]. (This reuses the existing Clausen theorem, rather than claiming a new square identity.) Applying 1+6x*d/dx at x=1 yields precisely D_m(1/2)[D_m(1/2)+6D_m'(1/2)]. No division by a nonunit occurs. QED.

COROLLARY (conditional, all primes). A zero of either Gauss value D_m(1/2) or the differentiated flux D_m(1/2)+6D_m'(1/2) suffices for the first original digit W_p=0 mod p. On the frozen target p mod24 in {13,19}, the Gauss-zero route is a concrete strictly weaker finite task than the full W_p=p mod p^3 objective. It keeps the distinct p-adic middle and second shells for the later digits.

## Exact computations and a newly isolated class split

Run the companion standard-library checker d25_gauss_flux_20261107.py, using F_p modular inverses and separate original coefficient recurrences. It tested every prime p=6m+1, 7<=p<=10000: 611 primes, including 312 in target residue classes. The factorization theorem passed all 611 independently evaluated cases.

The following *observed* mutually exclusive splitting had zero exceptions in these 611 cases, and is therefore a precise conjectural next proof target, NOT established for all primes:
  (2/p)=-1, i.e. p mod8=3 or 5: D_m(1/2)=0 and F_m(1/2)!=0;
  (2/p)=+1, i.e. p mod8=1 or 7: F_m(1/2)=0 and D_m(1/2)!=0.
Counts (p mod8 : zero D, zero F):
  1 : (0,143); 3 : (155,0); 5 : (157,0); 7 : (0,156).
This separates the original first digit into a Gauss-zero diagnostic on frozen supersingular classes versus a flux-zero diagnostic on the complementary residue classes. A proof of the class-selective Gauss-zero claim remains an open sublemma, potentially approachable via a finite-field quadratic transformation at z=1/2.

For the **next** p-adic digit, define alpha_p=U_(0,p)/p modp and beta_p=(W_p-U_(0,p))/p modp whenever U_(0,p)=W_p=0 modp. The checker directly computed the independently sourced rational unperturbed port U_(0,p) and the complete original W_p modulo p^2 for all 148 p=6m+1 <=1999 (77 frozen target primes). It observed alpha_p+beta_p=1 modulo p, i.e. W_p=p mod p^2, in all 148. This is an exact finite experimental certificate, not a proof of the uniform second digit. Importantly, the separate ports are generally NONZERO:
  p13 : (D,D',flux,alpha,beta)=(0,1,6,8,6);
  p19 : (0,2,12,4,16);
  p67 : (0,13,11,65,3);
  p373: (0,215,171,209,165).
For p19 the original unperturbed contribution is U0=76 mod361 and the complementary p-linear contribution is 16*p mod361; 76+304=19 mod361. At p373, U0=77957=209*p mod139129 and the remainder is 165*p, summing to p modulo p^2. These are real nontrivial cancellations between independently computed ports. The signed Clausen J_19=6 and J_373=98, plus the original valuation-two shell/p^2 values 9 and 266, remain separate unchanged prior observations.

BRC resolution: COMPOSE_APPLIED. Typed carrier (source=unperturbed-Gauss or original216, n, m, p, valuation, signed p-unit, derivative or coefficient, observer precision). The product observer loses the distinction between a zero Gauss value and a zero flux; the retained pair (D,F) resolves this information loss. The (alpha,beta) observer retains the p-linear source split instead of collapsing immediately to W/p. External finite-field algebra only, no native X6/H0/B0 computation.

## Remaining proof, native benchmark and durable state

Highest consumed immutable author frontier: 8ba15a97125826e510052d44ebe2db5318ade60f (single-q original216 reduction). The current theorem reuses Clausen identity and original216 parameter jets; it does not reprove prior shells, q/g first integral or E.2 tail. The immediate next mathematics is to derive a uniform finite-characteristic certificate for the class-selective D_m(1/2)=0 in p mod8=3,5, then a nontrivial first-order deformation identity for alpha+beta=1; use it to connect with the full third-digit signed boundary and existing E.2/Franel two-jet.

Mother target remains W_p=p modp^3 for p mod24=13,19, equivalently the frozen Delta_p-R_p=0 modp. Original same-class native p373 H0/B0 divided-power [X]U mod139129, rank/Frobenius/eta, signed Hesse Green, kappa, and an independent native replica remain NOT_EXECUTED/PENDING_OWNER, supported by https://github.com/awdawmip/enterprise-math/issues/1559.

Source original request onhour11-20261106-1400-exact-research-lane-continuation read WAITING_RESOURCE/EVENT_COLLECTION_IO, then same-ID bounded reconcile returned QUEUED. Research authority is not granted by this Site-scoped gateway; no native claim/session/run/Result is asserted. The old three staging objects remain independent and not admitted. Native client semantic checkpoint revision22 is historical, not a current claim. These author-side mathematical inputs and checker require independent review and formal Source continuation before admission.