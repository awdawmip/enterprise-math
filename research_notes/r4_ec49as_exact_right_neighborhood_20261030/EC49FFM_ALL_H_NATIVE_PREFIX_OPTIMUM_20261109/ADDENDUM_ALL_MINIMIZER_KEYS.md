# EC49FFM addendum — All attaining full BRC keys; quantized excess penalty

This is a direct analytic consequence of the four-low-signature native prefix proof in README_EC49FFM.md. Same original six signed X6 operations and nine-state observer; frozen scientific source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Strong key-specific lower bound

For ANY legal complete key K=(x,y,z), at one window h with all four low signatures 1,2,4,8 realized, define d=#c+#d=x+y-h-1 >=1. Every path has common signed-native microstep length

L=2(x+y+z-1)=2(h+d+z).

The two prefix lemmas give the sharper exact key-specific statement

**C_native(h,K) >= 2L+8 = 4(x+y+z+1) = 4h+16+4(d-1)+4(z-1).**

In particular every z>=2 key and every d>=2 key has C_native>=4h+20. At H10 these keys cost at least 60 edges; the previously computed z=1,d=1 family achieves 56.

## Complete characterization of every globally minimizing full key (all h>=4)

**The only keys admitting 4h+16 edges are K=(x,h+2-x,1) with x=4,5,...,h. There are exactly h-3 of them.**

Proof. Equality with 4h+16 in the key-specific lower bound requires d=z=1, so x+y=h+2 and

#f=h+1-y-2z=x-3, #g=h+1-x.

Equality in the prefix-count lower bound also requires exactly TWO different first native signed microsteps among the four witnesses. Since output 4 forces +E1 and output 1 forces +E2, these two are precisely +E1 and +E2. The exact observer reachability after a first operation is:

a->{2,8}, c->{4}, d->{1}, e->{2,8}, f->{2,4}, g->{1,8} (only low signatures shown).

To realize output 2 using only initial +E1 or +E2, the first operation MUST be f (starts +E1). To realize output 8 using those same initial steps, the first operation MUST be g (starts +E2). Consequently #f>=1 and #g>=1. With d=z=1 the displayed count identities imply x>=4 and x<=h.

Conversely for every such x the four explicit f/g-leading and c/d-ending words in README_EC49FFM attain 4h+16. This proves both directions. Boundary cases x=3 and x=h+1 (when otherwise count-legal) cannot attain the global minimum; x=3 lacks f and x=h+1 lacks g.

## Earlier exact-data crosscheck

The pre-existing independently enumerated H4-H8 130-key table in EC49FFJ, and the H9 70-key table in EC49FFK, have minimum-attaining keys exactly matching this analytic all-h classification: 1,2,3,4,5,6 keys for h=4,5,6,7,8,9 respectively. The new proof establishes the infinite result without extrapolating that finite computation.

The mother multiwindow <=5-key/<=93-edge problem remains open. The excess penalty is key-local: it may not be summed across overlapping keys/windows without a valid signed-prefix disjointness argument. Independent Driver review and formal Source Result admission pending.
