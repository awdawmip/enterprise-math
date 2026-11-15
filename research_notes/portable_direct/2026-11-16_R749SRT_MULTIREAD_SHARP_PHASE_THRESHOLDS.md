# R749SRT — Exact sharp multiple-read phase recovery and observation economy

2026-11-16 (Asia/Shanghai). Mathematical status: **AUTHOR_EXACT_NOT_REVIEWED**. This is an independent portable labeled-source study, continuing [R749SRS@9d9a2915](https://github.com/awdawmip/enterprise-math/blob/9d9a2915a44f6f481491ebd26ba8cd794763f3c5/research_notes/portable_direct/2026-11-16_R749SRS_SHARP_SHIFT_DECODER_AND_MINIMAL_CARRIER.md); frozen auxiliary Walsh source input remains \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This result concerns cutoff shifts in a *positive labeled integer source* model. It makes no assertion that these shifts are heartbeat-time operations or a signed BRC-port/X6-native morphism.

## Definitions and target

Let \`s=(1,1,2,3,6)\`, with the first source marked, and for every integer \`r>=1\` put
\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le r-1\},\
C_r=|\Omega_r|,\quad T_r=\sum_{\Omega_r} k_1,\quad E_r=T_r/(r C_r).
\]
Use the exact smooth part and ideal six-phase remainder established in R749SQR–SRS:
\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}
+\frac{115}{6r^3}-\frac{16315}{108r^4},
\quad R(r)=r^4(E_r-H_4(r)),
\]
\[
P(a)=\frac1{36}(455,-295,-25,185,-25,-295)_a,\qquad a\in\mathbb Z/6\mathbb Z.
\]
For a finite read-set \`A\subset\mathbb Z_{\ge0}\` containing zero, define the six **ordered** ideal signatures
\[
S_A(a)=(P(a+h))_{h\in A},\quad
Y_A(r)=(R(r+h))_{h\in A}.
\]
The specified decoder minimizes \(\|Y_A(r)-S_A(a)\|_\infty\) over *distinct* signatures and reports a unique phase if exactly one signature minimizes it; ties count as failure. For each read-set below all six ideal signatures are distinct. Let \(\tau_A\) be the **least positive integer** for which this decoder is correct for *every* integer \(r\ge\tau_A\).

## Main theorem — sharp thresholds for simultaneous observations

For the preceding fixed model and decoder, the exact all-integer thresholds are

| Read-set A (cutoff offsets) | Reads | Sharp \(\tau_A\) | Last failing r | Minimum distinct-signature separation |
| --- | ---: | ---: | ---: | ---: |
| \(\{0,1\}\) | 2 | **398** | 397 | \(35/6\) |
| \(\{0,1,2\}\) | 3 | **44** | 43 | \(15/2\) |
| \(\{0,1,5\}\) | 3 | **35** | 34 | \(15/2\) |
| \(\{0,1,2,3\}\) | 4 | **26** | 25 | \(15/2\) |
| \(\{0,1,2,3,4\}\) | 5 | **26** | 25 | \(15/2\) |
| \(\{0,1,2,3,4,5\}\) | 6 | **18** | 17 | \(15/2\) |

In particular **three observations at offsets 0,1,5 recover the full six-phase state for all \(r\ge35\)**; three *consecutive* observations suffice for all \(r\ge44\). Four consecutive observations suffice for all \(r\ge26\); six suffice for all \(r\ge18\). These are sharp for their particular ordered read-sets and the stated max-norm nearest-signature rule; no global minimum over all possible read sets is asserted.

## Exact proof — finite bridge and certified infinite tail

1. **Generating functions and degree.** The strict-prefix count and marked count have rational generating functions
\[
\sum_{r\ge1}C_r z^r=\frac{z}{1-z}\prod_{w\in s}(1-z^w)^{-1},
\qquad
\sum_{r\ge1}T_r z^r=\left(\sum_{r\ge1}C_r z^r\right)\frac{z}{1-z}.
\]
All poles are sixth roots of unity. Thus, in any fixed residue class modulo six, \(C_r,T_r\) are polynomials in the step index of degrees at most five and six. Reconstruct exactly by finite differences using six and seven samples. Independent weighted-sum enumeration checks the first 24 cutoffs.
2. **Uniform error.** For each phase \(a\), start at the first \(r_a\in[512,517]\) congruent to \(a\) modulo six and write \(r=r_a+6n\). With interpolated polynomials \(C_a(n),T_a(n)\), set
\[
B_a(n)=r^3T_a(n)-C_a(n)(r^4H_4(r)+P(a)),\qquad
U_a(n)=\frac{35}{12}C_a(n)-B_a(n).
\]
The accompanying exact-rational certificate proves that every coefficient of each \(C_a,B_a,U_a\) in ordinary powers of \(n\) is strictly positive; \(\deg B_a=4\), \(\deg C_a=\deg U_a=5\). The generating-function degree bound upgrades the interpolation to an identity for all \(n\ge0\). Therefore
\[
0<R(r)-P(r)<35/12\quad\text{for every integer }r\ge512.
\]
3. **Signature separation.** Direct evaluation of the six exact rational signatures gives minimum pairwise max-norm separation \(35/6\) for \(\{0,1\}\) and \(15/2\) for every other listed set. Consequently, at \(r\ge512\), the true signature has distance strictly less than \(35/12\), while every different signature is farther: its distance is \(>35/6-35/12=35/12\) (or larger). All future coordinates \(r+h\) also satisfy the same bound, since \(h\ge0\).
4. **Finite exhaustive bridge.** The accompanying standard-library Python program computes \(C_r,T_r\) by a recurrence independent of the generating-function interpolation, calculates \(R(r)\) with \`fractions.Fraction\`, and for each of the six read-sets evaluates all six ideal-signature distances for every integer \(1\le r\le511\): **3,066 exact decoder evaluations**. It records a failure (possibly a tie) at \(\tau_A-1\) and checks strictly positive decoder margins for each \(r\in[\tau_A,511]\), with the exact rational minimum. The six verified last-failure margins \(d_{\rm next}-d_{\rm true}\) are respectively
\[
-15526/747603,\quad -7325575/126080262,\quad
-47944007/50160321,\quad -524193275/384646236,\quad
-524193275/384646236,\quad -258193/1323420.
\]
Thus each threshold is sufficient through the finite bridge and infinite tail, and the immediately preceding failure proves minimality. \(\square\)

## Interpretation, reproducibility and next question

The source alphabet retains five labeled components throughout. The phase observer \(P\) has four distinct *single-read* values, but the specified multi-read signatures distinguish all six phases. A carrier preserving these read-sets and their shifts therefore needs six phase states; coarser four-state carriers suffice for some restricted future-operation families established in R749SRS. All counts and comparisons use exact integers/rationals; no numerical tolerance or floating rounding is used. Scientific input is frozen to the immutable predecessor model.

**Evidence:** \`R749SRT_MULTIREAD_DECODER_CERT.py\` and its JSON output in this directory; local execution result \`PASS\`. The certificate checks six residue-class tail positivity polynomials, 24 independently enumerated cutoffs, and all 3,066 finite decoder cases. Results are author-checked; independent review and native BRC port mapping remain open.

**Next:** determine the sharp all-precision phase recovery thresholds when the observation offsets are chosen under a cost/horizon budget; quantify a nonzero adversarial noise radius across all \(r\ge\tau_A\), and test typed joint/provenance preservation in a separately specified BRC interface.
