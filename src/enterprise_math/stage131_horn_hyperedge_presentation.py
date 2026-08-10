"""Stage131 execution presentations for finite Horn / multi-premise closures.

A Horn rule is a hyperedge

    P => c

from a finite premise set P to one conclusion c.  Synchronous derivation depth
is therefore an AND/OR min-max quantity rather than ordinary graph distance:

    depth(c) = min_(P=>c) [1 + max_(p in P) depth(p)].

Replacing a multi-premise rule by one unary graph edge per premise is generally
unsound because it changes conjunction into disjunction.  Thus the Stage131
shortcut problem leaves ordinary TC-spanners once premise width exceeds one.

A derived macro rule ``P=>c`` is semantically safe whenever c already belongs to
the base closure of P.  Adding any family of such rules cannot change the
closure operator on any seed set; it can only reduce forward-chaining depth.

The balanced binary AND-tree family gives exact storage/depth formulas for
multi-premise macros spanning s tree levels.  Those formulas expose a new
resource absent from unary chains: premise-literal storage can grow even when
rule count is small.

Horn closure, hypergraph reachability and AND/OR derivations are standard prior
mathematics/CS.  The project value is the Stage131 presentation interpretation
and explicit readout-versus-full-closure depth split.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable, Mapping, Sequence


Atom = Hashable


@dataclass(frozen=True)
class HornRule:
    premises: frozenset[Atom]
    conclusion: Atom
    name: str = ""

    def __post_init__(self) -> None:
        if not self.premises:
            raise ValueError("Horn rule premise set must be nonempty")
        for premise in self.premises:
            hash(premise)
        hash(self.conclusion)


RuleSet = tuple[HornRule, ...]


def normalize_rules(rules: Iterable[HornRule]) -> RuleSet:
    values = tuple(rules)
    if not values:
        raise ValueError("rule family must be nonempty")
    if any(not isinstance(rule, HornRule) for rule in values):
        raise TypeError("rules must be HornRule values")
    seen: set[tuple[frozenset[Atom], Atom]] = set()
    result = []
    for rule in values:
        key = (rule.premises, rule.conclusion)
        if key in seen:
            continue
        seen.add(key)
        result.append(rule)
    return tuple(result)


def horn_atom_set(rules: Iterable[HornRule], seeds: Iterable[Atom] = ()) -> frozenset[Atom]:
    values = normalize_rules(rules)
    atoms = set(seeds)
    for rule in values:
        atoms.update(rule.premises)
        atoms.add(rule.conclusion)
    return frozenset(atoms)


def synchronous_horn_closure_sequence(
    rules: Iterable[HornRule],
    seeds: Iterable[Atom],
) -> tuple[frozenset[Atom], ...]:
    family = normalize_rules(rules)
    known = frozenset(seeds)
    stages = [known]
    atom_count = len(horn_atom_set(family, known))
    while True:
        nxt = frozenset(
            set(known)
            | {
                rule.conclusion
                for rule in family
                if rule.premises.issubset(known)
            }
        )
        if nxt == known:
            return tuple(stages)
        if len(nxt) <= len(known):
            raise AssertionError("strict Horn round failed to add an atom")
        stages.append(nxt)
        known = nxt
        if len(stages) - 1 > atom_count:
            raise AssertionError("finite Horn closure exceeded atom-count round bound")


def horn_closure(rules: Iterable[HornRule], seeds: Iterable[Atom]) -> frozenset[Atom]:
    return synchronous_horn_closure_sequence(rules, seeds)[-1]


def horn_derivation_rounds(
    rules: Iterable[HornRule],
    seeds: Iterable[Atom],
) -> dict[Atom, int | None]:
    family = normalize_rules(rules)
    seed_set = frozenset(seeds)
    atoms = horn_atom_set(family, seed_set)
    stages = synchronous_horn_closure_sequence(family, seed_set)
    first: dict[Atom, int | None] = {atom: None for atom in atoms}
    for round_index, known in enumerate(stages):
        previous = stages[round_index - 1] if round_index > 0 else frozenset()
        for atom in known - previous:
            first[atom] = round_index
    return first


def horn_target_round(
    rules: Iterable[HornRule],
    seeds: Iterable[Atom],
    target: Atom,
) -> int | None:
    return horn_derivation_rounds(rules, seeds).get(target)


def horn_full_closure_rounds(rules: Iterable[HornRule], seeds: Iterable[Atom]) -> int:
    rounds = horn_derivation_rounds(rules, seeds)
    reachable = tuple(value for value in rounds.values() if value is not None)
    if not reachable:
        return 0
    return max(reachable)


def rule_is_semantically_derived(
    base_rules: Iterable[HornRule],
    candidate: HornRule,
) -> bool:
    family = normalize_rules(base_rules)
    return candidate.conclusion in horn_closure(family, candidate.premises)


def add_derived_horn_macros(
    base_rules: Iterable[HornRule],
    macros: Iterable[HornRule],
) -> RuleSet:
    base = normalize_rules(base_rules)
    macro_values = tuple(macros)
    if any(not rule_is_semantically_derived(base, macro) for macro in macro_values):
        raise ValueError("every macro rule must already be semantically derivable")
    return normalize_rules((*base, *macro_values))


def derived_macros_preserve_closure_exhaustive(
    base_rules: Iterable[HornRule],
    macros: Iterable[HornRule],
) -> bool:
    """Exhaustively verify closure equality for all seed sets on small atom sets."""
    base = normalize_rules(base_rules)
    extended = add_derived_horn_macros(base, macros)
    atoms = tuple(sorted(horn_atom_set(extended), key=repr))
    if len(atoms) > 14:
        raise ValueError("exhaustive closure preservation is limited to <=14 atoms")
    for count in range(len(atoms) + 1):
        for chosen in combinations(atoms, count):
            if horn_closure(base, chosen) != horn_closure(extended, chosen):
                raise AssertionError("derived macro changed Horn closure semantics")
    return True


def premise_literal_storage(rules: Iterable[HornRule]) -> int:
    family = normalize_rules(rules)
    return sum(len(rule.premises) for rule in family)


def rule_literal_storage(rules: Iterable[HornRule]) -> int:
    family = normalize_rules(rules)
    return sum(len(rule.premises) + 1 for rule in family)


def naive_unary_projection(rules: Iterable[HornRule]) -> frozenset[tuple[Atom, Atom]]:
    """Unsafe graph projection used only to expose the conjunction-loss boundary."""
    family = normalize_rules(rules)
    return frozenset(
        (premise, rule.conclusion)
        for rule in family
        for premise in rule.premises
    )


def unary_graph_closure(
    edges: Iterable[tuple[Atom, Atom]],
    seeds: Iterable[Atom],
) -> frozenset[Atom]:
    edge_values = tuple(edges)
    known = set(seeds)
    while True:
        nxt = set(known)
        nxt.update(target for source, target in edge_values if source in known)
        if nxt == known:
            return frozenset(known)
        known = nxt


def conjunction_projection_false_positive_witness() -> tuple[RuleSet, frozenset[Atom], frozenset[Atom]]:
    rule = HornRule(frozenset({"a", "b"}), "c", "a_and_b_to_c")
    rules = (rule,)
    exact_from_a = horn_closure(rules, {"a"})
    projected_from_a = unary_graph_closure(naive_unary_projection(rules), {"a"})
    if "c" in exact_from_a or "c" not in projected_from_a:
        raise AssertionError("conjunction-loss witness failed")
    return rules, exact_from_a, projected_from_a


@dataclass(frozen=True)
class AndTree:
    height: int
    leaves: tuple[str, ...]
    root: str
    local_rules: RuleSet
    node_height: Mapping[str, int]
    descendants_at_gap: Mapping[tuple[str, int], frozenset[str]]


def balanced_binary_and_tree(height: int) -> AndTree:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")

    node_height: dict[str, int] = {}
    levels: dict[int, tuple[str, ...]] = {}
    leaves = tuple(f"L{index}" for index in range(1 << height))
    levels[0] = leaves
    node_height.update({leaf: 0 for leaf in leaves})
    local_rules = []

    for level in range(1, height + 1):
        children = levels[level - 1]
        nodes = tuple(f"H{level}_{index}" for index in range(len(children) // 2))
        levels[level] = nodes
        for index, node in enumerate(nodes):
            left = children[2 * index]
            right = children[2 * index + 1]
            local_rules.append(
                HornRule(
                    frozenset({left, right}),
                    node,
                    f"local_{left}_{right}_to_{node}",
                )
            )
            node_height[node] = level

    descendants: dict[tuple[str, int], frozenset[str]] = {}
    children_by_node: dict[str, tuple[str, str]] = {}
    for rule in local_rules:
        values = tuple(sorted(rule.premises, key=repr))
        children_by_node[rule.conclusion] = (values[0], values[1])

    def descendants_gap(node: str, gap: int) -> frozenset[str]:
        key = (node, gap)
        if key in descendants:
            return descendants[key]
        if gap == 0:
            value = frozenset({node})
        else:
            if node not in children_by_node:
                raise ValueError("requested descendant gap below a leaf")
            left, right = children_by_node[node]
            value = descendants_gap(left, gap - 1) | descendants_gap(right, gap - 1)
        descendants[key] = value
        return value

    for level, nodes in levels.items():
        if level == 0:
            continue
        for node in nodes:
            for gap in range(1, level + 1):
                descendants_gap(node, gap)

    root = levels[height][0]
    return AndTree(
        height=height,
        leaves=leaves,
        root=root,
        local_rules=tuple(local_rules),
        node_height=node_height,
        descendants_at_gap=descendants,
    )


def and_tree_span_macros(tree: AndTree, span: int) -> RuleSet:
    if isinstance(span, bool) or not isinstance(span, int) or span <= 0:
        raise ValueError("span must be a positive integer")
    if span > tree.height:
        raise ValueError("span cannot exceed tree height")
    macros = []
    for node, height in tree.node_height.items():
        if height < span:
            continue
        premises = tree.descendants_at_gap[(node, span)]
        macros.append(
            HornRule(
                premises,
                node,
                f"span{span}_to_{node}",
            )
        )
    return tuple(macros)


def and_tree_macro_rule_count_closed(height: int, span: int) -> int:
    h = int(height)
    s = int(span)
    if h <= 0 or s <= 0 or s > h:
        raise ValueError("require 1<=span<=height")
    return (1 << (h - s + 1)) - 1


def and_tree_macro_premise_literals_closed(height: int, span: int) -> int:
    h = int(height)
    s = int(span)
    if h <= 0 or s <= 0 or s > h:
        raise ValueError("require 1<=span<=height")
    return (1 << (h + 1)) - (1 << s)


def and_tree_root_round_closed(height: int, span: int) -> int:
    h = int(height)
    s = int(span)
    if h <= 0 or s <= 0 or s > h:
        raise ValueError("require 1<=span<=height")
    quotient, remainder = divmod(h, s)
    return quotient + remainder


def and_tree_full_closure_rounds_closed(height: int, span: int) -> int:
    h = int(height)
    s = int(span)
    if h <= 0 or s <= 0 or s > h:
        raise ValueError("require 1<=span<=height")
    quotient, remainder = divmod(h, s)
    return quotient + max(s - 2, remainder)


@dataclass(frozen=True)
class AndTreePresentationReport:
    height: int
    span: int
    leaf_count: int
    base_rule_count: int
    macro_rule_count: int
    total_rule_count: int
    base_premise_literals: int
    macro_premise_literals: int
    total_premise_literals: int
    root_round: int
    full_closure_rounds: int


def and_tree_span_presentation_report(height: int, span: int) -> AndTreePresentationReport:
    tree = balanced_binary_and_tree(height)
    macros = and_tree_span_macros(tree, span)
    extended = add_derived_horn_macros(tree.local_rules, macros)
    root_round = horn_target_round(extended, tree.leaves, tree.root)
    full_rounds = horn_full_closure_rounds(extended, tree.leaves)
    if root_round is None:
        raise AssertionError("AND-tree root became unreachable")
    if root_round != and_tree_root_round_closed(height, span):
        raise AssertionError("AND-tree root depth disagreed with closed span law")
    if full_rounds != and_tree_full_closure_rounds_closed(height, span):
        raise AssertionError("AND-tree full closure depth disagreed with closed span law")
    if len(macros) != and_tree_macro_rule_count_closed(height, span):
        raise AssertionError("AND-tree macro count disagreed with closed form")
    macro_literals = premise_literal_storage(macros)
    if macro_literals != and_tree_macro_premise_literals_closed(height, span):
        raise AssertionError("AND-tree macro premise storage disagreed with closed form")
    base_literals = premise_literal_storage(tree.local_rules)
    return AndTreePresentationReport(
        height=height,
        span=span,
        leaf_count=len(tree.leaves),
        base_rule_count=len(tree.local_rules),
        macro_rule_count=len(macros),
        total_rule_count=len(extended),
        base_premise_literals=base_literals,
        macro_premise_literals=macro_literals,
        total_premise_literals=premise_literal_storage(extended),
        root_round=root_round,
        full_closure_rounds=full_rounds,
    )
