"""Small declared native graph fixtures for the finite monitor consumer."""
from fractions import Fraction

from path_monitor import Edge, NativeGraph, Node


def closed_word_graph(word, weights):
    """One labeled route returning to port P; internal routing labels retained."""
    position = [0] * 6
    nodes = [Node("P", tuple(position))]
    edges = []
    source = "P"
    for index, (step, weight) in enumerate(zip(word, weights)):
        position[abs(step) - 1] += 1 if step > 0 else -1
        last = index == len(word) - 1
        target = "P" if last else f"internal:{index + 1}"
        if not last:
            nodes.append(Node(target, tuple(position)))
        edges.append(Edge(f"edge:{index + 1}", source, target, step, weight))
        source = target
    if len(word) != len(weights) or position != [0] * 6:
        raise ValueError("fixture needs equally many weights and a closed nonempty word")
    if not word:
        raise ValueError("fixture word must be nonempty")
    return NativeGraph(tuple(nodes), tuple(edges))


def blind_pair():
    weights = {1: Fraction(2, 3), -1: Fraction(3, 5), 2: Fraction(5, 7), -2: Fraction(7, 11)}
    words = ((1, -1, 2, -2), (1, 2, -1, -2))
    return tuple(closed_word_graph(word, tuple(weights[step] for step in word)) for word in words)


def suffix_context_graph():
    # P and R are different routing states at the same spatial Cell.
    return NativeGraph(
        (Node("P", (0,) * 6), Node("Q", (1, 0, 0, 0, 0, 0)), Node("R", (0,) * 6)),
        (Edge("prefix", "P", "Q", 1, Fraction(2, 3)),
         Edge("future-suffix", "Q", "R", -1, Fraction(3, 5))),
    )


def branching_hidden_cycle_graph():
    return NativeGraph(
        (Node("P", (0,) * 6), Node("A", (1, 0, 0, 0, 0, 0)), Node("B", (1, 1, 0, 0, 0, 0))),
        (Edge("alternative-a", "P", "A", 1, Fraction(1, 2)),
         Edge("alternative-b", "P", "A", 1, Fraction(1, 3)),
         Edge("return", "A", "P", -1, Fraction(2)),
         Edge("hidden-out", "A", "B", 2, Fraction(3, 5)),
         Edge("hidden-back", "B", "A", -2, Fraction(5, 7))),
    )
