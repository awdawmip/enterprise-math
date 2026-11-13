# R46: uniform 389-source coverage and distant Farey-stage risk compiler

Status: Author-side theorem, exact finite S23/AV validation, independent mathematical review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: R45 Draft PR #1995, commit bae0abd5cb05f129ea91d1624126aa67af22b1b0.
Scope: auxiliary irrational-rotation observer; original historical owner labels are preserved, with no unproved native-X6 transfer.

## Theorem R46.1: uniform moving-block cover

Let 0<theta<1 be irrational and m>=2. The first m phases {t theta}, 0<=t<m, form m historical half-open arcs I_k of minimum length delta>0. Let g_H be the largest circular gap formed by the H phases {r theta}, 0<=r<H, with H>=m.

If g_H<delta, then every integer block [J-H,J) supplies at least one source phase to each historical arc I_k, for every integer J (even at arbitrarily distant or negative J).

Proof. Every such H-block is a common rotation of the initial H phases by (J-H)theta. Circular-gap lengths do not change under common rotation. An arc longer than the largest complementary gap cannot have no source in it. Strict inequality handles half-open endpoints. QED.

## Theorem R46.2: exact suffix risk compiler

Within a Farey stage a/i<theta<c/j, c*i-a*j=1, s=i+j, the current longest-gap source set at n is W(n)=[n-i,j) and has s-n integer sources. These sources retain their unique original historical owner labels. Let F(n) count historical arcs with no owner in W(n). The R35/R45 proven exact update is

    R_n-R_(n-1)=(F(n)-F(n-1))*min(i*theta-a,c-j*theta).

For the H sources t=j-H,...,j-1 define the last-source ages

    r_k=j-max{t in [j-H,j):owner(t)=k},  1<=r_k<=H.

Under R46.1 every r_k exists. Then

    F(n)=0                              if s-n>=H;
    F(n)=#{k:r_k>s-n}                   if 0<=s-n<H.

Thus a positive step in this stage occurs exactly at n=s-r_k+1, when that n lies in its proper update range, and its amplitude is the displayed min expression. Ages of distinct k are distinct.

Proof. When s-n>=H, W(n) contains H consecutive source phases ending before j; R46.1 supplies every owner. When s-n<H, W(n) is exactly the last s-n sources before j, and contains owner k iff r_k<=s-n. Advancing n deletes the source with age s-n+1 and changes the extinction count precisely when r_k=s-n+1. The stage law gives the claimed risk step. At a Farey boundary R45 transfers the old short-gap source class to the new long-gap class and initializes the new stage's F(s_old) from its own labels; the same endcap rule gives the step s_old+1. Starting from R_m=0 yields the entire risk. QED.

This uses at most H phases per stage, independently of the potentially enormous original source interval and without preloading R32's special last-source age pattern.

## Frozen S23/AV arithmetic certificate

The frozen exact interval is

    LO/D=262204504569236716045286/10^24
    HI/D=262204504569236716045287/10^24,

with m=128, H=389 and endpoint n=10^12+128. The cyclic order of the phases indexed 0..388, and of the historical indices 0..127, is the same at both endpoints of the interval. Each gap is affine in theta between collisions, so endpoint inequalities certify the whole interval.

| Bound | minimum original arc numerator | maximum 389-block gap numerator | strictly positive difference |
| --- | ---: | ---: | ---: |
| LO/D | 5525221276560321237554 | 3986471921738889810650 | 1538749354821431426904 |
| HI/D | 5525221276560321237493 | 3986471921738889810425 | 1538749354821431427068 |

All numbers in the table have denominator 10^24. This proves g_389<delta across the frozen interval. The H=388 test has equality, so 389 is the first H in [128,389] satisfying this sufficient strict-max-gap certificate; it is not asserted to be globally optimal among other possible certificates.

The extended verifier constructed every 389-source suffix at each of 78 exact Farey stages. Both rational endpoint evaluations give identical 128-owner last-source age vectors for every stage. A separate exhaustive stability check covered 2,502,656 source-versus-historical-boundary floor comparisons for 19,553 distinct candidate source indices; every nontrivial floor((t-z)*theta) was constant across the interval. Its minimum integer-numerator clearance was 1538749354821431426904. The first 389 phases' ordering was also verified stable over the interval.

After merging contiguous equal amplitudes, 9,697 positive single-step updates form **298 maximal affine risk runs** and

    R_(10^12+128)=-4017401528447+15321634290944*theta.

The generated 298-run TSV SHA-256 is

    2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6.

It agrees byte-for-byte with the frozen R32 reference. R32's table was used only as a regression oracle, not as an input to the phase-owner source-age construction.

## Distant Farey-boundary cross-check

At s=1,106,743 the prior Farey denominator pair is (i,j)=(476,361,630,382); the new longest class is the old u class, with sources [0,630382). It contains a complete uniform 389-source block, hence F_new(s)=0. The independent R45 boundary formula gives

    R_s=1-128*(476361*theta-124904)
       =15987713-60974208*theta.

The age compiler agrees. All 77 cross-stage boundary identities were separately checked, including 51 after one million cuts; the first two recover F_new(164)=67, F_new(225)=0.

## Complexity, reproduction and acceptance

For S Farey stages, m original arcs, a certified block length H and K emitted runs, the source-labelled compiler uses O(m log m + S H log m + K) comparisons/records plus Farey updates and exact parameter/order certificates. Modulo phase operations act on integers with bit length depending on source index and theta enclosure denominator, and their actual multiplication/division bit costs, historical preprocessing, precision construction and K-output cost are retained. On this frozen run S=78, H=389, K=298. The new method supplies a proof-certified independent long-horizon generator; R32's specialized shorter age shortcut can still be faster.

The standalone Python stdlib verifier is VERIFY_R46_COMPACT.py. The full executed author-side package additionally preserves VERIFY_R46.py, VERIFY_R46_STABILITY.py, VERIFY_R46_BOUNDARY.py, exact 78-stage certificate, generated TSV and immutable R32 regression oracle. Mathematical proof, exact finite validation, independent review and task acceptance are separate statuses.
