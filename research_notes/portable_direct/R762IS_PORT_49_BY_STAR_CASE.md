# R762IS — Sharpen the k=0 six-axis Port-Euler kernel to 49 events

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_STAR_CLASSIFICATION / NOT_REVIEWED.
Frozen scientific source: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R762IR at Draft PR #2946; same scientific model, no redefinition or new Task authority.

## Theorem

On the fixed six-axis composite Port graph with 20 support triangles, suppose each multiplicity satisfies n_S in {0,1,2,3}. If there is a connected even-degree Port multigraph realization, then there is one with the **same active Port set**, designated start Port, positive support types and per-support parity, with total event count at most **49**.

This improves R762IR's 50-event bound by resolving its unique exact terminal equality case. The overall k>0 theorem (support counts of four or more) retains its separately established bound and is not changed.

## Equality-case reduction lemma

Consider ANY legal 50-event history with exactly ten supports of multiplicity 3 and the other ten of multiplicity 2. At least one of the three-event supports can be reduced to one without violating any retained observer or Euler circuit condition, producing a 48-event witness.

Let F be the family of its ten 3-event support triangles. Supports whose three Ports are not all active can immediately be reduced from 3 to 1 on their sole allowed edge (all three assigned events are forced onto that edge; their degree parity is unchanged, and the same edge remains). Hence assume all ten triangles have all three Ports active.

If some triangle of F is connectivity-redundant in G_F (the union of these full support triangles), apply R762IR's connected-three-event GF(2) path correction to remove two of its events. This preserves the full active set and connectivity.

The only other case is that ALL ten full triangles are connectivity-essential. The finite 10-subset theorem in R762IR (verified exhaustively over C(20,10)=184,756 labeled subsets by two independent exact programs) classifies these families: there are exactly six, and each is the complete star
  F_a = {S subset {0,...,5}: |S|=3, a in S}
for one fixed axis a. This classification can also be read directly from the six verified integer masks in R762IR_EVIDENCE.json.

There are five spoke Ports {a,i} with i != a and ten outer Ports {i,j} with a not in {i,j}. Each of the ten triangles F_a has exactly one unique outer Port ij, plus the two spoke Ports ai and aj. After omitting ANY one star triangle j={a,i,j}, the remaining nine full triangles form a connected Port graph on precisely the other fourteen Ports (five spokes plus nine outer vertices), with the selected outer Port ij isolated in that triangle union. This is immediate because the star triangles join the spokes according to K_5 with one edge removed and attach each of the other nine outer Ports to its incident spokes. An exact 60-case finite check verifies every axis-star deletion.

All ten other supports are triples formed from the remaining five axes and have multiplicity 2. Every event of these supports joins two outer Ports. Fix any actual event edge e from any one of these supports and let ij be one of its endpoints. Choose the corresponding star triangle j={a,i,j} for reduction; the other endpoint of e is a different outer Port and so belongs to the connected fourteen-Port core after deleting j. Thus ij remains connected to the core through the unchanged edge e.

To preserve even degree, let d be the GF(2) boundary vector of the OLD three named events of support j. Write u=ai, v=aj, w=ij. Choose the ONE surviving edge f as follows:
- if d_w=0, choose the spoke-spoke edge uv;
- if d_w=1, choose the spoke-outer edge uw.
The parity boundary of f matches d at w. Therefore the difference (d XOR boundary(f)) is either zero or the pair-boundary e_u XOR e_v. Since all five spoke Ports are connected by the remaining nine full star triangles, this difference lies in their edge-incidence GF(2) span.

As in R762IR, every surviving three-event full triangle independently realizes any of its four even-parity boundary vectors **with all three local Ports connected**: the zero vector is realized by one copy of each of its three edges; a nonzero pair boundary by one copy of the desired pair-edge plus two copies of a different edge. Transport the needed delta along a spoke-to-spoke path in the nine-triangle union and change those three-event allocations accordingly. Other supports retain their old event edges.

The resulting graph has even degree everywhere. The nine surviving full-triangle supports furnish a connected fourteen-Port core; the unchanged two-event edge e keeps the remaining outer Port w connected to it; all prior active Ports remain active. The reduced support j still has one legal event, the support set is unchanged and all counts retain parity. A connected even-degree graph admits an Euler circuit from any original start Port. Total number of events is 48, proving the lemma.

## Derivation of the uniform 49 bound

Start with any legal input with n_S in {0,1,2,3}. Apply R762IR's general 11-three-event support reduction until at most ten supports have multiplicity 3, never changing the observed active set, start, parity or positivity.

For t<=10 three-event supports, and at most 20-t other supports each of multiplicity at most 2,
  sum_S h_S <= 3t+2(20-t) = 40+t <= 50.
If the inequality is strict, the total is at most 49. If equality holds, necessarily t=10, every one of the other ten supports has count exactly 2, and all 20 supports are present. The equality-case reduction lemma just proved gives a 48-event witness. Thus in all cases some witness has at most 49 events.

## Verification and evidence

Reused exact R762IR exhaustive 10/11-family enumeration and independent 2^20-family scan on the identical fixed triangles. The six all-essential ten-subset integer masks are:
  1023, 64527, 466033, 746898, 895652, 971592.
They correspond exactly to the six axis stars. A separate exact Python integer DSU check explicitly iterated all 6 center axes times all 10 star deletions and confirmed that the other 14 Ports are connected and the omitted outer Port is isolated: PASS for 60 cases. This last check is provided as the compact standalone script R762IS_STAR_CORE_CHECK.py.

The mathematical parity adjustment and connectivity argument is symbolic for all assignments of the named events, and the finite star classification has exhaustive replay code. The 49 bound is computer-assisted only in the stated small fixed-hypergraph classification, not an unbounded computational extrapolation.

## Remaining scientific questions

- Can the k=0 bound be lowered to 48 by resolving all 49-event boundary histograms, notably n3=9 / n2=11 and n3=10 / n2=9 / n1=1, with active-set and parity preservation?
- What is the actual optimal k=0 worst-case kernel size? A bound is not a lower-bound witness.
- Analyze k>0 four-event critical supports separately for the whole model.
- A signed native P000 TRIADIC_CLOSURE_E Cell/Link/time/rotation/force lift with residual conservation is a separate typed obligation.

Researcher: independently registered service-issued EM-DIRECT-CF96E0; Activity RA-EC47D4352B8B5C5025399F00. This is portable author evidence; the prior R762IQ researcher is historical provenance, not an assumed current shared Task CLAIM. Independent mathematical Review=NOT_REVIEWED.
