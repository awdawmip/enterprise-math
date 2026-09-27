# Antipodal quotient and the exact signed factor partition

Status: **PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Shared author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This proof uses the preserved conic and cyclic mark, not a numerical oracle. It adds no fixture to the current frozen probe.

Let N be odd and M=[[0,1],[-1,k]]. Write M^E v=(x,y) with v=(0,1). Since the integer companion preserves Q_k, its residue point satisfies

`x^2-kxy+y^2=1 mod N`.

Define three actual integer divisors from residue representatives:

`d=gcd(N,x)`, `g_minus=gcd(N,x,y-1)`, `g_plus=gcd(N,x,y+1)`.

Then, without any discriminant hypothesis,

`gcd(g_minus,g_plus)=1`, `g_minus*g_plus=d`.               (1)

## Proof with prime-power information retained

Modulo d, the conic identity gives y^2=1. Thus d divides (y-1)(y+1). Any common divisor of y-1 and y+1 divides 2, while d is odd. Each entire prime-power component of d therefore divides exactly one of y-1 or y+1. Consequently

`gcd(d,y-1)*gcd(d,y+1)=d`,

and these two gcds are coprime. They equal the definitions of g_minus and g_plus. This proves (1), including partial powers inherited from d; no factorization of d is an algorithm input.

The cyclic mark identifies g_minus with the complete M^E=I return divisor and g_plus with the complete M^E=-I return divisor. Indeed the two residual coordinates generate the ideal of all four entries of the corresponding residual matrix. When x=0 modulo a local prime power, the same cyclic identity makes M^E scalar, while determinant one forces that scalar to be one of the two local signs. Different components of N may choose different signs.

## A smaller factor-only readout

For an algorithm whose output is merely a proper factor, (1) yields a complete three-branch simplification of these two simultaneous-return observers:

1. If `1<d<N`, d itself is already a factor. No signed or trace gcd is needed to obtain a valid factor certificate.
2. If `d=1`, both signed common gcds equal 1. Neither signed return test can find a factor at this stage.
3. If `d=N`, compute `h=gcd(N,y-1)`. If h is proper, it splits the two local signs, and N/h is the opposite-sign factor. If h is 1 or N, every component chose the same sign and these simultaneous-return observations provide no proper factor.

The final division N/h and the gcd computations require their native receipts. A saturated d cannot be counted as failure before testing signs, and it cannot be counted as a factor. The y-only coordinate probe can have factors outside these simultaneous-return events and is a separate contract; this simplification does not claim to dominate every available single-coordinate probe.

The statement holds even for a degenerate discriminant, because it needs only oddness, the determinant-one conic, and the fixed cyclic basis. Local order promises and the trace-square lemma still require their own regularity hypotheses. This distinction prevents a setup exclusion from being mistaken for an algebraic failure of (1).

## Geometric and research interpretation

At each odd prime-power component, the x-coordinate detects return to the pair {v,-v}, which maps to the identity of the local antipodal quotient. Over a composite modulus, x=0 can have mixed local signs: the point need not equal either global v or global -v. Thus this observation must not be identified with a two-element orbit fold on the global residue set. In geometric language the projective image forgets an order-two unit in each component; the remaining y restores that fiber information. This is a precise instance of using a local geometric quotient while retaining the labels needed for a factor witness. It is the familiar sign-separation mechanism, here derived with exact composite-modulus ideals and valuations; it is not a new general factoring theorem or a free period finder.

The bounded native probe already computes all quantities in (1), so its saved output can later be reviewed against the identity without changing the source or rerunning the experiment. Actual use of the shorter early-stop observer would require a separately declared implementation and cost result; one may not retroactively subtract the executed comparison probes from its bill.

The main unsolved part is unchanged: obtain an exponent and geometric orbit whose antipodal return differs across unknown prime components often enough, at a justified total cost. The quotient/fiber proof supplies a lawful and cheaper selected observation, not that exponent-selection rule.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
