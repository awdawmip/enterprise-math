# D25 BRC: exact fourth-jet necessity at the second gauge digit

Date: 2026-11-02 Asia/Hong_Kong.
Classification: AUTHOR-DERIVED / EXACT PROOF / EXACT p13 WITNESS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
This is a new source-typed information-loss lemma, not a native H0/B0 experiment or an all-prime CM theorem.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-hourly-enterprise-math-20260923`. Previous new algebra source: `research_notes/portable_direct/20261102_hourly_d25_second_order_teich_jet.md` at commit `7e60477c0fa9d9e7dc0bee3fa5664c3597fe7aab`.

## Theorem: three first-digit ports do not determine the second gauge digit

Fix prime p>=5, p-unit z in Z_(p), c in Z_(p), q=(z^(p-1)-1)/p, and omega=z^(p²) modulo p³.
Assume c*q*z is a p-adic unit. On polynomials P with P(z)=theta P(z)=0 modulo p, define the first-order corrected three-port observation

~~~text
O1(P)=(P(z)/p, (theta P)(z)/p+q*(theta²P)(z), (theta²P)(z)) mod p.
~~~

Define the future signed/weighted gauge-shift readout

~~~text
G2(P)=[(1+c theta)P(omega)-(1+c theta)P(z)]/p mod p².
~~~

**Claim:** There is no function of O1(P) alone, even a nonlinear one, that gives G2(P) on all such polynomials.

**Exact witness:** P0(X)=0, P1(X)=(X-z)^3. Both have identical O1=(0,0,0). At z, P1=theta P1=theta²P1=0 and theta³P1=6z³. The second-order Teichmüller jet identity from the preceding source gives

~~~text
G2(P0)=0,
G2(P1)=p*3*c*q²*z³ (mod p²).
~~~

This difference is nonzero because p>=5 and c,q,z are p-units. Hence O1 has a fiber containing two inputs with different future gauge outputs. Retaining theta³P(z) mod p (or an equivalent repair coordinate) is mathematically necessary for **this universal future observer**.

For exact p=13, z=1/2, c=6: q mod13=10, z mod13=7, and

~~~text
G2(P1)=13*(3*6*10²*7³ mod13)=13*4=52 mod169.
~~~

Independent direct modular evaluation with modulus 13³=2197:
z=1099, omega=657, d=omega-z=1755 mod2197;
(1+6theta)(X-z)^3 at omega equals
d³+18*omega*d² =676 mod2197, so its quotient by p is 52 mod169.
This is an exact integer certificate. It is an observer-indistinguishability proof, not a fitted regression.

## Scientific consequence

The prior D25 p³ source-preserving four-port operator

~~~text
(V0,V1,V2,V3)=(P(omega)/p,theta P(omega)/p,theta²P(omega),theta³P(omega))
~~~

at precisions (p²,p²,p²,p) retains the third derivative needed by the future weighted gauge readout. Its earlier reduction to only the three modulo-p first-order ports cannot generally preserve this next-digit operation. The theorem is **scoped to polynomial inputs, p-unit z, c and q and this future operation**; it does not assert native X6 geometry or show any fixed D25 class has two distinct polynomial realizations with the same three-port data.

BRC resolution: COMPOSE_APPLIED; object population = the stated polynomial class; observer O1; future operation G2; exact fiber witness P0,P1; information-loss coordinate theta³P mod p.

Next exact D25 question: build and test a non-scalar, source-preserving signed correspondence between the *actual original* 216 and 2304 four-port tuples, retaining the high-index Clausen signed cutoff. At p373 discriminate against the first shift 316, new second shift digit 91, first projective defect 365, derivative mismatch 138 and fourth-digit ratio 228:114. Then target the frozen Delta_p-R_p=0 modulo p for p mod24 in {13,19}.

Control: Same actual 2026-11-02 Gateway read 0.6.11 reported UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false and executor_binding_configured=false; current task CLAIM/OPEN/Source checkpoint/Result/Review not created. Original recovery #6637 read-only SUCCEEDED; #6638 continuation FAILED, unreplayed. Project support issues #1558 (control) and #1559 (native benchmark) retain their boundaries; P000/worldview/scientific pin and scheduler settings unchanged.
