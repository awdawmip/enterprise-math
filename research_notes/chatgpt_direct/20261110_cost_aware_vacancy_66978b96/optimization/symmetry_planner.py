"""Exact Bellman quotient by interchangeable request slots.

Before the last round, slot zero is distinguished because every declared round
overwrites it.  The other slots form a multiset of observed (mask, value)
patterns.  In the last round every slot is interchangeable.  A histogram query
moves exactly one member; compilation chooses one matching physical slot.

The optional cuts in the final round are exact lower-bound cuts.  They change
neither the available observations nor the Bellman objective.  No actual
request value is an input to this planner.
"""
from __future__ import annotations

from math import comb

from bellman_planner import compatible, control_replay, key_cost, observe, write


class SymmetryPlanner:
    """Exact finite-horizon minimax planning with slot-symmetry compression."""

    def __init__(self, slots, targets, *, pruning=True):
        targets = tuple(targets)
        if slots < 1 or any(target < 0 for target in targets):
            raise ValueError('Positive slot count and nonnegative targets required')
        self.slots = slots
        self.colors = slots + 1
        self.width = (self.colors - 1).bit_length()
        self.modulus = 1 << self.width
        self.targets = targets
        self.pruning = pruning
        self.pattern_count = 3 ** self.width
        self.field_bits = slots.bit_length()
        self.field_mask = (1 << self.field_bits) - 1
        self.units = tuple(1 << (self.field_bits * p)
                           for p in range(self.pattern_count))
        self.powers = tuple(3 ** bit for bit in range(self.width))
        self.patterns = []
        self.compatibility = []
        self.unknown = []
        self.full_codes = [0] * self.modulus
        self.code_by_pattern = {}
        for code in range(self.pattern_count):
            mask = value = 0
            for bit, power in enumerate(self.powers):
                digit = code // power % 3
                if digit:
                    mask |= 1 << bit
                    if digit == 2:
                        value |= 1 << bit
            pattern = (mask, value)
            self.patterns.append(pattern)
            self.code_by_pattern[pattern] = code
            self.compatibility.append(sum(1 << residue for residue in range(self.modulus)
                                          if residue & mask == value))
            self.unknown.append(tuple(bit for bit in reversed(range(self.width))
                                      if not mask & (1 << bit)))
            if mask == self.modulus - 1:
                self.full_codes[value] = code
        self.round_keys = tuple(tuple((key, key % self.modulus,
                                        key_cost(key, self.width))
                                       for key in range(1 + target * self.colors,
                                                        1 + (target + 1) * self.colors))
                                for target in self.targets)
        self.last_values = {}
        self.last_actions = {}
        self.multi_values = {}
        self.multi_actions = {}
        self.terminal_seen = False
        self.cache_hits = 0
        self.evaluated_queries = 0
        self.evaluated_creations = 0
        self.bound_cuts = 0
        self.branch_cuts = 0
        self.safe_cuts = 0
        self._last_create_base = self.pattern_count * self.width
        self._multi_create_base = (self.pattern_count + 1) * self.width

    def _members(self, histogram):
        """Decode nonzero pattern counts, never expanding them into slots."""
        result = []
        code = 0
        while histogram:
            count = histogram & self.field_mask
            if count:
                result.append((code, count))
            histogram >>= self.field_bits
            code += 1
        return result

    def _histogram(self, codes):
        return sum(self.units[code] for code in codes)

    def _last(self, histogram):
        cached = self.last_values.get(histogram)
        if cached is not None:
            self.cache_hits += 1
            return cached
        members = self._members(histogram)
        occupied = 0
        for pattern, _ in members:
            occupied |= self.compatibility[pattern]
        keys = self.round_keys[-1]
        best = None
        action = None
        for key, residue, weight in keys:
            if occupied & (1 << residue):
                continue
            self.evaluated_creations += 1
            if best is None or weight < best:
                best = weight
                action = self._last_create_base + key
        lower = None
        if self.pruning:
            minimum_weight = min(weight for _, _, weight in keys)
            if best is not None and best <= 8 + minimum_weight:
                # Every continuation has at least one read and one final key.
                self.safe_cuts += 1
                self.last_values[histogram] = best
                self.last_actions[histogram] = action
                self.terminal_seen = True
                return best
            # Ending with K requires excluding every currently compatible slot.
            # Each such slot needs a new read; a fully known equal slot makes K
            # impossible in this final round.  Multiplicities count separately.
            for _, residue, weight in keys:
                count = 0
                impossible = False
                for pattern, multiplicity in members:
                    if self.compatibility[pattern] & (1 << residue):
                        if not self.unknown[pattern]:
                            impossible = True
                            break
                        count += multiplicity
                if not impossible:
                    score = 8 * count + weight
                    if lower is None or score < lower:
                        lower = score
            assert lower is not None
        # Read bits in the same high-to-low preference as the labelled planner.
        # Within a bit, every nonempty pattern bucket contributes one action.
        for bit in reversed(range(self.width)):
            for pattern, _ in members:
                if bit not in self.unknown[pattern]:
                    continue
                self.evaluated_queries += 1
                base = histogram - self.units[pattern]
                power = self.powers[bit]
                child0 = base + self.units[pattern + power]
                zero = self._last(child0)
                if self.pruning and best is not None and 8 + zero >= best:
                    self.branch_cuts += 1
                    continue
                child1 = base + self.units[pattern + 2 * power]
                one = self._last(child1)
                score = 8 + max(zero, one)
                if best is None or score < best:
                    best = score
                    action = pattern * self.width + bit
                if self.pruning and best == lower:
                    self.bound_cuts += 1
                    self.last_values[histogram] = best
                    self.last_actions[histogram] = action
                    return best
        if best is None:
            raise AssertionError('M=r+1 must leave a legal unoccupied residue')
        self.last_values[histogram] = best
        self.last_actions[histogram] = action
        self.terminal_seen = True
        return best

    def _multi(self, position, first, rest):
        cache_key = (position, first, rest)
        cached = self.multi_values.get(cache_key)
        if cached is not None:
            self.cache_hits += 1
            return cached
        members = self._members(rest)
        occupied = self.compatibility[first]
        for pattern, _ in members:
            occupied |= self.compatibility[pattern]
        best = None
        action = None
        for key, residue, weight in self.round_keys[position]:
            if occupied & (1 << residue):
                continue
            self.evaluated_creations += 1
            full = self.full_codes[residue]
            if position + 1 == len(self.targets) - 1:
                tail = self._last(rest + self.units[full])
            else:
                tail = self._multi(position + 1, full, rest)
            score = weight + tail
            if best is None or score < best:
                best = score
                action = self._multi_create_base + key
        for bit in reversed(range(self.width)):
            power = self.powers[bit]
            if bit in self.unknown[first]:
                self.evaluated_queries += 1
                score = 8 + max(self._multi(position, first + power, rest),
                                self._multi(position, first + 2 * power, rest))
                if best is None or score < best:
                    best = score
                    action = bit
            for pattern, _ in members:
                if bit not in self.unknown[pattern]:
                    continue
                self.evaluated_queries += 1
                base = rest - self.units[pattern]
                score = 8 + max(self._multi(position, first, base + self.units[pattern + power]),
                                self._multi(position, first, base + self.units[pattern + 2 * power]))
                if best is None or score < best:
                    best = score
                    action = self.width + pattern * self.width + bit
        if best is None:
            raise AssertionError('M=r+1 must leave a legal unoccupied residue')
        self.multi_values[cache_key] = best
        self.multi_actions[cache_key] = action
        return best

    def _codes(self, knowledge, position, *, terminal=False):
        maximum = len(self.targets) if terminal else len(self.targets) - 1
        if len(knowledge) != self.slots or not 0 <= position <= maximum:
            raise ValueError('Knowledge length or horizon position mismatch')
        try:
            return tuple(self.code_by_pattern[tuple(pattern)] for pattern in knowledge)
        except (KeyError, TypeError):
            raise ValueError('Knowledge must contain only observed in-domain bits') from None

    def value(self, knowledge, position):
        codes = self._codes(knowledge, position, terminal=True)
        if position == len(self.targets):
            self.terminal_seen = True
            return 0
        if position == len(self.targets) - 1:
            return self._last(self._histogram(codes))
        return self._multi(position, codes[0], self._histogram(codes[1:]))

    def action(self, knowledge, position):
        """Compile an abstract query to one matching actual physical slot."""
        codes = self._codes(knowledge, position)
        if position == len(self.targets) - 1:
            histogram = self._histogram(codes)
            self._last(histogram)
            action = self.last_actions[histogram]
            if action >= self._last_create_base:
                return ('create', action - self._last_create_base)
            pattern, bit = divmod(action, self.width)
            slot = codes.index(pattern)
        else:
            rest = self._histogram(codes[1:])
            self._multi(position, codes[0], rest)
            action = self.multi_actions[position, codes[0], rest]
            if action >= self._multi_create_base:
                return ('create', action - self._multi_create_base)
            if action < self.width:
                return ('read', 0, action)
            pattern, bit = divmod(action - self.width, self.width)
            slot = codes.index(pattern, 1)
        return ('read', slot, bit)

    def metrics(self):
        terminal = int(self.terminal_seen)
        return dict(states=len(self.last_values) + len(self.multi_values) + terminal,
                    nonterminal_states=len(self.last_values) + len(self.multi_values),
                    last_round_states=len(self.last_values),
                    distinguished_slot_states=len(self.multi_values),
                    terminal_states=terminal, cache_hits=self.cache_hits,
                    query_actions=self.evaluated_queries,
                    creation_actions=self.evaluated_creations,
                    pruning=self.pruning, lower_bound_cuts=self.bound_cuts,
                    dominated_branch_cuts=self.branch_cuts,
                    safe_creation_cuts=self.safe_cuts,
                    pattern_types=self.pattern_count,
                    histogram_field_bits=self.field_bits,
                    last_round_state_capacity=comb(self.pattern_count + self.slots - 1,
                                                   self.slots),
                    distinguished_round_state_capacity=self.pattern_count * comb(
                        self.pattern_count + self.slots - 2, self.slots - 1))


def worst_static_witness(planner, initial_knowledge=None):
    """Construct one static table attaining the solved worst-case value.

    This verifier follows a worst answer at each chosen query, accumulates the
    constraints on each initial slot, then chooses a fixed satisfying residue.
    The resulting static table is independently replayed through the policy.
    It is not passed to the planner or its physical action compiler.
    """
    knowledge = initial_knowledge or ((0, 0),) * planner.slots
    initial_constraints = list(knowledge)
    initial_slot_zero = True
    position = cost = 0
    while position < len(planner.targets):
        action = planner.action(knowledge, position)
        if action[0] == 'read':
            _, slot, bit = action
            children = tuple(observe(knowledge, slot, bit, answer) for answer in (0, 1))
            values = tuple(planner.value(child, position) for child in children)
            answer = int(values[1] > values[0])
            knowledge = children[answer]
            if slot or initial_slot_zero:
                initial_constraints[slot] = knowledge[slot]
            cost += 8
        else:
            key = action[1]
            cost += key_cost(key, planner.width)
            knowledge = write(knowledge, 0, key % planner.modulus, planner.width)
            initial_slot_zero = False
            position += 1
    initial_residues = tuple(value for _, value in initial_constraints)
    assert all(compatible(pattern, residue) for pattern, residue in zip(
        initial_constraints, initial_residues))
    replay = control_replay(planner, initial_residues, initial_knowledge)
    value = planner.value(initial_knowledge or ((0, 0),) * planner.slots, 0)
    assert replay['cost'] == cost == value
    return dict(initial_residues=initial_residues,
                initial_constraints=initial_constraints, **replay)
