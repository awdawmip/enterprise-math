# D25: exact CM conjugate collision and signed first-jet recovery

**Date:** 2026-11-05. **Task:** SECOND-DIGIT-LIFT; original publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical lane \`chatgpt-research-onhour-enterprise-math-20260923\` (not maintenance lane). **Status:** author-side exact algebra + finite exact checks; UNREVIEWED / NOT_ADMITTED. The p373 native H0/B0 benchmark is separate and NOT_EXECUTED.

## Theorem 1: exact CM branch collision only at primes 13 and 19

Let \(T^2=2\). At the original 216/2304 marked endpoints define

\[
u_\pm=\frac12\pm\frac T4,\qquad
v_\pm=\frac12\pm\frac T3,
\]

\[
J_3(u)=\frac{27(1+8u)^3}{u(1-u)^3},\qquad
J_4(v)=\frac{64(1+3v)^3}{v(1-v)^2}.
\]

Exact rationalization gives

\[
J_3(u_\pm)=J_4(v_\pm)=j_\pm=a\pm bT,\qquad
a=2417472,\quad b=1707264=2^8\cdot3^3\cdot13\cdot19.
\]

Thus the common quadratic equation is \(X^2-4834944X+14670139392=0\), with discriminant \(8b^2\). For any prime \(p>3\) with \((2/p)=-1\), work in the unramified extension \(R_r=(\mathbb Z/p^r\mathbb Z)[T]/(T^2-2)\). The difference \(j_+-j_-=2bT\) has valuation **exactly one** at \(p=13,19\), and valuation zero at every other \(p>3\). Hence **the high/low scalar CM values coincide modulo \(p\) precisely at 13 and 19**, but separate again modulo \(p^2\). Equivalently \(v_p(\operatorname{disc}P)=2\) exactly at these two primes.

## Theorem 2: the signed first jet separates the branches modulo every prime above 3

For each sign use the local algebraic CM map

\[
u_\pm(z)=\frac{1\pm\sqrt{1-z}}2,\quad
v_\pm(t)=\frac{1\pm\sqrt{1-t}}2,\quad
J_3(u_\pm(z))=J_4(v_\pm(t_\pm(z))).
\]

At \((z_0,t_0)=(1/2,1/9)\), implicit differentiation with

\[
u'_\pm(z_0)=\mp T/4,\qquad
v'_\pm(t_0)=\mp3T/16
\]

gives the **exact** slopes

\[
t'_+(z_0)=\frac{8T}{27},\qquad
t'_-(z_0)=-\frac{8T}{27},\qquad
\frac{t'_+-t'_-}{T}=\frac{16}{27}.
\]

This last difference is a unit for all \(p>3\). The normalized branch observer

\[
\boxed{\epsilon_{\rm jet}:=\frac{27}{8T}t'(z_0)\in\{+1,-1\}}
\]

therefore recovers the marked branch directly, even at 13 and 19.

## Theorem 3: exact scoped non-descent of a scalar-only CM observer

At \(p=13\) or 19, the two marked branches have equal \(j\bmod p\), yet distinct \(t'\bmod p\). A purported function taking only \(j\bmod p\) as input and recovering both signed jets would have the same input and different outputs: impossible. This is a strict **mod-\(p\), named-observer** non-descendence result. Retaining \(\epsilon_{\rm jet}\) gives an explicit admissible replacement without dividing by \(j_+-j_-\), which is a nonunit exactly in these cases.

## Proof and reproducibility

All statements follow from direct substitution into the two rational \(J\)-functions, integer factorization of \(b\), and implicit differentiation. The accompanying exact SymPy checker independently obtains the conjugate values and both slopes from the rational derivatives. It checks every 312 target primes \(p<10000\), \(p\equiv13,19\bmod24\), and has zero failures. Representative reductions in the \(1,T\) basis:

| \(p\) | \(a\bmod p\) | \(b\bmod p\) | \(v_p(j_+-j_-)\) | \((j_+-j_-)/(pT)\bmod p\) | \(t'_+/T\bmod p\) | \((t'_+-t'_-)/T\bmod p\) |
|--:|--:|--:|--:|--:|--:|--:|
|13|5|0|1|4|8|3|
|19|7|0|1|10|1|2|
|139|123|66|0|n/a|129|119|
|373|59|43|0|n/a|97|194|

**BRC/information-preservation consequence:** project \((j,t',\text{branch},\text{modulus})\mapsto j\bmod p\) loses a future-needed signed first-jet observer at 13 and 19. Retain HIGH_PLUS/LOW_MINUS, their \(T\)-odd components, integer lift/finite-field quotient, original 216/2304 endpoints, signed weight, half-endpoint carry \(K_p\) and upper-shell contribution \(C_A\). This theorem concerns an external CM algebraic map, not native crystalline Frobenius.


## Corollary: the mandatory signed finite-period correction is exactly \(+p\)

The preceding author's exact high-CM period transport gave the *infinite* weighted identity \(2P_\infty=3Q_\infty\). For the *finite original* sums, consume the frozen accepted first-digit \(W_p\equiv p\pmod{p^2}\) and the already proved 2304 theorem \(V_p\equiv p\pmod{p^3}\), for \(p\equiv13,19\pmod{24}\). The exact identity

\[
2W_p-3V_p+p=2(W_p-p)-3(V_p-p)
\]

immediately gives the **uniform finite correction**

\[
\boxed{2W_p-3V_p\equiv-p\pmod{p^2}},
\quad
\boxed{\frac{2W_p-3V_p+p}{2p^2}
      \equiv\frac{W_p-p}{p^2}
      \equiv\Delta_p-R_p\pmod p}.
\]

The last equality consumes the previous original-source-aligned scalar interface. Thus a finite operator modeled on the analytic relation must account for the signed \(+p\) term **before** testing its second digit. This exact correction is a direct dependency on the frozen mother objective, not a conjectural CM normalization. Independently recomputed with original binomial coefficients at \(p=13,19,139,373\): \(W_p=V_p=p\pmod{p^3}\), and the corrected divided residual is 0 in each case; those finite checks are diagnostics.

**Next exact scientific unit:** derive an integral terminating finite-\(p\) 216→2304 operator in the **marked** \((j,\epsilon_{\rm jet})\) representation and test, first at \(p=13,19\), whether it transports the original signed \(p^2\) half-endpoint carry and upper shell. The mother target \(W_p-V_p\equiv0\pmod{p^3}\), equivalently \(\Delta_p-R_p\equiv0\bmod p\) at the frozen scalar interface, remains open. The native fixed \(p=373\) original-class divided-power \([X]U\bmod139129\), rank, semilinear Frobenius/eta, kappa and independent replication remain **PENDING_OWNER** under support Issue #1559.
