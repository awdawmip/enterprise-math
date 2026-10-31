# Stage248 — exact horizon phase diagram for separate error caps

**2026-10-28 — AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** Parent Stage247 proof, exact code and certificate are in commit c2dbf682c021327dee18f57e2c6864feb6a09a39 under research_notes/n14_aux_iid_asymmetric_247_r2_local_20261028_1914/. This theorem concerns ONLY the external ternary IID laws P=(3,1,20)/24 and Q=(2,2,20)/24. A common full-ordered-history randomized stopping and classification policy may stop at integer time 0 through N. Define eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau), V_N(a,b)=min max(tP,tQ) subject to eP<=a and eQ<=b.

## Theorem, every integer horizon N>=1

For the *separate* caps a=3/10 and b=19/40:

- N<=8: NO feasible policy, so V_N(a,b)=+infinity.
- 9<=N<=12: feasible but strictly above the universal sequential TV lower bound: 27/5<V_N(a,b)<=9.
- N>=13: the bound is attained, exactly V_N(a,b)=27/5.

This is the complete horizon classification of cap feasibility and TV-bound sharpness, not an exact intermediate-period value theorem.

## A. Rational impossibility at N<=8

Every bounded stopping policy with horizon<=n can be expressed as a randomized terminal-decision kernel of a complete n-observation history: sample unused IID observations after its stopping time and ignore them. Therefore the finite total-variation data processing inequality applies without any Markov assumption on its original ordered stopping history:

1-eP-eQ <= TV(P^n,Q^n).

For n=8 calculate exact TV by the count triples x+y+z=8:

TV(P^8,Q^8) = (1/2) sum_{x+y+z=8} [8!/(x! y! z!)] *
 abs[(3/24)^x(1/24)^y(20/24)^z - (2/24)^(x+y)(20/24)^z]
 = 24591244757/110075314176.

But caps demand 1-eP-eQ >= 1-a-b=9/40, and

9/40 - TV(P^8,Q^8) = 878504663/550376570880 > 0.

This is a complete exact impossibility certificate for N=8 and all lower N by padding. Count grouping is valid for the full-terminal TV observer. As a separate crosscheck, all 3^8=6561 unmerged complete ordered histories were enumerated in Fraction arithmetic and gave the identical TV.

## B. Explicit N=9 feasible policy

Take exactly nine observations; for every ordered history h compute both exact positive masses p(h)=product_i P(h_i) and q(h)=product_i Q(h_i). Decide P if p(h)>q(h), decide Q if p(h)<q(h), and if tied decide P with probability 3/4, Q with probability 1/4. The count shortcut for the terminal likelihood comparison does not alter the full ordered observer: all P/Q history weights were independently enumerated.

Exact error sums (both 55 count triples and 3^9=19683 unmerged ordered histories) are

eP=16038379873/55037657088,  eQ=604628965/1289945088.

Both caps are strictly respected, with margins

a-eP=2364586267/275188285440 >0,
b-eQ=40474759/6449725440 >0.

Here tP=tQ=9. Thus N>=9 is feasible and V_N(a,b)<=9. Combined with A, N=9 is the *first* feasible horizon.

## C. Sharpness threshold N=13

Source-labeled sequential total-variation coupling in Stage246/247 establishes, for all full-history policies and finite N,

V_N(a,b)>=24(1-a-b)=27/5.

Stage247 proved an exact necessary-and-sufficient condition for *equality*, not merely sufficiency of one policy. For a+b<1 the policy must stop on first non2 symbol; let its total non2-signal mass be s. The equality equations impose s=4(1-a-b)=9/10 and z=2a+b-1=3/40 for total no-signal Q-guess mass. A horizon N can realize this only if

s<=1-(5/6)^N;

the two other Stage247 error-balance inequalities are satisfied by this cap pair. Rational signs locate the threshold:

s-[1-(5/6)^12] = 132311957/10883911680 >0,
[1-(5/6)^13]-s = 426831383/65303470080 >0.

Thus N<=12 cannot attain the TV bound. For feasible N=9,10,11,12, the policy observation set is the image of a finite-dimensional compact randomized policy polytope, so the infimum is attained and strictly larger than 27/5. No unobserved limit of adaptive strategies can evade the equality obstruction.

At N=13 take a positive-branch first-non2 rule with independent initial activation probability

w = (9/10)/[1-(5/6)^13] = 58773123072/59199954455.

If not activated, guess immediately; if activated, stop on first 0 (decide P), first 1 (decide Q), or after 13 symbols all equal 2. At every no-signal stop, guess Q with probability q=3/4, else P. The exact 13-sample source-labeled positive-path computation gives 30 ordered leaves, sums P/Q masses each to one, and yields

(eP,eQ,tP,tQ)=(3/10,19/40,27/5,27/5).

It meets the universal lower bound. Every N>=13 may reuse this at-most-13-sample policy, proving the sharp third case.

## Verification, method scope, authority and next question

Actually executed Python Fraction verifier verify_stage248.py outputs STAGE248_MIN_HORIZON_EXACT_PASS and checks:
(i) n=8 exact TV by independent count and 6561-history sums;
(ii) n=9 exact count-triple and 19683-full-history error sums, with rational cap margins;
(iii) n=13 explicit source-labeled policy, exact terminal mass normalization and all four observers, 30 ordered leaves;
(iv) exact positive horizon obstruction/feasibility margins.

These finite computations certify the finite arithmetic. The every-horizon theorem follows from the data-processing argument, the already-supplied Stage247 all-real equality rigidity theorem and the monotonic use of shorter rules at larger horizons.

BRC method applies to positive weighted source-labeled P/Q paths, survival hazard, branch identity and full P/Q observer separation. Count compression is justified only for fixed-time terminal likelihood/TV. P000's six native axes, triadic balance and future joint-observer obligations remain untouched; no native BRC software execution or X6 embedding is claimed.

This portable author scientific result is UNREVIEWED / NOT_ADMITTED. Native em_status reported research_authority_granted=false and the current owner query returned CONTROL_QUOTA. Neither a GitHub PR nor a local activity ID is a native claim, Source Result, Driver review or mathematical promotion.

**Stage249 open problem:** compute V_9(3/10,19/40), or V_12(3/10,19/40), *exactly* rather than the strict interval 27/5<V_N<=9. Give a rational feasible full-history policy and an exact two-time/two-error primal-dual certificate; justify observer-preserving Markovization before a quotient, and report formal admission separately.
