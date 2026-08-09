"""Image-separation tests for safe shell-label erasure.

The mathematical content is elementary: an auxiliary shell label is
recoverable from a retained coordinate exactly when distinct shell images are
pairwise disjoint.  This module packages that test as a reusable executable
research tool.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Mapping
from typing import TypeVar

Label = TypeVar("Label", bound=Hashable)
State = TypeVar("State", bound=Hashable)
Image = TypeVar("Image", bound=Hashable)


def shell_images(
    shells: Mapping[Label, Iterable[State]],
    transform: Callable[[State], Image],
) -> dict[Label, frozenset[Image]]:
    """Return the realized image set of every labeled shell."""

    return {
        label: frozenset(transform(state) for state in states)
        for label, states in shells.items()
    }


def overlap_pairs_from_images(
    images: Mapping[Label, Iterable[Image]],
) -> tuple[tuple[Label, Label, frozenset[Image]], ...]:
    """Return all distinct label pairs with a nonempty image intersection."""

    normalized = {label: frozenset(values) for label, values in images.items()}
    labels = tuple(normalized)
    overlaps: list[tuple[Label, Label, frozenset[Image]]] = []
    for i, left in enumerate(labels):
        for right in labels[i + 1 :]:
            common = normalized[left] & normalized[right]
            if common:
                overlaps.append((left, right, common))
    return tuple(overlaps)


def overlap_pairs(
    shells: Mapping[Label, Iterable[State]],
    transform: Callable[[State], Image],
) -> tuple[tuple[Label, Label, frozenset[Image]], ...]:
    """Return all shell collisions after ``transform``."""

    return overlap_pairs_from_images(shell_images(shells, transform))


def label_recoverable(
    shells: Mapping[Label, Iterable[State]],
    transform: Callable[[State], Image],
) -> bool:
    """Whether the shell label is a function of the transformed coordinate."""

    return not overlap_pairs(shells, transform)


def full_state_recoverable(
    shells: Mapping[Label, Iterable[State]],
    transform: Callable[[State], Image],
) -> bool:
    """Whether ``(label, state) -> transform(state)`` is injective."""

    seen: dict[Image, tuple[Label, State]] = {}
    for label, states in shells.items():
        for state in states:
            image = transform(state)
            previous = seen.get(image)
            current = (label, state)
            if previous is not None and previous != current:
                return False
            seen[image] = current
    return True


def label_decoder(
    shells: Mapping[Label, Iterable[State]],
    transform: Callable[[State], Image],
) -> dict[Image, Label]:
    """Build the unique decoder on the reachable image.

    Raises ``ValueError`` exactly when two distinct shell labels realize the
    same transformed value.
    """

    decoder: dict[Image, Label] = {}
    for label, states in shells.items():
        for state in states:
            image = transform(state)
            previous = decoder.get(image)
            if previous is not None and previous != label:
                raise ValueError("shell label is not recoverable from transformed image")
            decoder[image] = label
    return decoder
