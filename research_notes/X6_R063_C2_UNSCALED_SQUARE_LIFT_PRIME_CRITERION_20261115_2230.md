# X6 / R063 Stage0 — Prime-factor completeness theorem for C2

Research date: 2026-11-15. Parent Task RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Author-side Research lane chatgpt-research-onhour-enterprise-math-20260923; existing Researcher provenance EM-X6-FB6990. Status: **AUTHOR-PROVED / EXACT FINITE CHECK PASS / UNREVIEWED / NOT_ADMITTED**.

## Frozen source and precise question

In frozen owner branch research/r063-stage0-path-valued-sqrt-2500, the original Stage0 loader has Git blob b4e000a6377f2858ae434eb0eecd0c25c33e8592. Its part01.inc (blob 913078c642b8995bfc135ef0350912387a17cdb8, lines 6–39) defines **C2**, the unscaled Gaussian-square lift. For each canonical nonnegative Gaussian pair m>=n>=0 with m²+n²=r, square m+ni to obtain (m²−n²,2mn), then emit both coordinate orientations. Its target D(r) consists of all ordered nonnegative integer roots (a,b) satisfying a²+b²=r².

The original 512-radius archive classified C2 as incomplete for 484 radii, but a general exact decision rule and the missing-root formula were not given. This research determines both for every positive integer r.

## Exact theorem

Factor a positive integer r as

    r = 2^a * product_(p=1 mod 4) p^(e_p) * product_(q=3 mod 4) q^(f_q).

Define T(r) = product_(p=1 mod 4)(2e_p+1) and S(r) = product_(p=1 mod 4)(e_p+1), with empty products 1. Let epsilon(r)=1 exactly when every exponent f_q is even; otherwise epsilon=0. Let delta(r)=1 exactly when r is a perfect square or twice a perfect square; otherwise delta=0.

The numbers of distinct ordered nonnegative target roots and C2-generated roots are respectively

    D(r)  = 1 + T(r)
    C2(r) = epsilon(r) * (S(r)+delta(r))
    Missing_C2(r) = D(r) - C2(r).

**Necessary and sufficient completeness criterion: C2(r)=D(r) if and only if no prime 1(mod4) divides r and every prime 3(mod4) divides r to even exponent. Equivalently, r=2^a s² for a>=0 and odd s whose prime factors are all 3(mod4).**

## Proof

1. Standard unique factorization in the Gaussian integers yields r_2(r²)=4T(r) ordered signed representations of r² as a sum of two squares. Exactly four are axial (±r,0) or (0,±r). Every other representation lies in a sign-and-swap orbit of size eight; each generic orbit contributes two ordered nonnegative pairs. Hence D=2+2(4T−4)/8=T+1.

2. The Gaussian representation count for the input norm r is zero when an inert prime q=3(mod4) has odd exponent; otherwise it is 4S(r). A canonical pair m>=n>=0 represents one of eight elements in a generic orbit. The unique possible exceptional orbit of size four is axial if r is a square, or diagonal if r is twice a square. For positive r those cases are mutually exclusive. Therefore the number of canonical input pairs is (S+delta)/2 when epsilon=1.

3. Each canonical pair yields exactly two distinct oriented outputs. Equality m²−n²=2mn would require m/n=1+sqrt(2), impossible for positive integer m,n; the axis case is distinct too. Different canonical input pairs cannot square to the same unordered output: equality up to signs corresponds to a Gaussian unit or conjugation; exchange of output coordinates would require a 45-degree rotation of a nonzero integer Gaussian pair (up to units/conjugation), impossible since the rotated coordinates have the form (m±n)/sqrt(2). Thus the two outputs from each canonical input are distinct even after all input pairs are combined, establishing C2=epsilon(S+delta).

4. With any split prime, T>S, so epsilon(S+delta) <= S+1 < T+1. An odd inert exponent makes epsilon=0. In the remaining case, T=S=1, and r=2^a s² has one canonical axial or diagonal Gaussian input according to parity of a; delta=1 gives C2=2=D. This proves the iff statement.

The theorem is about the **historical R063 positive two-generator sector**, not a full signed-X6 Cell enumeration. It preserves separate labels for source roots, target roots and path BRC multiplicities.

## Executed finite independent checker and exact observations

Standalone exact Python source: research_checks/X6_R063_C2_UNSCALED_SQUARE_LIFT_PRIME_CRITERION_20261115_2230.py. Program SHA256: 8f151c8d34ba241c5f75539caa53942fcb709794baf26746e55d6b1ad3085e03. The checker independently enumerates original C2 pairs from the input norm via integer isqrt, enumerates all target norm-r² roots independently, tests source and target formulas against prime factorization, verifies set inclusion and the complete iff criterion for each r from 1 through 512. Actual execution exited 0 with PASS_X6_R063_C2_PRIME_CLASSIFICATION_512.

| Mutually exclusive radius class | Radii r in 1..512 | Missing ordered roots |
|---|---:|---:|
| Complete: no split primes, inert exponents even | 28 | 0 |
| Some inert q exponent odd | 332 | 962 |
| Split p present, all inert exponents even | 152 | 418 |
| **Total** | **512** | **1,380** |

Across the same 512 radii there are exactly 1,820 true ordered roots and 440 original C2 outputs. The 28 complete radii are 1, 2, 4, 8, 9, 16, 18, 32, 36, 49, 64, 72, 81, 98, 121, 128, 144, 162, 196, 242, 256, 288, 324, 361, 392, 441, 484 and 512.

The complete finite missing-pair certificate digest, using canonical JSON rows containing all missing coordinates, is SHA256 4fbd9097c08f78064f054dead9ca626f7f1e4eef7a7c7314f7aaed94e4a1f674.

For the actual frozen input N=2500 and r=50=2*5², the theorem predicts T=5, S=3, epsilon=delta=1. Thus D(50)=6 while C2(50)=4, with precisely (30,40) and (40,30) omitted. At r=3 the failure is an odd inert-prime exponent; at r=5 it is a split-prime exponent. This independently explains the original archived C2 classifications without using its brute results as discovery input.

## Dependency and next acceptance

Reuses prior X6 unit #40 (independent original 512-row SHA256 reconstruction) and unit #41 (exact 1,820-branch polynomial-coefficient oracle), without rerunning them. The **unchanged original six-blob loader, 17 native acceptance gates and 512 same-object regression** are still tracked by [support #2416](https://github.com/awdawmip/enterprise-math/issues/2416). This checker does not execute that original source; the authorized runner must preserve original code and discovery-before-brute barrier, and compare its C2 failure set and path data to this independent exact theorem.

Remaining mother task: exact historical LP011 bad argmax caller attribution; exact LP019 natural BRC signed-subtraction caller attribution; complete 28-LP current consumer dependency closure; independent Driver REQUEST_REVISION. Native semantic PROGRESS linkage remains subject to own current SID/claim/run authorization and authentic readback. No new CLAIM, Result, review or admission is asserted.
