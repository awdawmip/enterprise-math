# D25 — Franel/Harmonic E.2 two-jet and exact three-shell comparison for original 216

Date: 2026-11-06. Author-side portable research, NOT native fixed-373 execution or Source result acceptance.
TASK_RESEARCH / D25 / SECOND-DIGIT-LIFT. Task TP2-B6F4FC938FF94941C1B7.
Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
Current Research logical lane as supplied: chatgpt-research-onhour-enterprise-math-20260923.
Prior verified scientific frontier: original three-shell theorem at enterprise-math@eec361046d7677ee6b53bf85786af97e616e325d.
Status: AUTHOR-PROVED FINITE-VERIFIED UNREVIEWED NOT_ADMITTED; historical E.2 theorem used with explicit external provenance.

## Theorem A: exact terminating Franel/harmonic two-jet, all p=6m+1>3

Define
  V_p = sum_{n=0}^{p-1} (-1)^n(6n+1)((1/3)_n/n!)^3.
For 0<=n<=2m define B_n=binom(2m,n)^3 and
  H_{s,n}=sum_{j=2m-n+1}^{2m} 1/j^s   (empty sum = 0, s=1,2).
Set
  F_m = sum_{n=0}^{2m} B_n,
  L1_m = sum_{n=0}^{2m}(6n+1)B_n H_{1,n},
  L2_m = sum_{n=0}^{2m}(6n+1)B_n(H_{1,n}^2-H_{2,n}/3).

All rational denominators 1..2m are p-units. Then

  V_p = p F_m - p L1_m + (p^2/2) L2_m     (mod p^3).      (A)

The unperturbed coefficient has a stronger, exact integer identity:
  sum_{n=0}^{2m}(6n+1) binom(2m,n)^3 = p F_m.           (B)

Proof. Since 1/3=-2m+p/3,
  (-1)^n((1/3)_n/n!)^3
   = B_n product_{j=2m-n+1}^{2m}(1-p/(3j))^3
   = B_n[1-p H_{1,n}+(p^2/2)(H_{1,n}^2-H_{2,n}/3)]
     modulo p^3, for n<=2m.
For 2m<n<p, one factor of (1/3)_n is p/3, hence its cube has valuation
at least 3 and the term vanishes modulo p^3. This proves (A) except (B).
For (B), use B_n=B_{2m-n}, and (6n+1)+(6(2m-n)+1)=12m+2=2p.
Pairing all indices, including the fixed midpoint, proves (B) over Z.

Theorem (A) is a new explicit finite-jet representation of V_p; it is
not the known Van Hamme E.2 result itself.

## Imported external theorem and scoped consequence

The independently established Van Hamme E.2 congruence, quoted in
Guo–Schlosser, Results in Mathematics 78 (2023), Art.105, equation (1.2),
states for p=1 (mod 3):
  sum_{n=0}^{(p-1)/3} (-1)^n(6n+1)((1/3)_n/n!)^3 = p (mod p^3).
URL https://doi.org/10.1007/s00025-023-01885-8
The tail beyond (p-1)/3=2m vanishes as already proved. Therefore the
new Franel/harmonic observer satisfies the rigorous corollary, dependent
on that published E.2 result:
  F_m-L1_m+(p/2)L2_m = 1  (mod p^2).                    (C)

This source is external published mathematics and not native D25
original-216 experimental evidence or a frozen SOURCE scientific pin.

## Theorem B: original-216 finite 3-jet evaluator, all p=6m+1>3

Let a_n=(2n)!(3n)!/[216^n(n!)^5], W_p=sum_{n=0}^{p-1}(6n+1)a_n.
Define a rational-polynomial finite family
  A_n(t)=(-3m+t/2)_n(-2m+t/3)_n(-4m+2t/3)_n/[2^n(n!)^3],
with t-adic coefficients A_{n,r}=[t^r]A_n(t), r=0,1,2.
Then A_n(p)=a_n identically for 0<=n<p, and the source recurrence
  36(n+1)^3 A_{n+1}(t) =
  (2(n-3m)+t)(3(n-2m)+t)(3(n-4m)+2t)A_n(t)
holds in Q[t].
For x=n-3m, y=n-2m, z=n-4m, define
  c0=18xyz,
  c1=12xy+3z(2x+3y),
  c2=2(2x+3y)+3z.
The first three coefficients obey the exact recurrences
  36(n+1)^3 A_{n+1,0}=c0 A_{n,0},
  36(n+1)^3 A_{n+1,1}=c0 A_{n,1}+c1 A_{n,0},
  36(n+1)^3 A_{n+1,2}=c0 A_{n,2}+c1 A_{n,1}+c2 A_{n,0},
with initial A_{0,0}=1, A_{0,1}=A_{0,2}=0.
The unshifted t-polynomial has three precise zeros and consequently
  A_{n,0}=0 for n>2m;
  A_{n,1}=0 for n>3m;
  A_{n,2}=0 for n>4m.
Let J_r=sum_{n=0}^{p-1}(6n+1)A_{n,r}. Then
  W_p = J0+p J1+p^2 J2  (mod p^3).                       (D)
Proof: expand A_n(p) to degree two in the p-adic argument; all 1..p-1
denominators are p-units. The staircase follows by the zero factors
at n=2m,3m,4m; coefficient r only survives after r parameter
derivatives at the corresponding roots. Formula (D) retains the full
original coefficient family and its valuation-two gap.

## Exact mother-task bridge still requiring proof

The earlier original-216 three-shell theorem proved, for p=6m+1>3,
  W_p = P_{2m+1}
    + (p*a_{2m}/32)(Q0+p Q1)
    - (p^2*a_{2m}/576)q_{m-1}G0  (mod p^3),
where P, Q0, Q1, q, G0 have their exact definitions in
research_notes/portable_direct/20261106_onhour_d25_original216_three_shell_middle_jet.md
(commit eec361046d7677ee6b53bf85786af97e616e325d).
Combining that proved representation with (A), the wanted finite
transformation W_p=V_p (mod p^3) is precisely equivalent to

  P_{2m+1}+(p*a_{2m}/32)(Q0+p Q1)
     -(p^2*a_{2m}/576)q_{m-1}G0
   = p F_m-p L1_m+(p^2/2)L2_m  (mod p^3).               (E)

Equation (E) is a SPECIFIED OPEN UNIFORM CANCELLATION CLAIM, not a
consequence of (A)-(D) alone. If proved on p=13,19 (mod24), it finishes
the original scalar goal W_p=p (mod p^3) using established E.2. The
different proof channel through native p373 H0/B0 remains mandatory
for its own native benchmark, independent of scalar proof status.
Another exact equivalent formulation is:
   J0+p J1+p^2 J2 = p F_m-p L1_m+(p^2/2)L2_m (mod p^3).
This identifies a finite potential WZ/creative-telescoping pair with
explicit parameter deformations, not an assumption of its equality.

## Exact arithmetic and BRC provenance

Program d25_franel_e2_bridge_check_20261106.py independently evaluates
original factorial/binomial W, rational E.2 recurrence (including all
n<p), integer Franel and harmonic first/second jets. Program
d25_parameter_jet_oracle_20261106.py independently evaluates original
W via a t-polynomial derivative recurrence and binomial product.
Both were actually executed using Python standard library on all 148
primes 7<=p<=1999 with p=1 (mod6), including 77 target primes.
All verified equalities and the *observed* W=V passed, failures=0.
This finite numerical equality is NOT the missing uniform proof (E).

p=19: F mod361=22, L1 mod361=59, L2 mod19=4;
   22-59+19*4/2 = 1  (mod361);
   J0 mod6859=5491, J1 mod361=282, J2 mod19=8.
p=373: F mod139129=2421, L1 mod139129=5031, L2 mod373=14;
   2421-5031+373*14/2 = 1  (mod139129);
   J0 mod51895117=15521276, J1 mod139129=47909, J2 mod373=133.
For the original-216 p^2 valuation shell, the earlier source had
nonzero gap p19=3249=9*19^2 and p373=37008314=266*373^2.
All these signed/source-indexed contributions must remain represented.

BRC decision: COMPOSE_APPLIED. Carrier is
(n, original family, valuation shell, signed rational p-unit residue,
first/second parameter jet, external-source label, weight 6n+1).
Observer retains Franel/216 source identity and residue; quotienting
to total W alone would conceal the nonzero shell and correlated jets.
No native six-dimensional spatial-model transfer is asserted.

## Recovery and next exact step

Parent: D25 SECOND-DIGIT-LIFT, frozen original target W_p=p modp^3 for
p=13,19 mod24, source scientific input c47e13e4aba0e006366f989d6334d443f6333ae3.
Highest persisted source/checkpoint before this portable author unit:
native client revision 22 SERVER_SQLITE_COMMITTED and GitHub
eec361046d7677ee6b53bf85786af97e616e325d.
Unresolved native Source request: onhour11-20261106-1400-exact-research-lane-continuation,
same-ID reconciliation returned QUEUED after EVENT_COLLECTION_IO. No
current Source researcher session, claim, run or formal Result asserted.
Sites gateway v0.6.11 reported research_authority_granted=false, so no
role-bound mutation attempted. Old 3 staging records remain separately
provenanced, not imported into admitted Result.

Next smallest mathematical unit: seek a uniform finite WZ certificate
for equality (E), retaining the original low/middle/gap and the two
Franel harmonic jets, or a concrete obstruction to a specific candidate
WZ ansatz; test p=19 and p=373, including nonzero gap. Parallel native
support #1559 remains OPEN UNASSIGNED / NOT_EXECUTED / PENDING_OWNER;
requires same-original-class H0/B0 divided-power [X]U mod p^2,
Frobenius direction/eta, signed odd Green/Hesse/kappa and independent
reproduction by an actually authorized native executor. Portable
computations do not discharge that native experiment.
