"""Exact operational normal form for one-sided guarded translation words.

PR #310 proves that a nonempty integer action word is summarized by

    T = total translation,
    H = maximum preterminal prefix translation.

Under a fixed upper guard ``x < g`` the word induces the partial affine map

    x |-> x + T     on the domain x < g - H.

The empty word is the total identity and must remain distinct from every
nonempty partial identity.  This module proves at the executable-specification
level that the existing ``GuardedTranslationProfile`` is not merely sufficient:
it is an exact extensional normal form for these partial affine word maps.

Two different profiles always have an explicit separating integer state:

* empty versus nonempty: the nonempty guard cut itself;
* different peaks: the stricter guard cut;
* equal peak but different total translation: one integer immediately below
  the common guard cut.

Hence equality of induced partial maps is exactly equality of profiles.

Word concatenation is the closed product

    (T,H) * (U,K) = (T+U, max(H, T+K))

for nonempty factors, with the empty profile as identity.  This is the familiar
max-plus / tropical affine composition law.  A useful type-safe way to include
the identity is to regard ``None`` as minus infinity and let a profile act on a
suffix requirement ``z`` by

    Phi_(T,H)(z) = max(H, T+z),

while the empty profile acts identically.  Then profile multiplication is
exactly composition of these requirement transformers.

Max-plus affine semigroups and weighted-automaton summaries are standard prior
mathematics.  P024's contribution here is the exact guarded-integer word normal
form and its role as the minimal operation-language state before applying a
more task-specific observation quotient.
"""

from __future__ import annotations

from dataclasses import dataclass

from .guarded_translation_precision import (
    GuardedTranslationOutcome,
    GuardedTranslationProfile,
    apply_guarded_translation_profile,
    compose_guarded_profiles,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _validate_profile(profile: GuardedTranslationProfile) -> None:
    if not isinstance(profile, GuardedTranslationProfile):
        raise TypeError("profile must be GuardedTranslationProfile")
    _require_int("total_translation", profile.total_translation)
    if profile.preterminal_peak is None:
        if profile.total_translation != 0:
            raise ValueError("empty profile must have zero total translation")
        return
    _require_int("preterminal_peak", profile.preterminal_peak)
    if profile.preterminal_peak < 0:
        raise ValueError("preterminal peak must contain the zero prefix")


def guarded_profile_partial_affine_outcome(
    value: int,
    profile: GuardedTranslationProfile,
    guard: int,
) -> GuardedTranslationOutcome:
    """Evaluate only definedness and exact final integer value."""
    _require_int("value", value)
    _require_int("guard", guard)
    _validate_profile(profile)
    return apply_guarded_translation_profile(value, profile, guard, ())


@dataclass(frozen=True)
class GuardedProfileSeparation:
    state: int
    left: GuardedTranslationOutcome
    right: GuardedTranslationOutcome
    reason: str


def guarded_profile_separating_witness(
    left: GuardedTranslationProfile,
    right: GuardedTranslationProfile,
    guard: int,
) -> GuardedProfileSeparation | None:
    """Construct a state separating two distinct profile-induced partial maps.

    Returns ``None`` exactly when the profiles are structurally equal.
    """
    _validate_profile(left)
    _validate_profile(right)
    _require_int("guard", guard)
    if left == right:
        return None

    if left.is_empty or right.is_empty:
        nonempty = right if left.is_empty else left
        assert nonempty.preterminal_peak is not None
        state = guard - nonempty.preterminal_peak
        reason = "empty_vs_guarded"
    else:
        assert left.preterminal_peak is not None
        assert right.preterminal_peak is not None
        if left.preterminal_peak != right.preterminal_peak:
            # The larger peak has the smaller/stricter domain cut.  At that cut
            # it is disabled while the smaller-peak profile remains enabled.
            state = guard - max(
                left.preterminal_peak,
                right.preterminal_peak,
            )
            reason = "different_guard_domain"
        else:
            if left.total_translation == right.total_translation:
                raise AssertionError("distinct profiles lost their separating coordinate")
            state = guard - left.preterminal_peak - 1
            reason = "different_final_translation"

    left_outcome = guarded_profile_partial_affine_outcome(state, left, guard)
    right_outcome = guarded_profile_partial_affine_outcome(state, right, guard)
    if (
        left_outcome.defined == right_outcome.defined
        and left_outcome.final_value == right_outcome.final_value
    ):
        raise AssertionError("constructed state failed to separate guarded profiles")
    return GuardedProfileSeparation(
        state=state,
        left=left_outcome,
        right=right_outcome,
        reason=reason,
    )


def guarded_profiles_extensionally_equal(
    left: GuardedTranslationProfile,
    right: GuardedTranslationProfile,
) -> bool:
    """Exact extensional equality of the induced partial affine maps.

    The theorem proved by ``guarded_profile_separating_witness`` is that this is
    equivalent to structural profile equality, independently of the chosen
    integer guard location.
    """
    _validate_profile(left)
    _validate_profile(right)
    return left == right


def guarded_profile_product(
    left: GuardedTranslationProfile,
    right: GuardedTranslationProfile,
) -> GuardedTranslationProfile:
    """Monoid product corresponding to literal word concatenation."""
    _validate_profile(left)
    _validate_profile(right)
    return compose_guarded_profiles(left, right)


def guarded_requirement_transform(
    profile: GuardedTranslationProfile,
    suffix_peak: int | None,
) -> int | None:
    """Max-plus affine action on a suffix peak; ``None`` represents -infinity.

    If a suffix requires preterminal prefix height ``suffix_peak``, prefixing it
    by ``profile`` changes the combined requirement to the profile-composition
    peak.  The empty suffix requirement is represented by ``None``.
    """
    _validate_profile(profile)
    if suffix_peak is not None:
        _require_int("suffix_peak", suffix_peak)
        if suffix_peak < 0:
            raise ValueError("suffix_peak must contain the zero prefix")
    if profile.is_empty:
        return suffix_peak
    assert profile.preterminal_peak is not None
    if suffix_peak is None:
        return profile.preterminal_peak
    return max(
        profile.preterminal_peak,
        profile.total_translation + suffix_peak,
    )


def guarded_requirement_composition_identity(
    left: GuardedTranslationProfile,
    right: GuardedTranslationProfile,
    suffix_peak: int | None,
) -> bool:
    """Executable max-plus homomorphism identity.

    ``Phi_(left*right) = Phi_left o Phi_right`` on every suffix requirement.
    """
    product = guarded_profile_product(left, right)
    return guarded_requirement_transform(product, suffix_peak) == (
        guarded_requirement_transform(
            left,
            guarded_requirement_transform(right, suffix_peak),
        )
    )
