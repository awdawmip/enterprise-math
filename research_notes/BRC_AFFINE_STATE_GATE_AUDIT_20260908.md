# BRC affine state gates: compiled queries and complete D residue classes

Researcher-ID: EM-HME-0CE4FD / TASK_RESEARCH  
Global-Knowledge-Sync: main@91cd38d / GLOBAL_KNOWLEDGE_V1  
Canonical snapshot: 91cd38de772d892c0707ba356d7bbcecb44996bb  
Project parent: 9fb93e7ef1988f2feaabdc76133af08490400ddd

This checkpoint turns the two separated state criteria into a fixed modular lookup packet, retains all 52 earlier constructive state witnesses, and expands the D construction to 96 residue classes. Two prescribed sizes per class give 192 exact proper-factor certificates. The large constructed cases take a single-pass median 22.4 microseconds at their assigned multiplier, including the modular checks, both roots, gcd and product verification.

On the three published mathematical puzzle integers, the same 39 previously checked positions admit neither state subset. Compiled warm queries evaluate each 13-position packet in 2.6875–3.6500 microseconds. There is no public factor, new multiplier position, advancing ceiling or search extension. The measured task here is membership in these particular subsets; the D strip alone does not guarantee a square completion gap.

## Exact membership criteria and scope

For \(T=mN>0\), use \(J=\lfloor\sqrt T\rfloor\), \(R=T-J^2\), and the immediate ceiling gap \(A=\lceil\sqrt T\rceil^2-T\). D denotes \(0<R\le J\); U denotes \(J<R\le2J\).

For fixed \(m>0,c\ge0\), with \(T>c^2\),

\[
R=J-c
\iff H=4mN+4c+1\text{ is square}.
\]

Forward, \(H=(2J+1)^2\). Reverse, an odd square root \(y\) gives \(J=(y-1)/2>c\) and \(T=J^2+J-c\), so this is the actual floor root and a valid D state. Exact recognition enforces the threshold through \(y>2c+1\).

For the U boundary,

\[
A=1 \iff mN+1\text{ is square}.
\]

Its target is one below its immediate upper square, giving \(R=2J\). These criteria concern the D strip and the U boundary, not all D/U states or all square-completion witnesses. A zero mask means this packet has no matching state; it is not a statement that the input has no other factorization shortcut.

The fixed basis is inherited from the previous kernel-13 study. For odd squarefree \(d\), take \(m=c=d\). For even squarefree \(d\), take \(m=4d,c=2d\). Thus \(c^2=md\) and \(2c\) is divisible by \(m\). No parameters were fitted to the public outcomes.

## Compiling the modular tests

For each existing residue-table modulus \(M\), compile one 26-bit word for each \(r\pmod M\):

- Bit \(i\) records whether \(4m_i r+4c_i+1\) is a square residue modulo \(M\).
- Bit \(i+13\) records whether \(m_i r+1\) is a square residue modulo \(M\).

A query reduces \(N\) once per modulus and intersects the indexed words with its requested bits. Only survivors require an exact affine square-root test. Every exact square survives every constituent table, which proves the necessary-condition preservation of the compiled packet.

The static variant uses \(M=4032\). LOW12 uses the source order \(4096,3465,221,12673\). For this basis and odd \(N\), the D expression is \(1\pmod8\), so all its 4096 D bits are set at reachable odd residues. The U bits retain their power-of-two constraint. The compiled artifact explicitly verifies the former property over the odd residue indices.

All modular data reuse the repository's existing square-residue generators and checked-in static table. There are 24,487 compiled rows across five moduli. This is finite small-modulus compilation, not enumeration of candidate factors of the public integers.

## Cost observations

Both stages use nine paired, rotated-order rounds with eight repetitions per round. Timers include per-\(N\) reductions, state/predicate evaluation, result construction and equality checks. Tables, imports, input/source verification and expected-state preparation are outside the warm timers.

Public rows represent one \(N\) with all 13 assigned pairs. A constructive row represents 13 distinct positive \(N\), each with only its assigned pair. These are different workload shapes. Compare each variant with its own group's baseline, not a public row with a constructive row.

### Direct affine implementation

This stage calls the source floor-completion API for its baseline. The affine variants share each \(N\)'s modular phases across the selected pairs, but still loop over individual predicates.

All times below are microseconds per group.

| Group | Floor baseline | Affine 4032 | Affine LOW12 | LOW12 ratio vs floor |
| --- | ---: | ---: | ---: | ---: |
| RSA-270 | 68.1125 | 46.1250 | 24.1375 | 2.82x |
| RSA-896 | 54.0875 | 37.7250 | 21.7000 | 2.49x |
| RSA-2048 | 108.4625 | 77.4625 | 23.4625 | 4.62x |
| small_D | 19.9250 | 30.1000 | 45.5875 | 0.44x |
| small_U | 18.1375 | 29.8125 | 44.1375 | 0.41x |
| large_D | 108.3750 | 178.0250 | 152.8375 | 0.71x |
| large_U | 104.3875 | 135.5250 | 156.9750 | 0.66x |

This version retains all positive cases but its per-candidate overhead makes the positive cohorts slower. The public packet is faster because its modular exits avoid roots. That cost observation motivates compiling the fixed predicate packet; it is not a claim against the retained positive families.

The first static-table lookup costs 0.0148 ms; the first LOW12 build costs 2.5252 ms. Their raw source payloads are 504 and 2,559 bytes respectively.

### Compiled implementation

The baseline here returns the same bit-mask result as the compiled variants. Its timing is collected in this second paired run; the earlier run is preserved without replacing its measurements.

| Group | Floor baseline | Compiled 4032 | Compiled LOW12 | LOW12 ratio vs floor |
| --- | ---: | ---: | ---: | ---: |
| RSA-270 | 95.8875 | 77.2125 | 3.3500 | 28.62x |
| RSA-896 | 81.5375 | 24.9375 | 2.6875 | 30.34x |
| RSA-2048 | 210.7500 | 139.2375 | 3.6500 | 57.74x |
| small_D | 47.2750 | 19.2875 | 36.3500 | 1.30x |
| small_U | 19.9000 | 13.5125 | 22.8875 | 0.87x |
| large_D | 194.8250 | 137.3000 | 250.0625 | 0.78x |
| large_U | 173.9000 | 184.2875 | 193.0375 | 0.90x |

Compiled LOW12 is faster in all nine public paired rounds per input, with warm median ratios 28.62x, 30.34x and 57.74x. The mechanism is visible in the exact counters: it makes zero affine-root calls for these packets.

The compiled 4032 variant retains occasional positive speed gains: 2.45x on small D, 1.47x on small U and 1.42x on large D in this run. Large U has no median gain. LOW12 is not uniformly preferable for positive singleton queries. No routing policy is trained or changed from these measurements.

### Setup, storage and loading

The compiled static payload occupies 16,128 bytes, LOW12 81,820 bytes, and all five tables 97,948 bytes. The measured source-table setup takes 3.0964 ms, compilation 225.9907 ms, and initial serialization 22.5310 ms. The exported certificate includes precompiled payloads, so repeated use need not regenerate them.

A separate encoding-only audit reloads exactly those saved bytes. Its nine paired rounds preserve every byte, table length, bit assignment and SHA256 digest:

| Encoding | Envelope characters | Median checked load |
| --- | ---: | ---: |
| Base85 | 51,819 | 8.1534 ms |
| Base64 | 55,207 | 0.744367 ms |

Base64 is faster in all nine paired rounds, by a median ratio of 10.95x. This loader includes JSON parsing, decoding, decompression, hashing, uint32 construction and byte equality; filesystem I/O is excluded. The original single Base85 load was 24.2872 ms and remains in the raw first-stage record. It must not be used as the denominator of the paired encoding comparison.

The warm packet ratios do not describe first-use costs. Loading is paid once when reusing the tables, and compilation is a separate preparation operation. Both encodings are retained as audit evidence; Base64 supplies the verified faster loading representation.

## Public-input provenance and coverage

The fixed inputs remain the RSA Inc-attributed MysteryTwister mathematical puzzles: [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf), and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf). Their complete decimal inputs and digests are consumed from the pinned prior certificate. No present-day unresolved status is inferred from these PDFs.

All 13 basis positions per input were already recorded in the kernel-13 certificate. The first stage adds 78 state-predicate observations on those 39 existing positions. The compiled and encoding stages consume those observations. Public unique multiplier positions remain 312.

LOW12's D/U survivor counts after successive moduli are:

| Input | After 4096 | After 3465 | After 221 | After 12673 |
| --- | ---: | ---: | ---: | ---: |
| RSA-270 | 13 / 6 | 5 / 1 | 1 / 1 | 0 / 0 |
| RSA-896 | 13 / 7 | 1 / 0 | 0 / 0 | 0 / 0 |
| RSA-2048 | 13 / 6 | 1 / 1 | 0 / 0 | 0 / 0 |

The 4032-only affine stage requires 11, 7 and 10 roots respectively; LOW12 requires zero. The compiled evaluator stops as soon as the intersection is empty.

Each performance stage has 2,808 warm public-position visits and 3,744 warm constructive-position visits per variant. Warmups, validation and instrumentation are additional replays. These are cost measurements on fixed observations, not independent trials or a larger challenge search.

## Complete residue classes for the D construction

The D strip also has a useful positive parametrization. Set

\[
a=b^2-c,\qquad
mN=a^2-b^2=b^4-(2c+1)b^2+c^2.
\]

Because \(m\mid2c\) and \(m\mid c^2\),

\[
N\in\mathbb Z
\iff m\mid b^2(b^2-1).
\]

For odd squarefree \(m=d\), each prime divisor \(\ell\mid m\) permits

\[
b\equiv0,\;1,\;-1\pmod\ell.
\]

These three residues are distinct, so CRT gives \(3^{\omega(m)}\) classes modulo \(m\). The constructed \(N\) is automatically odd.

For even \(d=2e\), \(m=8e,c=4e\) with odd squarefree \(e\). Odd \(N\) requires \(b\equiv1\) or \(7\pmod8\), together with the same three choices modulo each odd prime divisor of \(e\). This gives \(2\cdot3^{\omega(e)}\) classes.

For the 2-adic statement, a multiple of four has an even quotient \(N\), and \(b\equiv2\pmod4\) fails divisibility by eight. For odd \(b\),

\[
b^4-(8e+1)b^2+16e^2\equiv1-9b^2\pmod{16}.
\]

An odd quotient by \(8e\) requires this to be \(8\pmod{16}\), equivalently \(b^2\equiv1\pmod{16}\), or \(b\equiv\pm1\pmod8\).

The exact class counts are:

| \(d\) | \(m\) | \(c\) | Odd-input residue classes |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 |
| 13 | 13 | 13 | 3 |
| 14 | 56 | 28 | 6 |
| 3 | 3 | 3 | 3 |
| 15 | 15 | 15 | 9 |
| 2 | 8 | 4 | 2 |
| 5 | 5 | 5 | 3 |
| 6 | 24 | 12 | 6 |
| 30 | 120 | 60 | 18 |
| 22 | 88 | 44 | 6 |
| 105 | 105 | 105 | 27 |
| 33 | 33 | 33 | 9 |
| 7 | 7 | 7 | 3 |
| Total | — | — | 96 |

These counts are complete for this basis's D parametrization and its odd-input condition. They do not classify every factorable integer or every D state.

For every allowed residue \(r\pmod m\), the executed construction chooses

\[
b=mk+r,\qquad k\in\{3,\;2^{511}+3\}.
\]

Since \(c\le m\) and \(b\ge3m\), \(a-b=b^2-b-c>m\), and \(b^2>2c+1\). Thus

\[
J=a-1,\quad R=b^2-2c-1=J-c>0,\quad A=b^2=J+c+1,
\]

with the correct immediate ceiling and D state.

To prove a proper factor, write \(L=a-b,V=a+b\), and \(h=\gcd(L,m)\). From \(m\mid LV\), \(m/h\mid V\), so \(L/h\mid N\) and \(L/h\mid L\). Therefore

\[
\gcd(N,L)\ge L/h\ge L/m>1.
\]

Also \(V>m\) gives \(N=LV/m>L\ge\gcd(N,L)\). The returned gcd is consequently nontrivial.

All 192 prescribed certificates pass the mask admission, exact affine root, exact completion-gap root, gcd, product and D-state checks. The 96 large inputs have 2045–2065 bits. The single-pass median times are 2.0 microseconds for small cases and 22.4 microseconds for large cases. They cover one assigned multiplier, including four mask checks, both roots, gcd and product verification. Construction, table loading and later annotations are outside these timers.

These are deliberately constructed composites. General prime factors, coprimality and new semiprime counts are not asserted; no new primality checks were performed. The earlier 12 verified small prime pairs remain identified in their own certificate. These positive certificates are not public-challenge factors.

## Verification, dependencies and continuation

Companions:

- [Initial affine checker](../experiments/brc_affine_state_gate_audit_20260908.py)
- [Initial affine observations](../experiments/brc_affine_state_gate_audit_20260908.json)
- [Compiled-mask and residue-family checker](../experiments/brc_compiled_affine_gate_audit_20260908.py)
- [Compiled payloads, timings and 192 proper-factor certificates](../experiments/brc_compiled_affine_gate_audit_20260908.json)
- [Preceding paired-state study](BRC_KERNEL13_STATE_PAIRS_20260908.md)

Both scripts pin the source core, residue-filter API, shortcut catalog and static-table module, plus their input certificates. The compiled checker additionally pins the complete initial affine checker and result. AST parsing and executed assertions passed. Production code and its 46 previously passing selected tests are unchanged.

The encoding helper and residue-family helper were appended after the compiled timing run, then executed separately on saved masks and observations. Both are included in the final reproduction script. Neither extension repeats the public arithmetic or changes the previously measured variants.

Reuse disposition: COMPOSE_APPLIED for existing floor completion and square-residue tables, the derived affine criteria, and their fixed compiled packet. The previous goal turn is classified as PROGRESS from its verified project artifacts. This checkpoint adds mathematical and measured evidence; the parent objective remains active.
