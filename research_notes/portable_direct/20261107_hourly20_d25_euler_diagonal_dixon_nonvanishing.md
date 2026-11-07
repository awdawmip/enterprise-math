# D25 — Dixon evaluation of the B5 Euler-cutoff diagonal

2026-11-07 · TASK_RESEARCH / author-side theorem + exact computation · UNREVIEWED / NOT_ADMITTED.

Parent `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Hourly20 reported lane `chatgpt-research-hourly-enterprise-math-20260923`; distinct maintenance lane `chatgpt-hourly-enterprise-math-20260921` not used. This portable proof is not a native session/CLAIM/run/result.

## Exact input and problem

The previously published B5 reflected-prefix observer at `10635cfb1086d1c59ba7ca61a03a6f87c6744a5e` (another Research lane's author science, not its identity) introduced the Euler finite-cutoff diagonal
[
 T_{B,p}=2\beta\sum_{j=0}^{k}q_jr_j\pmod p,\quad \beta=1/9,
]
where (p=8k+5) is prime,
[
 q_j=\binom{k}{j}\binom{3k+1}{j},\quad
 r_j=\frac{3\,k!\,(3k+1)!\,(j!)^2}{64\,(k+j+1)!\,(3k+j+2)!}\quad(0\le j\le k).
]
Here (3\,k!) means (3\times(k!)), matching the original executed recurrence (r_0=3/[64(k+1)(3k+2)]). All denominators are units in (mathbb F_p). Previous evidence observed nonzero diagonals at 48 target primes below 2500; the universal status was open.

## Theorem: exact closed form and universal nonvanishing

For every prime (p=8k+5\ge5),
[
 \boxed{T_{B,p}\equiv\frac{(k!)^2((3k+1)!)^2}{192}\ne0\pmod p.}\tag{1}
]
Thus, in particular, **the B5 Euler cutoff diagonal is nonzero for all** (p\equiv13\pmod{24}). This is a statement about the individual provenance-tagged diagonal, not the complete B5 overflow observer (E_B).

### Proof over rational numbers and reduction to finite characteristic

Let (r_0=3/[64(k+1)(3k+2)]). Cancellation yields
[
 \frac{q_jr_j}{r_0}=
 \frac{(-k)_j(-3k-1)_j}{(k+2)_j(3k+3)_j}.
]
Because ((1)_j/j!=1), the exact rational sum is
[
 S_k=\sum_{j=0}^{k}\frac{q_jr_j}{r_0}
 ={}_3F_2\left(\begin{matrix}1,-k,-3k-1\\k+2,3k+3\end{matrix};1\right).
]
This is Dixon's well-poised ({}_3F_2(1)) sum with (a=1,b=-k,c=-3k-1). Its convergence condition (1+a/2-b-c=4k+5/2>0) is satisfied, and the sum terminates at (j=k). Apply NIST DLMF §16.4.4 (https://dlmf.nist.gov/16.4.E4):
[
\begin{aligned}
S_k&=\frac{\Gamma(3/2)\Gamma(k+2)\Gamma(3k+3)\Gamma(4k+5/2)}
{\Gamma(2)\Gamma(k+3/2)\Gamma(3k+5/2)\Gamma(4k+3)}\\
&=\frac{2((k+1)!)^2((3k+2)!)^2(8k+4)!}
{(2k+2)!(6k+4)!((4k+2)!)^2}.
\end{aligned}\tag{2}
]
Every denominator factorial in (2) is indexed below (p), as are the original Pochhammer denominators. Hence (2) reduces faithfully modulo (p). Since (T_{B,p}=2r_0S_k/9), one obtains
[
 T_{B,p}=\frac{(p-1)!k!(k+1)!(3k+1)!(3k+2)!}
 {48(2k+2)!(6k+4)!((4k+2)!)^2}\quad\bmod p.\tag{3}
]
Wilson reflection gives
[
 (p-1)!=-1,\quad ((4k+2)!)^2=-1,\quad
 (6k+4)!(2k)!=-1\quad\bmod p.
]
Substitute into (3):
[
 T_{B,p}=-\frac{(k!)^2((3k+1)!)^2(3k+2)}{96(2k+1)}\pmod p.
]
From (8k+5\equiv0\pmod p) follows ((3k+2)/(2k+1)\equiv-1/2), proving (1). Every numerator factorial is indexed below (p), and (p\nmid192). Therefore (T_{B,p}\ne0) for **all** primes in the stated class, including (p=5). QED.

## BRC observer consequence

The B5 stream carries Euler flag (C(z)=1-z), reflected index (p-1-j), the cutoff boundary (i=j), and the weight operator (1+8z\partial_z). The corresponding boundary component (T_{B,p}) is always a unit; any source-aware Fricke/gauge/adjoint formula must explicitly retain or exactly compensate it. The B3 stream (the (p\equiv19\pmod{24}) target class) uses (C(z)=1) and has no Euler boundary term. As a direct corollary, at any nonzero (x\in\mathbb F_p), the same diagonal port equals (2x\sum_jq_jr_j=9xT_{B,p}\ne0).

## Independent executable finite checks

Companion standard-library checker `d25_euler_diagonal_dixon_20261107.py` was implemented and executed. Exact rational terminating series vs the factorial quotient: (k=0,\ldots,11), all equal. For all **1292 primes** (p<50000), (p\equiv5\pmod8), independent finite-field q/r recurrences agreed with both factorial formulas, and each value was nonzero. Examples: p:T = 5:3, 13:3, 29:2, 37:16, 61:25, 109:36, 373:289, 997:741. Computation validates the implementation; universal nonvanishing follows from Dixon+Wilson.

## Frontier, native state and next experiment

Mother target still OPEN: (W_p\equiv p\pmod{p^3}), equivalently the frozen (\Delta_p-R_p\equiv0\pmod p), for (p\equiv13,19\pmod{24}). Next: insert (1) into B5 reflected-prefix equation (3) from `10635cf...`, and into Cartier port equations from `463de60c...`; find a source-aware Fricke/adjoint **off-diagonal compensation** consistent with both streams' lower Gauss injections. Discriminate at p=13,19,43,67,373; do not repeat the earlier full sums or native p373 H0/B0, which remains separately due with independent replication (#1559).

Native status was read in this run: `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; Site `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. Original requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` remain historical/unreconciled. No native Researcher authority, claim, run, checkpoint, Result or mathematical admission is asserted. Author-side status: `REGISTER_PENDING / SYNC_DEBT / UNREVIEWED / NOT_ADMITTED`.
