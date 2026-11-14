# R762AO — Exact fault-tolerant BRC diagnostics on the AK4 conditional source/frame observer

**Scientific status:** author-derived conditional finite-state theorem; reproducible exact verification; NOT_REVIEWED / NOT_NATIVE_ADMITTED.
**Provenance:** Enterprise Math task RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142, researcher EM-X6-3050F6. Continue R762AM–AN (Draft PR #2421, immutable author-side commit 1a1fd9de4204f968cc5dddd2e28b3c24da6e9e0c). Scientific source pin a72226e2430ffa4786321ac86e7f0c599d5f0389. P000 is unchanged.

## 1. Model and exact question

Retain AK4's eight live states R=(C3 x {E}) union ({E} x S3), plus optional absorbing undefined state U. The source state s belongs to Z/3Z; frame h belongs to S3. Permutations use images of 0,1,2; E=012, c=120, t=102, and left multiplication.

The partial actions are S(s,E)=((s+1) mod 3,E), C(0,h)=(0,ch), T(0,h)=(0,th), and all other applications give absorbing U. The observer reports the source and frame **cycle types**: EE, EC, ET, CE, or U. Its eight live initial-observer fibers have sizes 1,2,3,2.

The initial observation is reliable and costs zero primitive event letters. Every subsequent diagnostic word in {S,C,T}* operates on a separately reset fresh copy of the SAME unknown initial state; ONLY its terminal observer output is returned. The diagnostic word multiset is fixed in advance (nonadaptive); repetitions count as separate runs. There are e known-position erasures and t unknown-position adversarial corruptions among terminal reports; the initial read is unaffected. Determine the fewest nonempty probe runs N and minimum total primitive event letters L guaranteeing unique identification for EVERY initial state and fault pattern.

## 2. Complete arbitrary-length separation-mask theorem

There are exactly five ambiguous unordered pairs within initial-observation fibers: one CE source pair, one EC frame-cycle pair, and three pairwise combinations of the ET transpositions.

**Lemma.** On these five pairs, the separation mask of ANY finite diagnostic word is either zero or precisely one of five masks: the CE-only mask of shortest representative S (length 1); the EC-only mask of shortest representative C (length 1); and the three one-versus-two ET masks of shortest representatives T (length 1), CT (length 2), TC (length 2).

**Proof.** If the word begins with S, every state with a nonidentity frame immediately enters the same absorbing U, so only the CE pair can be distinguished. If it begins with C or T, both nonzero-source CE states enter U, so the CE pair cannot be separated.

For EC and ET, take the full prefix of frame letters C,T up to the first S, or to the word end. Let its left-product be g in S3. An even g maps all three input transpositions to transpositions, so no ET pair can be separated, and any following S makes all three U. If g is a nontrivial 3-cycle, it maps one initial frame 3-cycle to E and the other to a nontrivial 3-cycle, so only the EC pair can be separated; g=E separates neither EC input. If g is odd, it maps the two initial frame 3-cycles to transpositions, while exactly one of the three input transpositions maps to E and the others to nonidentity 3-cycles. At terminal readout, the resulting ET partition singles out that one. If an S follows, only that singled-out state may survive, with the others now absorbing U; later actions can erase the cut but cannot introduce another cut. The odd permutations supply exactly the three possible singleton choices, realized by T, CT, TC. Their minimum word lengths follow by checking all one-letter actions. No other mask occurs. QED.

Independent finite verification: generate the COMPLETE transformation monoid, not a bounded-length sample. It has 75 maps; their terminal output vectors have 43 distinct patterns, and only these five nonzero pair-separation masks.

## 3. Sharp robust-code theorem

Two states in different baseline fibers are already distinguished. For equal-baseline pairs, their terminal probe strings must have Hamming distance d >= e+2t+1 for unique decoding of up to e known erasures and t unknown substitutions. This is necessary (if a pair has distance <= e+2t, a received string can be made compatible with both by erasing differences and dividing the rest among the two allowed substitutions) and sufficient (triangle inequality after omitting erased coordinates). All terminal outputs use finite typed symbols, so this classical code-distance argument applies without numerical approximation.

**Theorem AO1.** Put d=e+2t+1, for any nonnegative integers e and t. The independent-reset, fixed diagnostic interface above has exact minima

N_min(d) = 2d + ceil(3d/2) = ceil(7d/2),

L_min(d) = 2d + ceil(5d/2) = ceil(9d/2).

One fixed multiset of words attains BOTH optima simultaneously. This is an all-length theorem for every integer d >=1.

**Proof.** Let a,b count the two exclusive S and C masks; let x,y,z count the three ET cuts represented respectively by T, CT, TC. The distance conditions are exactly

a >= d, b >= d, x+y >= d, x+z >= d, y+z >= d.

Therefore N=a+b+x+y+z >= 2d+ceil(3d/2). Because the least word lengths of these masks are 1,1,1,2,2, the event-letter cost obeys

L >= a+b+x+2y+2z
  >= 2d + (x+y)/2 + (x+z)/2 + 3(y+z)/2
  >= 2d + 5d/2.

Integrality gives L >= ceil(9d/2). For d=2k, choose a=b=2k and x=y=z=k. For d=2k+1, choose a=b=2k+1, x=y=k+1, z=k. These meet all five distance constraints and achieve both bounds. Use the shortest representatives S,C,T,CT,TC repeated with those multiplicities. QED.

| Terminal fault allowance | d | Optimal runs | Optimal letters |
|---|---:|---:|---:|
| None | 1 | 4 | 5 |
| One known erasure | 2 | 7 | 9 |
| One arbitrary substitution | 3 | 11 | 14 |
| One erasure plus one substitution | 4 | 14 | 18 |

The optional absorbing initial U is a distinct singleton under the reliable baseline and does not change the optimum.

## 4. BRC interface, reproduction and next dependency

Retain each diagnostic word, reset boundary, terminal observer symbol and original-source candidate. For a pair (p,q) of candidate source/frame states define its separation multiplicity rho_W(p,q) as the exact number of reset experiments whose terminal outputs differ. The five within-fiber integers are a sufficient typed ordered-BRC *robustness certificate* for this fixed decoding objective. Collapsing to a commutative total of positive branch weights erases which word/output positions distinguish which candidate pair; no such information loss is used in the theorem.

Code file: R762AO_FAULT_BRC_VERIFY.js, executable with Node.js and no dependencies. It rebuilds all 9 totalized states, closes the 75-map monoid under S,C,T, determines 43 distinct terminal observer vectors and five distinct nonzero masks, then independently solves exact saturated-distance dynamic programs for minimum number of tests and minimum letter cost for d=1,...,7. The JSON evidence contains full masks, state indices, and check counts. All assertions passed in the author-side JS execution. The universal theorem follows from Section 3, not from finite extrapolation.

**Future/native question:** obtain an actual P000-admissible TRIADIC_CLOSURE_E signed-X6 Cell/Link/Port transition table with V29 PASS/TRANSFER source update, V17/V39 frame transport, repeatability, and available observation/reset channels. Form its actual future-separation semigroup and compute the minimum native BRC residual and error-tolerant code. Current results use the explicitly conditional AK4 model. The science is author-side; native Source Activity/PROGRESS, Result and independent Driver acceptance require separate authorized operations.
