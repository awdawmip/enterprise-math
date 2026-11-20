# R1160A: Output-size lower bound for complete bounded primitive-turn atom generators

Scope: exact explicit enumeration of every [b+ai] with integers 0<a<b<=H, gcd(a,b)=1, each emitted as a separate atom, in a word-RAM/streaming output model with unit cost per atom. This is a distinct elementary complexity observation for the current Gregory-Machin atom-generator task, not a claim about support-two searches, compressed representations or implicit membership oracles.

Let N(H)=#{(a,b):1<=a<b<=H, gcd(a,b)=1}. Counting a by each b gives N(H)=sum_{b=2}^H phi(b). For an elementary lower bound, begin with T=H(H-1)/2 ordered candidate pairs. Each noncoprime pair is divisible in both coordinates by some d>=2. By a union bound, their number B obeys
B <= sum_{d=2}^H binom(floor(H/d),2) <= (H^2/2) sum_{d=2}^infinity d^{-2}.
Because the terms are decreasing, sum_{d=2}^infinity d^{-2} <= 1/4 + integral_2^infinity t^{-2}dt = 3/4.
Therefore N(H)>=T-B >= H^2/8-H/2, and for every integer H>=8,
N(H) >= H^2/16. Trivially N(H)<=H(H-1)/2. Hence **N(H)=Theta(H^2)**.

Consequently any algorithm that explicitly outputs the entire admissible atom universe must take Omega(H^2) output operations; it cannot have o(H^2) total running time even with free factorization and perfect deduplication. A Gaussian-prime signature generator can improve construction constants, data organization, early filtering, incremental bounds or downstream group operations, but cannot eliminate this output-size lower bound for the full raw universe. The two complete bounded regressions reported separately (H1000=304191; H1100=368117 atoms) are compatible with the theorem. This is a known elementary counting consequence, not a novelty claim for the general totient summatory function.

Open distinctions: a succinct implicit representation, a sparse sub-universe query, a compressed grouped direction family, or a thresholded downstream Pareto search could still have o(H^2) cost relative to the full universe because it does not actually emit all atoms. The theorem does not bound those different computational objectives.

Status: author-scope exact proof, staged before Source publication; independent Driver review not performed.