# R284DV — 最小间隔见证族的无取模、无圆弧精确数值观察器

Date: 2026-11-22 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED
Domain: the 512 R284DQ/R284DT witness states of frozen R284CO auxiliary Port model, not arbitrary 65,536 source states or native X6 dynamics.

## Frozen source and semantic scope

P=17179869143. Frozen determinant source:
awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py, Git blob b46e0f682b58e47c27094b4bea6fa4e55119a3ee.
Frozen ordered-codeword SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4.

This result builds on R284DT (seven integer windows and seven affine value laws) and R284DU (eight-bit direct Boolean unique winning-arc label). It sharpens the preceding numeric observer: even the integer residue reduction modulo P is unnecessary on this subfamily.

## Theorem 1: explicit compact determinant without the general 12-variable routine

Take X,Y,Z,U2,U1,U0,W,R,B in {0,1}. Define the lower 12-source-variable skeleton by a=b=2, u1=u2=u3=g=h=1, and x=1+X, y=1+Y, z=1+Z, w=1+W, r=1+R. The upper source bits are (U2,U1,U0,B), mapped to the source det top mask in the R284CO order.

Put

- u=44-xw, p1=11+x, p2=4+w;
- v=-ru-z(4+x)-y(w+11);
- q1=-rp1+Xz+12y, q2=-rp2+5z+yW;
- k0=1651128u+v, k1=1651128p1+q1, k2=1651128p2+q2, k3=60-XW.

Then the original *unreduced* integer source determinant on each of the 512 states is exactly

T=(1120831-U2)k0-(390140+U1)k1-(394466+U0)k2-(1497640+B)k3.

**Proof:** Substitute a=b=2, u1=u2=u3=g=h=1 and the five binary lower variables into the original frozen R284CO formula. Its four k coefficients reduce to the displayed expressions; collecting the original base term and four top-bit subtractions yields T exactly. This is an integer polynomial identity (and is also independently checked against the full frozen determinant for every one of 512 states).

## Theorem 2: the quotient is a four-case polynomial in two lower bits

Define the exact integer quotient polynomial

Q(X,W)=3992-145X-146W-108XW.

For every permitted nine-bit input,

Q(X,W) P <= T < [Q(X,W)+1] P.

Consequently the canonical original circular residue is exactly

g=T-Q(X,W)P,

with **no division/modulo operation**.

The complete exact integer bounds (128 states in each fixed (X,W) class) are:

| XW | Q | min T | max T | min g | max g |
|---|---:|---:|---:|---:|---:|
| 00 | 3992 | 68590378587804 | 68590544905284 | 8340968948 | 8507286428 |
| 01 | 3846 | 66088429282788 | 66088595600268 | 14652558810 | 14818876290 |
| 10 | 3847 | 66095572062516 | 66095738379996 | 4615469395 | 4781786875 |
| 11 | 3593 | 61742992700561 | 61743156246083 | 15722869762 | 15886415284 |

Each row's minimum is strictly above QP and its maximum strictly below (Q+1)P. The bounds result from exact enumeration of the 128 assignments to the seven remaining binary variables for each XW class; thus the finite-domain quantifier is completely covered, including the upper partner bit B. The original unreduced determinant equality is independently checked at all 512 inputs, so no observer map is silently changed.

## Corollary: direct complete numerical observer and paired-gap law

Let l be R284DU's direct eight-bit Boolean winning label and (s_l,c_l) the matching R284DT seven-window coefficients. Define

D_direct=s_l [T-Q(X,W)P]+c_l.

For all 512 states this integer is exactly the original maximum of the 64 point-to-arc distances and l is the unique winning arc label. No original arc generation, event envelope, arbitrary determinant routine, or modular reduction is required in the *observation* computation.

For the corresponding upper-B partner the determinant difference is exactly k3=60-XW and the quotient Q is unchanged. Both states retain the same winning label and the same affine slope, so their absolute numerical observer difference is precisely

|D_direct(B=0)-D_direct(B=1)| = 60-XW.

The 256 pairs therefore split into 192 pairs with exact gap 60 and 64 pairs with exact gap 59. Together with the already certified global minimum-gap completeness of R284DN, this recreates the sharp 256-pair witness family through a compact integer/Boolean circuit.

## Reproducibility and cost boundary

The published Python verifier checks (i) compact polynomial equals the full pinned determinant on 512 states, (ii) exact four-case quotient bounds, (iii) quotient-free residue equals the original modular residue, (iv) direct numeric value and unique label agree with all 64 original arcs in **32,768 independent direct integer comparisons**, and (v) all 256 sharp paired differences. No floating-point operations, approximate thresholds or inferred asymptotics.

Construction/observation arithmetic has 0 modulo divisions, 0 direct arc-distance calls and 0 event queries, but still uses multiplication/addition of integers up to ~47 bits, including the P*Q subtraction; it is not a zero-cost observer. A broader complexity/runtime advantage requires whole-path timing and representation/precision accounting. The construction is specific to these 512 frozen witness states; changing the input domain requires new quotient and winner-label certification.

Files:
research_notes/portable_direct/R284DV_compact_no_modulus_numeric_observer_checker.py
research_notes/portable_direct/R284DV_compact_no_modulus_numeric_observer_certificate.json

Local exact Python verification passed. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED. This does not promote a formal Enterprise Math Result, BRC theorem, P000 or a claim on another owner's Task. Current native Activity association remains pending authentication of the original Researcher session.

Next: simplify the integer circuit further by factoring k0,k1,k2 and assessing total multiplication count and bit complexity, including whether a single parameterized family extends this quotient stability beyond the eight skeletons; compare actual runtime with the generic R284DS heap envelope.
