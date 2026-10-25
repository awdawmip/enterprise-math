# R4-EC14 — Positive-density source loss, exact spectral rate, and grade duality in BRC

**2026-10-25 · author-side proof draft · not an accepted Enterprise Math Result.**

Frozen normative sources: GLOBAL_KNOWLEDGE_V1 main@ee7806e5717ca691678361ef779ed98115813649; Enterprise Math source main@b2049e0f8fc7c595260b4aedae50b16629523af3; P000 ACTIVE_LOCKED (startup original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc). Researcher: locally declared EMR4-LOCAL-20261025-EC14; activity RA-EMR4-20261025-1329-EC14LD. Native task query: CONTROL_QUOTA; native session creation: STATIC_READONLY_SCOPE_DENIED/operation_sent=false. No current owner or canonical CLAIM was established.

Parent: R4-EC13 exact auxiliary BRC grade law at immutable commit 387c93150bcf0c98f543d991471fbb27501dfd05. This is the **auxiliary positive-path-mass affine binary BRC**, not a native Heartbeat X6 propagation theorem. Native space remains six-dimensional plus separately typed time; no P000 change, physical-residual inference, phase cancellation, or native X6 computation is claimed. The index n denotes BRC word length, never heartbeat time. BRC method usage: REUSE_APPLIED/REUSE_EXECUTED (EC13 clean-source fine-state transition).

## 1. Model and exact observers

Each path is a length-n ordered word over bits a=0,1 with mass one. State (q,r,e,t): control q=0,1,2; r=0 means no 00 and last input not 0, r=1 means no 00 and last input 0, r=2 means 00 has appeared; orientation e=±1; signed grade t=e*k. From q=0: bit 0 maps (q',eta,b)=(2,-1,-1), bit1 (2,+1,-1); from q=1: bit0 (0,-1,-1), bit1 (0,+1,-1); from q=2: bit0 (1,+1,+1), bit1 (2,+1,-1). Set e'=eta e, t'=t+e'b. Source r updates by the literal occurrence of 00 (once dirty, always dirty). Every edge satisfies the universal identity

    t'-t = e (1-2a).

Let j=(n-t)/2 count negative grade increments, and let C[n,j] count paths avoiding 00. The triangular bit-to-grade-sign bijection from EC13 gives exactly C[n,j]+D[n,j]=binom(n,j). This is the grade-conditioned SOURCE query, not a full (orientation, displacement, final control, ordered future input) query.

On the eight clean states
(0,0,-),(0,0,+),(1,1,-),(1,1,+),(2,0,-),(2,0,+),(2,1,-),(2,1,+),
define the row transition matrix M(u): retain edges whose new r is not 2, assign weight u if t'-t=-1, else weight 1. Let v start in (0,0,+), and 1 denote the all-one terminal vector. Therefore C_n(u)=sum_j C[n,j]u^j = v^T M(u)^n 1.

The exact rational BRC certificate inherited and independently checked from EC13 is

    C(x,u) = sum_{n>=0} C_n(u) x^n = N(x,u)/Delta(x,u)
    N(x,u) = (1-u*x^2)(1-u*x^3)
    Delta(x,u) = 1-(1+u)*x+2*u^2*x^4-u^3*x^6.

The full original polynomial certificate is (I-x*M)H=(1+u*x^2)*Delta*v and 1^T H=(1+u*x^2)*N with H explicitly given in EC13. All algebra here is for the stated positive-weight BRC.

## 2. Theorem A: finite exponential inequality with an explicit prefactor

For every integer n>=1, 1<=j<=n-1, p=min(j,n-j)/n, one has

    0 <= C[n,j]/binom(n,j)
       <= (n+1) * (1-p^2)^floor(n/2).                                      (A)

**Proof.** For any clean fine state, the unrestricted next two bits have total weighted grade mass (1+u)^2: at each state, of the two inputs one changes grade positively and the other negatively. The literal two-bit word 00 necessarily makes the source dirty within two steps. Its weight is at least m^2 where m=min(1,u). Thus the row sums of M(u)^2 do not exceed (1+u)^2-m^2, and one extra step has total row mass at most 1+u. Inducting over disjoint two-step blocks gives C_n(u) <= (1+u)^n * [1-(m/(1+u))^2]^floor(n/2).

By coefficient positivity, C[n,j] <= u^(-j)*C_n(u). Choose u=j/(n-j), then m/(1+u)=min(j,n-j)/n=p. Under Binomial(n, j/n), the value j is a mode, and a mode on n+1 possible values has probability at least 1/(n+1). Equivalently, u^(-j)*(1+u)^n/binom(n,j) <= n+1. These inequalities yield (A), with no asymptotic approximation. QED.

In particular, for any fixed alpha in (0,1), for j/n -> alpha,

    liminf -n^(-1)*log(C[n,j]/binom(n,j))
      >= -(1/2)*log(1-min(alpha,1-alpha)^2) > 0.                          (A')

A vanishing numerator gives positive infinite negative log.

**Exact endpoint exception.** The unique sign sequence j=0 is realized by bit word 0 followed by n-1 copies of 1; the unique j=n sign sequence is realized by all 1 bits. Neither contains 00, so for every n>=1,

    C[n,0] = C[n,n] = 1.                                                    (B)

Thus each boundary grade fibre stays perfectly clean although every fixed interior density suffers exponentially vanishing clean proportion.

## 3. Theorem B: exact large-deviation rate, not merely an upper bound

For u>0 let lambda(u) be the unique Perron eigenvalue of the exact eight-state clean matrix M(u), and psi(s)=log lambda(exp(s)). The clean graph has a directed 8-state cycle, and the states (2,0,-) and (2,0,+) have self-loops of grade exponent 0 and 1 respectively. Hence the graph is primitive, the Perron eigenvalue is positive, simple and real analytic in u, and the grade additive functional is neither a constant nor a coboundary.

Consequently psi''(s)>0. The exact transition and the endpoint loops imply psi'(s) strictly increases from 0 as s->-infinity to 1 as s->+infinity. For each alpha in (0,1) a unique saddle u_alpha>0 satisfies

    alpha = u_alpha * lambda'(u_alpha)/lambda(u_alpha).

Put H(alpha)=-alpha log(alpha)-(1-alpha)log(1-alpha). For every integer sequence j_n/n -> alpha in (0,1),

    lim_{n->infinity} -1/n * log[C[n,j_n]/binom(n,j_n)]
       = I(alpha)
       = H(alpha)-log(lambda(u_alpha))+alpha*log(u_alpha).                 (C)

This rate is strictly positive, with explicit lower bound (A').

**Proof of the logarithmic lower and upper coefficient asymptotics.** Perron-Frobenius gives a positive overlap between the initial vector, terminal vector, and the dominant right/left eigenvectors; hence the total graded generating function C_n(u) is dominated by lambda(u)^n. Coefficient extraction on the complex circle u exp(i theta) gives

    C[n,j] = u^(-j)/(2 pi) integral_{-pi}^{pi}
              exp(-i j theta) v^T M(u exp(i theta))^n 1 d theta.

For theta different from zero modulo 2 pi, equality of spectral radius with the positive matrix would require phases exp(i theta h)=exp(i omega)d_source/d_target on every positive-weight edge. The grade-0 self-loop imposes exp(i omega)=1; the grade-1 self-loop then imposes exp(i theta)=1. Thus the twisted transfer has a strict spectral gap off the zero phase. At zero, analytic perturbation yields a local cumulant expansion of the principal eigenvalue:

    lambda(u exp(i theta))/lambda(u)
      = exp(i psi'(log u) theta - psi''(log u) theta^2/2 + O(theta^3)).

The grade-0 and grade-1 loops also rule out zero asymptotic variance (which would require a common per-edge grade constant plus a state coboundary). Hence psi''>0. Split the Fourier integral into the local Gaussian neighborhood and uniformly contracting complement. For j/n in any compact subinterval of (0,1), use the moving unique saddle u_{j/n}. The local integral is a positive constant times n^(-1/2)lambda(u_{j/n})^n u_{j/n}^{-j}, with uniform exponentially smaller outside contribution. This is the required *local coefficient lower bound*, not only the Chernoff upper bound. Stirling gives log binom(n,j)=n H(j/n)+O(log n), establishing (C) for every sequence with j/n->alpha. QED.

The EC13 rational function supplies an explicit algebraic way to evaluate lambda(u):

    lambda^6 - (1+u)lambda^5 + 2u^2 lambda^2 - u^3 = 0.                  (D)

Choose its Perron dominant positive root, not an arbitrary algebraic root. The positive initial/final Perron overlaps preclude cancellation of the dominant pole by N(x,u).

## 4. Theorem C: symmetry, midpoint value and boundary-rate expansion

A direct identity is

    Delta(x,u) = Delta(u*x,1/u).                                           (E)

The smallest positive denominator root corresponds to the noncancelled dominant Perron eigenvalue. Therefore lambda(u)=u lambda(1/u), and Legendre duality together with H(alpha)=H(1-alpha) yields the exact spectral symmetry

    I(alpha)=I(1-alpha),    0<alpha<1.                                     (F)

**Caution:** this asymptotic rate symmetry is not a claim that C[n,j]=C[n,n-j] at finite depth.

At u=1 the clean mass is Fibonacci F_{n+2}, so lambda(1)=phi=(1+sqrt(5))/2. Differentiating (D) yields psi'(0)=1/2. Therefore

    I(1/2)=log(2/phi)=0.211935355500...                                   (G)

Expansion of the Perron algebraic root near u=0 gives

    lambda(u)=1+u-2u^2+7u^3+O(u^4),

and saddle inversion gives

    I(alpha)=2alpha^2+O(alpha^3)       (alpha -> 0+),
    I(alpha)=2(1-alpha)^2+O((1-alpha)^3) (alpha -> 1-).                     (H)

The leading 2j^2/n in nI(j/n) matches the coefficient in EC13's square-root crossover e^{-2c^2} when j~c sqrt(n). This is a **consistency check**, not a proof that (C) is uniform for j=o(n), nor permission to interchange limiting operations.

## 5. Exact validation, evidence, boundary and continuation

The author-side reproducibility bundle contains the *actually executed* complete Python DP, independent rational recurrence and exact symbolic certificate programs. Verification:
- 8,191 ordered original bit words exhaustively checked for n<=12.
- Exact integer eight-state BRC DP through n=200, all j; comparison of all 20,301 coefficients against an independent integer recurrence from N/Delta.
- Exact integer cross-multiplication of (A) for all n<=200, 1<=j<n; both endpoint coefficients checked through 200.
- Exact SymPy identities for the EC13 transfer certificate and grade duality; spectral midpoint; algebraic series expansion.
- Five numerical PF saddle estimates, only illustrations: I(.1)=.0232733844, I(.25)=.1277607637, I(.5)=.2119353555, I(.75)=.1277607637, I(.9)=.0232733844.
- Original complete reproduction sources and machine validation report are retained in the independent R4-EC14 ZIP. This GitHub manuscript may be more concise than the complete executed paper; it preserves each theorem, all hypotheses and all load-bearing arguments.

**Scientific status:** An author-derived exact finite theorem and author-derived PF asymptotic theorem, both awaiting independent Driver scrutiny. The infinite-dimensional/native P000 space is not inferred from the auxiliary BRC counts; BRC word length is not physical time. The common denominator/coding operation is a grade quotient only; it does not prove preserving every future BRC input or source port.

**R4-EC15 next:** Determine a mathematically uniform sharp moving-saddle estimate in the regime j->infinity, j=o(n), j/sqrt(n)->infinity; specifically test and, if valid, prove log P(clean|j)=-(2+o(1))j^2/n on an explicitly bounded intermediate range. Existing EC13 square-root asymptotic and EC14 positive-density rate do not alone settle it. Independently retain the fixed-transfer exact six-versus-seven control-state question and R193 native source/time correspondence as open.
