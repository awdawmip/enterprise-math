# D25: Universal CM/Hasse residue-class theorem and exact first-jet transfer (2026-11-07)

Status: AUTHOR-SIDE PROVED (classical quadratic transformation, Hasse invariant, Deuring CM reduction); EXACT FINITE CHECKED; UNREVIEWED / NOT_ADMITTED. The Deuring step is an established external theorem used with its stated CM/good-reduction hypotheses. This does not assert a native Result.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Author-side research lane reference: chatgpt-research-hourly-enterprise-math-20260923; maintenance lane excluded. Consumes the prior aggregate Frobenius theorem at d7b9e35c199010b9a71f1dab7c8a0e22199c6489 and does not duplicate onhour X0(6) Fricke-cover work at 948d2a02273b7b4db83372b760ff69c5cc3a7c0e.

## Theorem 1: complete residue-class classification

For EVERY rational prime p >= 5 with p = 8k+5, define in F_p[z]

H_p(z) = SUM_{j=0}^k binom(3k+1,j) binom(k,j) z^j.

Then

    H_p(1/9) = 0 (mod p)  IF AND ONLY IF  p = 13 (mod 24).

Equivalently H_p(1/9) is nonzero for every p = 5 (mod 24). This discharges the previously open universal zero/nonzero classification, formerly tested only on finitely many primes.

### Algebraic Lemma 1: exact polynomial quadratic transform

Put d=(p-1)/4=2k+1 (odd), r=5k+3, s=7k+4, t=(p+1)/2; define

G_p(z)=SUM_{j=0}^r binom(r,j)binom(s,j)z^j,
L_d(u)=SUM_{j=0}^d binom(d,j)binom(3d,j)u^j.

The preceding source theorem established G_p(z)=(1-z)^t H_p(z) over F_p[z]. We additionally prove the polynomial identity

    G_p(4u(1-u)) = (1-2u)^p L_d(u)       in F_p[u].          (A)

Proof: the classical Gauss quadratic transformation, interpreted as a formal power series over Q, is

  2F1(1/8,3/8;1;4u(1-u)) = 2F1(1/4,3/4;1;u).

Reducing the first p coefficients mod p gives G_p on the left and L_d on the right: -r=1/8, -s=3/8, -d=1/4, -3d=3/4 in F_p, and denominators j! are invertible for j<p. Hence G_p(4u(1-u)) - L_d(u) is divisible by u^p in F_p[[u]].

The polynomial L_d satisfies the hypergeometric ODE

  u(1-u)L''+(1-2u)L'-(3/16)L=0.

The ODE is invariant under u -> 1-u. For polynomial solutions of degree <p, the coefficient recurrence (n+1)^2 a_{n+1}=(n(n+1)+3/16)a_n gives uniqueness up to constant, while the leading coefficient of L_d(1-u) is (-1)^d times that of L_d(u). Since d is odd, L_d(1-u)=-L_d(u). In F_p[u], (1-2u)^p=1-2u^p, so the right of (A) is symmetric under u->1-u, as is the left. Their difference is therefore divisible by both u^p and (1-u)^p. Its degree is at most p+d=10k+6 <2p=16k+10; hence the difference vanishes. QED.

### Lemma 2: the transformed value is an exact elliptic Hasse invariant

Let u_+ = (3+2 sqrt(2))/6 and u_- = (3-2 sqrt(2))/6. These algebraic numbers satisfy u(1-u)=1/36, hence 4u(1-u)=1/9, and neither 1-2u nor 1-1/9 vanishes at primes p>=5. For p=5 mod8, 2 is a nonsquare, u_+ and u_- reduce into F_{p^2} and u_+^p=u_-.

Consider the elliptic curve over Q(sqrt(2))

  E_u: y^2 = x(x^2+2x+1-u) = x((x+1)^2-u).

Its discriminant is 64u(1-u)^2, nonzero at every prime p>=5, so it has good reduction at either prime of Q(sqrt2) above p.

The Hasse invariant, coefficient of x^{p-1} in [x((x+1)^2-u)]^{(p-1)/2}, is

  A_p(u) = [x^{2d}]((x+1)^2-u)^{2d}
         = SUM_{j=0}^d (-u)^j binom(2d,j)binom(4d-2j,2d).

Its constant coefficient is binom(p-1, (p-1)/2)=1 in F_p. For 0<=j<d the ratio of consecutive coefficients, after reducing 4d=p-1, is

    (j+1/4)(j+3/4)/(j+1)^2.

The same initial value and coefficient ratios define L_d(u); hence

    A_p(u) = L_d(u)                  in F_p[u].               (B)

Since a smooth elliptic curve is supersingular exactly when its Hasse invariant vanishes, (B) converts the original binomial observation into a CM reduction test.

### Lemma 3: exact CM and Deuring classification

For the curve E_u,

    j(E_u) = 64 (1+3u)^3 / [u(1-u)^2]
           = 2417472 +/- 1707264 sqrt(2).

Consequently its two j-values solve

    J^2 - 4834944 J + 14670139392 = 0,

the Hilbert class polynomial of discriminant -24. The explicit CM classification for this j (CM discriminant -24, field Q(sqrt(-6))) is recorded by LMFDB and standard CM references. Thus E_u has CM by the full imaginary quadratic order of discriminant -24 over the algebraic closure.

Deuring's CM reduction theorem at a prime of good reduction p>=5 implies E_u is supersingular if p is inert in Q(sqrt(-6)), ordinary if p splits. Within p=5 mod8 there are only p=5 or 13 mod24, and quadratic reciprocity yields

    (-6/p) = +1 if p=5 mod24;
    (-6/p) = -1 if p=13 mod24.

From (A), G=(1-z)^t H, (B), and nonzero factors at z=1/9, the vanishing equivalences are

    H_p(1/9)=0 <=> G_p(1/9)=0 <=> L_d(u_+)=0
             <=> A_p(u_+)=0 <=> E_{u_+} supersingular
             <=> (-6/p)=-1 <=> p=13 mod24.

This proves Theorem 1.

## Theorem 2: unconditional first derivative and third-jet consequences

For all p=13 mod24, H_p(1/9)=0 is now proved. Differentiating (A) in characteristic p and using the prior G=(1-z)^t H gives, at u=u_+ or u_-,

    4(1-2u)(8/9)^t H_p'(1/9)=(1-2u)^p L_d'(u).

Here (1-2u)^{p-1}=-1, because u^p=1-u. Therefore the EXACT derivative bridge is

    H_p'(1/9) = -L_d'(u) / [4(8/9)^t]             in F_p.     (C)

The preceding proven squarefree theorem for H_p shows H_p'(1/9)!=0. The symmetry L_d(1-u)=-L_d(u) gives L_d'(1-u)=L_d'(u), so L_d'(u)^p=L_d'(u): the derivative in (C) lies in F_p^\times.

The earlier conditional aggregate Frobenius-carry statement for
C_p(z)=-z^p(1-z)H_p(z)^2 is now UNCONDITIONAL for every p=13 mod24:

    C_p''(1/9)=-(16/81)H_p'(1/9)^2 !=0,
    C_p'''(1/9)=5 H_p'(1/9)^2 !=0    in F_p.      (D)

It preserves the declared polynomial source ports and future differential observations; this is NOT yet an identity between separately p-adic source-indexed native tail terms, nor a proof of the full 216/2304 weighted p^3 congruence.

## External anchors and actual arithmetic checks

Exact CM discriminant/j-values: https://www.lmfdb.org/EllipticCurve/?field=2.2.8.1&jinv=-1707264%2Aa+%2B+2417472
Hilbert polynomial -24 table: https://citeseerx.ist.psu.edu/document?doi=ed861a61214ba1d1ade9209c231c9f001e8125ce&repid=rep1&type=pdf
Deuring reduction criterion: https://mathoverflow.net/questions/18591/reduction-of-cm-elliptic-curves and https://arxiv.org/abs/1209.5207

The source-attached standard-library Python program ran and PASSed 43 primes p<1000 in p=5 mod8, separately checking H vs L vs direct Hasse coefficient, both residue branches, the F_{p^2} Frobenius transfer and nonzero first derivative. For p=5,13,29,37,53,61 it independently checked the complete polynomial identity (A) coefficientwise. CM j minimal polynomial verified exactly. Examples: p=13 H=0, p=29 H=7, p=373 H=0, H'=369. Finite tests corroborate the general proof; the universal conclusion rests on Gauss's transform and CM/Deuring theorems.

## Continuation and source boundary

This author-side result proves the formerly open universal CM zero/nonzero classification. Next smallest scientific problem: connect the now universal exact first-jet and third-jet observations to the actual mod p^3 SECOND-DIGIT weighted 216/2304 transfer, with a two-legged source-aware finite cutoff operator; distinguish the onhour Fricke 6:8 common cover work. Frozen mother objective Delta_p-R_p=0 mod p for p=13,19 mod24 remains OPEN; original native p373 experiment NOT_EXECUTED.

During this turn authenticated site em_status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 retain UNKNOWN_PRESERVE. No new session/CLAIM/OPEN/Result/native checkpoint or review. REGISTER_PENDING; controller support remains enterprise-math issue #1558. P000 and native X6 provenance rules unchanged; classical CM arithmetic is an explicitly external auxiliary proof model.
