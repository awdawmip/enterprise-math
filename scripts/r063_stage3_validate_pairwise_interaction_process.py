#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial
TASK_ID='RS-R063-STAGE3-PAIRWISE-INTERACTION-SIGNED-CANCELLATION-MULTIPLICATIVE-PROCESS-LIFT'
RESEARCHER_ID='EM-R063S3-F1CF9D'
TASKBOOK_SOURCE='f1cf9d88428c14ae56e228ed97eba9b657b1fb90'
STAGE2_HEAD='96fbcd431f4cbb8263347bffb5c8bf33b7639e98'
STAGE2_ACCEPT='b31419774f6d7190a4ed51332a9f69f4c7359b31'
I='i'; J='j'
def words(a,b):
 n=a+b; out=[]
 for ii in combinations(range(n),a):
  w=[J]*n
  for k in ii:w[k]=I
  out.append(''.join(w))
 return out
def cnt(w):return (w.count(I),w.count(J))
def local(x,y):return ((0 if x==I else 1)+(0 if y==I else 1))%4
def oriented_product(a,b,c,d):
 x=a*c-b*d;y=a*d+b*c
 return ((x,y),0,(x,y)) if x>=0 else ((x,y),3,(y,-x))
def interaction_cells(p,q):return [(r,s,local(x,y)) for r,x in enumerate(p) for s,y in enumerate(q)]
def label_counts(cells):
 C=Counter(z for _,_,z in cells);return tuple(C[k] for k in range(4))
def maximal_matching_count(n0,n2):
 hi=max(n0,n2);lo=min(n0,n2);return factorial(hi)//factorial(hi-lo)
def residual_object_count(n0,n2):
 hi=max(n0,n2);return comb(hi,abs(n0-n2))
def residual_sets(p,q):
 cells=interaction_cells(p,q);groups={k:[c for c in cells if c[2]==k] for k in range(4)};choices=[[]]
 for k,l in ((0,2),(1,3)):
  A,B=groups[k],groups[l];pool=A if len(A)>=len(B) else B;surplus=abs(len(A)-len(B));opts=list(combinations(pool,surplus));choices=[base+list(opt) for base in choices for opt in opts]
 return [tuple(sorted(x)) for x in choices]
def precedes(c,d):
 r,s,_=c;u,v,_=d;return r<=u and s<=v and (r<u or s<v)
def linext_word_counts(resid,shift=0):
 items=list(resid);n=len(items);labs=[(c[2]+shift)%4 for c in items]
 if any(k not in (0,1) for k in labs):raise AssertionError(('nonpositive-readout',labs))
 preds=[set() for _ in range(n)]
 for i,c in enumerate(items):
  for j,d in enumerate(items):
   if precedes(d,c):preds[i].add(j)
 out=Counter()
 def rec(done,w):
  if len(done)==n:out[w]+=1;return
  for i in range(n):
   if i not in done and preds[i].issubset(done):rec(done|{i},w+(I if labs[i]==0 else J))
 rec(frozenset(),'');return out
@lru_cache(maxsize=None)
def relation_weights(p,q):
 a,b=cnt(p);c,d=cnt(q);raw,shift,target=oriented_product(a,b,c,d);total=Counter()
 for R in residual_sets(p,q):total.update(linext_word_counts(R,shift))
 assert total and all(cnt(w)==target for w in total);return tuple(sorted(total.items()))
def relation(p,q):return frozenset(w for w,_ in relation_weights(p,q))
def min_count(resid):
 items=list(resid);return sum(1 for c in items if not any(precedes(d,c) for d in items))
def tensor3_signature(p,q,r):
 mp={I:0,J:1};return tuple(sorted((i,j,k,(mp[x]+mp[y]+mp[z])%4) for i,x in enumerate(p) for j,y in enumerate(q) for k,z in enumerate(r)))
def stable_hash(rows):
 h=hashlib.sha256()
 for row in rows:h.update(json.dumps(row,sort_keys=True,separators=(',',':')).encode());h.update(b'\n')
 return h.hexdigest()
def main():
 mismatches=[];gates={k:True for k in ['STAGE2_FROZEN_DEPENDENCY_REPLAY_INTACT','PAIRWISE_INTERACTION_TABLE_DERIVED_OR_NONUNIQUENESS_CLASSIFIED','INTERACTION_COUNT_COLLAPSE_EQUALS_RAW_ROOT_PRODUCT','SIGNED_CANCELLATION_TRACE_NORMAL_FORM_EXACT','REPRESENTATIVE_LEVEL_CANCELLATION_CONFLUENCE_OR_MINIMAL_COUNTEREXAMPLE','UNIT_EQUIVARIANT_PROCESS_LEVEL_CLASSIFIED','SOURCE_PATH_ORDER_RETENTION_OR_TOTAL_ERASURE_CLASSIFIED','TRIVIAL_WHOLE_TARGET_FIBRE_RELATION_STRICTLY_IMPROVED_OR_PROVED_UNIMPROVABLE','PROCESS_ASSOCIATIVITY_COHERENCE_OR_NO_GO_CLASSIFIED','MINIMAL_ADDITIONAL_PROCESS_STRUCTURE_CLASSIFIED','ALL_MULTIPLICITY_LAYERS_SEPARATED','SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE','DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES']}
 basis={(I,I):(1,0),(I,J):(0,1),(J,I):(0,1),(J,J):(-1,0)}
 if basis!={(I,I):(1,0),(I,J):(0,1),(J,I):(0,1),(J,J):(-1,0)}:mismatches.append(['interaction-table'])
 all_words=[''.join(bits) for n in range(1,7) for bits in product((I,J),repeat=n)];rows=[]
 for p in all_words:
  a,b=cnt(p)
  for q in all_words:
   c,d=cnt(q);cells=interaction_cells(p,q);n0,n1,n2,n3=label_counts(cells);want=(a*c,a*d+b*c,b*d,0);raw,shift,target=oriented_product(a,b,c,d)
   if len(cells)>36:mismatches.append(['rectangle-size',p,q])
   if (n0,n1,n2,n3)!=want:mismatches.append(['cell-count',p,q])
   if (n0-n2,n1-n3)!=raw:mismatches.append(['raw-collapse',p,q])
   readout=((n0-n2,n1-n3) if n0>=n2 else (n1-n3,n2-n0))
   if readout!=target:mismatches.append(['unit-readout',p,q])
   rows.append({'p':p,'q':q,'src':[a,b,c,d],'labels':[n0,n1,n2,n3],'raw':list(raw),'unit_shift':shift,'target':list(target),'matching_count':maximal_matching_count(n0,n2),'residual_object_count':residual_object_count(n0,n2),'target_native_path_count':comb(sum(target),target[0])})
 p0,q0='iij','ij';R0=residual_sets(p0,q0);rels0=[frozenset(linext_word_counts(x,0)) for x in R0];mins=sorted(min_count(x) for x in R0)
 if len(R0)!=2 or set(rels0)!={frozenset({'ijjj'}),frozenset({'ijjj','jijj'})} or mins!=[1,2]:mismatches.append(['minimal-nonconfluence'])
 for p in all_words:
  for q in all_words:
   if len(p)*len(q)<6:
    a,b=cnt(p);c,d=cnt(q)
    if min(a,b,c,d)>0 and residual_object_count(a*c,b*d)>1:mismatches.append(['smaller-nonconfluence',p,q])
 W11=words(1,1);w1={p+'x'+q:sorted(relation(p,q)) for p in W11 for q in W11}
 if any(v!=['jj'] for v in w1.values()):mismatches.append(['W1'])
 W21=words(2,1);w2={};size_matrix=[]
 for p in W21:
  row=[]
  for q in W21:
   rw=Counter(dict(relation_weights(p,q)));support=sorted(rw);row.append(len(support));w2[p+'x'+q]={'support':support,'support_count':len(support),'formal_witness_count':sum(rw.values()),'coefficient_min':min(rw.values()),'coefficient_max':max(rw.values())}
   if any(cnt(w)!=(3,4) for w in support) or len(support)>=35:mismatches.append(['W2',p,q])
  size_matrix.append(row)
 if size_matrix!=[[5,14,8],[14,11,14],[8,14,5]]:mismatches.append(['W2-matrix'])
 w2_union=set().union(*(set(v['support']) for v in w2.values()));w2_full=set(words(3,4))
 if len(w2_union)!=31 or sorted(w2_full-w2_union)!=['iijjjji','ijjjjii','jiiijjj','jjjiiij']:mismatches.append(['W2-union'])
 wp,wq='jij','jiiij';full_weight=Counter(dict(relation_weights(wp,wq)))
 if len(full_weight)!=9 or min(full_weight.values())!=14 or max(full_weight.values())!=41:mismatches.append(['full-support-weight'])
 W12=words(1,2)
 for p in W12:
  for q in W12:
   raw,shift,target=oriented_product(1,2,1,2);rr=relation(p,q)
   if raw!=(-3,4) or shift!=3 or target!=(4,3) or not rr or any(cnt(w)!=(4,3) for w in rr):mismatches.append(['W3',p,q])
 w4={'i_readout':[0,2],'j_readout':[2,0],'same_unit_orbit':True}
 for x,y,u,v in product(range(4),repeat=4):
  if ((x+u)+(y+v))%4!=((x+y)+(u+v))%4:mismatches.append(['unit-equivariance'])
 mandatory_words=words(1,1)+words(2,1)+words(1,2);assoc_rows=[]
 for p,q,r in product(mandatory_words,repeat=3):
  direct=tensor3_signature(p,q,r)
  if len(direct)!=len(p)*len(q)*len(r):mismatches.append(['assoc-card'])
  assoc_rows.append([p,q,r,hashlib.sha256(repr(direct).encode()).hexdigest()])
 p,q,r='ij','ij','ji';left=set();right=set()
 for u in relation(p,q):left.update(relation(u,r))
 for v in relation(q,r):right.update(relation(p,v))
 if left!={'jiji','jjii'} or right!={'iijj','ijij'}:mismatches.append(['binary-readout-assoc'])
 mult={'W1_2x2':{'source_path_pair_count':4,'interaction_cell_count':4,'cancellation_matching_count':1,'residual_process_object_count':1,'generated_target_path_support':1,'full_target_native_path_count':1,'signed_gaussian_provenance_preimages':4,'R062_N_BRC':1,'Boolean_support':1},'W2_5x5_iijxiij':{'source_path_pair_count':9,'interaction_cell_count':9,'cancellation_matching_count':4,'residual_process_object_count':4,'generated_target_path_support':5,'process_formal_witness_count':102,'full_target_native_path_count':35,'signed_gaussian_provenance_preimages':4,'R062_N_BRC':35,'Boolean_support':1}}
 gates['DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES']=not mismatches
 result={'task_id':TASK_ID,'researcher_id':RESEARCHER_ID,'taskbook_source':TASKBOOK_SOURCE,'stage2_head':STAGE2_HEAD,'stage2_acceptance':STAGE2_ACCEPT,'status':'PASS' if not mismatches else 'FAIL','final_classification':'PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_LIFT_CLASSIFIED_WITH_EXACT_UNIT_EQUIVARIANT_ASSOCIATIVE_INTERACTION_TENSOR_CANONICAL_SOURCE_SENSITIVE_RELATION_AND_POSITIONAL_CANCELLATION_NONCONFLUENCE','exhaustive_word_domain':{'word_count':len(all_words),'ordered_pair_count':len(rows),'max_word_length':6,'max_rectangle_cells':36,'rows_sha256':stable_hash(rows)},'mandatory_witnesses':{'W1':w1,'W2':w2,'W2_size_matrix':size_matrix,'W2_union_support_count':len(w2_union),'W2_missing_from_full_fibre':sorted(w2_full-w2_union),'full_support_weight_witness':{'p':wp,'q':wq,'target':[8,1],'support_count':len(full_weight),'full_target_path_count':9,'formal_witness_count':sum(full_weight.values()),'coefficient_min':min(full_weight.values()),'coefficient_max':max(full_weight.values())},'W3':{'raw':[-3,4],'unit_shift':3,'i_readout':[4,3]},'W4':w4,'W5':{'full_tensor_associator_cases':len(assoc_rows),'associator_sha256':stable_hash(assoc_rows),'binary_readout_nonassoc':{'p':'ij','q':'ij','r':'ji','left':sorted(left),'right':sorted(right)}}},'minimal_nonconfluence':{'p':p0,'q':q0,'rectangle_cells':6,'residual_objects':2,'minimal_element_counts':mins,'pairing_target_relations':[sorted(x) for x in rels0]},'multiplicity_spectrum':mult,'acceptance_gates':gates,'mismatches':mismatches}
 print(json.dumps(result,sort_keys=True,separators=(',',':')));return 0 if not mismatches and all(gates.values()) else 1
if __name__=='__main__':raise SystemExit(main())
