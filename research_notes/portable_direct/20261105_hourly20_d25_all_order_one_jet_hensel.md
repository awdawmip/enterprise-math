# D25 — all-order one-jet Gauss recurrence and p-adic Hensel lifting

Date: 2026-11-05 (+08). TASK_RESEARCH; logical Research lane: chatgpt-research-hourly-enterprise-math-20260923.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Status: AUTHOR-DERIVED EXACT ALGEBRA / 94-PRIME FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## All-order theorem

Let p=6n+1>=7 be prime, x=1/2, u=p-1, and
G(z)=_2F_1(-n,-2n;1-p/2;z), Psi(z)=G(z)(G(z)+12zG'(z)), q_m=G^(m)(x).
The full derivative sequence is determined exactly over Q by q_0=g=G(x), q_1=v=G'(x) and

    q_(m+2) = u*q_(m+1) + [4*m*(m-1)-2*m*(u-2)+8*n^2]*q_m,  m>=0.        (1)

Proof. Gauss' ODE is
    z(1-z)G''+[1-p/2-(1-3n)z]G'-2n^2 G=0.
At x=1/2 its coefficients satisfy a=1/4, a'=0, a''=-2, b=-u/4, b'=(u-2)/2.
After m differentiations and Leibniz:
    (1/4)q_(m+2)-(u/4)q_(m+1)+[-m(m-1)+m(u-2)/2-2n^2]*q_m=0,
which proves (1). This is a rational-polynomial identity for every m.

G terminates at degree n and has p-integral coefficients: the factors (1-p/2+j), j<n, and k!, k<=n, are p-units. Hence for any 2<=r<=p and h in p Z_p, all factorials m!, m<r, are p-units and

    G(x+h)  = sum_(m=0)^(r-1) q_m*h^m/m!         (mod p^r),
    G'(x+h) = sum_(m=0)^(r-1) q_(m+1)*h^m/m!     (mod p^r).   (2)

Higher Taylor coefficients are p-integral, and terms with m>=r vanish modulo p^r.

## Constructive arbitrary-digit Hensel lift

Assume Psi(x)=0 (mod p) and A=Psi'(x) is a p-unit, which are the previous first-digit and simple-root premises on the D25 target prime classes. From the first jet alone:

    A = 14*g*v+6*(v^2+g*q_2), q_2=u*v+8*n^2*g.

Starting with h_1=0, suppose Psi(x+h_e)=0 modulo p^e. Define

    t_e = -[Psi(x+h_e)/p^e]*A^(-1) (mod p);
    h_(e+1) = h_e+t_e*p^e,  e=1,...,r-1.        (3)

Then Psi(x+h_(e+1))=0 mod p^(e+1), and x+h_r is its unique root mod p^r reducing to x mod p. Proof: Taylor modulo p^(e+1) gives Psi(x+h_e+t p^e)=Psi(x+h_e)+t p^e Psi'(x) and Psi'(x+h_e)=A mod p. Equations (1)-(3) therefore evaluate the entire root from (p,g,v) without separately evaluating higher derivatives. The implementation declares 2<=r<=p so all displayed inverse-factorials are units; higher precision can retain integral polynomial coefficients/divided-power data instead.

## Actual independent exact check

The companion standard-library Python executable d25_clausen_all_order_one_jet_20261105.py was run in this research turn. For each of the 94 primes p=1 mod6, 7<=p<=1200, at r=6 it independently compares (i) the first-jet-derived Psi(x+h) against (ii) direct evaluation by the original terminating hypergeometric recurrence, verifies the unit derivative, and verifies the final root modulo p^6. All 94 pass. The earlier p^4 roots for 13, 19, 373 are checked again.

  p   root mod p^6         Psi'(x) mod p    root mod p^4
  7   70137                3                508
  13  2137402              6                23888
  19  30557520             5                62406
  31  464142959            27               535417
  37  1785289572           23               1088300
  73  29205270272          57               11878524
  373 1705677423763125     211              7348554128

The newly proved recurrence is general; the stated numerical window is its finite check. No native H0/B0 or crystalline computation was performed.

## Typed BRC observer, mother goal and continuation

The observer for this exact local problem is (p,n,branch,g,v,q_m,h_e,Psi(x+h_e)) with signed polynomial and precision provenance. The first-jet compression is proved sound for the future operations of computing local G,G',Psi and Hensel roots through p^r. The distinct signed original 216 valuation shells, the previously derived Q=(W-Psi)/p=F+pH+p^2 I mod p^3, its base-p carries, and native X6/CM Frobenius carriers are preserved separately.

Frozen mother target: Delta_p-R_p=0 mod p on p=13,19 mod24; its existing scalar equivalent is W_p=p mod p^3. NEXT exact science unit: seek a non-tautological finite-sum telescope or branch-local closed evaluation of the signed F,H ports forcing the second-digit cancellation uniformly; reject/test proposed formulas against independently calculated p=13,19,373 inputs. The cubic I=T0+T1+T2+T3-gamma and earlier p4 one-jet results are inherited work, not newly completed units. Genuine original p373 H0/B0 [X]U mod139129, Frobenius direction, eta, kappa, and independent review remain open.

## Control provenance

Fresh read-only requests em-h20-20261105-2317-task-current and em-h20-20261105-2317-continuation-current returned SUCCEEDED, Source bc1c7c8acc203994682e06d6960f9785c55d3e26 (observed 2026-11-05 15:22 UTC). Existing native checkpoint remains SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, HANDOFF_READY/NO_LIVE_CLAIM, and successor route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. No verified own authorized session/CLAIM/OPEN or new native checkpoint exists for this portable author result. Existing Source, contributors, publication and their do-not-repeat entries are unchanged.
