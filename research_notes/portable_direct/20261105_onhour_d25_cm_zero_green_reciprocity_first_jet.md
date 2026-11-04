# D25 — CM-zero slope/defect reciprocity and signed first-jet information loss
2026-11-05 · Research author-side · UNREVIEWED / NOT_ADMITTED.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3
Research lane: chatgpt-research-onhour-enterprise-math-20260923 (distinct from maintenance).

## Scoped theorem A: reciprocal at a CM zero

For p>=5, d in {3,4}, set C=(d-1)/d² and use the original Sun polynomials:
F_d(X)=sum_{k=0}^{p-1} (1/d)_k(1-1/d)_k/(k!)² X^k (mod p),
E_d=(F_lift,d²-H_lift,d(X(1-X)))/p² (mod p).
The previously author-proved (not admitted) exact results give
E_d=C X^p Q_d and
B_C(F_d²,Q_d)=2(1-X^p)-2(1-X)F_d³,
where u=X(1-X), v=1-2X and
B_C(f,g)=u²(fg''-f'g'+f''g)+uv(fg'+f'g)-4Cufg.

Assume a point x in a characteristic-p extension satisfies x^p=1-x, u(x)!=0 and F_d(x)=0. Then the root is simple, Q_d(x), E_d(x) are nonzero and

    Q_d(x) = x/(u(x)² F'_d(x)²),
    E_d(x) F'_d(x)² = C/u(x).                     (1)

Proof: f=F_d² has f=f'=0 and f''=2F_d'² at x, so B_C(f,Q)(x)=2u(x)² F_d'(x)² Q_d(x). The Green right-hand side equals 2x. As u(x)!=0, x!=0, and 2 is a unit, both factors F'_d(x),Q_d(x) must be nonzero. Solve and use E=C x^p Q=C(1-x)Q. QED.

In the D25 target classes p≡13,19 (mod24), work in F_p[s]/(s²-2), with
x_3=(2+s)/4, x_4=(3+2s)/6. Their u values are 1/8 and 1/36; Frobenius interchanges x with 1-x. Therefore, *conditional on the actual finite-field zero of both periods*,

    E_3(x_3) F'_3(x_3)²=16/9,
    E_4(x_4) F'_4(x_4)²=27/4,                    (2)

and the value part of the signed defect observer reduces exactly to

    -E_3(x_3)+E_4(x_4)
    =-16/(9 F'_3(x_3)²)+27/(4 F'_4(x_4)²).       (3)

This eliminates the expensive Q-value computations in this observer and preserves original sources/signs. It is not a full third-digit cross-model proof.

## Scoped theorem B: Legendre descent and observer parity

For p>=5 and d=3 or 4 let n=floor(p/d). The two upper hypergeometric parameters reduce mod p to {-n,n+1}; their finite coefficients agree with those of the terminating series
_2F1(-n,n+1;1;X)=P_n(1-2X). Thus

    F_d(X)=P_n(1-2X) (mod p),
    F_d(1-X)=(-1)^n F_d(X),
    F'_d(1-X)=(-1)^(n+1) F'_d(X).                 (4)

At the two original quadratic observation points, Frobenius therefore fixes F'_d(x_d)². By (2), E_d(x_d) is also in F_p when F_d(x_d)=0. The first-jet type itself splits:
- p≡13 mod24: n_3 even, n_4 odd, so F'_3(x_3)∈s F_p while F'_4(x_4)∈F_p.
- p≡19 mod24: n_3,n_4 even, so both derivatives lie in s F_p.

This is a precise observer/Frobenius character split, not a claim about the native H0/B0 semilinear Frobenius.

## Scoped theorem C: flux-value compression loses derivative information

At an ordinary CM zero x with u(x)!=0, let L_C F=uF''+vF'-CF=0. Choose a *local* solution G of L_C G=0 with G(x)=1,G'(x)=0. These local series jets exist through orders <p by the ordinary-point coefficient recursion (inverting only indices smaller than p). Put H=F G. Then the symmetric-square operator T_C annihilates H to the same jet order. One has H(x)=0, H'(x)=F'(x)!=0, and the Green Lagrange identity yields
D B_C(F²,H)=F² T_C H+H T_C(F²)=0.
At x, B_C(F²,H)=2u² F'² H(x)=0. Hence it is zero to the available local jet order.

Thus Q and Q+lambda H have identical local Green flux and the same value at x, but their derivatives differ by lambda F'(x). Accordingly the original E'_d(x)=C(1-x)Q'_d(x) changes by lambda C(1-x)F'(x) !=0 for lambda !=0. This is a **scoped observer-fiber witness**: scalar Green flux at the CM root uniquely specifies the defect VALUE, but not the derivative demanded by the signed weighted observer. The globally fixed original polynomial Q remains unique under its full inhomogeneous recurrence and endpoint constraints. Preserve Q' or an equivalent second observer rather than collapsing to value-only flux.

## Exact computation and next action

A standalone standard-library integer/finite-field checker constructs F independently from its hypergeometric coefficients and Legendre representation, constructs Q using the previous exact Green recurrence, and verifies (2), (4), Frobenius character and nonzero slopes. All 166 primes <=5000 with p≡13,19 mod24 and both models: 332 model-prime instances, all F(x)=0 and all checks PASS, 0 failures. These finite zeros support but do not establish the all-prime CM-zero hypothesis.

Anchor tuples (p,d,E_d(x),F'_d(x)): (13,3,6,11s), (13,4,1,7), (19,3,18,15s), (19,4,17,3s), (139,3,138,126s), (139,4,122,3s), (373,3,132,316s), (373,4,137,193). Earlier *independent full p³ convolution* witnesses agree on the displayed E values; the present checker uses Green transport rather than rerunning those convolutions.

BRC reuse: COMPOSE_APPLIED. Carrier=(original d, p, valuation/provenance, F,F',Q,Q', operation tag); signed complex/quadratic amplitudes and the derivative-before-Frobenius observer are retained. The value quotient is exact on the CM-zero fiber, whereas the future derivative observer does not factor through that quotient. No native X6 spatial proof or native H0/B0 benchmark is claimed.

Next precise science: combine the reduced value (3) with the original p-adic period-square/derivative observer and derive a genuine identity for the remaining signed first-jet combination
    (3s/4) C_3(1-x_3) Q'_3(x_3) - (s/6) C_4(1-x_4) Q'_4(x_4).
Test at p=13,19,139,373; seek a source-preserving terminal Green/WZ certificate proving W_p-V_p=0 mod p³, then the frozen mother Delta_p-R_p=0 mod p. Fixed p=373 same-class original native H0/B0 [X]U mod139129, module rank, semilinear Frobenius, kappa and independent replication remain PENDING_OWNER/NOT_EXECUTED under #1559.

Historical request onhour-d25-20261104-1702-continuation-read: FAILED/SOURCE_TREE_SIZE_LIMIT, not replayed. Native Research session/claim/run/checkpoint/Result: NOT_ESTABLISHED/NOT_ADMITTED. Earlier three staging uploads remain independent; no promotion or merger. This artifact is GitHub author-side evidence only.