"""EC49FYF — integer verifier of full column S_11 symmetry and hard-state prefix pruning.
Frozen normalized P10/C11 Farey–CRT observer (BRC16943). Python 3 standard library.
Run: python EC49FYF_S11_HARD_PREFIX_VERIFY.py > EC49FYF_S11_HARD_PREFIX_OUTPUT.json
"""
import itertools,json
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
R=range(10); J=range(11); H=[101,788,833]
def p10(h,n):
 h%=10;n%=10
 if h%5==0 and n%5==0:return False
 slope=5 if h%5==0 else (n*pow(h%5,-1,5))%5
 return slope in {(0,0):[3],(0,1):[0,3,4,5],(1,0):[2,3,4,5],(1,1):[2,3]}[(h%2,n%2)]
def masks():
 D=set();directions=0
 for a in R:
  for c in R:
   if __import__('math').gcd(__import__('math').gcd(a,c),10)!=1:continue
   directions+=1
   x,y=next((x,y) for x in R for y in R if (c*x-a*y+1)%10==0)
   mask=sum(1<<t for t in R if p10(x+a*t,y+c*t))
   D.add(mask)
 assert directions==72 and sorted(D)==F
 return directions
def read(U,z,t,j):return int(bool(U & (1<<t)) and z!=j)
def min_transversal(U):
 edges=[V & ~U for V in F if V!=U and (V&U)==U]
 cand=[t for t in R if not (U>>t&1)]
 for k in range(len(cand)+1):
  sols=[list(S) for S in itertools.combinations(cand,k) if all(any(e>>t&1 for t in S) for e in edges)]
  if sols:return sols
 return []
def pair_is_allowed(U,first,second,T):
 positives=[(t,j) for t,j in [first,second] if U>>t&1]
 negatives=[(t,j) for t,j in [first,second] if not U>>t&1]
 if len(set(j for t,j in positives))<len(positives):return False
 rows=[t for t,j in negatives]
 if len(set(rows))<len(rows):return False
 return any(set(rows)<=set(tr) for tr in T)
masks()
states=[(U,z) for U in F for z in [-1]+list(J)]
invariance=0
for swap in range(10):
 def sig(j):return swap+1 if j==swap else swap if j==swap+1 else j
 for U,z in states:
  zz=-1 if z==-1 else sig(z)
  for t in R:
   for j in J:
    assert read(U,z,t,j)==read(U,zz,t,sig(j))
    invariance+=1
T={U:min_transversal(U) for U in H}
assert [len(T[U]) for U in H]==[6,4,8]
for U in H:assert all(len(x)==3 for x in T[U])
rows=[]
for t in R:
 branches={}
 for bit in [0,1]:
  active=[U for U in H if read(U,-1,t,0)==bit]
  excluded=[]
  for u in R:
   for j in [0,1]:
    if (u,j)==(t,0):continue
    if any(not pair_is_allowed(U,(t,0),(u,j),T[U]) for U in active):excluded.append([u,j])
  branches[str(bit)]={'hard_masks':active,'forbidden_second_query_count':len(excluded),'excluded':excluded}
 rows.append({'first_row':t,'branch0':branches['0'],'branch1':branches['1']})
expected={0:(3,5),1:(19,0),2:(3,8),3:(9,0),4:(5,5),5:(5,3),6:(5,5),7:(9,0),8:(5,7),9:(1,7)}
for row in rows:
 t=row['first_row']
 assert (row['branch0']['forbidden_second_query_count'],row['branch1']['forbidden_second_query_count'])==expected[t],row
print(json.dumps({
 'schema':'EC49FYF_FULL_COLUMN_SYMMETRY_HARD_PREFIX_V1',
 'science_pin':'BRC16943','status':'ALL_PASS',
 'states':600,'masks':50,'rows':10,'columns':11,'queries':110,
 'adjacent_generators_checked':10,'equivariance_equalities_checked':invariance,
 'hard_full_masks':H,'minimum_transversals':{str(U):T[U] for U in H},
 'root_query_orbits':10,'root_excluded_rows_if_depth_14':[1],
 'second_query_canonical_candidates_after_first':19,
 'two_query_prefix_necessary_constraint_forbidden_counts':rows,
 'scope':'Normalized complete 600-state indexed product observer, no height restriction; exact symmetry and necessary pruning, not proof of Q=14 or Q=15'
},ensure_ascii=False,indent=2))
