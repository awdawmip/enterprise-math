"""Two-petal comparison window. Replays source-resolved directed edges, no native port calls."""
from collections import Counter, deque
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd, isqrt, lcm


EDGES = (("R","L"),("L","R"),("R","S"),("S","R"))
CYCLES = {"A": (0,(0,1)), "B": (1,(2,3))}


def replay(w, q, save=False):
    positions = ["R","R"]
    flux = [[0]*4 for _ in positions]
    a = b = e = 0
    receipt = []
    for letter in w:
        assert positions == ["R","R"]
        token, pair = CYCLES[letter]
        for edge in pair:
            start, stop = EDGES[edge]
            assert positions[token] == start
            positions[token] = stop
            flux[token][edge] += 1
            for t,row in enumerate(flux):
                for cell in ("R","L","S"):
                    change = sum(v*((j==cell)-(i==cell)) for v,(i,j) in zip(row,EDGES))
                    assert (positions[t]==cell) == (cell=="R")+change
            assert positions.count("R")<=2 and positions.count("L")<=1 and positions.count("S")<=1
            assert all(v==0 for v in flux[0][2:]+flux[1][:2])
            if edge == pair[1]:
                if letter == "A":
                    a += 1
                else:
                    e = (e+a) % q
                    b += 1
            # The reverse edges are chords. At either intermediate leaf the tree
            # edge has just one more departure than the corresponding chord.
            assert flux[0][0] == flux[0][1] + (positions[0]=="L")
            assert flux[1][2] == flux[1][3] + (positions[1]=="S")
            assert flux[0][1] == a and flux[1][3] == b
            if save:
                receipt.append({"edge":">".join(EDGES[edge]),"token":"alpha" if token==0 else "beta",
                                "locations":positions[:],"entry":e, "completed_flux":[a,b],
                                "per_token_flow":[x[:] for x in flux]})
    return (a,b,e), receipt


def count_pairs(w):
    return sum(x=="A" and y=="B" for i,x in enumerate(w) for y in w[i+1:])


def physical_audit():
    cases = moves = splits = left_petals = right_petals = 0
    stream = sha256()
    groups = Counter()
    q = 6
    for length in range(11):
        for word in product("AB",repeat=length):
            w = "".join(word)
            (a,b,e), _ = replay(w,q)
            assert (a,b,e) == (w.count("A"),w.count("B"),count_pairs(w)%q)
            for cut in range(length+1):
                left,right = w[:cut], w[cut:]
                composed = count_pairs(left)+count_pairs(right)+left.count("A")*right.count("B")
                assert composed % q == e
                splits += 1
            groups[a,b,e] += 1
            stream.update(f"{w}:{a},{b},{e}\n".encode())
            cases += 1
            moves += length
            left_petals += a
            right_petals += b
    assert [groups[3,3,i] for i in range(6)] == [4,3,3,4,3,3]
    return {"q":q,"complete_words":cases,"complete_petals":moves,"physical_edge_steps":2*moves,
            "cost_counts_for_full_binary_tree_words":{
                "simulated_named_token_departure_checks":2*moves,
                "source_vertex_balance_equalities":12*moves,
                "directed_return_edge_commits":moves,
                "reconstructed_outgoing_flow_equalities":4*moves,
                "exact_A_increments":left_petals, "exact_B_increments":right_petals,
                "entry_modular_additions":right_petals, "native_acquisition_calls":0,
                "one_probe_readout_bits":1, "shared_root_capacity":2,
                "fixed_q_generic_entry_bits":(q-1).bit_length(),
                "per_counter_bits_at_length_at_most_10":(10).bit_length(),
                "saved_raw_trace_words":2,"saved_raw_edge_receipts":8},
            "boundary_split_checks":splits,"word_and_final_state_sha256":stream.hexdigest(),
            "uncompressed_receipts":{w:replay(w,q,True)[1] for w in ("AB","BA")}}


def polynomial_table(n):
    table = {}
    for a in range(n+1):
        for b in range(n+1):
            if a*b == 0:
                table[a,b] = [1]
                continue
            coeffs = [0]*(a*b+1)
            for i,c in enumerate(table[a-1,b]):
                coeffs[i] += c
            for i,c in enumerate(table[a,b-1]):
                coeffs[a+i] += c
            assert min(coeffs)>0 and sum(coeffs)==comb(a+b,a)
            table[a,b] = coeffs
    return table


def divisors(k):
    return [d for d in range(1,k+1) if k%d==0]


def mobius(n):
    result=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:
                return 0
            result=-result
        p+=1
    return -result if n>1 else result


def ramanujan(d,r):
    return sum(v*mobius(d//v) for v in divisors(gcd(d,r)))


def distributions():
    table = polynomial_table(12)
    # The direct enumerator uses ordered letter pairs, independently of the
    # last-letter polynomial recursion, and checks the full coefficient lists.
    direct = Counter()
    for n in range(13):
        for w in product("AB",repeat=n):
            direct[w.count("A"),w.count("B"),count_pairs(w)] += 1
    for (a,b),cs in table.items():
        if a+b<=12:
            assert cs == [direct[a,b,i] for i in range(len(cs))]
    tested = uniform = compact = 0
    examples = {}
    for (a,b),cs in table.items():
        for q in range(2,19):
            nums = [sum(cs[r::q]) for r in range(q)]
            assert sum(v>0 for v in nums) == min(q,a*b+1)
            orders = [d for d in divisors(q) if a%d+b%d<d]
            period = lcm(*orders)
            assert min(s for s in range(1,q+1) if all(nums[(r+s)%q]==v for r,v in enumerate(nums))) == period
            same=len(set(nums))==1
            assert same==(period==1)
            uniform+=same
            if (a+b)%q==0:
                g=gcd(q,a)
                ds=divisors(g)
                total=comb(a+b,a)
                for r,v in enumerate(nums):
                    assert q*v == sum(ramanujan(d,r)*comb((a+b)//d,a//d) for d in ds)
                phi=lambda d:sum(gcd(d,x)==1 for x in range(1,d+1))
                assert sum((q*v-total)**2 for v in nums) == q*sum(
                    phi(d)*comb((a+b)//d,a//d)**2 for d in ds if d>1)
                assert [r for r,n in enumerate(nums) if n==max(nums)]==list(range(0,q,g))
                assert period==g
                compact+=1
            if (a,b,q) in [(3,3,6),(2,4,6),(5,7,6),(4,7,12),(0,0,6)]:
                examples[f"{a},{b},{q}"]={"residue_counts":nums,"least_period":period}
            tested+=1
    return {"range_a_b":[0,12],"range_q":[2,18],"all_word_direct_replays_up_to_length_12":8191,
            "parameter_triples":tested,"uniform_distributions":uniform,
            "ramanujan_parseval_triples":compact,"examples_a_b_q":examples}


def earliest():
    table = polynomial_table(24)
    out = []
    for q in range(2,25):
        support = uniform = None
        uniform_at_q = []
        for n in range(q+1):
            for a in range(n+1):
                coeffs = table[a,n-a]
                counts = [sum(coeffs[r::q]) for r in range(q)]
                if min(counts)>0 and support is None:
                    support=n
                if len(set(counts))==1:
                    if uniform is None:
                        uniform=n
                    if n==q:
                        uniform_at_q.append(a)
        assert support == isqrt(4*(q-1)-1)+1
        assert uniform == q
        assert uniform_at_q == [a for a in range(q+1) if gcd(a,q)==1]
        out.append([q,support,uniform,len(uniform_at_q)])
    return out


def state_tests(q):
    states = list(product(range(q),repeat=2))
    def nexts(s):
        x,h=s
        return (((x+1)%q,h), (x,(h+x)%q))
    colors = {s:int(s[1]==0) for s in states}
    while True:
        palette = {}
        new = {}
        for s in states:
            ka,kb=nexts(s)
            signature=(colors[s],colors[ka],colors[kb])
            new[s]=palette.setdefault(signature,len(palette))
        if len(set(new.values()))==len(set(colors.values())):
            break
        colors=new
    assert len(set(new.values())) == q*q
    # Enumerate actual maps on the q^2 boundary states, by composition with
    # each letter. Do not infer their number from parameter counts.
    identity = tuple(states)
    queue = deque([identity])
    seen = {identity}
    state_set = set()
    while queue:
        f=queue.popleft()
        u,c=f[0]
        v=(f[q][1]-c)%q  # states[q] is (1,0)
        assert f == tuple(((x+u)%q,(h+c+x*v)%q) for x,h in states)
        state_set.add(f[0])
        for i in range(2):
            target = tuple(nexts(s)[i] for s in f)
            if target not in seen:
                seen.add(target)
                queue.append(target)
    assert len(seen)==q**3 and len(state_set)==q*q
    # A^k B tests one specified residue within a common flux fiber.
    for a,h,target in product(range(q),repeat=3):
        k=(-a-target)%q
        assert ((h+a+k)%q==0)==(h==target)
    return {"q":q,"reachable_and_inequivalent_observer_states":q*q,
            "distinct_word_transformations":len(seen),"single_target_suffix_tests":q**3}


def main():
    data={"window_version":"two_named_petals_boundary_entry_v1",
          "source_strength":"external finite comparison; native port calls 0",
          "directed_edge_order":[">".join(e) for e in EDGES],
          "physical_replays":physical_audit(),
          "word_distributions":distributions(),
          "q_first_full_support_first_uniform_number_uniform_at_q":earliest(),
          "finite_control":[state_tests(q) for q in range(2,10)]}
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
