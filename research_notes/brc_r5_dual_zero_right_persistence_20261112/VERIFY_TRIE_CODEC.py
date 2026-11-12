#!/usr/bin/env python3
"""Deterministic succinct LOUDS codec for the 1,065 minimal R5 dual-zero words.
Requires the sibling VERIFY_RIGHT_PERSISTENCE.py from the same immutable commit.
Checks exact source-derived labels, complete decode, and bit/byte accounting.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import deque
import VERIFY_RIGHT_PERSISTENCE as f

candidate=getattr(f,'candidate',None)
if candidate is None: candidate=f.candidates
qset=(15,12,3)
words={}
for q in qset:
    for n,masks in sorted(candidate[q].items()):
        mask=min(masks,key=lambda s:(s.bit_count(),s))
        rc=(1-Q(36*q,n))/23
        base=tuple(f.X[k]+rc*f.x*f.H[k] for k in range(28))
        @lru_cache(None)
        def legal(msk):
            return all(base[k]+f.x*f.P[msk][k]/n>=0 for k in range(28))
        @lru_cache(None)
        def canonical_order(msk):
            if not msk:return ()
            if not legal(msk):return None
            for j in range(15):
                if (msk>>j)&1:
                    prev=canonical_order(msk^(1<<j))
                    if prev is not None:return prev+(j+1,)
            return None
        w=canonical_order(mask)
        assert w is not None and len(w)==mask.bit_count()
        words[q,n]=w
assert len(words)==1065
flat_labels=sum(map(len,words.values()))
assert flat_labels==6379 and max(map(len,words.values()))==10

# Canonical rooted trie (children ordered by atom label, labels in 1..15).
root={}
for pair,word in words.items():
    node=root
    for a in word:
        node=node.setdefault(a,{})
    assert '_term' not in node
    node['_term']=True

def encode():
    queue=deque([root]); louds=[]; edge_labels=[]; ends=[]
    while queue:
        node=queue.popleft()
        ends.append(int(node.get('_term',False)))
        for a in sorted(j for j in node if j!='_term'):
            louds.append(1);edge_labels.append(a);queue.append(node[a])
        louds.append(0)
    return louds,edge_labels,ends
louds,labels,term=encode()
N=len(term);E=len(labels)
assert len(louds)==N+E and N==E+1
assert N==2880 and E==2879 and sum(term)==1065

# Decoder processes the bytes of the LOUDS packed payload to rebuild all words.
def packed(bits):
    b=bytearray((len(bits)+7)//8)
    for i,value in enumerate(bits):
        if value:b[i//8] |= 1<<(7-(i%8))
    return bytes(b)
def bit_array(values,width):
    return [(v>>j)&1 for v in values for j in range(width-1,-1,-1)]
def unpack(blob,number_bits):
    return [(blob[i//8] >> (7-(i%8)))&1 for i in range(number_bits)]
trie_bits=len(louds)+4*len(labels)+len(term)
trie_payload=packed(louds+bit_array(labels,4)+term)
replayed=unpack(trie_payload,trie_bits)
replayed_louds=replayed[:N+E]
replayed_label_bits=replayed[N+E:N+E+4*E]
replayed_term=replayed[N+E+4*E:]
assert replayed_louds==louds and replayed_term==term
replayed_labels=[int(''.join(str(b) for b in replayed_label_bits[i:i+4]),2)
                 for i in range(0,len(replayed_label_bits),4)]
assert replayed_labels==labels
seen_paths=[()]
cursor=0; edge_cursor=0
for node_id in range(N):
    parent_word=seen_paths[node_id]
    while replayed_louds[cursor]==1:
        a=replayed_labels[edge_cursor]
        assert 1<=a<=15 and a not in parent_word
        seen_paths.append(parent_word+(a,))
        cursor+=1;edge_cursor+=1
    assert replayed_louds[cursor]==0
    cursor+=1
assert cursor==len(louds) and edge_cursor==E and len(seen_paths)==N

# Derive pair keys from the labeled port vectors, no stored pair-to-node table.
W=tuple(a[f.k0] for a in f.atoms)
K=tuple(a[f.k1] for a in f.atoms)
decoded={}
for word,is_terminal in zip(seen_paths,replayed_term):
    if not is_terminal:continue
    n=-sum(W[a-1] for a in word)
    k1weight=sum(K[a-1] for a in word)
    assert k1weight%36==0
    q=-k1weight//36
    assert (q,n) in words and (q,n) not in decoded
    decoded[q,n]=word
assert decoded==words

# LOUDS: 1 per edge, 0 per node; terminal bit/node; labels 4 bits/edge.
# Flat comparator: 4 bits/label plus 4 bits/length of each of the 1065 words.
trie_bits=len(louds)+4*len(labels)+len(term)
flat_bits=4*flat_labels+4*len(words)
assert trie_bits==20155 and flat_bits==29776
flat_payload=packed([bit for word in words.values()
                     for bit in bit_array((len(word),)+word,4)])
assert len(trie_payload)==2520 and len(flat_payload)==3722
print('CERTIFIED_PAIR_WORDS',len(words),'FLAT_ATOM_LABELS',flat_labels)
print('TRIE_NODES',N,'TRIE_EDGES',E,'SHARED_PREFIX_LABELS',flat_labels-E)
print('EXACT_DECODED_PAIR_WORDS',len(decoded))
print('PACKED_TRIE_PAYLOAD_BITS',trie_bits,'BYTES',len(trie_payload))
print('PACKED_FLAT_PAYLOAD_BITS',flat_bits,'BYTES',len(flat_payload))
print('PAYLOAD_BYTES_SAVED',len(flat_payload)-len(trie_payload))
print('PASS_R5_PREFIX_TRIE_LOUDS_EXACT_BIJECTIVE_CODEC')
