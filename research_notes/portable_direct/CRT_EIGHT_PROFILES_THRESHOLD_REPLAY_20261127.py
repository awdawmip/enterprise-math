"""Count the reduced eight-profile domain without computing its spectra."""

from functools import cache
from itertools import combinations_with_replacement
import json
from math import comb


@cache
def rectangle_counts(max_rows, cols):
    """Counts of span-compatible triples for each positive height."""
    counts = [0] * (max_rows + 1)
    thresholds = list(combinations_with_replacement(range(cols + 1), 3))
    for first_a in range(cols + 1):
        states = [state for state in thresholds
                  if state[0] <= first_a <= state[2]
                  and (state[0] == 0 or state[2] == cols)]
        incoming = [tuple(i for i, prior in enumerate(states)
                          if all(x >= y for x, y in zip(prior, state)))
                    for state in states]
        counts_at_height = [int(state[0] == first_a) for state in states]
        for rows in range(1, max_rows + 1):
            counts[rows] += sum(counts_at_height)
            counts_at_height = [sum(counts_at_height[i] for i in choices) for choices in incoming]
    return tuple(counts)


def distinct_profiles(width):
    return sum(
        (-1) ** (rows + cols) * comb(width - 1, rows) * comb(width - 1, cols)
        * rectangle_counts(width, width - cols)[width - rows]
        for rows in range(width)
        for cols in range(width)
    )


def transpose(cutoffs):
    return tuple(sum(cutoff > col for cutoff in cutoffs) for col in range(len(cutoffs)))


def reverse_complement(cutoffs):
    return tuple(len(cutoffs) - cutoff for cutoff in reversed(cutoffs))


def attributes(cutoffs):
    width = len(cutoffs)
    full = (1 << width) - 1
    mask = sum((full ^ ((1 << cutoff) - 1)) << (row * width)
               for row, cutoff in enumerate(cutoffs))
    row_changes = sum(1 << row for row, (a, b) in enumerate(zip(cutoffs, cutoffs[1:])) if a != b)
    col_changes = sum(1 << (cutoff - 1) for cutoff in set(cutoffs) if 0 < cutoff < width)
    return mask, row_changes, col_changes


def fixed_points(width):
    words = [tuple(reversed(cutoffs)) for cutoffs in
             combinations_with_replacement(range(width + 1), width)]
    data = {word: attributes(word) for word in words}
    symmetric = [word for word in words if transpose(word) == word]
    central = [word for word in words if reverse_complement(word) == word]
    full_changes = (1 << (width - 1)) - 1

    def count_middle(a, d, possible_middle):
        ma, ra, ca = data[a]
        md, rd, cd = data[d]
        if (md & ~ma or a[0] > d[-1]
                or any(x > 0 and y < width for x, y in zip(a, d))):
            return 0
        count = 0
        for b in possible_middle:
            mb, rb, cb = data[b]
            if md & ~mb or mb & ~ma:
                continue
            if ra | rb | rd == full_changes and ca | cb | cd == full_changes:
                count += 1
        return count

    transpose_fixed = sum(count_middle(a, d, symmetric) for a in symmetric for d in symmetric)
    reversal_fixed = sum(count_middle(a, reverse_complement(a), central) for a in words)
    return len(symmetric), len(central), transpose_fixed, reversal_fixed


def count(width):
    symmetric, central, transpose_fixed, reversal_fixed = fixed_points(width)
    distinct = distinct_profiles(width)
    burnside_sum = distinct + transpose_fixed + reversal_fixed
    assert burnside_sum % 4 == 0
    orbits = burnside_sum // 4
    return {
        "width": width,
        "monotone_masks": comb(2 * width, width),
        "corner_pairs": (width + 2) * comb(2 * width, width) // 2,
        "span_compatible_triples": rectangle_counts(width, width)[width],
        "distinct_profile_triples": distinct,
        "transpose_fixed_masks": symmetric,
        "reverse_complement_fixed_masks": central,
        "transpose_fixed_triples": transpose_fixed,
        "reverse_complement_fixed_triples": reversal_fixed,
        "combined_fixed_triples": 0,
        "orbit_representatives": orbits,
        "subset_transitions_if_scanned": orbits * width * (1 << (width - 1)),
    }


if __name__ == "__main__":
    previous = count(7)
    assert previous["span_compatible_triples"] == 24665832
    assert previous["distinct_profile_triples"] == 1208040
    assert previous["orbit_representatives"] == 304170
    print(json.dumps([previous, count(8)], indent=2))
