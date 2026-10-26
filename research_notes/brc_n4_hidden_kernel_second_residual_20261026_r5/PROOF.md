# N=4 hidden-kernel residual: first-branch bit does not ensure four-observation fidelity

Author-level exact positive rational BRC-style branch-mass model, NOT a native Heartbeat/P000/Shor calculation, formal Result, independent review, or task CLAIM. Current GLOBAL_KNOWLEDGE_V1 pinned input: a307e21a64150ced71df99120a1a14f0487946e9. Prior frontier: research_notes/brc_n3_rational_lifting_onebit_repair_20261026_r5/NEXT_TASK.md.

## Statement

For finite horizon N=4, arbitrary randomized nonanticipative stop-and-decision policies depending on the entire ordered history can realize a four-vector O=(P(decide Q),Q(decide P),E_P tau,E_Q tau) not realizable by ANY randomized policy depending only on time, exact likelihood ratio L=P/Q, and the first-branch bit b=1[first=a], EVEN if b is retained at every later time.

A strictly positive rational 32-leaf example below admits a strict support separation for

J=e_P+e_Q-(33/8)E_P tau+(17/4)E_Q tau:

  min_full J = -427/384,
  min_bit_and_LR J = -141/128,
  min_bit_and_LR J - min_full J = 1/96 > 0.

These signed expectation coefficients are admissible support hyperplane coefficients for comparing attainable four-vectors; they are NOT proposed physical sampling fees.

## Model: exact ordered branch masses

At observation step 1, symbols a,b,c,d have:
Q=(1/6,1/6,1/6,1/2); P=(1/6,1/6,1/3,1/3).

At step 2, symbols x,y have Q=P=(1/2,1/2) after every first symbol.

At step 3, symbols u,v have Q=(1/2,1/2), P=(1/4,3/4) after ax; after all other length-2 prefixes Q=P=(1/2,1/2).

At step 4, symbols s,t have Q=P=(1/2,1/2) after every length-3 prefix. All 32 leaf masses are positive. All conditional distributions sum to 1 exactly.

Consequences: L1(a)=L1(b)=1, L1(c)=2, L1(d)=2/3; L2(ax)=L2(ay)=1; L3(axu)=1/2 and L3(axv)=3/2, whereas L3(ayu)=L3(ayv)=1.

The first-step bit truly separates a and b (both have LR=1), but does not separate ax from ay at step 2, even when retained with the exact LR.

## Full Bellman support proof

For arbitrary real support coefficients (A,B,C,D), put H(l)=min(A*l,B) and c(l)=C*l+D. At a prefix h with likelihood l, the exact Q-normalized backward value is

V_t(h)=min[ H(l), c(l) + E_Q( V_{t+1}(hZ) | h ) ],  t<4;
V_4(h)=H(L(h)).

This follows by conditioning on prefix under Q and minimizing the linear objective over stop-and-decision versus continue. Randomized actions cannot improve the linear minimum, so Bellman induction covers ALL randomized nonanticipative policies, not merely the listed deterministic witness.

Take A=B=1, C=-33/8, D=17/4. Then

H(l)=min(l,1); c(l)=(34-33*l)/8.
c(1)=1/8, c(2)=-4, c(2/3)=3/2,
c(1/2)=35/16, c(3/2)=-31/16.

Because step 4 is uninformative, V_3(l)=min(H(l),H(l)+c(l)). Thus

l           1/2     1       3/2      2        2/3
V_3(l)      1/2     1      -15/16   -3        2/3

At t=2, unrestricted values for hidden pair:

V_2(ax)=min(1, 1/8 + (1/2-15/16)/2)=-3/32;
V_2(ay)=min(1, 1/8 + 1)=1.

At t=1, unrestricted policy may choose differently for ax and ay:

V_1(a)=min(1, 1/8 + ((-3/32)+1)/2)=37/64.

Other branches have V_1(b)=1, V_1(c)=-11 and V_1(d)=2/3; after c, three further samples each yield signed incremental cost -4. At root stop value is H(1)=1; continue value is

1/8 + (1/6)*(37/64)+(1/6)*1+(1/6)*(-11)+(1/2)*(2/3)
  = -427/384 < 1.

For compressed bit/LR policies, the time-2 decision at ax and ay must be identical. Their conditional Q weights remain 1/2 each given a, because earlier nonanticipative actions cannot depend on unobserved x/y. Time 3 and later have no further hidden-kernel distinction relevant to the future: the final step is uninformative, and the Bellman value V_3 depends only on L. Hence the BEST compressed common time-2 value at the a-fiber is

V_2^bit(a)=min(1, 1/8 + (1/2)*[ ((1/2-15/16)/2) + 1 ])
          =33/64.

It follows that V_1^bit(a)=min(1,1/8+33/64)=41/64.

The b,c,d branch values are unchanged, since b,c,d are distinguishable by (bit,L) at time 1 and all their later signals are uninformative. Consequently the root compressed optimum is

V_0^bit= min[1,1/8 + (1/6)*(41/64)+(1/6)*1+(1/6)*(-11)+(1/2)*(2/3)]
       =-141/128.

The strict gap is exactly 1/96. If every full-history four-vector could be represented by some bit/LR policy, the minima of this real linear functional would agree; contradiction. This proves the stated universal-fidelity failure, even with randomized policies and persistent first-step bit.

## Explicit attainability witness

The following full-history deterministic policy attains -427/384:

- Sample at root; at a sample x/y; at ay stop and decide P; at ax sample u/v.
- At axu stop at time 3 and decide Q. At axv sample fourth letter and decide P at time 4.
- At first letter b stop at time 1 and decide P.
- At first letter c sample through time 4 and decide P.
- At first letter d stop at time 1 and decide Q.

The exact ordered-leaf calculation gives
O_full = (17/48, 11/24, 37/16, 43/24);
J(O_full)=-427/384.
Every compressed bit/LR randomized policy has J>=-141/128 and therefore cannot replicate this four-vector.

## Minimal repair for this model

Retain the first bit b=1[first=a], exact L, time, and ONE further time-2 bit r=1[second letter=x AND first=a]. This separates ax from ay, the only remaining pair of histories that have the same compressed state but different conditional future-likelihood laws. At time 3, the last step is conditionally uninformative and the exact LR determines both terminal loss and remaining signed sample cost. The finite-state occupancy-flow/conditional randomization construction then reproduces all four observations for every full-history strategy in this FIXED tree. Conversely, any deterministic quotient that identifies ax and ay while otherwise retaining only the described observations fails by the strict support gap. No general N=4 minimal-bit count or native-space embedding is asserted.

## Verification and limits

Actual local execution used Python fractions.Fraction only, enumerated 61 prefixes and all 32 positive leaves, tested P/Q normalization, computed full and compressed Bellman values, and directly accumulated the explicit policy's P/Q errors and stopping expectations. The validated source is VERIFY.py (local SHA-256 2d79e4badd4f1780afb3a0b7a598560d36c49a321ccd9f4c2b2a15868a50bd2f); see EXACT_CHECK_OUTPUT.txt. The full quantifier over randomized policies is the Bellman argument, while the program validates the concrete model. This is external BRC-style positive branch mass, not native BRC-Shor phase or Heartbeat X6 computation. Native session_start denied by STATIC_READONLY_SCOPE_DENIED, operation_sent=false; owner/CLAIM and independent Driver acceptance have NOT been established. This author-side note is not a formal Result.

## Next question

For general positive rational N=4 ordered trees, derive a sharp necessary/sufficient root-envelope criterion for safe merging of a chosen pair of equal-LR time-2 histories, and find a constructive minimum residual alphabet with a finite exact rational certificate. Separate decision-value fidelity from stronger pathwise occupancy preservation.
