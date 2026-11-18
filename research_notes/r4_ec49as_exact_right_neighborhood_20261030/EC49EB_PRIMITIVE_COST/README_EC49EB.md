# EC49EB — Exact primitive-step cost and BRC-factor coincidence (2026-11-02)

Author-side analytic proof / executed exact finite checks. Parent EC49EA, Draft PR #1730. Status PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Scientific inputs remain frozen: GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e; Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. P000 and ACTIVE worldview unchanged.

## Typed model

The genuine ordered signed X6 primitives underlying operators are a=(-E1,-E1) (cost 2), b=(-E2,-E2) (cost 2), c=(+E1,+E2,-E1,-E2) (cost 4), d=(+E2,+E1,-E2,-E1) (cost 4), e=(+E3,+E1,+E1,-E3) (cost 4). A future word of exactly h operator letters returns from historical endpoint -2E1 when its full six-axis displacement is +2E1. We observe the order in which adjacent positive primitive pairs A=(+E1,+E2), B=(+E2,+E1) first occur, including the historical seam, with five output buckets N,A,B,AB,BA.

Nine genuine length-10 histories realize the nine atom states N0,N1,N2,A0,A2,B0,B1,AB,BA of EC49EA, each with positive counts (2,2,0,0,0,0). One future word contributes five bucket-indicator columns on those nine atoms. Full nine-feature recovery means rank 9 of the selected word:bucket columns. Let C(h) minimize the sum of genuine signed primitive step lengths of all distinct selected returning words, allowing any number of words; C_equal(h) imposes equal entire six-axis positive-step count vectors across selected words. Each distinct word is charged once; output columns and independent instruments are separately counted.

## Theorem 1: all-h exact optimal primitive costs

h=1: C(h)=C_equal(h)=infinity, maximum transfer rank 5.
Even h>=2: C(h)=C_equal(h)=12h+8.
Odd h>=3: C(h)=9h+7; C_equal(h)=12h+12.

Cost-optimal word counts are four/even, three/odd unrestricted and four/odd equal count. The nine-feature minimum requires nine independent scalar word:bucket output columns per BRC/count instrument; all constructions below have a unimodular nine-column submatrix.

Proof of all lower bounds. For a returning word let s=n_a, q=n_c+n_d, r=n_e. Full X6 return forces n_b=0 and r=s+1, giving h=q+2s+1, positive primitive counts p=(h+1,q,r,0,0,0), and genuine signed primitive cost L=2s+4q+4r=4h-2s. If q=0 the word produces the same five-bucket identity transfer as every other q=0 word. If q>0, it produces at most three nonempty output buckets. All word output columns add to the common all-ones column. Thus k event-bearing words span rank<=1+2k; one no-event word and k event-bearing words span rank<=5+2k.

For h=2m even, q is odd>=1, so s<=m-1 and each L>=3h+2. Four event-bearing words are necessary to reach rank9, giving total>=12h+8. For h=2m+1 odd, a q=0 word has s=m and L=3h+1, whereas q>=2 implies s<=m-1 and L>=3h+3. Three event-bearing words rank<=7 and two identity words plus one event-bearing word rank<=7, so full-rank three-word recovery must use one no-event plus two event-bearing words, cost >=(3h+1)+2(3h+3)=9h+7. Four or more words cost >=4(3h+1)>9h+7; one/two words cannot reach rank9. With equal positive counts all words have identical q; q=0 gives rank5, while q>=2 requires at least four event-bearing words each cost >=3h+3, hence >=12h+12. At h=1 only e returns, rank5.

Constructive upper bounds, valid for every stated h. For even h=2m write A0=a^(m-1), E=e^m, F=e^(m-1). Choose four words cA0E, dA0E, ecA0F, edA0F. Each has h letters, cost 3h+2, positive counts (h+1,1,m,0,0,0) and full return. Select nine bucket columns: first word A,AB,BA; second B,AB; third A,AB; fourth B,AB. The nine-by-nine atom determinant is -1. For odd h=2m+1, choose a^m e^(m+1), cc a^(m-1)e^m, dd a^(m-1)e^m, with primitive costs (3h+1,3h+3,3h+3); select all N,A,B,AB,BA outputs from the first, A,AB from the second and B,AB from the third, determinant +1. For odd common-count recovery choose cc a^(m-1)e^m, dd a^(m-1)e^m, ecc a^(m-1)e^(m-1), edd a^(m-1)e^(m-1); all have p=(h+1,2,m,0,0,0), each cost3h+3. Select the same nine outputs as even case, determinant -1. Every operation ends with a negative primitive; a/e adds no new adjacent A/B pair across operation boundaries, making the indicated transfer matrices invariant with m. All exact signed paths and seams are reconstructed by executed verifiers.

Dual positive BRC factors X(w)=product_i x_i^p_i(w), Y(w)=product_i y_i^p_i(w) (all x_i,y_i>0), plus independent count, obey p(wt)=p(w)+p(t), X(wt)=X(w)X(t) and Y(wt)=Y(w)Y(t). A positive future factor scales each transfer column by a nonzero number and preserves rank. Thus minimum-cost certificates recover rank H9 for every finite native historical population, and can recover full rank27 when the historical matrix itself has rank27. Cost does not count scalar readout columns or instruments as repeated primitive executions.

## Theorem 2: complete positive numerical BRC coincidence locus

For odd h=2m+1>=3 every returning word lies in a positive-count fiber p_j=(h+1,2j,m+1-j,0,0,0), j=0,...,m. Each has numerical factors
X_j=x1^(h+1)*x3^(m+1)*(x2^2/x3)^j;
Y_j=y1^(h+1)*y3^(m+1)*(y2^2/y3)^j.
There exists a three-word FULL-RANK-NINE returning certificate with all numerical X and Y factors identical iff x3=x2^2 AND y3=y2^2. Necessity: a full-rank triple requires exactly one q=0/j=0 event-free word and two q>=2/j>=1 event-bearing words. Equality of any positive-j factor with j=0 implies (x2^2/x3)^j=(y2^2/y3)^j=1, so strict positivity forces both bases=1. Sufficiency: on this locus all fibers have equal numerical X/Y factors, while the above odd three-word certificate retains determinant+1. No restriction applies to axes1,4,5,6. A weak claim of coincidence among arbitrary words (without full recovery) would be trivial because different word orderings can have exactly the same count vector.

The factor-only logarithmic observer has (log X_j,log Y_j)=constant+j*(log(x2^2/x3),log(y2^2/y3)). Off the locus it distinguishes m+1 positive-count fibers; on the locus all m+1 collapse to one numerical pair, a maximum uniform-fiber-index distinction loss log2(m+1) bits. Distinct word labels and A/B output buckets remain available, so the unimodular recovery survives numerical factor equality; preserving count/provenance is crucial.

Explicit integer h=3 witness: x=(2,3,9,1,1,1), y=(5,2,4,1,1,1), returning words aee,cce,dde each give future X=1296,Y=10000, while their selected nine output columns have determinant+1. Replacing x3=9 by x3=8 changes the two distinct X fibers to 1024 and 1152.

## Validation and limits

Two executed standard-language validators passed: an independent Python-standard-library original, reconstructing nine historical native X6 paths, exact seams, output matrices, rational/integer rank and dual BRC concatenation; and a standalone JavaScript/Node.js checker preserved losslessly as gzip/base64 VERIFY_EC49EB.js.gz.b64. Both exhaustively enumerate returning h-letter words for h=2,...,8, counts 4,15,56,210,792,3003,11440, with exact optimal (C,C_equal): (32,32),(34,48),(56,56),(52,72),(80,80),(70,96),(104,104). Their nine-by-nine certificate determinant pairs are (-1,-1),(+1,-1),(-1,-1),(+1,-1),(-1,-1),(+1,-1),(-1,-1). Python's 9-row 0/1 rational rank test uses prime 1000003: nonzero 9x9 determinants are bounded by 9^(9/2)<1000003 (Hadamard), so rank9 over rationals iff mod this prime, and displayed certificate determinants use exact integer Bareiss. Finite exhaustion proves its finite domain; general all-h result follows the analytic lower bounds and uniform witness families, not numerical extrapolation. The full actual Python checker, its original output, longer proof, both reports, and hashes are in the companion immutable local evidence archive.

Method: REUSE_APPLIED to EC49EA exact signed X6/BRC transfer and nine-state instrument; EXTEND_EXISTING_TOOL for exact primitive-cost optimization. Neither theorem changes P000, nor claims physical dynamics outside the declared observer or formal native Source adoption. Gateway authentication is read-only and owner lookup failed CONTROL_QUOTA; author GitHub draft is distinct from registered Result/review.

Next EC49EC: minimize prefix-trie genuine signed-primitive edge count when multiple selected words share path prefixes. Enumerate h=2,3,4 and compare independent costs 32,34,56, keeping full seam/terminal bucket labels, both BRC channels and provenance; then prove or refute a general trie-cost formula.
