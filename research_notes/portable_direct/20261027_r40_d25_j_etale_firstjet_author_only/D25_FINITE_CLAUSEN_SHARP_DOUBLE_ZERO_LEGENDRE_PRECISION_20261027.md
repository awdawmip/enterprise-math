# D25 finite Clausen: sharp double zeros, Legendre bridge, p-adic signed precision

2026-10-27; AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is same-author portable auxiliary mathematics, not native H0/B0, a Source CLAIM/OPEN/checkpoint, independent review or an admitted LIFT Result. Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7, scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, Taskbook blob 53a3ef039325534e3715add837f0eee332289984 remain unchanged.

## Reused antecedent
For every prime p=6r+1>=7, set A_r(z)=sum_{k=0}^r binom(r,k)binom(2r,k)(z/2)^k in F_p[z]. The already published *author-only* finite Clausen result in this PR proves C_{0,p}(z)=sum_{k=0}^{2r} c_k z^k mod p = A_r(z)^2, where c_k=(3k)!(2k)!/[216^k(k!)^5]. That antecedent is reused, not re-attributed. Earlier work proved only the conditional at-least-double zero at z=1; its sharp multiplicity and lifted signed precision were open.

## Theorem 1: all-prime simple roots and exactly double Clausen roots
The coefficient recurrence a_{k+1}/a_k=(r-k)(2r-k)/[2(k+1)^2] gives the exact differential equation
  z(2-z)A''+[2-(1-3r)z]A'-2r²A=0.
As 3r=(p-1)/2, over F_p this reduces to
  z(2-z)A''+(2-3z/2)A'-2r²A=0.                (E)
A(0)=1, A(2)=sum binom(r,k)binom(2r,k)=binom(3r,r) !=0 mod p, and deg A=r<p with a unit leading coefficient. At any multiple geometric root ζ (multiplicity m>=2), ζ is neither 0 nor 2. The first term of (E) has leading order m-2 with coefficient ζ(2-ζ)m(m-1) !=0 (since 2<=m<=r<p), while the other terms have order >=m-1, a contradiction. Hence gcd(A,A')=1 over F_p and C_{0,p}=A² has exactly r geometric roots, each of **exact multiplicity 2**, for every p=6r+1.

At any A(ζ)=0, C''(ζ)=2A'(ζ)^2 !=0 and C'''(ζ)/C''(ζ)=3A''(ζ)/A'(ζ)=-3(2-3ζ/2)/[ζ(2-ζ)]. Thus IF A(1)=0, then C(1)=C'(1)=0, C''(1)=2A'(1)^2 is a unit and C'''(1)=-3 C''(1)/2. The first nonzero jet at z=1 is exactly second order; do not infer that A(1)=0 holds for all target primes from this theorem.

## Theorem 2: entire-polynomial finite Legendre pullback
Let P_n denote the ordinary Legendre polynomial with P_n(1)=1. Since P_{2r}(x) is even, write P_{2r}(x)=L_{2r}(x²). Then
  A_r(z) = L_{2r}(1-z/2) in F_p[z].            (L)
Proof: B(z)=P_{2r}(sqrt(1-z/2)) is a true degree-r polynomial, B(0)=1. The Legendre ODE yields z(2-z)B''+(2-3z/2)B'+(2r)(2r+1)B/4=0. In F_p, 2r+1=-4r, so this is exactly (E). Equation (E) determines consecutive coefficients uniquely by unit multiplier 2(k+1)^2 for k<r; hence A=B. In particular A_r(1)=0 iff P_{2r}(x)=0 for x²=1/2. This is a new exact reduction, NOT a proof of universal target-class vanishing. For p≡13,19 mod24, (2/p)=-1 and x lies in F_{p²}, but this fact alone does not force a zero.

## Theorem 3: quantified lifted signed-branch defect
Define the **specific polynomial lift** A_r in Z_(p)[z] and Ctilde_r=A_r². Only Ctilde_r mod p=C_{0,p} is known; Ctilde_r is NOT identified with the original hypergeometric C_p modulo p²/p³, and not with native H0/B0.

IF A_r(1)=0 mod p, simple-root Hensel lifting produces unique ζhat∈1+pZ_p with A_r(ζhat)=0 and A_r'(ζhat) a unit. For δ=p^n u, n>=1, u∈Z_p^×,
  v_p(Ctilde_r(ζhat+δ))=v_p(Ctilde_r(ζhat-δ))=2n.
Taylor expansion and (E) at z=1 mod p give 2A'(ζhat)A''(ζhat)=-A_r'(1)² mod p, a unit. Hence
  v_p(Ctilde_r(ζhat+δ)-Ctilde_r(ζhat-δ))=3n,
  (Ctilde_r(ζhat+δ)-Ctilde_r(ζhat-δ))/p^(3n)
       = -A_r'(1)² u³ (mod p).                 (S)
The signed two-source contrast is invisible until digit 3n, although each scalar has valuation 2n. This holds for the stated Hensel ball and selected square lift, not arbitrary source maps or unknown H0/B0 operators.

## Exact author validation
Companion standard-library checker tests ODE, coefficient recurrence, entire-polynomial Legendre bridge (L), gcd squarefreeness, Clausen equality and derivative identities at p=7,13,19,31,37,43,61,67,73,79,103,109,211,373,997,1213; six target p=13,19,37,43,373,997 additionally undergo explicit Hensel root lifting mod p^7 with δ=p and δ=p² for (S). Local full author check PASS: p13 A'(1)=7 and signed residue 3; p19 A'(1)=1 and residue 18; p373 A'(1)=294 and residue 100. This is exact finite arithmetic, not an independent review. Original unabridged local note/checker/output SHA256 respectively:
  48263d83b4fbc3221869c67e424d7b1b7fbb33d3697fb915300027a42560500a
  4ad0010b14cc781e05554bde21575ea7269ab664bfb76192a09fec5cfaa1b3ff
  95838f238eddd5c8cb83ed57d71dc157357b7e0221e84e8db5d5a53673c38f36
The GitHub note/checker here are consumable condensed source, not claimed byte-identical to those local originals.

## Observer/BRC and unresolved fronts
Carrier: (root, signed p-adic offset, precision index n, unit u, exact lift identity); observation Ctilde mod p^e, future operations +/- exchange and differential jets. Reuses finite Clausen provenance, proves precise information-loss budget without erasing branch. An external z-polynomial is not a P000 native X6 slice map.

Target-class universal A_r(1)=0 (equivalently Legendre special-value zero) remains UNPROVED; original H0/B0 p373 [X]U mod139129, rank/eta/Frobenius and signed Delta-R remain PENDING_OWNER/NOT_RUN (#1559). UR V2 original 94687-byte SHA256=4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unverified; do not reprove its math. No current Source CLAIM/OPEN/checkpoint or predecessor completed units verified; a current-input-only continuation seed must retain completed_units=[] and receive full input readback before prepare. Existing quota=5/5 and Site static_machine_readonly/write_relay_enabled=false prohibit assuming native writer. Next independent scientific unit: prove/falsify all-target A(1)=0 or separately certify transfer from this auxiliary Ctilde observer to the actual C_p/W_p and original-class Frobenius.
