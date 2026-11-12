#!/usr/bin/env python3
"""Generic Fenwick/BP prefix-count theorem with exact frozen R5 size accounting."""
T,N,E,LABELS=1065,2880,2879,6379
assert E==N-1
steps=sum(i & -i for i in range(1,T+1))
assert steps==6277 and LABELS+T==7444
louds_bits=(N+E)+4*E+N
bp_bits=2*N+4*E+N
old_bits=louds_bits+12*T+T+11*N
new_bits=bp_bits+11*T+11*T+27
assert (louds_bits,bp_bits,old_bits,new_bits)==(20155,20156,65680,43613)
assert ((old_bits+7)//8,(new_bits+7)//8)==(8210,5452)

# Generic terminal-ancestor test: all prefix terminal intervals are contiguous.
words=[('a',),('a','b'),('a','c'),('b',),('b','a','c'),('c','a')]
root={}
for word in words:
    node=root
    for x in word:
        node=node.setdefault(x,{})
    node['#']=True
ranges={}
order=[]
def dfs(node,prefix=()):
    left=len(order)
    if node.get('#'):order.append(prefix)
    for x in sorted(k for k in node if k!='#'):
        dfs(node[x],prefix+(x,))
    ranges[prefix]=(left,len(order))
dfs(root)
assert set(order)==set(words)
activation=[('b','a','c'),('a',),('c','a'),('a','c'),('b',),('a','b')]
bit=[0]*(len(words)+1)
increments=0
for upto,word in enumerate(activation,1):
    j=order.index(word)+1
    while j<=len(words):
        bit[j]+=1;increments+=1;j+=j & -j
    def prefix(k):
        out=0
        while k:out+=bit[k];k-=k & -k
        return out
    active=set(activation[:upto])
    for node,(lo,hi) in ranges.items():
        assert prefix(hi)-prefix(lo)==sum(w[:len(node)]==node for w in active)
assert increments==sum(i & -i for i in range(1,len(words)+1))

print("TRIE_NODES_EDGES_TERMINALS",N,E,T)
print("FENWICK_TOTAL_INCREMENT_WRITES",steps)
print("PREVIOUS_PREFIX_INCREMENT_WRITES",LABELS+T)
print("FENWICK_SAVED_WRITES",LABELS+T-steps)
print("BP_DFS_TRIE_BITS",bp_bits)
print("OLD_INDEXED_ACTIVE_COUNTER_TRIE_BITS",old_bits)
print("NEW_BP_INDEXED_THREE_FRONTIER_FENWICK_BITS",new_bits)
print("OLD_NEW_PACKED_BYTES",(old_bits+7)//8,(new_bits+7)//8)
print("LOGICAL_PACKED_BYTES_SAVED",(old_bits+7)//8-(new_bits+7)//8)
print("PASS_R5_FENWICK_BP_EXACT_COST_AND_GENERIC_PREFIX_QUERY")
