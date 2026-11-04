# D25 signed third-digit observer: explicit Frobenius/differentiation commutator
Date: 2026-11-04. TASK_RESEARCH author-side portable continuation, UNREVIEWED / NOT_ADMITTED.
Original task/publication/science pin: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7 / c47e13e4aba0e006366f989d6334d443f6333ae3.
Reuse the just-proved all-coefficient finite-support transport (proof: `20261104_onhour_d25_sun_global_support_and_full_boundary_jet.md`; exact checker: `d25_sun_global_support_full_jet_checker_20261104.mjs`).

## Exact operator identity

Let p=13 or 19 (mod 24), s²=2 in F_p[s], x_3=(2+s)/4 and x_4=(3+2s)/6. Since (2/p)=-1, x_d^p=1-x_d. With C_3=2/9, C_4=3/16, and reduced universal boundary polynomials Q_d, the previous new theorem proves E_d(X)=C_d X^p Q_d(X) and therefore
  E_d(x_d)=C_d(1-x_d)Q_d(x_d);
  E'_d(x_d)=C_d(1-x_d)Q'_d(x_d).
Differentiating the *already Frobenius-reduced expression* gives an incorrect result; its difference from the true original derivative is exactly C_d Q_d(x_d).

For the prior four-source D25 signed observer, define its defect part:
  S_def = -E_3(x_3)+E_4(x_4)+(3s/4)E'_3(x_3)-(s/6)E'_4(x_4).
The loss caused by the wrong observer order is the **exact all-target-prime correction**
  T_order = (3s/4) C_3 Q_3(x_3) - (s/6) C_4 Q_4(x_4).
Since (1-x_3)^(-1)=4+2s and (1-x_4)^(-1)=18+12s, this simplifies to
  **T_order = (3+3s)E_3(x_3) - (4+3s)E_4(x_4)**.
This equation works in the full quadratic extension; it makes no scalar-only assumption. It identifies precisely which signed two-source term would be lost by pre-evaluation Frobenius compression.

The complete defect-side expression is equivalently
  S_def = C_3(1-x_3)[-Q_3(x_3)+(3s/4)Q'_3(x_3)]
        + C_4(1-x_4)[ Q_4(x_4)-(s/6)Q'_4(x_4)].
This is a direct low-degree signed differential representation. It preserves source labels and distinguishes ordinary derivatives from the induced Frobenius observer.

## Exact discriminating finite tests

The independent original-polynomial BigInt checker in the preceding checkpoint reconstructs E_d(x_d) and E'_d(x_d); a separate modular quadratic-ring computation in this turn combined those values by the displayed identities.

| p | (E_3,E_4) | true weighted defect derivative | order correction T_order | wrong-order derivative | complete S_def |
|---|---|---|---|---|---|
|13|(6,1)|4+3s|1+2s|3+s|12+3s|
|19|(18,17)|7+18s|5+3s|2+15s|6+18s|
|139|(138,122)|32+75s|65+48s|106+27s|16+75s|
|373|(132,137)|222+371s|221+358s|1+13s|227+371s|

Every tested T_order is nonzero, giving four exact counterexamples to the procedure of Frobenius reduction before differentiation.
For the two previously pinned full four-source witnesses, original period-side contributions were
p=139: P_square+P_derivative = 17+(106+64s)=123+64s;
p=373: P_square+P_derivative = 236+(283+2s)=146+2s.
Adding the independently reconstructed S_def gives 0 in both quadratic fields. The nonzero contributions and their cancellation are retained as separate evidence. This tests the correct operation order but is not an all-primes W_p-V_p theorem.

## Next precise research action

Use the displayed two low-degree differential operators and the original p-adic period-square/derivative pair to construct an all-target-prime terminating relation, preferably with explicit Green/WZ or period transform, preserving original signed third-digit summands and p-valuation. 13,19,139,373 are the regression witnesses. The original native p=373 H0/B0 [X]U modulo 139129, rank, actual semilinear Frobenius and independent replication (#1559) remain a separate unexecuted benchmark. Native service 0.6.11 current observation: research_authority_granted=false; Source CLAIM/run/checkpoint/Result not established. Old failed request onhour-d25-20261104-1702-continuation-read was not reissued. Research identity is not the maintenance conversation.
