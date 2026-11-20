# C02 / Euler recorder: exact repeated-coupling time-window aliasing

Date: 2026-11-20. Scope: `RS-EULER-RR-20261012-10`, symbolic finite Z3 positive-world model; author-side note; NOT_REVIEWED. This derives a new *conditional time-window identity* from the frozen ideal recorder E, not a native heartbeat timing/physical-measurement law. Original BRC ZIP and actual implementation remain separately unresolved.

## Frozen assumptions

Each complete positive world w carries fixed weight p_w>0, sum_w p_w=1, and labels j_w,a_w,r_w in Z3. Define E(j,a,r)=(j,a,r+j-a), and omega a primitive cubic root with omega^2+omega+1=0. The source and reference labels remain unchanged while E is applied n consecutive times. Initially the receiver is calibrated: r_w=a_w. The integer n counts *applications of E*; no claim is made that one such operation equals one unit of native physical time. No intervening feedback, register query or changing weight is included.

## Proposition and proof

Put d_w=j_w-a_w (mod 3). Iteration gives r_w(n)=a_w+n d_w. At n>=1 the within-world source/receiver relative phase is omega^(r_w(n)-j_w)=omega^((n-1)d_w). The single-observation correlation is
C_RS(n)=sum_w p_w omega^((n-1)d_w).
Consequently C_RS(1)=1 for every calibrated input, while the average of N consecutive observations is
Cbar_RS(N)=sum_w p_w A_N(d_w),
A_N(d)=(1/N)sum_{k=0}^{N-1} omega^(k d).
If d=0, A_N=1. If d=1 or2, the cubic relation gives
A_N(d)=0 for N=0(mod3);
A_N(d)=1/N for N=1(mod3);
A_N(d)=(1+omega^d)/N for N=2(mod3).
Thus |A_N(d)|=0 when 3 divides N, otherwise exactly 1/N. Writing p0=sum_{w:d_w=0}p_w, we obtain
Cbar_RS(3m)=p0 (m>=1),
|Cbar_RS(N)-p0|<=(1-p0)/N for all N>=1.
For the same setup, every branch returns to its initial receiver after three E applications, E^3=I. Hence repeated *engaged* coupling and disengagement immediately after the first perfect recording are distinct protocols, despite the same initial preparation.

## Sharp positive-weight witness

Take three complete positive worlds p_w=1/3, a_w=0, r_w=0, j_w in {0,1,2}. All worlds have r(1)=j and C_RS(1)=1. Under repeated coupling, the exact 3-observation time average is 1/3: the j=0 branch contributes 1 and the j=1,2 branches each average to zero. For n=2, C_RS(2)=(1+omega+omega^2)/3=0. If the interaction is disengaged after n=1 and the receiver is held fixed with no further query/write, then C_RS(n)=1 for all later readings. The same single-time source/receiver record is therefore insufficient to specify later time-window correlations unless the future interaction protocol is retained.

The result distinguishes a complete-world branch correlation, the temporal average of such correlations, and independent single-register marginal statistics. The result requires no factorization of positive world weights or independent reference/source labels. It does not examine first environmental memory reuse, actual typed-BRC contacts, hidden-path timing, old-value inverse cleanup or the four original ZIPs.

## Recalculation

Use exact quotient ring Q[omega]/(omega^2+omega+1), represented by integer/rational coefficient pairs (a,b) for a+b omega. Check d=0,1,2 and N=1..12 by direct enumeration, compare against the three residue cases. Expected test: every case passes; at N=3,6,9,12 nonzero d averages (0,0), and at N=3m+1 they are (1/N,0). Companion file: `check_eulerrr_time_window_20261120.py`.

Source: fixed C02 taskbook `research_tasks/RS-EULER-RR-20261012-10_C02_GEN2.md` at `b29cadc5dd6eca7b76723b27eaefafaeaf42aa8d`; prior provisional recorder note `research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md` at `a6627d28d1e02f16ec5ca4d5118801c005cca583`. This is a scoped deduction of the frozen E identity with a new averaged-observation statement; independent review NOT_REVIEWED.
