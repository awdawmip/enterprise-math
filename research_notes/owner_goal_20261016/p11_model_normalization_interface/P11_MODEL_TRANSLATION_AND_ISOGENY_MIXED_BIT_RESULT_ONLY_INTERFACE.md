# One mixed bit: models, translations and isogeny transport

Author EM-DVR-F73673. FROZEN UNREVIEWED bounded same-method-family RESULT_ONLY paper interface. This groups the separate degree clarification and the following isogeny consequences with the already independently assessed A/B model-normalization facts. It reuses Fisher's existing Cassels–Tate naturality, not a new pairing algorithm or external discovery. There is no Native RR, vote, shared Tool, new Task, computation or actual mixed bit. These papers are excluded from the active core98 Task and its actor's inputs and clocks. Its present scientific outcome is not assumed.

## 1. Precisely which result is being reused

For elliptic curves over a number field K, write S(E)=Sha(E/K) and b_E for the elliptic Cassels–Tate pairing using the canonical principal polarization. All objects here are external classical group/cohomology objects. For an actual K-isogeny phi:E->E', its actual dual phihat:E'->E satisfies phihat phi=[d] and phi phihat=[d], where d=deg(phi). Fisher, Higher descents on an elliptic curve with a rational2-torsion point, Section3 Theorem3.1(i), states

    b_E'(phi*x,z)=b_E(x,phihat*z).

Its Theorem3.1(ii) states that the image of an isogeny on Sha is the orthogonal complement of the kernel of its dual. Fisher explicitly says these facts do not depend on finiteness of Sha. These existing results, and ordinary bilinearity, are the entire duality input below. They are not attributed to the author's new proof or to an unread implementation.

The local primary is Fisher_Higher_Descents_author_primary.pdf,411230B SHA256784c3ccf22bfe312f25237603ea8deb35565aac1018c9bb96ed1f9f4e4f2a129, author version dated2015-09-10; the actual Section3 Theorem3.1 is on printed page6. The theorem and following proof have been personally read from the already retained exact primary text. This does not claim that all30 pages or the publisher-rejected SD13 full text have been read. No new provider call or arithmetic program was used.

## 2. Degree parity under the SAME isogeny

Let x in S(E)[4], y in S(E)[2], and set b=b_E(x,y). Bilinearity gives2b=b_E(x,2y)=0, hence b is0 or1/2. For the SAME actual isogeny on both arguments, naturality gives

    b_E'(phi*x,phi*y)
       = b_E(x,phihat phi*y)
       = b_E(x,[d]y) = d*b.

Consequently an odd-degree simultaneous transport preserves this bit, while every even-degree simultaneous transport has value0. An even-degree isogeny is therefore not a replacement for a pointed same-E identification when retaining this particular bit. If the original value is1/2, both-images transport loses it. This is a conditional information-loss statement, not an assertion that the actual core98 value is nonzero. The actual self-isogeny[2] illustrates the identity: it has degree4 and sends y to0, so its transported pairing is0 whatever b was.

At odd d, phi is also an isomorphism on the2-primary parts of Sha. Multiplication by odd d is an automorphism on every2-primary torsion group: each finite-order element has a unique preimage under[d]. The inverse to phi is[d]^-1 phihat, since both compositions are identity. No finiteness of the whole2-primary group is needed. This does not exhibit any isogeny or solve a torsor-identification problem from numerical curve invariants.

If DIFFERENT actual maps phi,psi:E->E' are used for the two entries, the correct formula is instead

    b_E'(phi*x,psi*y)=b_E(x,phihat psi*y).

The degree of either map alone does not determine this scalar. Neither a common isogeny class, a shared j-invariant, an untyped map printout nor the parity rule just proved supplies the missing dual-composition identity. Model identifications and domains must be recorded individually.

## 3. The correctly typed dual-lift route

Suppose an actual y' in S(E') satisfies phihat*y'=y. Then

    b_E'(phi*x,y')=b_E(x,y).

Unlike simultaneous transport of both entries, this route retains the value at every degree. Two such lifts differ by k in K0=ker(phihat:S(E')->S(E)); naturality gives b_E'(phi*x,k)=b_E(x,0)=0. Thus the scalar is independent of the chosen valid dual lift. This assertion neither constructs a lift nor assumes that an arbitrary locally soluble curve with Jacobian E' is that lift.

Fisher Theorem3.1(ii), applied to phihat, gives the exact abstract existence condition

    y in im(phihat) iff b_E(y,t)=0 for every t in ker(phi:S(E)->S(E')).

The quantifier is over the actual full kernel on Sha, not merely the rational geometric kernel of the curve isogeny, nor a few selected Selmer classes. No such full kernel or orthogonality calculation is supplied here. Treating this condition as automatically satisfied would invent a dual lift.

There is a second type issue if an evaluator accepts a four-cover and a TWO-cover. Although phi*x is killed by4, a lift y' of y need not be killed by2. A general dual lift is therefore insufficient for that particular API. Since y is killed by2, 2y' belongs to K0. The coset

    o_phi(y) = 2y' + 2K0 in K0/2K0

is independent of the chosen lift: replacing y' by y'+k adds2k. Moreover o_phi(y)=0 iff a lift killed by2 exists. Indeed if2y'=2k for k in K0, then y'-k is killed by2 and still maps to y. Conversely a killed-by2 lift makes the coset zero. This is a group-theoretic obstruction with a complete proof, not a computed certificate or an executable new algorithm. Computing it requires a certified full K0 and an actual lift or another rigorous construction; both are presently unspecified here.

For an isogeny of degree2, K0 is killed by2 because phi phihat=[2], so2K0=0 and the obstruction is the actual class2y' in K0. It cannot be removed by changing the lift inside that fibre. Any such y' is killed by4. An available order-four lift does NOT meet the second-two-cover hypothesis merely because its image y has order2. At odd degree the2-primary inverse above supplies the unique killed-by2 lift, but still only after the maps and y have actually been identified.

## 4. One reusable interface, with proof and observation kept distinct

The already separately assessed A/B facts are reused at their exact scopes. For the split-real cubic with three rational roots, actual pointed same-Jacobian identifications differ by signs; a half-valued mixed scalar is sign-independent. Rational target translation changes a finite Selmer label by a rational-point Kummer class and leaves its Sha image unchanged. Under the full first-form-zero hypothesis, the weaker stated Sha-level lower-lift relation suffices for the intended mixed scalar. None of those conditional facts exports an actual curve isomorphism, local points, lift or evaluator.

Full n-cover maps TO E have degree n^2. The separate frozen degree clarification expressly corrects the earlier untyped degree2/degree4 phrase; two-/four-cover maps to E have degrees4/16. A four-to-two factor, when a compatible factorization is actually proved, has degree4; a quartic's hyperelliptic projection goes to P1 and normally has degree2. Embedding/model degrees do not supply covering-map degrees. The old A source and its true narrow independent verdict are preserved rather than silently rewritten.

An admissible mathematical transport certificate for this interface must therefore name: actual curves and polarizations; actual isogenies or pointed isomorphisms with their sources/targets and verified identities; the actual locally soluble Sha classes and stated order bounds; and one of the following relations: SAME odd-degree transport, or an actual dual lift with its required order bound. If using a weaker pairing-annihilated discrepancy, that annihilation must itself be proved. The theorem gives a conditional scalar equality, not permission to infer these inputs from a library's type name.

Failure/UNKNOWN stops include an even-degree simultaneous transport offered as a nonzero-bit certificate; unequal maps without the required dual-composition relation; a lift only in the wrong torsion subgroup for the evaluator; a missing full-kernel hypothesis when invoking the existence criterion; or missing actual model/local/class evidence. A valid even-degree transport with value0 does not prove that the original bit was0. A successful conditional transport says nothing about numerical rank until a separate correct rank theorem's hypotheses hold.

This one bounded interface groups standard same-family model/translation/isogeny consequences and the explicit dual-lift order obstruction. It is not several independent discoveries or a newly registered Tool. Existing A6363B and B9244B Sourceef9bca0d7cf6bd2ce79e5e8fbf39d13efb6fd167 remain unchanged; their independent reports are Source5e1052833bbc3c88ad21f3b2338835a9d5542a53. Their PASS does not review this new isogeny proof or supply missing inputs. A genuine new nonauthor assessment is required for this grouped extension. No current Task input, runtime, resource or claim changes; old233 STOP and the five accepted old Tasks remain unchanged. Actual core98 e/rank remain UNKNOWN here. Parent remains OPEN.
