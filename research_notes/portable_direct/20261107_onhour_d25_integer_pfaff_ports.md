# D25: Integer Pfaff ports for the original-216 Gauss first digit

Date: 2026-11-07. TASK_RESEARCH author-side second scientific unit in the same on-hour lane chatgpt-research-onhour-enterprise-math-20260923. Separate maintenance lane chatgpt-hourly-enterprise-math-20260921 excluded. Publication TP2-B6F4FC938FF94941C1B7; frozen input c47e13e4aba0e006366f989d6334d443f6333ae3. Status: exact elementary transformation PROVED / finite character classification CHECKED / UNREVIEWED / NOT_ADMITTED. Consumes (without recredit) the first-digit Gauss/216 factorization published at 60ee874dfc21167baa5fb984b6ac3816fe2cbe10.

## Exact integer transformation, valid for EVERY integer m>=1

Set D_m(z)=sum_(k=0)^m binom(m,k)binom(2m,k) z^k. Define INTEGER ports
  S_m=sum_(k=0)^m binom(m,k)binom(2m+k,k),
  T_m=sum_(k=0)^m k binom(m,k)binom(2m+k,k).
Then the following two equalities hold over Q for every m>=1:
  2^m D_m(1/2) = S_m,                                     (I)
  2^m [D_m(1/2)+6D'_m(1/2)] = (1-12m)S_m+24T_m.         (II)

Proof. Apply the terminating Pfaff hypergeometric transformation with a=-m, b=-2m, c=1:
  D_m(z)=(1-z)^m _2F1(-m,2m+1;1;z/(z-1)).
The terminating function on the right equals
  G_m(w)=sum_(k=0)^m binom(m,k)binom(2m+k,k)(-w)^k.
At z=1/2, w=-1, w'=-4; thus G_m(-1)=S_m and G'_m(-1)=-T_m. Product and chain rules yield
  D_m(1/2)=2^-m S_m,
  D'_m(1/2)=2^-m(-2m S_m+4T_m).
This proves (I)-(II) without primality, p-adic completion or numerical interpolation.

## A new all-prime modular representation theorem

For any prime p=6m+1>3, let W_p be the original full 216 weighted sum. Insert (I)-(II) into the previously proved original-scalar first-digit factorization W_p=D_m(1/2)[D_m(1/2)+6D'_m(1/2)] modulo p. Since 1-12m=3-2p, obtain
  **2^(2m) W_p = 3 S_m (S_m+8T_m) (mod p).**            (III)
This preserves the two distinct integer observer ports. It reduces the frozen target's p^1 cancellation to a finite binomial divisibility question without modular rational denominators in either S_m or T_m.

For p mod24 in {13,19}, a sufficient specific first-digit lemma is
  S_( (p-1)/6 ) = 0 (mod p).
Its status is still OPEN for all primes. On the complementary p mod8=1,7 class the observed alternative is S_m+8T_m=0 mod p. Neither follows solely from Pfaff; equation (III) is the proved theorem.

## Executed exact tests, class evidence and a scope counterexample

The independent integer-Pfaff checker d25_integer_pfaff_ports_20261107.py was actually executed. For every one of 611 primes p=6m+1 with 7<=p<=10000, including 312 frozen target primes, it computed the pair (S_m,T_m) by a modulo-p recurrence with unit denominators. For p<500 it also compared against direct arbitrary-precision integer binomial sums. All comparisons passed.

The **observed** character-class split (611/611; not yet an all-prime theorem) is:
  p mod8=3,5: S_m=0, S_m+8T_m !=0 (mod p);
  p mod8=1,7: S_m!=0, S_m+8T_m=0 (mod p).
Precise integer residue witnesses (p; S_m,T_m):
  (7;4,3), (13;0,1), (19;0,4), (31;21,9),
  (37;0,28), (43;0,33), (67;0,23), (73;39,59),
  (373;0,119), (5113;5019,1290).
The proof's rational identities apply for composite 6m+1 as well, but a naive extension of the **prime-class divisibility observation** to every integer m fails: m=14 yields 6m+1=85, S_14=68 mod85. This is a precise quantifier-boundary witness, not an objection to the prime conjecture.

## BRC, next exact action and Source continuity

COMPOSE_APPLIED: typed carrier m,k,p, source-specific integer coefficient binom(m,k)binom(2m+k,k), retained pair (S_m,T_m) and observer 3S_m(S_m+8T_m). The two factor-zero mechanisms can be distinguished without division or lossy total-only compression. This is external arithmetic, not native H0/B0/CM execution.

Next scientific action: seek a proof of the prime-class divisibility S_m=0 modulo 6m+1 for primes p mod8=3,5, preferably via a finite involution/character sum or a recurrence with controlled prime specialization. Once established, lift the TWO separate integer ports and the original t-jet to modulo p^2, and then retain the existing signed Clausen J_19=6, J_373=98 and nonzero second shell when proving the full mother W_p=p mod p^3 for p mod24=13,19. The original same-class native p373 divided-power H0/B0 [X]U, rank/Frobenius/eta, signed Hesse Green, kappa/Delta-R and independent reproduction remain unexecuted and pending an authorized owner: https://github.com/awdawmip/enterprise-math/issues/1559.

Original native continuation target_request_id: onhour11-20261106-1400-exact-research-lane-continuation; last read WAITING_RESOURCE/EVENT_COLLECTION_IO, same-ID bounded reconcile QUEUED. Historical native client checkpoint rev22; no verified current Researcher session/claim/run or accepted Result in this Site gateway; existing three staging objects remain separate. This is a second author-side GitHub scientific contribution, not a new formal Source Task or Result.