# Auxiliary paper review of the complete-two-list QR/CRT prefix lemma

**Verdict: PASS within the exact stated paid model; no further mathematical correction is required.** I read the complete frozen 14,442-byte paper and checked equations (A)–(N), the finite boundary cases and the exclusions. The uniform discrepancy and the proposed finite cost bound follow from the stated hypotheses. This review does not accept a Native Result or complete a Task.

Reviewer native identity: **UNKNOWN**. Exposure: **DIRECTED_NONBLIND**. I was not a producer of the theorem, prototype or initial proof. I had the Root-supplied statement and shared context, and supplied two pre-freeze review clarifications: use the local relative bound (5/\sqrt p) before obtaining the final (6^k\sqrt M), and count only real materialized entries, excluding virtual modulus-1 singletons. The author incorporated those clarifications; this review involvement is explicitly disclosed. This is therefore an honest directed auxiliary review, with no claim of a clean-room, blind, or Native decisive review. I did not execute any scientific checker or experiment.

Reviewed paper: `QR_CRT_COMPLETE_PARTIAL_LISTS_PREFIX_NEARLINEAR_LEMMA.md`; SHA256 `d52df511d3e591fed210c231f0e8da7c8d3aedf6d9125656ad45dc4062340885`; Git blob `774e0e5b946ccc59b07d7dd957ae15fdc01196d0`. The paper is assistance for the actual selected Researcher on `RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST` / `TP2-F3369CF79B942BBC9DAB`. This reviewer created no session, authority, claim, Result, acceptance or Source publication.

## Exact theorem and charge model

The hypotheses are squarefree odd (M), (\gcd(N,M)=1), arbitrary integer shift (c), and positive **integer** (L). The predicate is the conjunction that (x^2-N) is a quadratic residue **including zero** at every prime of (M). There is no extra (x)-unit filter. The two complete group lists are materialized for every nontrivial group and every accepted offset in the entire length-(L) prefix is inspected. The separate additive charges have fixed positive (\lambda,\mu):

\[
 W\ge\lambda E+\mu C_L(c),\qquad
 E\ge\sqrt S\ (M>1).
\]

For two real groups the stronger (E\ge S_P+S_Q\ge2\sqrt S) is available. If one group has modulus 1 its singleton may be virtual and the sole real list has (S\ge\sqrt S) entries. At (M=1), both groups may be virtual with (E=0), while (C_L=L). The final paper uses this weaker real-entry account throughout; it does not silently charge the virtual singleton. Arbitrary unbalanced partitions are permitted.

The paper's conclusion is precisely

\[
 W\ge\frac{\min(\lambda,\mu)L}
 {(6\sqrt2)^K(K+2)(1+2\log L)},\qquad
 K=\max\{j\ge0:(j+2)!/2\le L^2\}.
\]

It is a bound for the declared complete-list and complete-enumeration model. Early successful factor extraction, rank-only queries, additional pruning predicates, compressed/implicit/shared or amortized structures, and general factorization algorithms are expressly outside it. The result supplies no lower bound for those other models.

Nonblocking wording recommendation for the actual Researcher’s integration: the final paragraph’s phrase “never materializes both complete lists” should be stated as “avoids any required nontrivial full group list.” The precise model already permits an uncharged virtual modulus-1 group, so materializing only its other, nontrivial full list remains inside the model. This clarification changes no formula or proof and requires no edit to the frozen original.

## Local Gaussian and Weil calculation

The Gaussian expansion is valid even at zero. With the same additive character and the same Gauss sum (\tau), completing the square gives

\[
 \sum_x e_p(ux^2+hx)=\chi(u)\tau e_p(-h^2/(4u)).
\]

Insertion into the character expansion therefore cancels the two factors (\chi(u)) and the same (\tau), yielding the exact signed identity

\[
 B_p(h)=\sum_{u\ne0}e_p(-Nu-h^2/(4u)).
\]

There is no omitted (\chi(-1)) or complex phase, including for (p\equiv3\pmod4). For (h\ne0), the parameters (-N,-h^2/4) are nonzero field residues since (p\nmid N) and (p>2); choose their coprime integer representatives to apply the cited theorem. For (h=0), the exact value is (-1), handled separately.

I independently extracted page 1 from the actual saved Harcos PDF with `pdftotext` and read Theorem 1 and its sum definition. It states that for prime (p>2) and parameters coprime to (p), the ordinary Kloosterman sum has magnitude at most (2\sqrt p). Its hypotheses match the use above. The saved PDF is 229,506 B, SHA256 `ee17d5dff37e572d0a00727954cb5cbab0ea57693f90e010a4e6446edb2cc394`, from the cited author-hosted URL. I checked all five frozen member pins, including that PDF, its page-one extraction and the parameter records. I did not fetch another paper or claim to have read Weil's original 1948 article or prove the classical deep input independently.

The zero-inclusive indicator

\[
 I_p(x)=\tfrac12[1+\chi(x^2-N)+\mathbf1_{x^2=N}]
\]

has mean (a_p=(p+\chi(N))/2\ge1). At a zero of (x^2-N) it is exactly 1, rather than the incorrect half-weight obtained without the final term. There are (1+\chi(N)\le2) zeros. For nonzero (h), the Weil estimate and this root correction give

\[
 |H_p(h)|\le\sqrt p+1,qquad
 \frac{|H_p(h)|}{a_p}
 \le\frac{2}{\sqrt p-1}\le\frac5{\sqrt p}.
\]

The final inequality is (3\sqrt p\ge5), valid already at the smallest allowed prime (p=3). Local positivity also holds at its smallest possible count (a_3=1). Thus both zero roots and the smallest local group are covered.

## Composite frequencies and the genuine prefix bound

For (b_p=(M/p)^{-1}\pmod p), CRT gives exactly

\[
 H_M(h)=\prod_{p\mid M}H_p(hb_p).
\]

The local frequency vanishes iff (p\mid h). Hence (d=M/\gcd(h,M)) contains precisely the nonzero-frequency primes, giving

\[
 |H_M(h)|\le S\,5^{\omega(d)}/\sqrt d.
\]

The proof retains the full local means at the other primes; it does not apply a prime-modulus nonzero-frequency bound to every nonzero composite frequency. With the positive-character convention for (H_M), inversion gives the paper's negative phases (e_M(-hc)e_M(-ht)). The arbitrary shift (c) changes only a unit-modulus phase.

At conductor (d), the frequencies are exactly (h=(M/d)b) with (\gcd(b,d)=1). The geometric sum has frequency (b/d). Since (d) is odd, pairing (b,d-b), and enlarging from units to all (1\le b<d), gives

\[
 \sum_{(b,d)=1}\Big|\sum_{t<L}e_d(bt)\Big|
 \le d H_{(d-1)/2}\le d(1+\log d).
\]

This is valid for all prefix lengths, incomplete blocks and multiple periods. Completion therefore yields

\[
 |C_L(c)-\delta L|
 \le\delta(1+\log M)
       \sum_{d\mid M,d>1}5^{\omega(d)}\sqrt d
 \le\delta6^k\sqrt M(1+\log M).
\]

The last step uses the exact divisor product
\(\prod_{p\mid M}(1+5\sqrt p)-1\le6^k\sqrt M\).
The intermediate 5 is sufficient to pay for the divisor grouping; simply starting with 6 at every nonzero local factor would not justify the same final 6. At (M=1) the conductor sum is empty and (C_L=L) exactly. No prefix conclusion was inferred from global density alone.

## Finite cost argument and all-size modulus coverage

Ordering distinct odd primes gives (p_i\ge i+2), and therefore

\[
 \delta\ge2^{1-k}/(k+2),\qquad M\ge(k+2)!/2.
\]

Both are correct for every subset and the empty subset. Define (D=6^k\sqrt M(1+\log M)).

For (M\le L^2), one has (k\le K). If (D\le L/2), then
\(C_L\ge\delta L/2\ge L/[2^k(k+2)]\), stronger than the required count bound. If (D>L/2) and (M>1), the real entries satisfy

\[
 E\ge\sqrt S>
 \frac{L}{\sqrt2(6\sqrt2)^k\sqrt{k+2}(1+\log M)}
 \ge\frac{L}{(6\sqrt2)^K(K+2)(1+2\log L)}.
\]

The last comparison uses (k\le K), (\log M\le2\log L), and (\sqrt{2(K+2)}\le K+2). It does not require a positive prefix count in this second case. At (M=1) use the direct count instead of charging virtual cells.

For (M>L^2), let (R_j) be the shortest sorted prime prefix exceeding (L^2). Its preceding prefix has at most (K) primes, so (j\le K+1), without bounding the total (k). Its accepted count obeys

\[
 S_j>\frac{L^2}{2^K(K+3)},\qquad S\ge S_j.
\]

The first inequality follows from (R_j>L^2); the second is deliberately non-strict because remaining local counts can equal 1. Thus
\(E> L/[2^{K/2}\sqrt{K+3}]\), stronger than the target because
\(K+2\ge\sqrt{K+3}\), (6^K\ge1), and (1+2\log L\ge1).
This covers arbitrarily large (M) and arbitrarily large total prime counts.

At (L=1), (K=0) and the requested denominator is 2. (M=1) contributes the real inspection charge (\mu); (M>1) has at least one real entry and contributes (\lambda). Both cover the bound without virtual-cell charges. Finally (K=O(\log L/\log\log L)), so the fixed-positive-charge finite inequality gives (W\ge L^{1-o(1)}\). It makes no stronger linear-rate or bit-complexity assertion.

## Provenance and outcome

The original prototype/auxiliary authors remain UNKNOWN and the review remains nonblind. Root's disclosed owner/contribution aliases are EM-DVR-FBF223, EM-DVR-4C90FB, EM-DVR-C1A1D9, EM-DIRECT-E1F2B6, EM-DIRECT-FA0C27 and EM-DIRECT-49ADE6; these are provenance disclosures, not identities assigned to this reviewer. The Source-saved input CRT interface and its attribution remain unchanged.

The paper's squarefree odd domain does not silently extend to the separately saved prime-power result or even primes. No 63/3043 checks, old 600/1400 corpus, producer code, or scientific checker was imported or executed. No new numerical experiment, Source/native write, identity, claim, Task, RR, acceptance, Working Truth, Foundation or mathematical parent completion is created by this review. Mathematical parents remain OPEN. Adoption and formal Task judgment remain with Root and the actual authorized Researcher/Driver.
