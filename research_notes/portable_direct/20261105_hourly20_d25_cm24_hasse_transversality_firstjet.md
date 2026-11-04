# D25: CM(−24) Hasse first-jet transversality, inert nonvanishing, and conditional p² root lift

Date: 2026-11-05. Status: **AUTHOR-DERIVED / PROVED IN STATED SCOPE / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED**.
Task lineage: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Original frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. This is a portable auxiliary elliptic/CM observer and **not** the native H0/B0 373 experiment.

## 1. Universal exact polynomial differential certificate (proved)

For every prime p≥5, let m=(p−1)/2 and put

H_p(t) = Σ_{k=0}^m binom(m,k)^2 t^k,
Q(t) = t^4−140t^3+294t^2−140t+1,
A(t)=16t(1−t²), B(t)=1+2t−7t²,
C_p(t)=A(t) H'_p(t)+B(t) H_p(t),
T(t)=1+18t−23t².

Then the following identity holds in **the full polynomial ring F_p[t]**, not merely after reduction modulo Q:

**A C'_p − T C_p + [Q+64t(t−1)²] H_p = 0.**  (1)

Proof. The exact hypergeometric equation for H_p is

t(1−t)H''_p+[1+(2m−1)t]H'_p−m²H_p=0.

Since 2m≡−1 and m²≡1/4 (mod p), this becomes

t(1−t)H''_p+(1−2t)H'_p−H_p/4=0.

Substitution in the derivative of C_p gives

C'_p=(1+18t−23t²)H'_p+(6−10t)H_p=T H'_p+(6−10t)H_p.

Eliminating H'_p by C_p=AH'_p+BH_p yields

A C'_p−T C_p=[A(6−10t)−TB]H_p
             =−[Q+64t(t−1)²]H_p,

the identity (1), with no assumption that the candidate split-class zero vanishes. QED.

## 2. Exact transversality at all CM branches (proved)

disc(Q)=2^32·3^6. Thus for p≥5 the four roots are simple. Q(0)=1, Q(1)=16, Q(−1)=576, hence all roots a in F̄_p avoid 0, ±1. At such a root, if C_p(a)=0, then from (1)

**C'_p(a)=−4 (1−a)/(1+a) H_p(a).**  (2)

Moreover H_p(a) ≠ 0: if H_p(a)=0 then C_p(a)=0 and A(a)≠0 force H'_p(a)=0. This is impossible. Indeed H_p(0)=1, deg H_p=m<p, and at a∉{0,1} the ordinary-point second-order differential equation uniquely determines the Taylor series from the first two coefficients through degree m; all relevant factorials <p are invertible. Therefore (2) is a nonzero derivative. Every intersection of C_p=0 with Q=0 is transverse, for every p≥5, without first proving that such an intersection exists.

The earlier inversion-symmetric observer D_p=t^{−(p+3)/4} C_p in A_p=F_p[t]/(Q), and its two-coordinate field norm, remain defined for p≡5 (mod 8). Equation (1) retains the full quartic branch and the original Hasse value/derivative; the two-coordinate norm is an exact readout for vanishing, not a replacement for future branch-level derivatives.

## 3. Inert-class norm is always nonzero (proved using classical Deuring CM reduction)

For p≡13 (mod 24) the prime is inert in K=Q(√−6), since (−6/p)=−1. Every root a of Q gives the Legendre curve E_a: y²=x(x−1)(x−a), with good reduction for p≥5: a and (1−a) are p-adic units because Q(0)=1 and Q(1)=16. Its j-invariant 256(1−a+a²)^3/[a²(1−a)²] satisfies the Hilbert class polynomial

H_{−24}(J)=J²−4834944J+14670139392.

For an entirely algebraic check, with U=256(1−t+t²)^3 and V=t²(1−t)²,

U²−4834944 U V+14670139392 V²
 = 4096 Q(t) (t⁴+136t³−120t²−32t+16)
   (16t⁴−32t³−120t²+136t+1).    (3)

By the classical Deuring reduction criterion, E_a is supersingular at all these inert good primes. Its Legendre Hasse invariant is proportional to H_p(a), so H_p(a)=0. The polynomial H_p has simple roots away from 0,1 by the same ODE argument in §2, hence H'_p(a)≠0; thus C_p(a)=A(a)H'_p(a)≠0 for all four roots. Consequently, in the earlier norm-compressed observer,

**N_{F_{p²}/F_p}(t^{−(p+3)/4} C_p(t)) ≠ 0 for every p≡13 (mod 24).** (4)

This upgrades the previously finite-tested inert-class **nonvanishing** to a sourced general theorem, without inferring the still-open split-class vanishing. Deuring criterion reference: https://link.springer.com/article/10.1007/s10231-024-01528-x (Theorem 4.1); CM reduction background https://link.springer.com/article/10.1186/s40687-015-0040-y. The j-minimal polynomial and factorization are exact arithmetic checks, not a numerical CM guess.

## 4. Unique mod-p² first-jet root lift (proved conditionally)

Take p≡5 (mod 24) and assume Q | C_p mod p. (That split-class vanishing remains a uniform **CONJECTURE**, despite 85/85 finite checks to p≤5000 and the earlier 281/281 checks to p≤20000.) Let

R=(Z/p²Z)[t]/(Q), α=t mod Q.

The ring R is finite étale over Z/p²Z and reduces to F_{p²}×F_{p²}; the derivative C'_p(α) is a unit by §2. Write C_p(α)=p u. There exists a **unique** δ in R/pR such that ζ=α+pδ satisfies C_p(ζ)=0 mod p², namely

**δ=−u/[C'_p(α) mod p]
     =(1+α)u/[4(1−α)H_p(α)] mod p.** (5)

Taylor expansion proves the statement and uniqueness. It preserves each algebraic CM branch through the finite étale algebra; it does not assert a crystalline Frobenius lift or prove the split-class hypothesis.

Direct integer certificates with coordinate basis (1,t,t²,t³) are:

- p=29: u=(17,8,16,17), δ=(19,20,28,9); C_p(t+29δ)=0 in (Z/841)[t]/Q.
- p=53: u=(49,21,2,24), δ=(0,41,33,10); C_p(t+53δ)=0 in (Z/2809)[t]/Q.

## 5. Exact verification and scope

The Python standard-library checker d25_cm24_hasse_transverse_lift_20261105.py executed on 2026-11-05:

- p≡5 (mod 8), 5≤p≤5000: **168 primes**, full coefficient-by-coefficient polynomial syzygy (1) and quotient first-jet relation;
- split p≡5 (mod 24): **85** finite checks of C_p mod Q =0, explicitly *not* a general proof;
- inert p≡13 (mod 24): **83** checks of H_p mod Q =0 and C_p mod Q≠0, corroborating the general sourced result;
- split primes p≤500: **12** direct mod-p² root substitutions and derivative inverse certificates.

All assertions passed. Modular arithmetic uses exact integers, binomial coefficients, finite quotient ring arithmetic and direct evaluation; it does not simulate original-class crystalline H0/B0, [X]U, or native Frobenius.

## 6. Next action and intact parent objective

Seek an exact CM isogeny, character-sum, or finite-field hypergeometric identity proving Q|C_p for **all** p≡5 (mod 24), now with transversality and explicit p² root-lift response available. Separately, for the **frozen native** p=373 original-class task obtain authenticated H0/B0 divided-power module, [X]U mod p², rank/semilinear direction and normalization η; then compare native κ and Δ_p−R_p while retaining odd Hesse/Green observer. This report grants no task CLAIM, OPEN, checkpoint, Result, review or P000 change.

Canonical Source continuation read: research-hourly20-20261105-0117-fresh-continuation, SUCCEEDED at Source daa92f7892541c5da16d2a7dbfcd28782b1214af, existing checkpoint SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED; new execution_authorized=false. Historical Source completed_units and prior_contribution_ids are preserved separately, not overwritten by this author-side note.
