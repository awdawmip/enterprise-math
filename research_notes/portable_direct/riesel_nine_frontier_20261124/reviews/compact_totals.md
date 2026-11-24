# Shared-context check of the v14 compact-root total costs

This is collaborative mathematical checking by the two-tail task, not an
independent project Review. The inspected files were
`exact_total_v14/proof.md`, `verify_exact_totals.py`, and the saved native
certificate. No old full execution was rerun for this check.

The unrestricted lower-bound lemma is sufficient: m pairwise-coprime full
integer terms require m different covering primes. With a displayed
dictionary of size 20+s, this yields both tau=20+s and delta_P=s. The
private-position checks alone would not suffice; the script additionally
checks all pairwise gcds of the full terms, which is the needed assertion.

The upper covers are verified over the complete order periods, 20160 for
the cost-six, seven, and eight roots, and 60480 for the cost-nine root.
They cover index zero as well as every positive index. The lower-bound
terms have strictly positive indices. The bound a^2−1>max(dictionary)
ensures every selected prime divisor is proper. Thus the change between
positive and nonnegative indexing does not affect these four conclusions.

The native intervals end at the largest witness index and are not claimed
as complete covering periods. The exact periodic upper-cover verification
is separately performed by the phase calculator. This distinction is
present in both proof and certificate.

The retained certificate reports native execution enabled and PASS. The
four witness counts 26,27,28,29 sum to 110. Their pair counts
325,351,378,406 sum to 1460. The maxima 773,1133,2480,2048 sum to 6434
one-step updates; half-interval floors sum to 3216 two-step evaluations.
Multiplying each maximum by its dictionary size gives 179521 individual
prime readouts, and the joint readout and recomposition counts are each
6434. These values agree with the saved certificate and the script.

The fourth root agrees exactly with the present two-tail conditional
minimum. Its nine supplementary primes agree as a set with our recorded
dictionary. The prior three global-minimum scopes and the fourth
conditional-minimum scope are retained separately. None of the equality
proofs requires their classification proofs; only the minimum scopes do.

No mathematical correction was identified in these claims. The resulting
exact unrestricted totals are 26,27,28,29 for the four stated compact
roots. The companion source supplies the concrete integer witnesses and
their native execution records.
