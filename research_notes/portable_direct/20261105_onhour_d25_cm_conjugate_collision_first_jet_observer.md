# D25 / SECOND-DIGIT-LIFT: CM conjugate collision and first-jet branch recovery

2026-11-05. TASK_RESEARCH, logical research lane `chatgpt-research-onhour-enterprise-math-20260923`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; Publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. **Author-side exact proof, executed exact regression, UNREVIEWED / NOT_ADMITTED**. This is separate from the native H0/B0 experiment.

## Exact branch data

Let (T^2=2) and take the two marked CM points
[
u_pm=	frac12pm T/4,qquad v_pm=	frac12pm T/3,
]
for the known rational functions
[
J_3(u)=27(1+8u)^3/[u(1-u)^3],quad
J_4(v)=64(1+3v)^3/[v(1-v)^2].
]
Direct rationalization establishes
[
J_3(u_pm)=J_4(v_pm)=j_pm=apm bT,
quad a=2417472,quad b=1707264=2^8 3^3cdot13cdot19.
]
The exact polynomial is (P(X)=X^2-4834944X+14670139392), with discriminant (8b^2).

**Theorem 1 (CM collision at the two smallest target primes).** For (p>3), ((2/p)=-1), in the unramified quadratic ring (R_r=(mathbb Z/p^rmathbb Z)[T]/(T^2-2)), one has (j_+-j_-=2bT). The two branches have identical scalar (jmod p) precisely when (pin{13,19}). In those cases (v_p(j_+-j_-)=1), so they separate modulo (p^2); at all other (p>3), their difference is a unit. Equivalently (v_p(operatorname{disc}P)=2) exactly at 13 and 19.

**Theorem 2 (unit first-jet branch recovery).** Mark the two branches by
[
u_pm(z)=(1pmsqrt{1-z})/2,quad
v_pm(t)=(1pmsqrt{1-t})/2,quad
J_3(u_pm(z))=J_4(v_pm(t_pm(z))).
]
At (z_0=1/2,t_0=1/9), their exact first derivatives are
[
t'_+(z_0)=8T/27,qquad t'_-(z_0)=-8T/27.
]
Thus the normalized observer (epsilon_{mathrm{jet}}=27t'(z_0)/(8T)in{+1,-1}) identifies the branch, with ( (t'_+-t'_-)/T=16/27) a unit modulo every (p>3), including (13,19).

**Theorem 3 (scoped non-descent).** At (p=13) or 19, no rule with input only (jmod p) can output the correct signed jet for both branches: the two inputs coincide, while their first-jet outputs are distinct. Keeping the marked first jet is an exact, observer-specific remedy; it does not require division by the nonunit (j_+-j_-).

## Proof

Substitution and rationalization of (J_3,J_4) give the two exact conjugate expressions and factorization of (b), proving Theorem 1. Implicit differentiation at the marked endpoint, where (u_pm'(z_0)=mp T/4), (v_pm'(t_0)=mp3T/16), gives
(t_pm' =J_3'(u_pm)u_pm'/[J_4'(v_pm)v_pm']=pm8T/27). All relevant denominators and derivative factors are units at the exceptional target primes; (T^2=2) and (p>3) make the first-jet difference a unit for all such primes. Theorem 3 follows from the resulting two-point fiber contradiction.

## Exact regression and next scientific dependency

The accompanying checker independently differentiates both rational CM maps, verifies the exact conjugate values, factorization, discriminant, and checks every 312 target primes (p<10000) in both classes (13,19mod24) (zero failures). Representative ((p,j	ext{ const},j	ext{ odd coeff},v_p(j_+-j_-),t'_+/T,(t'_+-t'_-)/T)mod p):
(13:(5,0,1,8,3)); (19:(7,0,1,1,2)); (139:(123,66,0,129,119)); (373:(59,43,0,97,194)).
At (p=13,19) respectively, the normalized lifted gap ((j_+-j_-)/(pT)mod p) is 4 and 10.

**BRC observer preservation:** keep HIGH_PLUS/LOW_MINUS branch, (1,T) coefficients, signed first jet, integer-lift versus finite-field reduction, original 216/2304 endpoints, upper-shell signed valuation and half-endpoint carry. Scalar (jmod p) is a lossy quotient for precisely these two small target primes.

**Next exact finite-(p) unit:** construct an integral terminating transform using the *marked* pair ((j,epsilon_{mathrm{jet}})), and test whether the original (p=13,19) half-endpoint carry (K_p) and signed upper shell (C_A) map to the true (W_p-V_pmod p^3). A (j)-only divided-difference proof would lose a (p)-digit at 13 and 19. The frozen mother target remains (Delta_p-R_pequiv0mod p) for both residue classes. Original fixed (p=373) H0/B0 divided-power ([X]Umod139129), rank, semilinear direction/eta, kappa, odd observer and independent verification remain **NOT_EXECUTED/PENDING_OWNER** under Issue #1559. No Source claim/run/Result is implied.
