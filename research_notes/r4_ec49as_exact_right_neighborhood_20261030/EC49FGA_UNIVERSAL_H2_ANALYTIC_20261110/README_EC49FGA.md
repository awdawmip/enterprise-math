# EC49FGA — Universal exact H2/Hh BRC signed-X6 prefix minimum

Date: 2026-11-10 (Asia/Shanghai). Researcher: EM-DIRECT-424B5A / TASK_RESEARCH; activity RA-C4E3ED7605765071A75B6307. Classification: author-side mathematical theorem, analytic infinite tail with previously published exact finite base; independent Driver review pending. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Model and theorem

Use the original six ordered native signed-X6 operation codewords:
a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
Each signed integer denotes a step along a named native axis; operation-horizon h is not native microstep length.

Admissible length-h words satisfy #e=#a+1>=1, strictly positive complete BRC key K=(h+1-#g,h+1-2#e-#f,#e), and the original nine-state DFA. The required low signatures 1,2,4,8 are its terminal states 3,7,2,6 respectively. Fix the four H2 low paths de, ed, ce, ec, associated with signatures 1,2,4,8. For each integer h>=3 choose one admissible Hh word for each of the same four signatures, with arbitrary complete keys. Let M(h) count the minimum number of distinct nonempty ORDERED SIGNED-NATIVE MICROSTEP prefixes in the union of the eight paths.

**New universal exact formula (H2-low/Hh-low auxiliary model):**

$$ M(h)=4h+42 \qquad \text{for every integer } h\geq 10. $$

The lower bound for h>=14 is analytic, including arbitrary keys and unequal native path lengths. The four values h=10..13 use already-published exact exhaustive integer DP certificates (82,86,90,94). The upper bound is an earlier explicit family (EC49FFU/FFY). The original frozen 24-observation mother objective, including H2/H3 high labels and <=5 full keys, remains a distinct problem.

## Analytic lower bound for every h>=14

Let B be the native prefix set of the four fixed H2 words. Direct expansion gives |B|=28; each H2 path has native length 8.

**Lemma 1 (length and root-support dichotomy).** Each admissible low-output word contains both an e and at least one c or d. The former follows from #e=#a+1>=1; the latter follows from the original DFA, as a/e/f/g transitions cannot enter any required low state without a c/d. Hence any chosen Hh word w has native length

$$ L(w)=2h+2(\#c+\#d+\#e)\geq L_0:=2h+4. $$

Computing reachable low outputs from the original DFA after each first operation gives:
a -> {2,8}; c -> {4}; d -> {1}; e -> {2,8}; f -> {2,4}; g -> {1,8}.
The only two different first-operation letters whose low-output reachability covers {1,2,4,8} are {f,g}. Any four-signature family therefore either (A) uses exactly f and g as its first letters, or (B) uses at least three different first letters.

**Lemma 2 (case A).** The two f-initial paths must produce 2 and 4, and the two g-initial paths must produce 1 and 8. Select one path from each group. Their first native steps +1 and +2 differ, so they have disjoint nonempty native prefix sets. Each has at least L0 native prefixes. Each intersects B in exactly its first native microstep: f starts (+1,-1) whereas B's only +1 start continues +2 (code c), and g starts (+2,-2) whereas B's only +2 start continues +1 (code d). Thus B plus the two representatives already costs at least

$$ 28+2(L_0-1)=4h+34. $$

**Within-group branch lemma:** If two operation words have the same horizon h and begin f (respectively g) but end in the two distinct reachable low signatures of that group, then either word contributes at least FOUR ordered native-prefix edges absent from the other. Proof: from DFA state 4 after f, a/e/f/g leave state 4 invariant, while the first c enters output 4 and the first d enters output 2. From state 5 after g, the same neutral letters leave state 5 invariant, while first c enters output 8 and first d enters output 1. Hence different requested final labels require opposite first deciding c/d transitions after a common neutral prefix. At the first differing operation: (i) c vs d has differing first native steps and the additional length-four code contributes >=4 edges; (ii) deciding c/d vs neutral a/e/f/g: the neutral path must later take the opposite deciding code, so one further operation exists. The two distinct codes share at most one first native microstep (only c/f or d/g do); the decision-branch path has >=3 new edges in its length-four decision plus >=2 in a later code, and the neutral-branch path has >=1 new edge at divergence plus >=4 when its later opposite decision occurs. (iii) two different neutral letters start with distinct signed microsteps (-1,+3,+1,+2), and both paths must later take c/d, giving >=2+4 new edges. Codewords are prefix-free, so later microsteps cannot re-merge after a native-prefix split. Therefore each path contributes >=4 fresh native prefix edges.

The second f-initial and second g-initial paths each add at least four edges outside the chosen representatives. The fresh edges start after the first f or g code, so none is in B; different f and g groups are disjoint. Thus case A costs at least

$$ 4h+34+4+4=4h+42. $$

**Lemma 3 (case B).** Pick three Hh paths starting with three distinct first operation codes. Each native length is >=L0. Different first operation codewords share at most one native microstep (only c/f and d/g share one), so conservatively the union of three whole native paths has at least 3L0-2=6h+10 prefixes. The intersection of each chosen high path with B is an initial prefix chain of size <=8, because the longest fixed H2 word is 8 microsteps. Therefore B adds at least 28-3*8=4 prefixes, giving

$$ M(h)\geq 6h+14\geq4h+42 \quad(h\geq14). $$

The two cases exhaust every valid four-label realization, proving the analytic lower bound for all integer h>=14. No full-key bound is assumed.

## Constructive upper bound and finite bridge

For every integer h>=4 retain the H2 words and choose the following Hh words:
signature 1: gfe + g^(h-4) + d;
signature 2: fe + g^(h-3) + d;
signature 4: fe + g^(h-3) + c;
signature 8: gfe + g^(h-4) + c.
Each is valid for the original DFA and native-X6 endpoint, with two complete keys (3,1,1) and (4,h-2,1).

The two high prefixes fe g^(h-3) and gfe g^(h-4) each have native length 2h and start with different signed axes. Adding the final c and d alternatives costs eight native edges per group. Hence the four Hh paths cost 2(2h+8)=4h+16. Their only common native prefixes with the H2 baseline are the first +1 and +2 microsteps; the H2 baseline contributes another 28-2=26. Therefore the eight paths cost **exactly 4h+42**. This family was previously published in EC49FFU/FFY and is reused here.

Previously published unrestricted-key exact integer DP results, independently read back for this report:
H10=82: EC49FFV commit de8f6306e63828368b972509a78ceea0b358401d, report_H10.json, blob c8d24fdf4dac3df9f09d36d57cdf1a05714e00df.
H11=86, H12=90, H13=94: EC49FFW commit aa91c76788d5bc60c41221e9ea8cdb2426add1f2, EXACT_REPORT_EC49FFW.json, blob 5c50c0edd7ec081b6d5e62be8116b8f97165060f.
These four complete finite cases bridge h=10..13 to the analytic h>=14 proof. They are reused exact prior certificates, not newly executed long enumerations.

## Verification, reuse and next target

VERIFY_EC49FGA.py independently checks the original DFA first-code reachability table, the unique two-first-code cover {f,g}, the baseline's literal 28 native-prefix edges and full native signed-X6 observer/complete-key/endpoint/prefix counts of the explicit witness for every h=4..200. EXACT_AUDIT_EC49FGA.json contains the recorded exact audit summary. These finite checks audit transcription and witnesses, while the lower bound follows from the structural proof above.

The concurrent EC49FFZ high-seed absorption theorem, commit e62b28f6ddf43b5ad4acb325ad7f529a41db0298, studies the *different* fixed H2/H3 high-seed model with optimum 4h+16. Our formula retains the H2-low baseline with 28 native edges. P000 and ACTIVE worldview are unchanged. There is no formal CLAIM/Result for the historical EC49AS text, whose native control query returned NO_CURRENT_IMMUTABLE_PUBLICATION.

Next question: integrate the high-seed absorption family with intermediate H4..H9 frozen high/low quota under **at most five complete keys and at most 93 native prefixes**, and seek either an exact feasible full 24-label witness or a finite typed dual certificate for a specified candidate class.
