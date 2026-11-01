# D25: exact triangular 216/2304 value bridge and full-rank observer certificate

Date 2026-11-01; research lane TASK_RESEARCH; logical conversation chatgpt-research-hourly-enterprise-math-20260923 (separate from maintenance).
Status: AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.
Consumed, not recredited: prior exact Clausen cut-off and Hadamard bridge at project commits 813d9a8c66c9facccbafd5492d439f1288ade1cd and 86149263e38c22292c9def1e0f69092efa1be77e.

## I. Exact finite 216 special-value certificate

For every prime p>=7 with p=1 mod 6 let u_n=(1/6)_n(1/3)_n/(n!)^2, v_n=(1/2)_n(1/3)_n(2/3)_n/(n!)^3, b_n=(1/8)_n(3/8)_n/(n!)^2 and h_n=b_n/u_n. All are exact rationals.
Original W_p(1/2)=sum_{n=0}^{p-1}(6n+1)v_n/2^n; auxiliary B_p(z)=sum_{n=0}^{p-1} b_n z^n.

**Theorem A, exact over Q:**

    W_p(1/2) = sum_{0<=i,j<p, i+j<p} [6(i+j)+1] 2^(-i-j) b_i b_j/(h_i h_j).

Proof: The prior exact Clausen formal identity gives v_n=sum_{i+j=n}u_i u_j for every n. Replace v_n in the finite weighted sum and exchange sums; b_i/h_i=u_i exactly. The strict i+j<p triangular cutoff is part of the theorem, and denominators are rational, not automatically invertible modulo p.

## II. Observer information rank

For an arbitrary coefficient vector a in Z_(p)^p define Q_p(a)=sum_{i+j<p}[6(i+j)+1]2^(-i-j)a_i a_j and M_ij=1_{i+j<p}[6(i+j)+1]2^(-i-j). Then W_p(1/2)=Q_p(u_0,...,u_{p-1}) for the hypergeometric vector.

**Theorem B, exact for every prime p>=7:**

    det(M) = (-1)^(p(p-1)/2) (6p-5)^p / 2^(p(p-1)).

Proof: Reverse the columns of M. The resulting matrix is upper triangular, with each diagonal entry (6p-5)/2^(p-1). Column reversal contributes (-1)^(p(p-1)/2). Since 6p-5=-5 modulo p and p>5, M is invertible over F_p.

Consequently no F_p-linear measurement map F_p^p -> F_p^k with k<p can determine Q_p(a) on every fiber: a nonzero v in its kernel and fiber constancy would imply Q_p(x+v)-Q_p(x)=0 for all x; subtract x=0 and polarize to get 2 Mv=0, contradiction.

**Constructive B_p(1/9) witness.** h_1=27/32. Put q(z)=z-3/32. Then (T_H q)(1/9)=0, so a(z)=1 and a_e(z)=1+e q(z) have identical transformed single-point values, but

    Q_p(a_e)-Q_p(a) = (109/16)e + (2665/1024)e^2   (exact rationals).

The two numerators 109 and 2665 are coprime; for each p>=7 the nonzero polynomial has at most two roots. One of e=1,2,3 distinguishes their mod-p weighted observables. This proves a universal generic rank-one compression failure. It does NOT exclude a recurrence-specific CM special-value identity for the single hypergeometric input.

## III. Signed high-index tail and accurate p-adic carry

Let Y_p(z)=sum_{n<p}u_n z^n, s=Y_p(1/2), d=(z d/dz Y_p)(1/2), and

    T_p = sum_{0<=i,j<p, i+j>=p}[6(i+j)+1]2^(-i-j)u_i u_j.

**Exact identity:** W_p(1/2)=s^2+12 s d-T_p. For p=6r+1, the coefficient valuations v_p(u_i) on i=0..p-1 are 0 on i<=r, 1 on r<i<=2r, and 2 on 2r<i<p. Every pair i+j>=p has total valuation at least 2: zero+zero pairs add to at most 2r<p and zero+one pairs to at most 3r<p. Hence T_p is divisible by p^2 in Z_(p); C_p=T_p/p^2 mod p is a defined, signed high-tail digit.

**Theorem C (conditional on s=0 mod p, any prime p=1 mod6):** choose digits in 0..p-1:

    s/p = a0+p*a1 (mod p^2); d=d0+p*d1 (mod p^2).

Then W_p(1/2)=p (mod p^3) iff both conditions hold:

    E1: 12*a0*d0 = 1 (mod p),
    E2: (12*a0*d0-1)/p +12*(a1*d0+a0*d1)+a0^2-C_p =0 (mod p).

The quotient in E2 is the actual integer carry after E1, not an arbitrarily dropped modular term. Proof: divide W=s^2+12sd-p^2 C_p by p and compare its two residue digits modulo p^2. The zero premise for Y_p(1/2) is verified in the finite target sample, and is not asserted here as a universal CM theorem.

## IV. Exact checks, provenance, and next action

Executed Python standard-library integer modular check: 37/37 primes 7<=p<=400 with p=1 mod6 passed original weighted-3F2 vs triangular expression, signed high-tail reconstruction, T_p divisible by p^2, and explicit transformed-value fiber witness. 21/21 target primes p mod24 in {13,19} passed sample Y_p(1/2)=0 mod p and W_p(1/2)=p mod p^3; finite evidence only.
Independent modular Gaussian elimination verified the determinant formula for p=7,13,19,31,37,43,61, with determinant residues respectively 5,8,5,5,32,5,56.
Digit witnesses (p; a0,a1,d0,d1,carry,Cp,E2): 13;11,5,7,6,71,0,0 | 19;8,4,1,9,5,12,0 | 37;23,18,24,11,179,11,0 | 373;24,176,294,291,227,196,0.
Verifier: d25_triangular_hadamard_rank_digit_20261101.py in the same portable_direct folder, with actual execution (not native H0/B0).

BRC application: generic coefficient observer dimension p is required for this unrestricted quadratic form, while the structured hypergeometric and precision-bounded observer reduces to (s,d,Cp) with the explicit integer carry. Scope is classical auxiliary coefficient vectors, signed pair/truncation relation, Hadamard and p^3 future operations; no native X6 identification or whole-model lower bound is claimed.

Next mathematics: prove or precisely refute the general Y_p(1/2) CM selector for both 13/19 classes and derive E1/E2 via an actual arithmetic/CM trace preserving triangular and Hadamard source information, rather than from a finite fit. Frozen mother goal A_p=p mod p^3 for residues 13/19 remains open.

Control handoff: the Research lane historical service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94 was read-only recovered at bridge #6637; exact continuation #6638 definitively FAILED with UPSTREAM_CODE_REVIEW_REQUIRED, without a new Source claim/run/checkpoint. Project #1558 owns code-review/deployment remediation; #1559 owns original 373 H0/B0. Do not replay #6638, borrow maintenance identity, adopt neutral staging as scientific progress, or claim native admission. Original Source authority and frozen scientific pin remain distinct.
