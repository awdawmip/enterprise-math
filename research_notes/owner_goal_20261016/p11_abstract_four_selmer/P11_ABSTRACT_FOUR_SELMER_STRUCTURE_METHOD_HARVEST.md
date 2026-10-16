# Method harvest: the abstract four-Selmer group from a full two-Selmer pairing

Status: UNREVIEWED DERIVED METHOD COROLLARY, object 12 of the same P11 classical descent family. EM-DVR-F73673. This extracts the exact-sequence mechanism used in the eleventh fixed-core paper; it is not an additional independent discovery, registered shared Tool, executed four-descent, new Task or Native Result. Both frozen objects require genuine nonauthor review before this new corollary is treated as reviewed. Earlier paper verdicts are not transferred.

## 1. Typed input and precise output

Let E/Q be a classical elliptic curve with full rational two-torsion, in the retained full Kummer model. Suppose the full two-Selmer space W and its genuine pulled-back Cassels–Tate pairing have been determined. Write

nu=dim_F2 W,
rho=rank_F2(full Cassels pairing on W),
k=dim_F2 delta_2(E[2](Q)).

The pairing rank rho is even. It must be the **full** Cassels rank: a compatibility rank from the tenth paper or a vertical restriction of unproved full coverage is not this input. The value k is actual rational two-torsion Kummer image dimension, not automatically two for every split curve.

Import the standard theorem that im(pi:Sel⁴→Sel²) equals the full Cassels–Tate radical, with pi induced by [2]:E[4]→E[2]. This is stated for n≥2 in Shukla–Stoll2302.01640v1, Introduction/PDF pages 1–2, without a Sha-finiteness premise. As in the eleventh paper, that theorem is an explicit classical input, not a conclusion from bilinearity alone.

The derived abstract structure is

Sel⁴(E/Q) ≅ (Z/4)^(nu−rho−k) ⊕ (Z/2)^(rho+k).

In particular

|Sel⁴|=2^(2nu−rho−k),
|2Sel⁴|=2^(nu−rho−k).

These are group-theoretic theorem outputs. They do not specify any generators, four-cover coefficients, local lift certificates, Mordell–Weil rank or full Sha group. No scientific program or rank/point enumeration is run by writing or consuming the symbolic formula.

## 2. Exact kernel, with the local condition checked

For i:E[2]→E[4], the module sequence

0→E[2] --i-->E[4] --[2]-->E[2]→0

identifies the kernel of i on H¹(Q,E[2]) with K0=delta_2(E[2](Q)). Thus its restriction to W has kernel K0 of order 2^k. Every element of K0 is a rational Kummer class, so lies in the radical of the full pairing.

The identities i(delta_2(P))=delta_4(2P) and pi(delta_4(P))=delta_2(P) hold globally and at every completion. They give i(W)⊂Sel⁴ and pi(Sel⁴)⊂W. Moreover ker(pi on Sel⁴)=i(W): if i(a) is four-Selmer, its localization is delta_4(P_v); applying pi gives P_v=2Q_v, so a_v differs from delta_2(Q_v) by an element of the local connecting image delta_2(E[2](Q_v)). It is therefore two-Kummer at every place, and a is in W. This proves the local/global kernel assertion rather than merely invoking exactness of unrestricted cohomology.

Let R be the full Cassels radical, of dimension nu−rho. The imported lifting theorem now gives the exact sequence

0→W/K0 --i-->Sel⁴ --pi-->R→0.

Consequently |Sel⁴|=2^(nu−k)·2^(nu−rho). It is finite and killed by four, independently of any finiteness conjecture about all Sha.

On E[4], i composed after pi is multiplication two. Hence

2Sel⁴=i(R).

Since K0 is contained in R, the kernel of i restricted to R still has dimension k. It follows that |2Sel⁴|=2^(nu−rho−k). Nonnegativity of this exponent is also forced by K0⊂R; it is not an extra unverified rank inequality.

## 3. Finite exponent-four classification

Write the finite group killed by four as (Z/4)^a⊕(Z/2)^b. Its doubled subgroup has size 2^a, so a=nu−rho−k. Its total size then gives

2a+b=2nu−rho−k,
b=rho+k.

This proves the structure formula. No explicit splitting or generator selection is asserted. In particular a statement that the abstract group has a certain number of order-four factors is not a certificate naming their four-cover representatives.

For the primitive P11 family, the accepted no-rational-four-torsion boundary makes delta_2 injective on E[2](Q), so k=2. Its exact specialization is

Sel⁴ ≅ (Z/4)^(nu−rho−2) ⊕ (Z/2)^(rho+2).

That no-four-torsion fact is already in the old accepted return and Driver review; no new Fermat proof is supplied or counted here. At the eleventh core (9,8), k=2 is also directly certified by the two independent classes U_(−1),U_17.

As a conditional substitution of already separate inputs, nu=4,rho=0,k=2 gives (Z/4)²⊕(Z/2)², exactly the eleventh abstract result. No new parameter is evaluated here. Any use of another curve's nu or rho still requires its own complete input proof; the formula does not create those values.

## 4. Composition with the existing method family

The tenth exact joint kernel, once genuinely reviewed and source-bound, can supply nu through its actual Legendre matrices and can decide whether the vertical space is the full Selmer group. The ninth finite vertical formula can supply the full rho only if that coverage is proved, or if the missing nonvertical pairings are separately supplied. The matrices M/K in the tenth compatibility theorem are not Cassels matrices and cannot be inserted as rho.

When the nonvertical quotient is nonzero and only a restricted Cassels matrix is known, the exact rho input is missing. The abstract four-Selmer structure is then UNKNOWN at this interface. One must preserve that boundary rather than silently select the lower restricted rank. A nonzero vertical restriction remains useful for its separately justified rational-rank bound, but it does not fill the missing full-rank argument.

This is a composition within the same full-Kummer/local-image/Cassels method family, not a proposal for another tool family. The current fixed-(233,119) Task requires its own admitted per-place certificates and actual scientific invocation; no abstract Sel⁴ formula substitutes for those outputs, resumes the stopped actor or restores the exhausted preparation budget.

## 5. Source strength and limits

The primary kernel/image input and n-Kummer exact sequences are in the actually read Shukla–Stoll arXiv:2302.01640v1 Introduction/PDF1–2, exact PDF SHA256f84fee9a3cd3e2e37aee1c0b41f08296e88988a5f1142c5911b4d16762e408ce. Its full comparison with the exact FSS0710.2079v1 pairing identifies the full-descent pairing used by P11 with the pulled-back Cassels–Tate pairing. The retained Stoll2001 split model supplies the earlier Kummer conventions. No new full Git publication of those local PDFs, general-duality proof, or independent reading of all Poonen–Stoll references is claimed. The standard lifting theorem is explicitly imported at its stated number-field/elliptic scope; a reviewer may challenge that exact theorem binding separately from the elementary group calculation.

The eleventh fixed-core paper is a frozen author input whose own review/source status must be kept distinct. The present proof restates the needed global/local kernel derivation so that its general cardinality formula is checkable as a separate method corollary, not an inference from a numerical example. It claims no historical novelty or additional independent research count.

Missing or false full Selmer dimensions, a merely restricted zero form, a wrong pairing model, a missing lifting theorem, an unjustified local-kernel argument or the unproved substitution k=2 invalidates the corresponding output. No explicit four-cover, rational point, rational rank, saturation, odd-primary Sha, full Sha finiteness, parameter-family classification or Native acceptance follows. All curve/cohomology objects remain external classical arithmetic under Heartbeat X6, with no native-plane, physical-time, Working Truth or Foundation change. No scientific program, new Task, old Task reopening or budget extension is authorized by this corollary.
