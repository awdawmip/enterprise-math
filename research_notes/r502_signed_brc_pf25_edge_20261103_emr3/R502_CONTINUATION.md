# R502 scientific continuation (2026-11-03)

Last durable frontier: R501 rank 24 at 3be6d6c7f2686c08a5e0a25f12ab4f8dddcf0068.
New R502: for k>=1, D_25(k)>0 exactly when 1<=k<=9, and D_25(k)<0 exactly when k>=10, with r=2k+1 and s=3. Signed BRC R462 scientific pin 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Proof: R452/R462 inherited polynomial p_t degree bound; degree <=150 for f_25; degree <=49 interpolating Newton S, positive G_25 and denominator L; 151 exact equality checks; 9 exact positive values; 50 shifted Newton coefficients at k=10 all negative.
Evidence: R502_VERIFY.js and R502_EVIDENCE.json; independent four-point Catalan/ballot SymPy determinant check in R502_INDEPENDENT.py. All are author-side, Driver unreviewed, without native CLAIM/Result.
Native scope: authenticated static_machine_readonly; session_start STATIC_READONLY_SCOPE_DENIED, operation_sent=false; task owner enumeration CONTROL_QUOTA. No owner assertion.
Next independent executable unit: m=26 fixed s=3 and k>=1, test degree upper bound 156, G_26 degree105, 52 Newton coefficients, 157 equality points; classify entire integer range using exact shifted differences plus finite exceptions. Alternative complementary mechanism: fixed k=9,10,19 rank-generating rational denominator/pole diagnostics. Maintain source-vs-actual-admission distinction and immutable R462 input.