# Riesel continuation v15: complete R3 ninth-budget observation, global minimum and two exact total costs

Date: 2026-11-24, Asia/Hong_Kong.

Researcher-ID: `EM-DIRECT-970E1C / TASK_RESEARCH`  
Activity-ID: `RA-D2EC212845B63844081F9A14`

## Results

The state remains the full integer trajectory \(F_n(a)=a^2 2^n-1\), advanced by positive singleton BRC action \(x\mapsto2x+1\) at the fixed Heartbeat X6 anchor, with unit weight and multiplicity. The old twenty-prime dictionary P and the fixed 43-prime R3 fiber retain their definitions. The latter is specified completely in [the Chinese analysis](analysis_zh.md) and the scripts.

1. **Complete ninth-budget root predicate on all of R3.** The inherited basic-pair theorem forces 5 and 13. The zero-W branch, where W={19,73}, has exactly eight types of irredundant nine-prime supplements: 675936 phase dictionaries and 86519808 signed CRT descriptions. The inherited one-W branch has 4800 phase dictionaries and 307200 signed descriptions. The two-W branch now has a complete canonical root-existence predicate with 15914 phase and 489992 signed descriptions. Same-root dictionary replacements are part of the two-W proof; its counts are not counts of every raw dictionary. The complete budget-eight predicate is explicitly included. See [zero-W proof](zero/proof.md), [one-W proof and minimum](one/proof.md), and [two-W root predicate](both/proof.md).
2. **The complete minimal ninth-budget observer on R3.** Exactly 59 free prime coordinates are individually necessary and jointly sufficient. If their squarefree product is M9, a finite modulus N decides delta_P<=9 on R3 iff M9 divides N. This holds both for root residues and for complete future residue trajectories. Hence \(\Omega_9(R_3)=\widehat\Omega_9(R_3)=840\). The least sufficient modulus M9 has 594 decimal digits and 1973 binary bits; this is a fixed-budget result, not a general bit-complexity theorem. See [observer proof](observer/proof.md).
3. **A finite exact-cost 9/10 obstruction at order 840.** The essential coordinate 127681 can be toggled while retaining a common ten-prime completion. The actual two ordinary roots have 906 and 907 digits, exact costs nine and ten, and at least 103 identical complete prime-coordinate trajectories. The two extra common primes are the least prime divisors of Phi560(2) and Phi1680(2). Neither cyclotomic integer is assumed prime; full order-gcd checks establish exact orders of every prime factor.
4. **The global R3 exact-cost-nine minimum.** The minimum over all positive a in R3 with delta_P(a)=9 is the 151-digit integer \(a_9=A_3+11380571075S_3\), with exact total cost tau(a9^2)=29. All canonical two-W CRT starts were compared; the one-W minimum is larger; the entire zero-W branch was excluded below the winning index by a complete CRT search with mathematically valid nonnegative-index pruning. See [global minimum proof](global/proof.md).
5. **The one-W branch minimum has a different total cost.** Its 156-digit minimum \(a_{1W}=A_3+811311504227722S_3\) has delta_P=9 and tau=28. The old prime 113 is redundant because of joint old/new phases, while 28 pairwise-coprime full integer terms force the exact total. An explicit ordinary arithmetic progression preserves the exact pair (9,28).
6. **Two exact total costs at every higher supplemental budget.** For every integer s>=9, infinitely many ordinary roots in R3 have \((\delta_P,\tau)=(s,s+19)\). Together with the inherited s+20 construction, the same fixed 43-channel trajectory realizes both pairs for every such s. The new proof uses a dyadic refinement with exact prime orders 84*2^j and 28*2^k, a shift of three to control every fixed-prime collision, and a saturation/CRT construction making all private full-integer terms pairwise coprime. See [cost-gap spectrum proof](gap/proof.md).

The exact global minimum is:

```text
4535953965311753528081323514270677649037193321945505620446333306332288510872289104091229337616491589657748499046945212207565221052351500539027726253413
```

Its supplement is `{5,13,19,73,38737,487824887233,1153,3457,816769}`. The free t phases, after n=32+144t, are 1 modulo 2 for 1153, 0 modulo 4 for 3457, and 2 modulo 4 for 816769. Both the covering upper bound and unrestricted integer lower bound are proved.

## Exact arithmetic and actual native execution

The inventory files retain complete cyclotomic products and deterministic recursive n-1 primality certificates. The all-prime reductions are proved using joint residual incidence and the covering-interval theorem, rather than a prime-size cutoff. The zero-W lower exclusion processes all 47 geometries; each nonnegative partial CRT extension can only increase its representative. Later progression representatives are not discarded based on an incidental cost-eight first root.

The complete observer check uses exponent period **60480**, v period 5040 and 1872 residual positions. It checks all 59 actual ordinary on/off root pairs by exact set cover over the complete proved prime universe, without evaluating the explicit branch predicates. All on roots have exact cost nine; all off roots have cost greater than nine. General off-root finiteness is not asserted, except for the separately completed 9/10 pair at order 840.

The two compact roots in `global/global_minimum_certificate.json` have three witness sets: 29 terms for the global minimum, and two sets of 28 terms for the same one-W minimum. The native execution actually completes:

| Operation | Count |
|---|---:|
| Native one-step updates | 9424 |
| Native two-step composite evaluations | 4712 |
| Prime quotient/remainder readouts | 453040 |
| Joint readouts and exact recompositions | 9424 each |
| Fixed-43 residue comparisons | 405232 |
| Witness entries across the three sets | 85 |
| Gcd-one checks within those sets | 1162 |

There are two distinct roots, not three. Counts across sets do not assert that all witness entries or pairs are distinct. Native execution produces witness intervals; covering the whole infinite trajectory is supplied separately by exact periodic proofs and complete period checks. The compact dictionaries have period 20160; this is not the full observer universe period.

The new gap-spectrum examples have costs (10,29) and (11,30), root sizes 603889 and 639638 bits, and respectively 406 and 435 gcd-one checks. Their complete hexadecimal roots, progression moduli, phase data and witness indices are retained. Complete integer terms are actually evaluated; the certificate specifies them losslessly by root and exponent rather than repeating every large integer string. These two examples use scalar arithmetic, with no additional native-run claim. The every-s theorem is proved independently of this finite execution.

A separate [finite-pool exploration](total/proof.md) computes minimum cover size 29 for the eight saved zero-W representatives within the specified 86-prime pool. This is not a lower bound on unrestricted tau across all primes.

## Reproduction

From this directory, with Python 3 and its standard library:

```sh
python zero/verify_zero_nine.py
python zero/verify_minimum_below_bound.py
python one/verify_one_w_minimum.py
python both/verify_both_tail.py
python observer/verify_observer.py
python gap/verify_gap_spectrum.py
python total/verify_selected_pool.py
python global/verify_global_minimum.py --source-dir /path/to/src
```

The source directory must contain the frozen `enterprise_math` modules from EM commit `b1efc6c805661ed7b476e6e730107da6043176ee`. The user reproduction archive contains those four exact files under `src/`; their Git blob IDs are checked before native execution. The scientific note references their immutable existing source rather than duplicating the runtime here. Omitting `--source-dir` makes the global script run its scalar checks only and explicitly records that native execution was not performed. The saved global certificate was produced with native execution enabled.

The global checker reads the adjacent zero and one certificates, records their exact SHA-256 dependencies and recomputes all two-W CRT starts. Those dependency hashes identify actual calculations; they do not replace the written all-prime proofs. Regeneration can change elapsed-time fields and corresponding certificate hashes without changing the mathematical results.

## Immutable dependencies and external inputs

- Complete v13 R3 budget-eight classification and observer: `awdawmip/enterprise-math@e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124`.
- V14 forced basic pair, one-W classification and R4 spectrum: `awdawmip/enterprise-math@9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124`.
- Prior R3 exact s+20 finite spectrum: `awdawmip/enterprise-math@5cfe4d64429f284232029341c6ba774e2eb6f727:research_notes/portable_direct/riesel_eight_spectrum_20261124`.
- Crittenden-Vanden Eynden covering-interval theorem, primary modern proof: Balister, Bollobas, Morris, Sahasrabudhe and Tiba, *Covering intervals with arithmetic progressions*, <https://par.nsf.gov/servlets/purl/10165575>.
- Bang's primitive-prime-divisor theorem, as stated in Lemma 12 of the observed Filaseta-Finch-Kozek author draft: <https://www.whittier.edu/sites/default/files/media/academics/math/Kozek_Sierpinski_JNTdraft(2008).pdf>. The file's first page is dated 23 December 2007; numbering is relative to this actual draft.

## Remaining boundaries

The original fixed root a_star is not proved to have infinite covering cost. The two-W result is a complete canonical root predicate, not an enumeration of every raw nine-prime dictionary. The full joint (delta_P,tau) spectrum is not classified; in particular, existence of an R3 exact-cost-nine root with tau<=27 remains unresolved. The exact value 840 belongs to R3; R1 and R2 inherit the lower bound 840 and retain the known upper bound 26880. The narrower R4 retains its exact order 720. Fixed-budget modulus bits and the general Theta(2^b) maximum-prime-order theorem are separate results.

The entries in `reviews/` are shared-context collaborative mathematical checks. Scientific preservation, Activity association and knowledge journal publication have separate actual source states. Independent project Review, formal proof acceptance, and Foundation promotion are not claimed.
