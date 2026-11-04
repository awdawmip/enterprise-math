# EC49FAS — All-horizon safe-suffix theorem for H2-rooted signed-X6 BRC paths

Date: 2026-11-04. Evidence: author-side analytic proof and executed exact finite checker. Parent: EC49FAR@c6a17e1bdab5da463ee5075e19f1b5c3c4b7cb8f. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. P000 and ACTIVE Heartbeat World native six-axis premises unchanged.

## Exact input and scope

Use the same seven ordered native signed-X6 operation codes: a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). Signed numbers denote native axis labels. An admissible word of operation length h has signed X6 net (2,0,0,0,0,0). Its full positive BRC key counts positive occurrences on all six native axes; operation order and its nine-history, five-bucket observer remain separately retained. Allowed final signatures are D=de, E=ed, C=ce, J=ec, F=feg, G=gef. Here an H2-rooted word means its first two **operations** are exactly one of de, ed, ce, ec.

## Theorem A — exact safe-suffix language (all h>=2)

Write a legal H2-rooted word as R s, where R belongs to {de,ed,ce,ec}, and let obs denote the exact nine-history observer. Within the six permitted signatures:

* For R=de or ed, obs(Rs) is permitted if and only if suffix s contains **no c**. In that case obs(Rs)=obs(R).
* For R=ce or ec, obs(Rs) is permitted if and only if suffix s contains **no d**. In that case obs(Rs)=obs(R).

Proof. Every operation terminates with a negative native axis direction; therefore a transition (+1,+2) or (+2,+1) can only occur **inside** an operation. Only c has the first transition, and only d has the second. After de or ed, the nine-history vector contains a B bucket but no A; c would turn at least one B into absorbing BA, while all other suffix operations preserve the entire signature. After ce or ec there is an A bucket but no B; d would turn A into absorbing AB, while the other suffix operations preserve it. Transitions A->AB and B->BA are irreversible. The established H2 rigidity lemma EC49FAQ shows that the only permitted signature from each rooted path is its own. These two facts give both directions for any suffix length.

Displacement validity forces n_b=0 and n_e=n_a+1 for the complete word; each root has exactly one e and zero a. Consequently suffix s has equal a,e multiplicities and its remaining symbols belong to {d,f,g} for R=de/ed or {c,f,g} for R=ce/ec. This is an exact regular/commutative-count characterization: no nine-history observer simulation is necessary for generating the H2-rooted admissible final signatures.

## Theorem B — exact count for each full key and horizon

Let h>=2 and K=(x,y,z,0,0,0). Put r=x+y-h-1, f=h+1-y-2z, g=h+1-x. There are H2-rooted words with this key and a permitted signature exactly when z>=1, r>=1, f>=0, g>=0, with all quantities integers (the implied length identity holds). At each such key, **each of the four H2 roots has exactly**

    N_h(K)=(h-2)! / ((z-1)!^2 (r-1)! f! g!)

safe operation-word continuations. Thus the combined number over four roots is 4 N_h(K), and the four possible final signatures {D,E,C,J} are always all realizable at this key; their indicator rows have rational rank 9 by the explicit integral minor of EC49FAR. The key set has size

    A(h)=sum_{k=0}^{floor((h-2)/2)} binom(h-2k,2).

Proof. For either root group, the suffix has exactly z-1 e's, z-1 a's, r-1 copies of its permitted c or d, f copies of f and g copies of g. Its (h-2) positions can be permuted in the stated multinomial number of ways. The full positive key is K for all four roots. Conversely the safe-suffix characterization forces precisely these counts. Summing nonnegative compositions of r-1,f,g for each z gives A(h), as in EC49FAQ.

## Theorem C — all-horizon total, generating function, and recurrence

Let T(n) count safe suffixes of length n **per fixed H2 root**, with suffix signed net zero. Then

    T(n)=sum_{k=0}^{floor(n/2)} n!/(k!^2 (n-2k)!) * 3^(n-2k)
    T(n)=[u^0] (3+u+u^(-1))^n
    sum_{n>=0} T(n)t^n = 1/sqrt((1-5t)(1-t)).

Here [u^0] denotes the Laurent constant coefficient, treated as a formal-power-series operation. Hence T(0)=1, T(1)=3, and for n>=1,

    (n+1)T(n+1)=(6n+3)T(n)-5n T(n-1).

The exact number of admissible H2-rooted operation words at horizon h is **4 T(h-2)**. Proof: balanced a/e choices contribute paired u/u^(-1), and the three other safe suffix letters contribute 3. The constant-term evaluation follows from the central-binomial formal identity; differentiating the displayed generating function yields the recurrence. This is an exact analytic census, and no numerical asymptotic estimate is needed.

## Executed validation

Python 3 stdlib VERIFY_EC49FAS.py was actually executed, producing adjacent EXACT_REPORT_EC49FAS.json with status PASS. The checker independently reconstructs native signed X6 steps and nine-history transitions; for every balanced suffix of h-2 operations at h=2..7 it compares the native observer to the safe-suffix criterion, computes complete positive X6 keys, checks the multinomial count of all four roots per key, and checks rank 9 over rational fractions. It evaluates the closed count/key formulas for h=2..10 and the recurrence for n=1..14. H8 and H9 counts computed by this formula are 15,956 and 73,932 (respectively 50 and 70 H2-reachable keys), agreeing with the separately previously reported EC49FAQ full-suffix finite enumeration.

Counts h=2..10: admissible words across roots = 4, 12, 44, 180, 780, 3492, 15956, 73932, 346060. The analytic theorem is for every integer h>=2; this execution's native brute-force checks cover h=2..7, with arithmetic formula/recurrence checks over the displayed larger finite ranges.

## Research value and next EC49FAT

EC49FAS replaces H2-rooted suffix observer scanning with one allowed-symbol predicate and exact per-key multinomial. The mixed H2/H3–H6 H8/H9 optimizer may now enumerate only admissible native H2 paths, merging them with non-H2 paths in the native ordered primitive-prefix trie, enforcing the four EC49FAR rank clauses. First inspect the 22 shared fifth-key candidates in each of the four frozen early schedules; compute a joint H8/H9 93-edge threshold decision with an exact prefix-cost certificate or a scoped lower bound. The unrestricted H9 mother optimum remains author-side bounded 80<=E*_H9<=94. This source artifact does not assert Source CLAIM, Result or independent Driver review.
