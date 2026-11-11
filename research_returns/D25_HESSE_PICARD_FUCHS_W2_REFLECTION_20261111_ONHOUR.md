# D25: original-Hesse Gauss–Manin, Picard–Fuchs bridge, and a second-digit reflection theorem

Date: 2026-11-11 (UTC). Scope: TASK_RESEARCH mathematical author evidence, **AUTHOR-PROVED / UNREVIEWED / NOT_ADMITTED**. This is a durable independent scientific source, not a native Source semantic checkpoint or frozen Result.

## Exact provenance and frontiers

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; original publication TP2-B6F4FC938FF94941C1B7; immutable scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Current own bridge-lane run historically opened as RUN-d3deee35d5e9e40b9358ebbb under CLAIM MCP-6de695b532e654210160c52c, original request onhour-d25-20261111-registered-open-v1 (bridge issue #6777). Original conversation: chatgpt-research-onhour-enterprise-math-20260923; Researcher EM-ENTERPRISE-9C9163, activity RA-629C868A22A736334628BEFA. The bridge's earlier original-curve Hesse W2 and Weierstrass equivalence are in issues #6779 and #6782; the latter is confirmed uploaded staging, **not** assumed Source-published. The earlier publish_checkpoint #6781 entered OUTCOME_UNKNOWN; reconcile was requested at #6783. These are provenance, not proof of a later successful native publication.

The inherited D24 UR/JT0, 19 native units, 2 Green units, ordinary Hesse norm/Hilbert-90, W2 Hesse cubic, coefficient-level C_p and explicit Weierstrass conversion are CONSUMED, NOT RECREDITED. This note adds a new connection/Picard–Fuchs calculation and a proved polynomial congruence. It retains both signed ports; it does not identify a coefficient involution with crystalline Frobenius.

## I. Exact Gauss–Manin for the original Hesse curve

Work over Z[1/6,a,a^{-1},(a^3-1)^{-1}], with t=a^3, d=t-1, and the smooth Hesse cubic x^3+y^3+z^3-3axyz=0. Use the *explicit projective isomorphism* recorded in issue #6782 to the Weierstrass equation

    Y^2 = X^3 + A X + B,
    A=-27a(a^3+8),   B=54(a^6-20a^3-8).

Set e0=[dX/(2Y)] and e1=[X dX/(2Y)]. The Hesse residue omega_H=[dx/(3(y^2-ax))] on z=1 satisfies omega_H=2e0 under that isomorphism. The discriminant factor is

    D = 4A^3+27B^2 = -5038848(a^3-1)^3 = -2^8*3^9*d^3.

For k=0,1,2, let I_k=X^k dX/Y^3. With f=X^3+AX+B, the exact-differential relation

    d(X^r/Y)=[r X^(r-1) f - (X^r/2) f']/Y^3 dX

reduces all I_k to e0,e1. The reduction is

    I_0 ≡ (2/D)(9B e0 + 6A e1),
    I_1 ≡ (2/D)(2A^2 e0 - 9B e1),
    I_2 ≡ (2/D)(-3AB e0 - 2A^2 e1).

The congruence is equality of algebraic de Rham classes, not a numerical approximation. These formulas follow by solving polynomial identities against r=0,1,2 exact differentials; D is a unit in the declared base. Differentiating Y^2=f with respect to a and reducing I_0,I_1,I_2 gives the complete two-dimensional Gauss–Manin matrix, in column convention:

    nabla_(∂a) (e0,e1) = (e0,e1) M_a,
                        [ -3a²/(4d)       3a(t+8)/(4d) ]
    M_a =               [ -1/(12d)        3a²/(4d)    ].

The trace is zero. Since da/dt=1/(3a²), with t=a^3, the corresponding matrix is

                        [ -1/(4d)         (t+8)/(4ad) ]
    M_t =               [ -1/(36a²d)       1/(4d)    ].

The two geometric forms omega_H, nabla_(∂t)omega_H are a *cyclic rank-two basis*: in (e0,e1) coordinates their columns are

    Q_t = [ 2     -1/(2d)        ]
          [ 0     -1/(18a²d)     ],
    det(Q_t) = -1/(9a²d), a unit for every p>=13 in the target primes.

This gives an explicit integral geometric basis interface to the native missing H0/B0 comparison. It is still not the missing p-adic divided-power Frobenius matrix.

A second exact differentiation using M_t yields the relative Picard–Fuchs equation for a horizontal period y(t) of omega_H:

    t(t-1)y'' + (5t-2)/3 y' + y/9 = 0.                         (PF-t)

Write u=1/t and y=t^(-1/3)v(u)=a^(-1)v(u). Then (PF-t) becomes

    L[v] := u(1-u)v'' +(1-2u)v' -(2/9)v =0,                    (PF-u)

the Gauss hypergeometric equation with parameters (1/3,2/3;1). Its unique normalized power-series solution over Q is

    F(u)=sum_(k>=0) c_k u^k,   c_k=(3k)!/[27^k(k!)^3],
    c_(k+1)/c_k=(3k+1)(3k+2)/[9(k+1)^2].

Thus the **existing frozen ordinary Hesse polynomial A_p(u)** is precisely the first residue-field truncation of an algebraically derived original-Hesse Picard–Fuchs solution. This is a relation of specified differential equations and coefficients; the crystalline Frobenius observer is still a distinct pending comparison.

## II. New exact second-digit polynomial reflection theorem

**Theorem (all primes p≡1 mod 3, p>=7).** Write p=3n+1, so n is even. Over (Z/p²)[u] let

    P_p(u)=sum_(k=0)^(2n) c_k u^k,
    A_p(u)=sum_(k=0)^n c_k u^k.

All denominators 27^k(k!)^3, 0<=k<=2n<p, are p-units. Then

    L[P_p](u) = 0 (mod p²),         P_p(1-u)=P_p(u) (mod p²),  (REFLECT)
    P_p(u) = A_p(u) (mod p).

Proof. The recurrence for c_k kills all coefficients of L[P_p] below degree 2n; the final coefficient is exactly

    -[(6n+1)(6n+2)/9] c_(2n) u^(2n)
       = -[2p(2p-1)/9]c_(2n)u^(2n).

The factorial valuation v_p(c_(2n))=1 because 2n<p and 3(2n)=2p-2. Hence the final coefficient is divisible by p². For n<k<=2n, v_p(c_k)=1, and for 0<=k<=n v_p(c_k)=0. This proves both the differential congruence and P_p≡A_p (mod p).

The operator L is invariant under u↦1-u, so Q(u)=P_p(1-u) is another polynomial solution of degree <=2n. The coefficient recurrence for any such solution at degrees 0,...,2n-1 is

    (k+1)^2 q_(k+1)=((3k+1)(3k+2)/9) q_k (mod p²).

Since 2n<p, each (k+1)^2 is invertible modulo p². Therefore Q=P_p(1)*P_p coefficientwise, and evaluation at u=1 gives P_p(1)^2=1 (mod p²). Mod p, the coefficient identities (1/3)≡-n and (2/3)≡n+1 show

    A_p(u) ≡ {}_2F_1(-n,n+1;1;u) = Legendre_n(1-2u) (mod p).

Because n is even, P_p(1)≡Legendre_n(-1)=1 (mod p). As p is odd and P_p(1)^2=1 modulo p², this forces P_p(1)=1 modulo p². Hence Q=P_p, proving REFLECT. ∎

For the original quadratic CM source u=(2-T)/4 in R_2=(Z/p²)[T]/(T²-2), conjugation sigma(T)=-T satisfies sigma(u)=1-u exactly. Thus REFLECT implies **sigma(P_p(u))=P_p(u)** at both conjugate source ports modulo p²; the T-coordinate of P_p(u) vanishes modulo p². This holds for every target prime p≡13 or 19 (mod 24). The residue-field supersingular condition A_p(u)=0 (mod p) then makes P_p(u) a scalar p-times-first-digit readout.

The exact truncated ordinary coefficient A_p has a quantified PF lift defect:

    L[A_p](u) = -[p(p+1)/9] c_n u^n.

The additional **p-adic tail** E_p=P_p-A_p=sum_(k=n+1)^(2n)c_k u^k cancels this defect modulo p², while sigma(P_p(u)) is even. This is a canonical two-digit *Picard–Fuchs horizontal polynomial lift*, not a native Frobenius solution and not a proof of the mother LIFT identity.

## III. Integer p=373 certificate and actual check coverage

For p=373, n=124, modulus 139129, T²=2, u=(2-T)/4, direct exact computation by two independent methods (coefficient recurrence and modular factorial ratios) gives:

    A_373(u)     =112646+57442T =373(302+154T)       (mod 139129),
    P_373(u)     =  8952+0T    =373*24                (mod 139129),
    P_373-A_373  = 35435+81687T=373(95+219T)        (mod 139129).

The second digit of A_373 on the conjugate port is 302-154T; the correction tail has the opposite T-coordinate, so the new P_373 first digit is scalar 24. The exact polynomial reflection theorem proves the parity cancellation for *every* stated target prime, not merely the finite checks.

Additional independent finite regression: p=13,19,37,43,61,67,109,139,157,163,181,211,229,277,283,307,331,349,373,379,397,421,463 (23 target primes below 500) checked by coefficient recurrence for P_p(u) and the zero T-coordinate. Exact checked examples (P_p(u)/p modulo p): p13→11, p19→8, p37→23, p43→31, p373→24. The cited finite computations support reproducibility; the theorem follows from the proof above.

## IV. Current mother objective and minimal next native operation

The original D25/LIFT target remains: prove or correctly classify Delta_p=(G_p h-1)/p ≡ R_p (mod p) at every p=13/19 (mod 24) with frozen original source ports, signed odd branch and native H0/B0/semilinear Frobenius. The present result gives a full de Rham connection, a cyclic basis, the precise Picard–Fuchs source of A_p, and a canonical W2 even horizontal truncation; it eliminates a geometric basis ambiguity and offers a **discriminating** native comparison. It does not assert that P_p/p, C_p/p, or A_p/p equals the crystalline kappa, eta, or Delta_p-R_p.

Next: bind the original source's divided-power fixed H0/B0 and Frobenius lift to (e0,e1) or the cyclic basis Q_t, compute a true 2×2 sigma-semilinear native [X]U modulo 139129 on the p373 original curve and its conjugate, and compare its normalized omega+6*nabla_lambda(omega), kappa and Delta/R readouts with the three distinct coefficient objects A_p/p, C_p/p and P_p/p. Preserve full matrix and signed ports. Independently check a source-approved H0/B0 basis-change matrix; missing native API/implementation should be recorded as a precise task-bound support request rather than replacing the experiment with this theorem.

No independent review, formal checker, or canonical Result acceptance is claimed.

## V. Exact original E3 port alignment (corrective source-bound discriminator)

The frozen source's *unmodified original E3 model* is

    E3_v: y²+xy+(v/27)y=x³,   v=(2-T)/4.

Here `v` must be distinguished from the Hesse parameter `a` and the Hesse inverse parameter `u=1/a³`. Direct computation of its Weierstrass invariants gives

    c4(E3_v)=(9-8v)/9,
    Delta(E3_v)=v³(1-v)/27³,
    j(E3_v)=27(9-8v)³/[v³(1-v)].

In the exact quadratic field T²=2, the resulting **signed port alignment** is

    j(E3_v)=2417472+1707264*T,
    j(Hesse_{a³=1/v})=2417472-1707264*T,
    j(Hesse_{a³=1/(1-v)})=2417472+1707264*T.

Thus the Hesse model `a³=4+2T` in sections I–III belongs to the CM **conjugate j-port** of E3_v; to match the E3_v j-port, start instead with the sigma-conjugate Hesse parameter `a_bar³=4-2T`. At p=373 (mod 139129), j(E3_v)=52279+37716*T, whereas j(Hesse_{a³=4+2T})=52279+101413*T. These are distinct in the quadratic ring. The p² Picard–Fuchs reflection theorem remains valid for **both** ports and its P_p(v) is σ-even, but the isomorphism or source-prescribed isogeny, coordinate/differential gauge, and H0/B0 basis comparison between Hesse_{a_bar} and *unmodified* E3_v still require explicit verification. Matching j alone does not supply the needed native comparison or its signed operator orientation.

This correction supersedes any shorthand in the preceding sections or prior W2 staging that identifies the particular `a³=4+2T` Hesse curve directly with E3_v at the same signed T-port. The mathematical matrix and reflection statements are unchanged as **Hesse-family statements**. Preserve `T↦-T` and both odd observables until a source-authenticated full two-column comparison is made. Native [X]U and κ/Delta-R remain NOT_RUN.
