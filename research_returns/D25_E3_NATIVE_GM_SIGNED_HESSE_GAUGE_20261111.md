# D25/LIFT: native-original E3 Gauss–Manin matrix and signed Hesse isomorphism (2026-11-11)

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3` (not rebased). Original Research lane `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-ENTERPRISE-9C9163`. This is a new author-proved exact algebraic de Rham geometry unit, independently integer-checked for five primes; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM**. Source-fixed H0/B0 [X]U benchmark remains NOT_RUN.

## A. Explicit original E3 connection, not a j-only match

Let p≥13 with p mod24∈{13,19}, R_r=(Z/p^r)[T]/(T²−2), σ(T)=−T, v=(2−T)/4. Then σ(v)=1−v and v(1−v)=1/8. The unmodified original curve is E_v:y²+xy+(v/27)y=x³. The exact short-Weierstrass transformation

    X=36x+3, Y=216y+108(x+v/27)

gives Y²=X³+A X+B with A=24v−27, B=16v²−72v+54 and D=4A³+27B²=−6912v³(1−v), a unit at all specified primes. At the frozen signed port, A=−15−6T, B=24+14T.

Use the full rank-two algebraic de Rham basis e0=[dX/(2Y)], e1=[X dX/(2Y)]. The original E3 invariant differential is ω_E=dx/(2y+x+v/27)=6e0. In column convention ∇_(∂v)(e0,e1)=(e0,e1) M_v, the exact matrix is

    M_v=1/[12v(1−v)] · [[4v−3, 8v−9],[1, 3−4v]].

Proof: For I_k=[X^k dX/Y³], exact differentials d(X^m/Y) imply

    I0=(18B e0+12A e1)/D;
    I1=(4A² e0−18B e1)/D;
    I2=(−6AB e0−4A² e1)/D.

Since ∇e0=−(A' I1+B' I0)/4 and ∇e1=−(A' I2+B' I1)/4, substitution A'=24, B'=32v−72, D=−6912v³(1−v) gives precisely the stated M_v. No Frobenius is assumed in this derivation.

At the original quadratic CM port,

    M_v=(2/3)[[-1−T,−5−2T],[1,1+T]],
    Q_E=columns(ω_E,∇_(∂v)ω_E) relative to (e0,e1)
       =[[6,−4−4T],[0,4]], det(Q_E)=24.

Thus Q_E is a full integral cyclic basis for every target p, and the exact v-derivative port observer is

    ω_E+6∇_(∂v)ω_E=(−18−24T)e0+24e1.

At the conjugate port replace T→−T. The frozen `∇_λ` observer must first be transported via its actual λ↔v parameter map; the formula does not invent that mapping.

## B. Explicit E3 to matching-signed-port Hesse isomorphism

The previous Hesse choice a³=4+2T has j=2417472−1707264T, conjugate to original E3's j=2417472+1707264T. Match the original signed port using t=(1−v)⁻¹=4−2T, a³=t, r²=−3, s=ar. For all target primes p≡1(mod3), Norm_Fp²/Fp(t)=8=2³ gives a cube root a∈Fp²; 3a² is a unit for Hensel lifting. Also −3 is a square mod p, so r Hensel-lifts in Z/p^r. This introduces no extra coefficient-field extension.

The already derived invertible Hesse projective map (bridge issue #6782, with conjugate a) yields

    H_a: Y_H²=X_H³ + A_H X_H+B_H,
    A_H=−27a(t+8), B_H=54(t²−20t−8).

The original E3 short-model coefficients are A_E=−3(t+8)/t and B_E=−2(t²−20t−8)/t². Because s²=−3a²,

    A_H=s⁴ A_E,  B_H=s⁶ B_E;

therefore (X_H,Y_H)=(s² X_E,s³ Y_E) is an exact invertible geometric map over R_r. It identifies de Rham bases by

    e0_E=s e0_H, e1_E=s⁻¹ e1_H, ω_E=3s ω_H (ω_H=2e0_H).

For a subsequently obtained genuine 2×2 σ-semilinear Frobenius matrix in this geometry, the necessary basis-conjugacy check is

    F_E=G⁻¹ F_H σ(G),   G=diag(s,s⁻¹),

with σ(r)=r, σ(a) the chosen conjugate root. This is a check on a **native** matrix, not its construction. Preserve both signed T ports and all off-diagonal entries rather than passing to an unlicensed rank-one/norm quotient.

## C. Exact finite certificates, residual objective

Author checker executed exact integer operations modulo p² at p=13,19,37,43,373, checking roots/Hensel lifts, A_H=s⁴ A_E and B_H=s⁶ B_E, every entry of M_v by independent exact-differential formulas, and det Q_E=24. At p=373 (mod139129), r=89697, a=(91441,45860), s=(50569,16406), A_E=(139114,139123), B_E=(24,14), A_H=(90958,96462), B_H=(135673,1296), coordinates (1,T). Proof of the all-prime identities is algebraic as above; the finite check is a regression, not a formal proof or native Frobenius calculation.

Previously verified Hesse W2 Source checkpoint: `39366228ee4242e54a60f67351c7e42d521ae610`; previous author PF/port correction: `research_returns/D25_HESSE_PICARD_FUCHS_W2_REFLECTION_20261111_ONHOUR.md` commit `14ce778aa38fdf09777a19214046422911d517a7`. Original native run resumed in bridge #6788 with writer generation 2; every new write requires live native authorization. Native H0/B0/[X]U, σ-Frobenius/η, original κ and Δ_p−R_p are still open under owner/capability issue #1559 (PENDING_OWNER). Next: obtain frozen λ↔v and fixed H0/B0 definitions, compute native original p=373 [X]U in the prescribed basis and compare both columns and signed ports through Q_E and G. Do not repeat the older Hesse coefficient computations.
