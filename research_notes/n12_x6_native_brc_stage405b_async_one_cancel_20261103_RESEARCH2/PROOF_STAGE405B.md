# Stage405-B — exact strict compression under one asynchronous POP and one synchronized inverse-pair CANCEL

Date: 2026-11-03 (Asia/Shanghai). Parent: Stage404-B, \`54c9f2c295e1b74e42589df4f549d24f454ff040\`, Draft PR #1736. Classification: **author-side proved scoped theorem + exact executable checks; UNREVIEWED / NOT_ADMITTED**.

Frozen scientific inputs (unchanged): Enterprise Math \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`, global science \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`; original P000 Git blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Current behavioral rules were separately read through global canonical main, including math proof rules and project method preferences. No P000/worldview modification.

## Question and typed observer

Let \(\mathcal D=\{\pm E_i:1\le i\le6\}\), with the formal inverse \(-d\). Two initially equal-length native **ordered** source words \(P,Q\) have observations consisting of their separate lengths, six-component displacements \(z_P,z_Q\), complete **directed adjacency** histograms \(J_P,J_Q\), all endpoint-derived triple-coordinate readouts, the exact native unweighted/positive-weight BRC endpoint count/mass, the signed multiplicative word trace when specified, and
\[
K(P,Q)=\#\{1\le i\le\min(|P|,|Q|):P_i=Q_i\}
\]
at *absolute positional alignment*. Source labels and native signed directions are preserved. Positive branch masses are not signed cancellation.

Allowed future operations: arbitrary common two-source \(\mathrm{APP}(a,b)\); at most one \(\mathrm{POP}_Q\) (remove Q's last symbol); at most one **synchronized** \(\mathrm{CANCEL}\) deleting the final two symbols in each source, enabled exactly if both terminal pairs consist of mutually opposite native directions. Every intermediate observable and operation enabledness is visible. This is a Path-formal history model.

## Theorem 405.1 — complete three-element fiber with a strict two-state quotient

Write \(A=+E_1,\ B=-E_1\), and \(Q=A^5\). Fix the current marginal observer
\[
m=5,\quad z_P=3E_1,\quad z_Q=5E_1,\quad
J_P(AA)=2,\ J_P(AB)=J_P(BA)=1,\quad J_Q(AA)=4,\quad K=4
\]
with all unspecified directed edges absent. The *entire* twelve-native-direction current-observation fiber is exactly
\[
F=\{(AAABA,Q),(AABAA,Q),(ABAAA,Q)\}.
\]
Under all finite legal future operation sequences as above, its exact future-observation equivalence partition is
\[
\boxed{\{\,(AAABA,Q)\,\}\ \sqcup\ \{\,(AABAA,Q),(ABAAA,Q)\,\}.}
\]
Thus the minimal extra-state count is \(q(F)=2\), requiring one fixed-length bit. The previous uniform four-paired-label suffix has three distinct states and requires two bits: this is a **strict lossless compression** under one asynchronous POP and one paired CANCEL.

### Proof: complete fiber

The required directed edge multiset \(\{AA,AA,AB,BA\}\) has an Euler trail starting and ending at A. Its single B must occupy one of the three interior positions 2,3,4. Those choices give the three listed words; no other native direction may appear because every adjacent edge is prescribed and m=5. The sole Q Euler trail with \(J_Q(AA)=4\) is \(A^5\). Each P contains precisely four A labels and one B, so the endpoint is \(3E_1\) and the coincidence with Q is 4. Any source-local multiplicative signed factor with a fixed value assigned per direction is identical on all three P words. All endpoint-derived native BRC summaries coincide. This proves completeness.

### Proof: equivalence of AABAA and ABAAA for arbitrary finite futures

Call these two P words \(P_1=AABAA\) and \(P_2=ABAAA\). Their original prefix lengths 4 and 5 have (respectively) the **same directed-edge histograms**, endpoint displacement, letter counts, and last letter A between the two histories:
\[
J(P_1[1:4])=J(P_2[1:4])=\{AA,AB,BA\},\qquad
J(P_1)=J(P_2)=\{AA^2,AB,BA\}.
\]
(The displayed prefix \([1:4]\) is inclusive and has length four.)

At every point in any legal common future trace, each word is its *surviving original prefix followed by an appended-letter suffix*. Since P initially ends with AA and no operation can singly pop P, a synchronized CANCEL can delete **at most one original P letter**: deleting two original P letters would require its original final AA to be an inverse pair. Consequently the surviving original P prefix always has length at least 4. Since Q initially is AAAAA, its CANCEL similarly deletes at most one original Q letter, and its one independent POP deletes at most one further original Q letter; its original prefix always has length at least 3. These statements hold for any interleaving of APP/POP/CANCEL, irrespective of appended directions.

The only discrepancies between \(P_1\) and \(P_2\) are at **original positions 2 and 3**: \(P_1[2:3]=(A,B)\), \(P_2[2:3]=(B,A)\). Both positions survive. For every surviving P original prefix of length 4 or 5, the full marginal displacement, directed-edge histogram, last letter and any direction-local multiplicative factor agree; all appended letters are shared between the compared executions. Thus the P marginal observation and all subsequent APP adjacency increments agree. Q's entire word is identical under the same actions in both executions.

For K, original Q positions 1 through 3 always exist and equal A, hence P's differing positions 2 and 3 contribute exactly one coincidence in either execution. All P positions 1 and 4 onward are identical between the executions, including subsequently appended labels; all Q labels are identical. Therefore K agrees after every operation, even when lengths diverge by one and the position compared at the asynchronous boundary shifts.

Finally, before the one possible CANCEL, whenever P's terminal pair consists of original letters it is the same AA pair in both histories; whenever it includes appended letters, its relevant original terminal letter is A in both histories. After CANCEL the cancellation budget is exhausted. Hence CANCEL enabledness is the same in both. POP enabledness depends on the identical Q and its remaining budget. This proves indistinguishability for **every finite legal future** and for **all twelve native APPEND symbols**.

### Proof: separation of AAABA from the other two

Use the same legal trace in both compared histories:
\[
\mathrm{APP}(B,B);\quad\mathrm{CANCEL}.
\]
Initially both P and Q end in A; the appended B makes both terminal pairs \(AB\), so CANCEL is enabled. After cancellation P retains its first four original symbols. For \(AAABA\) this is \(AAAB\), whose directed histogram has \(AA:2,AB:1\). For \(AABAA\) and \(ABAAA\) it is \(AABA\) or \(ABAA\), whose directed histograms both have \(AA:1,AB:1,BA:1\). Their new observable adjacency histograms differ. Hence these classes are distinguishable. The previous equivalence and complete enumeration prove the exact quotient.

## Native BRC computation and reproducibility

For all twelve signed native directions use the exact integer recurrence
\[
N_0(0)=1,\quad N_{n+1}(z)=\sum_{d\in\mathcal D}N_n(z-d).
\]
For typed positive branch weights \(w(+E_1)=2,\ w(-E_1)=3,\ w(d)=1\) otherwise, use \(W_{n+1}(z)=\sum_dw(d)W_n(z-d)\), separately from the negative signed word factor \(g(+E_1)=2,\ g(-E_1)=-3\).

For the present endpoints the exact results are
\[
N_5(3E_1)=105,\ N_5(5E_1)=1,\qquad
W_5(3E_1)=1040,\ W_5(5E_1)=32.
\]
The P signed word product is \(-48\) for all three histories. Counting the native five-step paths to \(3E_1\) gives 5 paths on axis 1 with 4A/1B and 100 additional paths with 3A and one matched non-first-axis inverse pair, hence 105. Positive weights produce \(5(2^4\cdot3)+100(2^3)=1040\).

\`REPRO_STAGE405B.js\` independently enumerates the full two-label Euler fiber, checks exact observer equality, executes the concrete separating trace, runs the complete native 12-direction integer BigInt BRC recurrence, and exhaustively compares finite continuation traces through **five actions** over APP symbols \(\{A,B,+E_3\}\). An independent Python integer implementation was executed over the same five-action depth, visiting **82,597** paired states and checking **91,322** transitions, giving \`STAGE405B_ASYNC_ONE_CANCEL_QUOTIENT_PASS\`. The unrestricted future/all-twelve-direction statement is proved above; the bounded computations provide test coverage rather than its logical basis.

## Reuse and next question

BRC reuse: \`REUSE_APPLIED\` to native endpoint count/typed weight recurrence, \`COMPOSE_APPLIED\` to the Stage404 residual-Euler complete marginal fiber and the Stage403 length-four sufficient-window frontier. The original two-source relationship K is preserved; the exact quotient improves the uniform suffix representation only for this precisely declared fiber.

**Stage406-B:** Determine a *general symbolic minimal key* for \(C=1\) from marginal directed-edge counts \(J_P,J_Q\), exact K, and feasible suffix transition signatures; identify whether a finite quotient algorithm can avoid enumerating complete source pairs. Test the boundary of the present argument when Q's original terminal pair becomes inverse (so paired CANCEL may delete two original Q labels), and investigate the resulting positional-alignment residual. Native Result and independent Driver acceptance remain separate.
