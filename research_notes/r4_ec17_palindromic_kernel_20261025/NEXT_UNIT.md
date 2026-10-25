# EC18 exact symmetric unimodality frontier

Input: EC17 E(x,u)=(1-u*x^2)/[1-(1+u)x+2u^2*x^4-u^3*x^6], exact D[n,k]=E[n-3,k-1]-E[n-3,k-2], E_n(u) palindromic and coefficientwise nonnegative. Author checked E_n unimodal for 10<=n<=256; this is **not** a theorem for unbounded n.

Target: prove E[n,k]>=E[n,k-1] for all integers n>=10 and 1<=k<=floor(n/2), or provide one exact counterexample. Prove with typed positive branch-count transducer, a finite invariant cone, or a combinatorial injection. Do not extrapolate a finite depth. If proved, the formula implies D[n,k]>=0 for all n>=13 and 1<=k<n/2. Strict positivity and small zero exceptions are separate obligations.

Use the exact EC17 polynomial construction B_k=x B_{k-1}-2x^4(1-x)B_{k-2}+x^6(1-x)^2 B_{k-3} when appropriate. No native X6/heartbeat claim without a separately verified native-state/readout bridge. This is an author-side draft with no formal CLAIM or independent Driver admission.
