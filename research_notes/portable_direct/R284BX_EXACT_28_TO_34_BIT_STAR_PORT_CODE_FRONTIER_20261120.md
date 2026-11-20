# R284BX — Five reproducible 28–34 bit star-Port observation codes

Date: 2026-11-20 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / FINITE_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED. Work mode: independent portable auxiliary algebra; no formal Task CLAIM, Result promotion, or native X6/BRC identification asserted.

## Frozen input and permitted change

Frozen predecessor is R284BW at commit `3e84b987574910e5b148a0ef38fdf81011c17d2d`, path `research_notes/portable_direct/R284BW_SMALL_MODULUS_SHARP_NOISE_20261120.md`, Git blob `037f88eb924d83a38a7389d7a24b6376871d7771`. Preserve its exact 4x4 star-Port model, 2-valued matrix alphabet, frozen leaf controls d1=6 and d2=13, and its complete fixed-pair noise obstruction at 59/2. Only the modulus and five free control values change.

For `C in {1,2}^{4x4}` and `E_ij` the single-entry elementary matrix, define

```
F_C(d0,d3,z1,z2,z3) =
det(diag(d0,6,13,d3) - C - z1*E01 - z2*E02 - z3*E03).
code(C) = F_C mod p, a point on the circle R/pZ.
```

Noise is adversarial real circular error of radius rho, with closed balls. Recovery is uniform over all 2^16=65536 row-major matrices, from a single read with fixed non-adaptive controls.

## Main exact finite theorem

For each row below, p is prime of the indicated bit length, the five controls are fixed as listed, the 65,536 code residues are pairwise distinct, and the **exact minimum cyclic inter-codeword distance** is g. Hence a circular nearest-neighbor decoder uniquely restores C for every 0 <= rho < g/2 (including arbitrary real errors, not only the integral values checked by the program). At rho >= g/2 recovery is impossible for the specified fixed code because a pair at distance g has overlapping error balls. No global minimum-bit-length or optimum-control assertion is made.

| bits | prime p | d0 | d3 | z1 | z2 | z3 | exact g | integer ± error |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 28 | 268435399 | 988826 | 637873 | 224007 | 661446 | 310514 | 1 | 0 |
| 31 | 2147483647 | 509251 | 307397 | 372686 | 124406 | 494014 | 3 | 1 |
| 32 | 4294967291 | 202052 | 981610 | 339700 | 614397 | 346881 | 10 | 4 |
| 33 | 8589934583 | 860189 | 661306 | 462704 | 258730 | 853243 | 16 | 7 |
| 34 | 17179869143 | 221288 | 961762 | 295480 | 300289 | 588278 | 34 | 16 |

In particular, the new 28-bit code is exactly lossless without noise; the new 34-bit code corrects all integer circular errors in [-16,16]. These complement rather than dominate R284BW's 35-bit, ±29 code. They expose an explicit storage-versus-finite-precision tradeoff at the same original matrix population and frozen leaf controls.

## Proof and complete certificate semantics

**Exact determinant identity.** Write the 16 matrix entries in row order as

```
[a,b1,b2,b3, u1,A11,x,y, u2,w,A22,z, u3,g,h,r].
T=6-A11; S=13-A22; U=T*S-x*w.
V=-r*U-z*(T*h+x*g)-y*(w*h+S*g).
p1=S*u1+x*u2; p2=T*u2+w*u1.
q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+S*u3).
q2=-r*p2+T*z*u3+u1*z*g+y*(w*u3-u2*g).
q3=U*u3+p1*g+p2*h.
J=-a*U-b1*p1-b2*p2.
K=-a*V-b1*q1-b2*q2-b3*q3.
F_C=d0*(U*d3+V)-z1*(p1*d3+q1)
    -z2*(p2*d3+q2)-z3*q3+J*d3+K.
```

The determinant identity follows by expanding along row 0 and then the lower 3x3 minors. The companion checker cross-verifies the identity against a separate signed 24-permutation Leibniz determinant calculation for 256 representative matrices per case, independent of the coefficient formula. This cross-check is implementation testing, not the sole justification of the identity.

**Complete finite part.** The checker enumerates the exact Cartesian product `itertools.product((1,2),repeat=16)` (65536 matrices). For each of the five pinned prime/control settings, it evaluates the integer formula with Python arbitrary-precision integers, applies remainder mod p, sorts the 65536 distinct residues and evaluates every 65535 consecutive gap **plus the circular wrap gap** `p-max+min`. Its exact minima are 1,3,10,16,34, with minimum-gap multiplicities 14,2,2,2,1 respectively. The primes are certified by exhaustive odd trial division through floor(sqrt(p)), not probabilistic primality testing. Sorting and finite enumeration exhaust all matrix pairs for distance: the minimum distance of a cyclic set occurs between consecutive cyclic neighbors.

**Uniform decoding.** Any two distinct centers have circular distance >=g; their closed radius-rho balls are disjoint when 2*rho<g. Therefore nearest-center decoding is unique for all 65536 matrices. Conversely the exhibited gap-g pair gives a midpoint reachable from two distinct centers at rho>=g/2. As an auxiliary software check, for each code the implementation also decodes all 65536 centers at errors `-(g-1)//2, 0, +(g-1)//2` (196608 per code, 983040 total). These discrete tests do not replace the real-radius proof.

**Structural residual test.** Across the fixed frozen model the 65536 nonconstant response signatures form 32768 two-element fibres; each fibre differs only at C03, with the exact cofactor q3 ranging from 59 to 196. This repeats the previous structural certificate, and keeps the hidden-edge residual visible rather than conflating the signature quotient with complete observability.

## Reproduction, evidence and independent scope

The reproducible standard-library program is `research_notes/portable_direct/R284BX_multiscale_port_checker.py`. Run:

```sh
python research_notes/portable_direct/R284BX_multiscale_port_checker.py
```

It writes `research_notes/portable_direct/R284BX_multiscale_port_verification.json`. The independently run exact calculation produced five row-major unsigned 64-bit big-endian residue SHA-256 digests, in table order:

```
28: a206bd8a1ad128f78be64687eded0e0edc30d253849d556eb28153e53adc05f5
31: e905b51a017c6dd9ac564882d185ae776f6f790037ca059a091af681dc457575
32: 0a4855eb296f5a79b63817a28c2c5227a0e60d7dbf5b0a92c26934bbd595af0d
33: afc43ad8488918c666a7eb5be2a2dadeae482535a27228393345bf32a550ee5f
34: b851f9830881f099e9804c194d691b0f68f4fdd4d1f3a7cfd8e46c967268c71b
```

Finite execution checks: 327680 complete candidate readings; 1280 independent determinant checks; 983040 nearest-neighbor perturbation checks; 32768 nonconstant signature fibres. For each row, the JSON stores an exact minimum-gap pair, modulus, controls, check counts, hashes and bounds. Source code and JSON are evidence, not an independent reviewer disposition. The general-H or native X6 interpretation is not claimed.

**Discovery versus validation.** The controls were found through seeded bounded search over integers, then frozen. All claims in this paper concern the fixed controls and are verified by a separate complete finite checker; no probabilistic discovery argument is used to prove them. The 35-bit R284BW construction remains separately certified with a different radius.

## Remaining scientific problems

The 34-bit witness does not attain the known fixed-pair noise limit rho<29.5 (it reaches rho<17); find a 34-bit or smaller setting with cyclic gap >=59, or a rigorous lower bound excluding one. Seek a 27-bit noiseless witness or a lower-bound certificate using the two-element residual-fibre structure. Reduce full nearest-neighbor table costs while preserving exact decoder semantics and include total preprocessing and memory costs when making complexity claims.

Contributor history: prior portable line historically identified as EM-DIRECT-E6B1DD; no verified current native Researcher SID/capability is asserted here. Activity association is bookkeeping pending under the currently lawful native source route. No unrelated current owner or Task CLAIM is altered.
