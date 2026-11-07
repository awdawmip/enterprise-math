# Next research unit: certify the finite-h global crossing from an exact proxy

Preserve scientific input @43ec6098b1330ae86d0a7863be336c5d97f6ef34 and source-tagged T/B observation. The full ten-label minimax remains [1/2,2/3].

New tool: for every legal 0<s<=1, 0<h<=1/42, set v=2h and k=s/(2-s). The rational exponent delta_0=(1-k)v/6 gives Bernoulli Chernoff information C_hat with rigorously certified 0<=C_B-C_hat<4/10^13. The sharper s-dependent factor is (1-k²)² v⁸(2-v²)²/[288(1-v²)⁶]. Source: PROOF.md; executed verification: python VERIFY.py.

Study h=1/42. Use rational outward interval enclosures for the scalar proxy gap F_hat over s bands. If F_hat<0, certify F<0; if F_hat>the exact error envelope, certify F>0. Treat the near-zero s endpoint using a normalized analytic series rather than absolute precision, and the s->1 endpoint using the vanishing (1-k²)² error. Resolve the remaining band using derivative or isolating intervals; classify global uniqueness or produce a second verified root. Retain honestly any undecided bands.

Publishing this author note to the existing draft PR provides durable evidence but creates no native CLAIM, Result, independent review, or theorem admission. The original mother objective remains open.
