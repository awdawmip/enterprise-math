# Adjacent traces restore the companion's primitive return ideal

Status: **PURE_SYMBOLIC_INTERFACE_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Shared researcher context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This is a successor to the frozen free-trace comparison, not an edit or rerun of that experiment.

Let N be odd, M=[[0,1],[-1,k]], and let Delta=k^2-4 have a paid unit certificate. Put V_n=tr(M^n), and let epsilon be +1 or -1. Define

`tau_epsilon=V_E-2*epsilon`,

`w_epsilon=V_(E+1)-epsilon*k`.

For the fixed cyclic mark v=(0,1), write `(x,y)=M^E v-epsilon*v`. Then

`gcd(N,tau_epsilon,w_epsilon)=gcd(N,x,y)`.                 (1)

This retains prime-power valuation; using only tau_epsilon need not do so.

## Linear ideal proof

The commuting signed residual B=M^E-epsilon*I satisfies

`B=[[y-kx,x],[-x,y]]`.

Taking its trace and the trace of M*B gives

`tau_epsilon=2y-kx`, `w_epsilon=k y-2x`.

Thus the map from (x,y) to (tau_epsilon,w_epsilon) has coefficient matrix

`[[-k,2],[-2,k]]`, with determinant `4-k^2=-Delta`.

It is invertible over Z/NZ by the paid regularity hypothesis. The two generated ideals are equal, proving (1), including every prime-power component. An implementation need not compute the inverse matrix. If Delta is nonunit, its actual setup factor/degenerate branch must be kept; no ideal equality from an unproved inverse is allowed.

The translated trace w supplies the derivative information lost by the symmetric trace quotient at return. This is the conic counterpart of retaining a translated Kummer coordinate on an elliptic curve. It is a use of standard Lucas/trace identities through a native observer contract, not a claim of global mathematical originality.

## A shorter intended native power program

The adjacent pair can be propagated without a full matrix or coefficient U_n. Start with `(V_0,V_1)=(2,k)`. For a public binary prefix n, the exact identities are

`V_(2n)=V_n^2-2`,

`V_(2n+1)=V_n V_(n+1)-k`,

`V_(2n+2)=V_(n+1)^2-2`.

For a zero bit compute the first two expressions; for a one bit compute the last two. Only one of the two squares is needed per bit. Each bit therefore requires two modular multiplications and two modular subtractions, plus declared branch/control work. All constants, setup, readout gcds, proper-factor divisions and proof/validation work remain paid. These are intended interface counts, not measured native digit costs or a benchmark.

After the pair is evaluated, the complete signed primitive-return observer uses (1). A factor-only contract may also retain individual proper gcds, but they can have a different event from simultaneous return. No witness is inferred merely from a saturated single trace.

Compared at the symbolic program level, this avoids some products present in the frozen two-coefficient power recurrence. Actual BRC digit cost depends on operands, reductions and the readout contract. A successor needs its own source, plan and execution; the frozen comparison's actual bill must remain unchanged. The existing primary implementation audit already identifies adjacent Lucas values and their doubling/differential formulas, so this is classical recurrence reuse, not a new exponentiation algorithm.

## Remaining selection problem

The repair does not change the complete matrix-return event at any fixed regular k,E. On squarefree N it cannot improve the factor returned by the single regular trace merely through valuation preservation. It can make the native representation/observer smaller and preserve depth at repeated factors. A useful factor-blind exponent and parameter rule, with failure probability and all costs, is still required for general factoring or a native Shor endpoint.

No native adjacent-trace program was executed for this note, and no numerical outputs were produced.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
