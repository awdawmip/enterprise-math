# D25 — exact single-carry shell for the directional Lucas jet

Date: 2026-11-06. Status: AUTHOR-DERIVED EXACT ALGEBRA / 428-PRIME INDEPENDENT FINITE-FIELD CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Logic lane: chatgpt-research-hourly-enterprise-math-20260923 (task identifier from prior author material, not a newly service-authenticated identity).

## General exact finite-field theorem (all primes q>=5)

Let 0<=a<b<c<q be integers, z in F_q, and let 0<=j<q. Put

  M_j(t) = z^j * binom(a+t,j) * binom(b+t,j) * binom(c+t,j) * j!/(1-3t)_j,

as a rational germ over F_q at t=0 (all denominator constant terms j! are units). Write u_j=M_j(0), e_j=M_j'(0), H_n=sum_{h=1}^n 1/h in F_q, H_0=0. Then:

(a) For 0<=j<=a,

  u_j=z^j * binom(a,j)binom(b,j)binom(c,j),
  e_j=u_j*(H_a-H_(a-j)+H_b-H_(b-j)+H_c-H_(c-j)+3H_j).

(b) For a<j<=b,

  u_j=0,
  e_j=z^j*(-1)^(j-a-1)*a!*(j-a-1)!/j! * binom(b,j)binom(c,j).

(c) For b<j<q, u_j=e_j=0.

If z is nonzero, every individual e_j in the shell a<j<=b is nonzero in F_q; this is a precise per-term first-order carry observable even when all the corresponding u_j vanish.

Proof: For j<=a, logarithmically differentiate each nonvanishing binomial and the reciprocal rising-factorial denominator; the latter contributes +3H_j. For j>a, binom(a+t,j) contains precisely one vanishing factor t, whose derivative is (-1)^(j-a-1)*a!*(j-a-1)!/j!. For j>b, both binom(a+t,j) and binom(b+t,j) contain a factor t, so their product has order >=2 at t=0 and e_j=0. No inversion of a zero u_j is used; all factorials and binomial numbers in the surviving shell are q-units for the stated ranges.

## Specialization and D25 observer

For every prime q>=5 set eps=1 for q=1 mod6 and eps=-1 for q=5 mod6, m=(q-eps)/6 and delta=(1-eps)/2. The unordered triple of residues of 2(q^2-1)/6, 3(q^2-1)/6 and 4(q^2-1)/6 modulo q is exactly

  {a,b,c} = {2m-delta, 3m-delta, 4m-delta}.

Use z=-1/2 and the preceding M_j. Then Z=sum u_j and L=sum(6j+1)u_j are supported on j<=a, while S=sum(6j+1)e_j decomposes EXACTLY as S_regular+S_singlecarry with disjoint indices j<=a and a<j<=b. This gives an independent explicit finite hypergeometric description of the previously defined scalar S, and shortens its exact sum to j<=b, strictly less than q. The carry shell has exactly b-a=m terms.

Under the inherited first-digit condition L=0 modulo q, the previously established B=6Z-S still holds. For the inherited quantity Theta_q=W_q/q-Z+S/6 (requiring W_q divisible by q), the same exact splitting gives

  6Theta_q = 6(W_q/q)-6Z+S_regular+S_singlecarry (mod q).

Thus the remaining conjectured Theta_q=0 is reduced to the explicit shell-matching certificate

  S_singlecarry = 6Z-6(W_q/q)-S_regular (mod q).

This equality is a new, isolated proof target. It is NOT claimed universally here; no native LIFT/JT2 or H0/B0 result follows without its own original-class bridge. Per-source binomial labels and the sum/quotient maps remain separate.

## Exact testing and computation scope

Accompanying standard-library Python program computes the shell via factorial/inverse and harmonic tables, independently computes the full scalar jet via hypergeometric-ratio differentiated recurrence over EVERY j<q, and checks the triple (Z,L,S) for all 428 primes 5<=q<=3000. Result: 428/428 PASS; L=0 in all these finite cases. The net shell sum is nonzero for 427/428 primes; q=17 is the one zero net shell in the tested domain. Even at q=17 each shell term is nonzero.

Some exact tuples (q; Z, S_regular, S_singlecarry, S_total):
  (5;3,1,3,4); (7;4,6,5,4); (11;10,3,8,0);
  (13;0,12,8,7); (19;0,15,17,13);
  (373;0,75,292,367); (1009;482,5,863,868);
  (2003;512,775,300,1075).

The double check is exact within the finite declared domain; it does not establish the general Theta_q cancellation. The split lemma itself is proved algebraically above.

## Native frontier preservation and next executable mathematical step

Source last verified before this note: immutable checkpoint state SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, task HANDOFF_READY with no live claim, execution_authorized=false; fresh 2026-11-06 control reads were requested and may remain QUEUED pending final receipts. No new Researcher session, CLAIM, OPEN, formal checkpoint, or review is asserted by this author-side note.

The original D25 next action remains native original-class p373 H0/B0 divided-power, [X]U mod139129, semilinear Frobenius direction/eta and kappa, then Delta_p-R_p. On the portable side, attempt a WZ/telescoping certificate specifically for the nonvanishing one-zero shell sum above, keeping the regular part and W_q/q separate. The shell support lemma is complete and should not be rederived; all prior Q/F/H/Clausen and signed-jet material is inherited, not credited anew.