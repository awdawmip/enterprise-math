# D25 — Exact low/far-upper finite Clausen defect via two source moments

**2026-11-03 +08:00 / AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**
TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Native H0/B0=NOT_EXECUTED; original mother `Delta_p-R_p=0 (mod p)` remains OPEN.

## Exact source and H4 theorem

For p=6r+1>=7 prime, set z0=1/2, c_k=(1/6)_k(1/3)_k/(k!)²,
`G(z)=sum_{k=0}^{p-1}c_k z^k`,
`F(z)=sum_{k=0}^{p-1}a_k z^k`,
`a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³`, theta=z d/dz.
The inherited classical formal Clausen identity `(sum_{k>=0}c_k z^k)^2=sum_{k>=0}a_k z^k` gives **exactly** `F=[G²]_{<p}`, i.e. equality of every coefficient in degrees below p, before modular reduction. The previous H3 original-source scalar defect is

`E_p=([(1+6theta)(F-G²)](z0))/p² (mod p)`.

The exact valuations in the *finite* Gauss coefficients are:
`v_p(c_k)=0` for 0<=k<=r; `v_p(c_k)=1` for r<k<=2r; and `v_p(c_k)=2` for 2r<k<=p-1.

Define the nonzero unit U_p=c_(p-1)/p² mod p, and
`A_0=1`, `A_s=(s!)²/[(11/6)_s(5/3)_s]` for 0<=s<=r-1.
Set `L_k=binom(r,k)binom(2r,k)` for 0<=k<=r, and the two prefix moments
`Lambda_k=sum_{s=0}^{k-1}2^s A_s`,
`Gamma_k=sum_{s=0}^{k-1}s*2^s A_s`, in F_p.

**H4 (PROVED for all p=6r+1>=7):**

`E_p=-2U_p sum_{k=1}^r L_k 2^(-k) [(6k-5)Lambda_k-6Gamma_k] (mod p).`

For the specified E_p observer this is a certified low/far-upper Gauss-pair localization: one upper boundary unit and **two running prefix moments** replace the full finite-Clausen polynomial convolution. A recurrence constructs it with O(p) modular operations when U_p is obtained from the original Gauss coefficient recurrence. The transformation retains original index and signed-weight provenance.

## Proof

The exact truncation identity gives `F-G²=-sum_{n=p}^{2p-2}[z^n]G² z^n`. For n=k+l>=p with 0<=k,l<=p-1, both indices cannot be <=2r since 4r<p. Thus at least one lies in the high band >2r and carries p². To survive after dividing by p² and reducing mod p, the other must lie in the **low** band <=r (valuation 0); mid/high and high/high pairs vanish. The k=0 case requires l>=p and is absent. The two ordered permutations give a factor 2.

Writing l=p-1-s, the cutoff k+l>=p is exactly 1<=k<=r and 0<=s<k. Consequently

`E_p=-2 sum_{k=1}^r sum_{s=0}^{k-1}(6(k+p-1-s)+1)c_k(c_(p-1-s)/p²)2^{-(k+p-1-s)} (mod p).`

The **exact** backward Gauss recurrence is
`c_(n-1)/c_n=n²/[(n-5/6)(n-2/3)]`.
For n=p-1-t it reduces mod p to `(t+1)²/[(t+11/6)(t+5/3)]`, whence by induction

`c_(p-1-s)/p²=U_p A_s (mod p).`

The old finite Gauss congruence gives c_k=L_k mod p for k<=r. Fermat yields 2^(-(p-1))=1, while the signed Euler weight becomes `6(k+p-1-s)+1=6k-6s-5 (mod p)`. The inner sum is thus `(6k-5)Lambda_k-6Gamma_k`, proving H4. QED.

Each A_s and its recurrence is a p-unit on 0<=s<r:
`A_(s+1)=18(s+1)² A_s/[(6s+11)(3s+5)]`.
Update moments by `Lambda_(k+1)=Lambda_k+2^k A_k`,
`Gamma_(k+1)=Gamma_k+k 2^k A_k`.
Only the declared E_p observer is compressed; no universal permission to erase full source/branch state is inferred.

## Actually executed exact checker

An independent author-side Python standard-library script `d25_clausen_defect_tail_20261103.py` computes original F and truncated Gauss G by distinct coefficient recurrences modulo p³, then directly obtains E_p from the weighted difference /p². Independently it uses U_p plus the two new low-prefix moments. **All 312** target-class primes 7<=p<=10000, p mod24 in {13,19}, passed both calculations. Examples: p=19 has U=2, E=7; p=373 has U=112, Lambda_r=77, Gamma_r=347, and E=177; p=1171 has U=1054 and E=0. This is finite exact validation alongside the all-domain algebraic proof; not native H0/B0 or independent mathematical acceptance. Reproducible input/program/readout are `d25_clausen_defect_tail_20261103.py` and `d25_clausen_defect_tail_20261103_results.json`.

## Next exact scientific action

Substitute H4's proven two-prefix defect into the earlier H3 original 216 signed-carry relation
`W/p=-6delta d²+p[4delta²d²-6epsilon d²+E_p] (mod p²)`.
Search for a terminating Gauss/CM or WZ certificate (or exact counterexample) coupling the second Hensel digit epsilon to H4's upper-tail source. Compare the two-prefix carrier to the existing three-band 216 source tower without losing original index/valuation, and derive the exact mapping to the **distinct** frozen mother Delta_p-R_p observer before any claim of task closure. Source/Gateway 0.6.11 still requires upstream code review, has no research authority or executor binding and native active-job quota 5/5; current D25 continuation read returned CONTROL_QUOTA. Support #1558 controls native repair; #1559 the separate p373 native H0/B0. No new session, claim, authorized run, checkpoint, Result, review or scientific admission is claimed.
