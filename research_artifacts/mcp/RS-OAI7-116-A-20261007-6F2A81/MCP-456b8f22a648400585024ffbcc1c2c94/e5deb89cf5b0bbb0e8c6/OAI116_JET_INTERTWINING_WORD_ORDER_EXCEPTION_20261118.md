# OAI7-116: Taylor-jet intertwining, ordered-word and exceptional-branch audit
Date: 2026-11-18 (Asia/Shanghai)
Task: RS-OAI7-116-A-20261007-6F2A81
Publication: TP2-2F98D558CBBC7F200E7D
Status: author-checked mathematical result, not an independent Driver review or full external-paper admission.

## Frozen source and scope
External source: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/construction.tex. Its formula is used as the object of independent re-derivation, not as a new Foundation result. Coefficient field F has characteristic zero, letters i are positive integers, jet order d>=1; rows/columns are indexed 0,...,d-1. Native P000/BRC carrier is not claimed.

## Theorem (exact all-jet identity, including constants)
For a(z)=sum_{q>=0} a_q z^q in F[[z]], define J_i a(z)=int_0^z a(t)/(t+i)dt in the formal characteristic-zero sense. Let pi_d(a)=(a_0,...,a_{d-1})^T. Set
T_i[r,q] = (-1)^(r-q-1)/(r*i^(r-q)) if 0<=q<r<d; otherwise 0.
Then pi_d(J_i a)=T_i*pi_d(a) for every a and d>=1. For every word w=(i_1,...,i_k), let J_w=J_{i_1}...J_{i_k}; the *rightmost* operator acts first. Then
pi_d(J_w 1)=T_{i_1}...T_{i_k}e_0.
For every finite noncommutative polynomial f=sum_w f_w x_w, with J_empty=Id, f(T_1,...,T_n)e_0=pi_d(sum_w f_w J_w 1). In particular the degree-zero coefficient is precisely f_empty, including when f has nonzero constant term.

Proof: formally 1/(t+i)=sum_{m>=0} (-1)^m t^m/i^(m+1). The coefficient of z^r in int a(t)/(t+i)dt, for r>=1, is (1/r)sum_{q=0}^{r-1}(-1)^(r-q-1)a_q/i^(r-q). This is exactly the rth row of T_i*pi_d(a), and the constant term is zero. Truncation before J_i does not affect any coefficient r<d. Apply this identity successively from the rightmost letter; extend by the polynomial's finite linearity. No commutative reordering is made.

## Exact failure witnesses for wrong conventions
Transpose failure: d=2, i=1 and e_0=(1,0)^T. pi_2(J_1 1)=(0,1)^T, T_1 e_0=(0,1)^T, but T_1^T e_0=(0,0)^T.
Word-order failure: at d=4,
pi_4((J_1 J_2 - J_2 J_1)1)=(0,0,0,-1/24)^T.
In general the z^3 coefficient of (J_i J_j-J_j J_i)1 equals (i-j)/(6*i^2*j^2), nonzero whenever i!=j. The z^2 coefficients agree, so truncation d<=3 cannot distinguish this particular commutator.

Exceptional n=s=1 branch: the external source's 1x1 hitting tuple is T_1=[1] (a separate small-formula convention). The truncation construction at d=1 instead gives T_1=[0] and pi_1(J_1 1)=0. Therefore the universal jet-intertwining statement above refers to the lower-triangular jet matrices; it is *not* asserted for the exceptional hitting tuple [1]. For size-at-most-one formulas in one variable, each nonzero leaf is either a scalar or x_1, and evaluation at [1] is nonzero.

## Exact finite audit (separate from proof)
One isolated JavaScript BigInt rational arithmetic execution on 2026-11-18 checked 464 independent equalities without floating-point operations or external numerical libraries: d=1..8; for each i=1..4 every jet basis column (144 cases), and for each d every word of length <=3 in alphabet {1,2,3} (320 cases). All matched. Explicit rational calculations gave the commutator coefficient -1/24 and the exceptional matrix discrepancy. This bounded test is supplemental; the displayed coefficient proof establishes the arbitrary-d theorem.

## Unresolved main-paper dependency
The source manuscript's stronger universal formula-size hitting theorem also uses word-series injectivity and an order-of-vanishing bound from a finite linear system. Those independent dependencies are not established here. The next scientific increment is to check those exact pinned lemmas and the dimension inequality with their hypotheses, then either integrate a complete independently checked hitting proof or identify the smallest unresolved lemma. The native six-axis/triadic carrier transfer remains a distinct, typed-interface question.
