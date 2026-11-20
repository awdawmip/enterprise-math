# R284BZ — A 34-bit frozen-double-leaf star-Port code achieving the global sharp noise threshold

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED.
Mode: independent portable auxiliary finite algebra; not a native X6/BRC physical observation or formal Task CLAIM.

## Frozen scientific problem and provenance

Scientific predecessor: R284BY_34BIT_SHARP_GAP41_PORT_20261120.md (Git blob d744984d5756a4b57692b0705d7a1f29a23db326). The observation model, alphabet and frozen controls are unchanged:
For C in {1,2}^{4×4}, define
F_C = det(diag(d0,6,13,d3) - C - z1 E_01 - z2 E_02 - z3 E_03) modulo a prime p.
The decoder gets one fixed-control, non-adaptive residue on the circle R/pZ, corrupted by arbitrary adversarial real circular error of radius rho. The goal is uniform recovery of all 65,536 row-major matrices. Only p and the five free controls are searchable, and the present witness uses the same p as R284BY.

## New explicit witness

p = 17179869143 (34 bits, prime).
d0 = 1120832; d3 = 1651128.
z1 = 390139; z2 = 394465; z3 = 1497639.

This changes only d0 by +10, d3 by -2 and z3 by -3 relative to R284BY; z1 and z2 remain fixed.

**Exact finite theorem:** All 65,536 code residues are distinct, with minimum circular distance exactly **59** (attained at 64 consecutive cyclic gaps). Consequently uniform nearest-center decoding works for every real rho with 0 <= rho < 59/2 = 29.5, including every integer circular error between -29 and +29. This bound is sharp for the specified code.

**Global sharpness for the entire frozen pair:** Fixing d1=6,d2=13 in this model, no choice of p,d0,d3,z1,z2,z3 can uniformly correct circular error with rho >= 29.5. Thus this 34-bit witness attains the optimum noise threshold across all available moduli and free controls *for these frozen values*, not a global minimum communication-bit theorem.

## Proof of the global upper bound

Write C row-major as
[a,b1,b2,b3, u1,A11,x,y, u2,w,A22,z, u3,g,h,r].
Set T=6-A11 and S=13-A22, so T in {4,5}, S in {11,12}, and x,w,u1,u2,u3,g,h in {1,2}. The cofactor multiplying b3 in the determinant is -q3, with
U=TS-xw, p1=S u1+x u2, p2=T u2+w u1,
q3 = U u3+p1 g+p2 h.
Since U >= 4*11-2*2=40, p1 >= 11+1=12 and p2 >= 4+1=5, these separate bounds alone yield >=57. The sharp value follows by direct monotonicity of q3 in positive variables: minimizing over u1,u2,u3,g,h at 1 gives q3=(TS-xw)+(S+x)+(T+w). For T>=4,S>=11 and x,w in {1,2}, the expression is decreasing in x and w because its x coefficient is (1-w)<=0 and its w coefficient is (1-x)<=0. Taking T=4,S=11,x=w=2 gives 40+13+6=59. Thus q3>=59, attained at A11=A22=2, x=w=2, u1=u2=u3=g=h=1. The exact finite upper cofactor bound is 196 (verified exhaustively, not needed for this upper-bound theorem).

Take two admissible matrices differing only in b3=C03 by one, with the attaining lower 3-by-3 block. Their integer determinants differ by exactly q3=59 for any free controls. After reducing modulo any p, their cyclic distance is at most 59. Therefore the minimum codeword separation of any injective configuration in the specified frozen model cannot exceed 59. At rho>=59/2, closed error balls for this pair overlap and deterministic worst-case unique recovery is impossible. This proof requires no exhaustive search over free controls.

## Proof of existence and executable certificate

The determinant equals the integer polynomial
F = d0*(U*d3+V)-z1*(p1*d3+q1)-z2*(p2*d3+q2)-z3*q3+J*d3+K,
where
V=-rU-z*(T*h+x*g)-y*(w*h+S*g);
q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+S*u3);
q2=-r*p2+T*z*u3+u1*z*g+y*(w*u3-u2*g);
J=-a*U-b1*p1-b2*p2;
K=-a*V-b1*q1-b2*q2-b3*q3.
This follows by cofactor expansion of the given 4x4 matrix. Its implementation is checked against a separate signed 24-permutation Leibniz determinant on 256 row-major sample indices.

The standalone Python standard-library checker enumerates all 2^16 matrices in lexicographic row-major order, uses exact arbitrary-precision integers, reduces modulo p, and sorts every residue. It checks all 65,535 adjacent gaps and the single wrap gap. The resulting minimum is **59**, with 64 gap witnesses, no duplicate residues, and 65,536 distinct candidates. Sorted-neighbor minimality establishes the exact minimum over every unordered matrix pair. For a concrete pair:
A=[2,2,2,2,1,2,2,2,1,2,2,2,1,1,1,2] has residue 15722869762;
B=[2,2,2,1,1,2,2,2,1,2,2,2,1,1,1,2] has residue 15722869821.
They differ only at C03 and their cyclic distance is exactly 59.

The checker also proves p prime by exhaustive odd trial division through floor(sqrt(p)), verifies all 65,536 codeword decodings with errors -29,0,+29 (196,608 checks), and records the SHA-256 of 65,536 residues serialized as unsigned 8-byte big-endian integers in row-major order:
b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4.
All computations are exact. Independent review is NOT_REVIEWED; the proof and executable exhaustive certificate support this author-level finite statement.

Reproduce:
python research_notes/portable_direct/R284BZ_34bit_gap59_checker.py
This writes R284BZ_34bit_gap59_verification.json in the same directory.

## Scope, residual and next questions

R284BY had gap 41, guaranteed rho<20.5 and corrected integer ±20. R284BZ achieves gap 59, rho<29.5 and integer ±29 while retaining 34 bits and the same p. It therefore matches the frozen-pair upper bound previously achieved with a 35-bit code in R284BW, reducing communication by one bit without sacrificing noise tolerance. Decoding may use a 65,536-entry sorted-residue table and binary search, with preprocessing and memory costs included in algorithmic comparisons.

The structural residual is the hidden C03 coordinate: the nonconstant response signature has 32,768 two-element fibres, and the full readout preserves the distinguishing constant cofactor q3. This is an auxiliary star-Port observation; no embedding into native X6, triadic balance, or physical measurement is claimed.

Next scientific targets: determine whether 33-bit or lower codes attain global gap 59; compress the full lookup decoder by an exact residual-preserving algebraic inverse; establish rigorous lower bounds on bit length under fixed d1=6,d2=13. A separately bounded 6,000-candidate perturbation search around the R284BX 33-bit witness found gap up to 26; this is exploration, **not** a 33-bit impossibility result.

Control: prior contributor lineage EM-DIRECT-E6B1DD, current native session identity/capability not attested, no CLAIM or independent review asserted. Research Activity semantic association requires its own lawful original-identity and Source CAS path.
