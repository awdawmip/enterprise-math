# The global minimum cost-eight root in the fixed R3 fiber

Date: 2026-11-24, Asia/Hong_Kong. Author proof and exact finite arithmetic in Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`.

## 1. Statement

Retain the full integer trajectory F_n(a)=a^2 2^n-1, the old dictionary P, and the historical fixed 43-prime fiber R3. The two previously proved all-prime results used here are the prefix dichotomy in `../prefix/proof.md` and the retained-prefix tail classification in `../tail/proof.md`.

The exact minimum is

```text
25391491002591320391732108159477707323814206756039394016382357924666368039179689189103105696777816709091120408108658618711788120139363377072408503
```

It has 146 decimal digits and satisfies

\[
\boxed{a_{8,\min}=\min\{a\in R_3:\delta_P(a)=8\}.}
\]

Its supplementary dictionary is

\[
\{5,13,19,73,38737,487824887233,1153,193\}.
\]

The last two root conditions are a=885 modulo 1153 and a=63 modulo 193. They give w=0 and w=4 modulo eight on n=32+36w. Along with the fixed odd-w channel and w=2 modulo four channel, these cover every integer w. All selected factors are proper because the positive R3 roots are already much larger than every classified prime. Exact supplementary cost eight follows from the established absence of seven-prime supplements in R3. The total-cost conclusion for this compact root is tau(a^2)<=28.

## 2. All roots in the retained-prefix branch

Write R3={A3+S3 k:k>=0}, where

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The conditional tail classification has exactly 30 binary, 2 ternary and 24 modulo-five phase dictionaries. The independent square-root signs produce 120, 8 and 192 CRT progression descriptions, respectively. Every root in the retained-prefix branch belongs to at least one of these progressions. Comparing their least positive representatives is therefore sufficient for this entire branch; possible overlap does not affect a minimum.

The exact calculator checks every phase pattern on its complete residual period, checks each prescribed root against its zero-phase equation, and evaluates all 320 CRT starts. Their family minima have 146, 162 and 165 digits. The smallest overall representative is the displayed binary root.

In the fixed R3 progression its index is exactly

\[
\frac{a_{8,\min}-A3}{S3}=63706.
\]

Thus there are exactly 63,706 positive R3 roots smaller than this candidate, corresponding to k=0,...,63705.

## 3. Exclude the entire other branch below this candidate

The prefix theorem proves that any complete eight-prime supplement omitting 19 and 73 must use all four primes

\[
Z=\{29,43,1429,5419\}
\]

as active period-seven channels on n=8+12v. This necessary condition is independent of the size or identity of its final two primes.

For any q in Z, activity on this progression requires a root residue in the exact set

\[
\mathcal R_q=\{\pm2^{-(4+6c)}\bmod q:0\le c<7\}.
\]

Each set has fourteen elements. The calculator deliberately also allows phases c=0 and c=6, which miss the residual A-set; the resulting test is weaker than the full covering condition and hence safe for exclusion.

For each k=0,...,63705, evaluate the four exact residues of A3+S3 k. The counts by the number of active Z coordinates are

| Active Z coordinates | 0 | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|
| Roots below the candidate | 21,939 | 31,370 | 10,276 | 121 | **0** |

The counts sum to 63,706. No smaller R3 root can therefore belong to the zero-W branch. The retained-prefix branch was completely minimized in Section 2. The prefix dichotomy excludes every other structure. These facts prove the global minimum stated in Section 1.

This is a finite exact exclusion of every smaller integer in a specified progression, supported by an all-prime structural theorem. It does not approximate the prime universe by a numerical cutoff. The certificate retains all 320 CRT starts, the exact activity categories, the count histogram and a digest of the complete finite mask stream. The self-contained script regenerates the entire calculation.

## 4. Reproduction and native interpretation

Run `python verify_minimum.py`. It uses only the Python standard library and writes `minimum_certificate.json`. Prime identities and the complete order inventories are established by the prefix and tail calculators; this component independently checks all exact orders used in the CRT and exclusion calculations.

The separate native execution in `../native` advances this particular 146-digit root through one entire 10,080-position covering-predicate period and retains the full integer and all joint readouts. The finite minimum comparison is an arithmetic proof about the original integer roots, while native execution verifies the claimed covering route and state semantics. Neither layer substitutes residue coordinates for the full typed integer register at the fixed X6 anchor.
