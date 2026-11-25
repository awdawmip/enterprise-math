"""Independent fixed-slot, reverse-CRT replay of the numerical R4 minimum."""
from collections import Counter
from functools import cache
import json
A=427862534250255874142059986311712045208460862156242374709749146714880029585009065541265479726658295808843521086362454718047435496681465110551998259577542161622793500228931578210883591253490428068977896911616949921393222257268332228484808322449966505904395308464777304242195893590213416972267332840402564470159978966396652296385533697227114107008635433673
S=555913265364989619697873741372709588670986629522837781333836453228687923187421391074561543226863273773190894562567333918792362053445593573850052370953876739565216134323755512367030826851461448887445240358521194430339039575739758436657254293728498346839912662754165409451691836095700927934351172974265672180517614278948584699085275521666505271546605819230
K=229695347680564422140
TERMS=[[tuple(map(int,s.split(':'))) for s in t] for t in json.load(open('observer_templates.json'))['templates']]
F={int(d):tuple(map(int,qs)) for d,qs in json.load(open('factor_stage2.json')).items()}
H={int(h):tuple(q for d,n in rows for q in F[d]) for h,rows in json.load(open('inventory.json')).items()}
@cache
def inv(m,q):return pow(m,-1,q)
def rootcat(h,b):
 for q in H[h]:
  t=pow(2,-(16+18*b),q)
  for sg in (t,-t):yield q,(sg-A)*inv(S,q)%q
O={c:tuple(rootcat(*c)) for t in TERMS for c in t}
E9=([(7,b) for b in (0,1,2,3,5)],[(12,b) for b in (0,8)],[(20,b) for b in (0,8,16)])
def ok9(k):
 return any(all(any(k%q==b for q,b in O[h]) for h in t) for t in E9)
def verify():
 nodes=Counter();win={}
 for t in TERMS:
  if t in E9:continue
  ch=sorted(t,key=lambda h:len(O[h]))
  def dfs(i,a,m,used):
   nodes[i]+=1
   if i==len(ch):
    for j in range(a,K+1,m):
     if not ok9(j):win[j]=[(ch[i][0],ch[i][1],q) for i,q in enumerate(used)]
    return
   for q,b in O[ch[i]]:
    if q in used:continue
    v=b+q*((a-b)*inv(q,m)%m) if m>1 else b
    if v<=K:dfs(i+1,v,m*q,(*used,q))
  dfs(0,0,1,())
 assert set(win)=={K},win
 a=A+S*K
 print(json.dumps({'root':str(a),'digits':len(str(a)),'k':str(K),'winning_slots':win[K],
                   'census':nodes,'distinct_exact10_at_or_below':len(win)},indent=2))
if __name__=='__main__':verify()
