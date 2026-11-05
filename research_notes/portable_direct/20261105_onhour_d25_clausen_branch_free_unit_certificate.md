# D25 — branch-neutral Clausen unit certificate, exact scoped result (2026-11-05)

**Status:** AUTHOR-SIDE EXACT PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED.
**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research conversation chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance.

## Input (already established)

For prime p=6n+1>=7, let Q=Q_p(1/2), D=(z d/dz Q_p)(1/2), with Q_p(z)=sum_{k=0}^{p-1} (1/6)_k(1/3)_k z^k/(k!)^2. The preceding **signed** Clausen boundary theorem gives

$$W_p\equiv Q(Q+12D)-p^2T_p\pmod{p^3},\qquad T_p=B_p/p^2\bmod p.$$

B_p is the original explicit boundary double sum in research_notes/portable_direct/20261105_onhour_d25_clausen_p3_convolution_boundary.md. The accepted first-digit result supplies W_p = p mod p^2 for target primes p=13,19 mod24.

## Theorem 1: exact factor-valuation dichotomy

Put F=Q and G=Q+12D. Because B_p is divisible by p^2, the accepted first-digit congruence implies

$$FG\equiv p\pmod{p^2}.$$

Therefore exactly one of F,G has p-adic valuation **exactly one** and the other is a unit. Define X to be the p-divisible factor and Y the unit factor. This result holds for every target prime **without assuming** the observed residue-class rule p|Q.

## Theorem 2: one branch-neutral second-digit certificate

The original third-digit claim is equivalent to one unit equality:

$$\boxed{W_p\equiv p\pmod{p^3}\ \Longleftrightarrow\
\frac{X}{p}\equiv Y^{-1}(1+pT_p)\pmod{p^2}.}$$

Proof: divide the previously established signed identity by p, obtaining W_p/p = (X/p)Y - pT_p mod p^2. Multiply by the unit Y inverse. The mod-p digit (X/p)Y=1 follows from the accepted first digit; only the mod-p^2 lift remains open. No separate first-digit WZ certificate is needed.

In the observed Q-divisible branch, set A=Q/p mod p^2 and H=(12D)^-1 mod p^2. Then the equivalent single equation is

$$\boxed{A\equiv H+pH(T_p-H^2)\pmod{p^2}.}$$

Indeed, (12D+pA)A=1+pT_p mod p^2, and A=H mod p follows from the accepted first digit. This eliminates the earlier canonical-digit carry and the independent leading equation 12ad=1 mod p.

## Theorem 3: exact mod-p simple-zero lemma

The polynomial q_n(z)=sum_{k=0}^n binom(n,k)binom(2n,k)z^k is Q_p(z) mod p, and satisfies

$$z(1-z)q_n''+(1-\tfrac32z)q_n'-\tfrac1{18}q_n=0\quad\hbox{in }\mathbb F_p[z].$$

Proof: the Gauss coefficient recursion cancels all internal coefficients; the terminal coefficient vanishes because n+1/6=p/6=0 mod p. At any z_0 different from 0 and 1, z_0(1-z_0) is a unit. If q_n(z_0)=q_n'(z_0)=0, differentiating the ODE and inducting forces all its Taylor coefficients to vanish (n<p), contrary to q_n(0)=1. Thus any root away from 0,1 is simple. In particular p|Q at 1/2 implies D is nonzero mod p.

## Finite exact audit and interpretation

The checker consumes the already published independent original-binomial Clausen boundary checker; all 80 primes p=1 mod6 in [7,997] pass the ODE, exact first-digit factorization and the new branch-neutral normalized equality. Among them 45 target primes have p|Q and 35 complementary primes have p|(Q+12D); this split is **finite observation**, not an all-prime theorem. Target anchors (p,Q/p mod p^2,(12D)^-1 mod p^2,T_p) are (13,76,141,0), (19,84,46,12), (139,7588,7449,91), (373,65672,128336,196).

## Frontier

Next scientific unit: construct a p-dependent terminal certificate for the branch-neutral unit equality, retaining signed T_p, then explicitly verify the frozen interface to Delta_p-R_p. The all-prime proof of p|Q on the inert classes is **optional for this branch-neutral reduction**, and remains an independent possible line.

Native fixed p373 original H0/B0 divided-power object, [X]U mod139129, actual rank, semilinear Frobenius/eta/kappa, signed observer and independent replication remain NOT_RUN (existing support #1559). This author-side proof is neither native execution nor an accepted Result. Source continuation onhour11-20261105-1102-d25-exact: SUCCEEDED, execution_authorized=false, Source observation 2026-11-05T03:11:25.331436+00:00.