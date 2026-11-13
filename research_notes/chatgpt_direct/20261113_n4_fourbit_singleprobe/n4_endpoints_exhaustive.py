"""Every endpoint-menu for every certified message, with explicit one-probe decoder."""
from itertools import combinations,product
from collections import defaultdict
from n4_four_bit_certificate import run
PAIRS=list(combinations(range(5),2))
W=run()
menus=0
max_reads=0
for message,states in W.items():
    for choices in product(PAIRS,repeat=4):
        groups=defaultdict(list)
        for w in states:
            active=tuple(i for i in range(4)if w[i] in choices[i])
            followup=tuple(w[i] for i in active)
            groups[active].append((w,followup))
        for active,rows in groups.items():
            distinct={future for _,future in rows}
            assert len(distinct)<=2,(message,choices,active,distinct)
            if len(distinct)==2:
                # Choose one original active endpoint slot whose bit separates the outcomes.
                outputs=tuple(distinct)
                j=next((j for j in range(len(active))if outputs[0][j]!=outputs[1][j]),None)
                assert j is not None
                selected_site=active[j]
                lookup={}
                for hist,future in rows:
                    bit=int(hist[selected_site]==choices[selected_site][1])
                    if bit in lookup: assert lookup[bit]==future
                    lookup[bit]=future
                assert len(lookup)==2
                max_reads=1
        menus+=1
assert menus==64*10**4 and max_reads==1
print('ENDPOINT_MENU_PASS:',menus,'(message, menu) combinations, <=1 original endpoint read')
