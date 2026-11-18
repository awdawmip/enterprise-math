# EC49FFE — exact 24-word H3-low BRC inventory census and order-residual witness

Date: 2026-11-09. Status: **AUTHOR FINITE PROOF / EXECUTED STANDARD-PYTHON CHECK / UNREVIEWED / NOT SOURCE-ADMITTED**.

**Frozen science** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original six signed-X6 primitive operations, original nine-state DFA and strictly positive full BRC keys `(x,y,z)`; native cost counts distinct nonempty **ordered signed six-axis microstep prefixes**. Behavioral rules read at their current main, separately from this science pin.

## A. Exact finite scope

At H2 and H3 request the full low signature set `L={1,2,4,8}`. Exactly four of H4–H9 request both high labels `B={16,32}`; the remaining two request all four low labels. One path per `(h,label)` requires **24 paths** and at most five complete full BRC keys. The present theorem classifies signature-quota feasibility, and separately checks a 106-edge legal construction; **106 is not claimed as a minimum**.

## B. Structural proof

By the EC49FFD full-key staircase, `K=(x,y,z)` has terminal high horizon `H=x+y-1` and low coverage exactly the integer interval `H-min(x-2*z,y) <= h < H`. A full-high horizon `h` needs one distinct key with `x+y=h+1`, `x>2z`, `y>0`; eligible keys are `(2*z+f,g,z)` with `z,f,g >=1`, `f+g=h+1-2z`. There are exactly `floor((h-1)^2/4)` such keys.

**H2 low forces K3=(3,1,1)**: its only low-label count solution has `z=1, #c+#d=1, #f=#g=0`. Hence four distinct late high keys plus K3 exhaust five keys. H9 must be high: otherwise the other four keys have terminal horizon at most H8 and K3 terminates at H3, so none can emit low at H9. Therefore all feasible patterns have high windows `{9,a,b,c}` where `{a,b,c}` is a three-element subset of `{4,5,6,7,8}`.

For every such high quadruple, enumerate the Cartesian product of its eligible high keys; adjoin K3 and test full-low feasibility at all other late horizons by exact interval containment. The EC49FFD explicit DFA-word construction proves the test is sufficient; the staircase proves necessity. Thus this is a complete finite proof over the stated 24-word family, with no optimization of native cost assumed.

## C. Exact outcomes

Ten high-window templates contain **36,288** typed full-key inventories: **12,276** signature-feasible and **24,012** infeasible, with nine templates admitting at least one feasible inventory. Full per-template counts: [`EXACT_REPORT_EC49FFE.json`](EXACT_REPORT_EC49FFE.json). The `{6,7,8,9}` high-window template has zero feasible inventories because the earliest low horizon of any full-high key with high endpoint H6 or later is H4 or later, leaving the required H3 low labels unsupported.

**Novel equivalence at the signature-inventory level:** the feasible inventories coincide with the 12,276 type-B (and mirrored type-C) EC49FEQ H3-mixed23 inventories. H2 already forces K3, which supplies high 16/32 at H3. Any other key that supplies one H3 low signature necessarily supplies *all four* H3 low signatures by the staircase. Thus the H3-mixed23 condition and H3-full-low24 condition are equivalent for the same four late-high windows and five-key scope. This equivalence does **not** identify their native costs or path counts; it avoids repeating an already classified cache-inventory search.

## D. Exact ordered-native witness

Choose high horizons H4,H6,H8,H9 and full-key inventory `{(3,1,1),(3,2,1),(3,4,1),(3,6,1),(3,7,1)}`. One signed-X6 legal 24-word system is:

```json
{"2":["de","ed","ce","ec"],"3":["deg","edg","ceg","ecg"],"4":["fegg","gefg"],"5":["deggg","edggg","ceggg","ecggg"],"6":["fegggg","gefggg"],"7":["deggggg","edggggg","ceggggg","ecggggg"],"8":["fegggggg","gefggggg"],"9":["feggggggg","gefgggggg"]}
```

The exact original DFA, full-key count identities, signed microsteps and native endpoints `(2,0,0,0,0,0)` are rechecked in [`VERIFY_EC49FFE.py`](VERIFY_EC49FFE.py). Its total distinct signed-native nonempty prefix count is **106**.

Replacing only H3 signature-8 word `ecg` by `gec` preserves its full key `(3,2,1)`, horizon, terminal DFA label 8 and X6 endpoint, and preserves all other paths and signatures; the native prefix count rises to **109**. This is an explicit **3-edge path-order residual**. Thus an interval/signature abstraction is a lossless *quota oracle* but not a lossless native-cost state; original microstep order must remain in cost optimization.

## E. Actual computation, evidence and provenance

Run `python3 VERIFY_EC49FFE.py > /tmp/EC49FFE.json` using Python standard library only. Locally executed run: `EXACT_PASS`; ten templates; 36,288 / 12,276 / 24,012 inventories; legal 24-word witness 106; one-word order variant 109. A separately implemented JavaScript integer enumeration independently reproduced the ten-row census before publication. Published source and report are stored here and read back from immutable GitHub blobs; no raw Solver/LP assumption enters the signature census.

Dependencies: exact original operation semantics `EC49FFC` at `2dd856c416f111d90d523dcb10cde952248ec814`; observer staircase `EC49FFD` at `df0dbc54707a6926db858631e5a03fea189dccde`; comparison H3-mixed23 `EC49FEQ/FET`; immutable science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 / ACTIVE worldview unchanged. **This author proof has no native CLAIM, formal Result, independent Driver mathematical admission or physical transfer.**

## F. Next discriminating scientific unit

On the 12,276 H3-full-low 24-path feasible inventories, run an exact **signed native-prefix cost lower-bound filter** using the existing depthwise packing and group-aware rational integer-dual methods. The immediate target is either a concrete <=93-edge valid full-key construction, or verified exclusion for a precisely stated subset; avoid redoing the 12,276-item signature enumeration. The present 106-edge construction is a bounded upper witness for one inventory, not a mother-objective improvement over the existing 94-edge witness.
