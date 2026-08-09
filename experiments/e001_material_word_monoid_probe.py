"""Finite transformation-monoid probe for E001 material operator words.

The underlying fact that functions on a finite set form a finite transformation
monoid is established mathematics.  This experiment only measures how strongly
one small E001 operator alphabet collapses at different finite amplitudes.
"""

from enterprise_math.material_program import HARDEN, SOFTEN, MaterialOperator
from enterprise_math.material_word_quotient import material_word_signature


def compose(first, second):
    """Compose finite tables: apply ``first`` and then ``second``."""
    return tuple(second[value] for value in first)


def generated_behavior_count(amplitude, generator_words):
    generators = [
        material_word_signature(amplitude, word) for word in generator_words
    ]
    identity = tuple(range(amplitude + 1))
    seen = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            following = compose(current, generator)
            if following not in seen:
                seen.add(following)
                frontier.append(following)
    return len(seen)


def main() -> None:
    generators = (
        (MaterialOperator(HARDEN, 2),),
        (MaterialOperator(HARDEN, 3),),
        (MaterialOperator(SOFTEN, 2),),
        (MaterialOperator(SOFTEN, 3),),
    )
    print("amplitude,behavior_classes")
    for amplitude in range(2, 9):
        print(f"{amplitude},{generated_behavior_count(amplitude, generators)}")


if __name__ == "__main__":
    main()
