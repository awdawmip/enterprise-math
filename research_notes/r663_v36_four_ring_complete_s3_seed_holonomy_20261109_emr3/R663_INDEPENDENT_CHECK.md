# R663 independent verifier: V17 slot transport as position pullback composition

The primary `R663_VERIFY.py` propagates labels directly through the old/new member dictionary. This independently structured verifier instead assigns to each legal transition `S→T` a permutation of **position indices** `p_{S,T}`: each new sorted position pulls its old index from the unchanged member, while the new member pulls the vacated member's old index. It accumulates the compositional group element `h ← h ∘ p_{S,T}` for the same length-four closed triad words.

The local standard-library run returned `R663_INDEPENDENT_GROUP_FACTOR_CROSSCHECK_PASS` and exactly the same six integer counts `207/48/48/48/9/9` over 369 words. This verifies the group action with a structurally distinct implementation, not an independent mathematical reviewer or a V29 native TRANSFER execution. No extra floating-point/trigonometric computation or physical model was used.
