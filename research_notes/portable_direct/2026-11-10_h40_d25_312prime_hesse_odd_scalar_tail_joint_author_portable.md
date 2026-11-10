# D25/LIFT: joint Hesse odd-port and scalar-tail exact census through p=10000

Date: 2026-11-10. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR_FINITE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is a portable author calculation, not native H0/B0/Frobenius, canonical CLAIM, Result or project admission.

## Exact finite proposition

Let P be all primes p <= 10000 with p mod 24 in {13,19}. The complete finite set has **312 elements** (157 in class 13, 155 in class 19).

In the coefficient ring R=(Z/p²Z)[T]/(T²-2), retaining the tagged port u=(2-T)/4 and involution T ↦ -T, define
```
A_p(u) = SUM[k=0..(p-1)/3] ((3k)! / (27^k (k!)^3)) u^k  mod p²
A_p(u) = p (a_p + b_p T)  mod p²
ordinary Hesse odd phi_p = 4*b_p mod p
ordinary Hesse norm N_p = a_p² - 2*b_p² mod p
```
For the distinct frozen scalar recurrence B_0=1 and B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)²), set a=(p-1)/6, b=(p-1)/3, h_p=SUM[k=0..a](12k+1)B_k mod p, S2=SUM[k=b+1..p-1]B_k, and t_p=(S2/p²)*h_p mod p.

**Full exact 312-prime enumeration:** no p in P has a_p=0, b_p=0, phi_p=0, N_p=0 or h_p=0. Among P, exactly one prime has S2/p² ≡ 0 (mod p) and exactly one has t_p=0: **p=157**.

At p=157 the ordered witness (a_p,b_p,phi_p,N_p,h_p,S2/p²,t_p) is (20,145,109,112,80,0,0). At p=373 it is (302,154,243,131,171,252,197). Hence, in the entire declared finite range, the Hesse odd observer remains nonzero while the scalar tail's divided second-digit correction vanishes only at 157.

The p=157 individual cross-observer separation and the scalar finite-field tail formula are prior author evidence reused without recredit. The scientific increment is **complete joint classification to p=10000 using two independent exact implementations for each of the two observer computations**.

## Full coverage and integer verification

For every integer 13<=p<=10000, trial division up to floor(sqrt(p)) selects exactly primes in the two stated residue classes. For every selected p:

1. Evaluate A_p(u) modulo p² by coefficient recurrence together with successive powers of u in R.
2. Independently evaluate the factorial coefficients using factorials mod p², and evaluate A_p(u) by Horner's rule in R. Compare both coordinates before dividing by p.
3. Evaluate h_p and S2/p² using the previously proved finite-field formula (the factorial/binomial tail formula, retaining the cutoff).
4. Independently evaluate the original frozen B recurrence modulo p³, divide each tail term by p² as an integer and compare h_p, S2/p² and t_p. All multipliers/denominators used are units for k<p.

The integer-only executable and complete 312-row JSON certificate are in conversation artifact `D25_HESSE_ODD_SCALAR_TAIL_312PRIME_PORTABLE_20261110.zip`; its SHA-256 is `8529c16d246275d8dcc3b953012b03a1ace5145f9cdf2d4fa002e2b785c21ae8`. Reproducing with `python verify_d25_joint_census.py` prints:
```
PASS 312 mod13 157 mod19 155 odd_zero [] norm_zero [] tail_zero [157]
```
The certificate JSON SHA-256 is `98f5e72c8510f079aa6416a0972286179371820fb7a508985751ff5e2318a4fe`; executable SHA-256 `9e373f828bd76781f88de8e8f4b95ee413ccd84a2970bdfa91acd87ccca00457`.

## Next scientific unit

This verified finite baseline sharpens any proposed relationship between the two genuinely distinct observers. Uniform all-prime Hesse-odd nonvanishing is still open. The original-class native H0/B0 divided-power module, Frobenius direction, eta normalization and original frozen R_p remain prerequisites for comparison with Delta_p and native JT2. The UR V2 original 94,687-byte bundle (expected SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains writer/provenance recovery debt; its mathematics must not be replayed. Native session/CLAIM and canonical checkpoint were not written in this author evidence step.
