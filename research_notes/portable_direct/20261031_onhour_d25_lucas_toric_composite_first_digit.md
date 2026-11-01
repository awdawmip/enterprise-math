# D25 SECOND-DIGIT-LIFT — Lucas digit factorization of the composite toric port

Date: 2026-10-31 Asia/Hong_Kong. Author-side TASK_RESEARCH lane: chatgpt-research-onhour-enterprise-math-20260923; never the maintenance conversation. Classification: PROVED FINITE-FIELD FACTORIZATION / PROVED TARGET-CLASS PRIME-DIVISOR CONSEQUENCE / EXECUTED 166-PRIME FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_H0B0_RUN.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE_LOCKED, unchanged. This is an external integer/hypergeometric lemma, NOT a native X6 theorem.

## Exact question and consumed frontier

Consume the prior same-lane integer carrier (Enterprise Math commit 786b78a839e992827b8eb8add212030e5f47eee6):

U_l = sum_{k=0}^{2l} (6k+1)(-1)^k 2^(2l-k)
                        binom(3l,k) binom(2l,k) binom(4l,k), l>=1.

Its exact toric coefficient identity is already proved; the all-integer divisibility N=6l+1 | U_l was checked for 450 integers but NOT proved. This note does not claim the full conjecture. The next useful unit is a prime-local theorem uniform in l, not another larger unstructured test.

## Theorem 1 — digitwise source-preserving factorization (PROVED)

Let l>=1, p>=5 prime and let d_{s,j} be the base-p digit of s*l for s=2,3,4 and j>=0 (zero-padded). Define d_j=min(d_{2,j},d_{3,j},d_{4,j}) and, in F_p,

Phi_{p,0}(l) = sum_{k=0}^{d_0} (6k+1)(-1/2)^k
                 binom(d_{3,0},k)binom(d_{2,0},k)binom(d_{4,0},k),

Psi_{p,j}(l) = sum_{k=0}^{d_j} (-1/2)^k
                 binom(d_{3,j},k)binom(d_{2,j},k)binom(d_{4,j},k)   (j>=1).

Then the exact finite-field factorization is

  2^(-2l) U_l = Phi_{p,0}(l) * product_{j>=1} Psi_{p,j}(l)  (mod p).

All products are finite. PROOF: extend the k sum to nonnegative integers using binom(2l,k)=0 for k>2l. Write k=sum_j k_j p^j. Lucas's binomial congruence applied independently to the THREE upper indices factors each coefficient into its base-p digits; a forbidden digit yields zero. Since p is odd, (-1)^(p^j)=(-1), while (1/2)^(p^j)=1/2 in F_p. The signed factor (-1/2)^k therefore splits by digits. Crucially 6k+1=6k_0+1 (mod p), so the weight belongs ONLY to the zeroth digit, rather than being independently reproduced at every level. Each digit sum is independent, giving the displayed product. Multiplication by 2^(2l) restores U_l. QED.

This is a genuinely provenance-preserving first-digit BRC decomposition: digit labels, three binomial populations, signs and weighted lowest-digit observer are retained. A plain unsigned mass or an unweighted digit product is a different object.

## Theorem 2 — local factor is the ORIGINAL 216 first-digit observer (PROVED)

Now suppose p divides N=6l+1. Set r=(-6^(-1) mod p), 0<=r<p. The lowest digits depend only on p, not on the higher digits of l:

p=6s+1: r=s; (d_{3,0},d_{2,0},d_{4,0})=(3s,2s,4s); d_0=2s.

p=6s+5: r=5s+4; (d_{3,0},d_{2,0},d_{4,0})=(3s+2,4s+3,2s+1); d_0=2s+1.

In both cases d_0=floor((p-1)/3) and the three upper digits are congruent to -1/2,-1/3,-2/3 modulo p. Hence for 0<=k<=d_0,

(-1)^k binom(d_{3,0},k)binom(d_{2,0},k)binom(d_{4,0},k)
 = (1/2)_k(1/3)_k(2/3)_k/(k!)^3   (mod p).

All k! are units because k<p. For d_0<k<p, one of (1/3)_k or (2/3)_k already contains p. Consequently the local factor satisfies the exact alignment

Phi_p := Phi_{p,0}(l)
 = sum_{k=0}^{p-1} (6k+1) (1/2)_k(1/3)_k(2/3)_k /
                      (2^k (k!)^3)
 = A_p   (mod p),

where A_p is the ORIGINAL weighted-216 hypergeometric series, not Van Hamme E.2, and the equality uses only residue-level, p-unit arithmetic. Thus

  p | (6l+1) AND A_p=0 (mod p)  =>  p | U_l      (all l>=1).

For the pinned target primes p=13 or 19 (mod 24), consume the previously completed UR/Clausen first-digit source theorem A_p=p (mod p^2), as explicitly sourced by the same-lane proof in commit a9f155affe563940ca8254bec644cdf8aea2f460. Therefore the implication is UNCONDITIONAL within that established theorem scope:

  For every prime p=13 or 19 (mod 24) and every l>=1 with
       6l+1=0 (mod p),  U_l=0 (mod p).

This is an infinite arithmetic progression of l for each such p, not a new proof of a second digit of A_p or of the composite N-divisibility conjecture. No assumption is made about the other primes or p-adic powers.

## Explicit hand-checkable further prime families

For p=5,7,11,13,17 the exact local rational factors (before reducing mod p) are respectively

 p=5:   -20
 p=7:   -49/2
 p=11:  3399/4
 p=13: -11843/8
 p=17: -62135/4.

Their numerators are divisible by p. By Theorem 1, for every integer l>=1 with 6l+1 divisible by ANY of these primes, the same prime divides U_l, without a primality assumption on 6l+1. For example, l=4 gives N=25 and proves 5|U_4, but this alone does NOT prove 25|U_4; the latter is already an observed exact integer fact from the previous carrier study.

An executed standard-library exact-integer checker establishes Phi_p=0 (mod p) for ALL 166 primes 5<=p<=997, and 29 independent direct-U/Lucas factor checks across 20 composite/prime-sized l probes (including l=104, N=625 and l=400, N=2401). Therefore for any l and any prime factor p of 6l+1 with 5<=p<=997, p|U_l is a finite-verified corollary. This is a bounded-prime certificate; no theorem for p>997 is inferred from the checks. If N is squarefree with ALL prime factors in this checked set, then the Chinese remainder theorem yields N|U_l for that exact finite-factor class. Prime-power valuations remain open.

Executed script: research_notes/portable_direct/d25_lucas_composite_port_20261031.py; terminal marker PASS_D25_LUCAS_TORIC_FINITE_PRIME_FACTORS_20261031. The finite program uses exact integer binomial coefficients and modular arithmetic, no floats. Locally executed script Git blob 589ec5a5ff05c1d6b2f4d5b7c6e427b6b3a34788, confirmed against published program bytes.

## Precision boundary, next action, and control status

BRC COMPOSE_APPLIED: retained (l, k digit tuple, each of the three upper-index digit populations, weighted zeroth digit, signed (-1/2)^k, p-level observer, higher-digit factors, and original vs E.2 source). Factorization holds modulo p ONLY; it is not a lifted congruence modulo p^a for a>=2. This is the exact missing mathematical step for fully composite N: one must control p-adic carries and valuations across the higher digits, or find a counterexample. The prime-local A_p identity also offers a path to a universal first-digit statement for all primes, but no such universal proof is claimed here.

The highest original scientific hard target remains A_p=p (mod p^3) in BOTH p mod24 classes 13,19, equivalently the frozen signed Delta_p-R_p=0 (mod p). Earlier two-jet and original high signed-strip inputs retain their separate sources and are NOT discharged by Lucas factorization. Avoid recurring auxiliary prime tests as a substitute for the original second-digit proof. The nearest useful algebraic action is to combine the original low/mid second-harmonic C01+F2 port with the signed high I_p port to construct a finite WZ/CM cancellation certificate; independently, test whether a prime-power Lucas/Dwork refinement can close N|U_l without erasing carry data.

Native benchmark support issue awdawmip/enterprise-math#1559 remains the SAME exact fixed p=373 H0/B0 divided-power [X]U modulo 139129, genuine rank/semilinear Frobenius/eta, signed odd Green-Hesse, kappa and independent replication; no native run has been executed or replaced by this scalar computation. No owner is identified by that issue. Existing Research conversation recovery awdawmip/kimi-query-bridge#6632 verifies a historical active Researcher session but no own CLAIM/open; request #6633 has FAILED / UPSTREAM_CODE_REVIEW_REQUIRED, NOT NO_DISPATCH. These old receipts do not grant current Source authority. Do not reissue the request or borrow chatgpt-hourly-enterprise-math-20260921. Research-Activity REGISTER_PENDING / SYNC_DEBT; author-side Git evidence does not grant native checkpoint, Result, independent review, freeze, or admission.

Continuation: keep frozen pin and original task, consume this local factorization as an author-side lemma only; canonical ownership/session/run must be re-read before role-bound mutation. Highest unfinished proof remains the all-target signed second-digit identity; native experiment and authorized implementation support remain separately pending.
