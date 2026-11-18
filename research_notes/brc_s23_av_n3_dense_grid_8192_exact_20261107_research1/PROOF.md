# S23 conditional AV: a uniform three-trial bound below 0.23805

Date: 2026-11-07. Status: AUTHOR_EXACT_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: research_notes/brc_s23_av_n3_uniform_quarter_upper_20261107_research1/ at commit 4e5f90f36d34ba1504dd4a9da38ded7006cc0a77 (PR #1777).
Reused kernel: predecessor KERNEL.json (Git blob 564acd9574876059c505fd8a40d14f2f6e0e3736); copied in VERIFY_EXACT.cpp as its same 8x27 integral coefficient matrix.

## Theorem

Let a,c range over the complete **real** box [1/2,7/8]^2. Put z=(1-a)c and let A(a,c) be the ordered three-label distribution (a,z,(1-a)(1-c)), with output labels (stop1,stop3,stop4). Let B(z)=(z,1-z), with Y=stop3,N=other. One unknown parameter pair is shared by three conditionally IID observations. For a parameter-independent stochastic 8x27 Markov kernel K, define

    E_K(a,c)=TV(A(a,c)^tensor3, B(z)^tensor3 K)
    delta_3=inf_K sup_{a,c in [1/2,7/8]} E_K(a,c).

Using the **same explicit rational K** as the predecessor, we certify

    delta_3 <= sup E_K
            <= 21441159240880986373 / 90071992547409920000
            = 0.23804468663880515...
            < 4761/20000 = 0.23805.

The previously established fiber bound 5211/21952 <= delta_3 remains valid. Thus the author-side bracket is

    5211/21952 <= delta_3 < 4761/20000,

whose certified upper-to-lower gap is below 0.000669.

## Analytic extension to all real parameter pairs

The preceding proof's coupling and Markov data-processing estimate gives

    |E_K(a,c)-E_K(a',c')|
      <= 3 TV(A(a,c),A(a',c')) + 3 TV(B(z),B(z'))
      <= 3*(2|a-a'|+|c-c'|).

For integer N, take the (N+1)^2 grid a_i=c_i=1/2+3i/(8N), 0<=i<=N. Every real parameter pair has a grid point at coordinate distance at most 3/(16N), so

    sup_real E_K <= max_grid E_K + 27/(16N).   (*)

This inequality holds for the complete continuous parameter square with the same K.

## Exhaustive exact grid certificate

Use N=8192 and D=8N=65536. At index (i,j), let
A0=4N+3i, C0=4N+3j, d=D^2,
p=[A0*D,(D-A0)*C0,(D-A0)*(D-C0)],
and w=d-p[1]. Then p entries are the exact one-trial A numerators over d; B numerators are [p[1],w] over d. Let M=1000000 and Knum be the integer kernel in VERIFY_EXACT.cpp.

For an output triple x, let n_r(x) count its label r. For each binary input triple y let h(y) be its count of Y; define G[x,h]=sum_{y:h(y)=h} Knum[y,x]. The *exact* integer numerator of the total variation at grid point (i,j) is

    T_ij = sum_{x in {0,1,2}^3}
      | M * product_{r=0}^2 p[r]^{n_r(x)}
        - sum_{h=0}^3 G[x,h] * p[1]^h * w^(3-h) |.

Then E_ij=T_ij/(2*M*D^6). The compiled C++17 program enumerates all 67,125,249 grid points and 1,812,381,723 individual ordered-output differences in exact signed-128-bit integer arithmetic. It reports

    max_ij T_ij = 37687045240223169510308060122316800
    denominator   = 158456325028528675187087900672000000
    maximizing grid indices (i,j)=(4508,8192).

Reduced,

    max_grid E_K = 21422604982162266373 / 90071992547409920000
                 = 0.2378386929864614...

Substitution into (*) gives

    sup_real E_K
      <= 21422604982162266373 / 90071992547409920000 + 27/131072
       = 21441159240880986373 / 90071992547409920000
       < 4761/20000.

The strict final inequality is checked using arbitrary precision boost::multiprecision::cpp_int products. During enumeration the integers stay within signed __int128: all probability numerators are nonnegative and normalized; for every (i,j), 0<=T_ij<=2*M*D^6, and for N<=8192, 2*M*D^6 < 2^127. The intermediary products are bounded by M*D^6. The aggregation G has nonnegative entries and each of eight kernel rows sums to M, verified by the program.

For independent continuity with predecessor certificate, the same program at N=256 yields the exact predecessor maximizer (141,256) and the same grid maximum 0.23783863368509628... . No floating point operations enter the certificate. Timing values are diagnostic only.

## Meaning and open frontier

This retains BRC positive-rational branch identities and the ordered observer map stop3->Y, stop1/stop4->N (BRC REUSE_APPLIED). It is a finite-n theorem about the **conditional AV auxiliary observation experiment**, not an automatic theorem for the six-source/ten-label S23 mother problem. Native P000 and ACTIVE worldview remain fixed. The user-facing mother bridge still requires its lawfully defined source and encoder/decoder maps.

Next: replace uniform Lipschitz enclosure with exact interval/Bernstein bounds for the fixed K, then attempt a primal/dual exact minimax certificate for delta_3; in parallel investigate the lawful ten-label bridge.
