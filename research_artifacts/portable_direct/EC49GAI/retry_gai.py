import csv,json,sys
from gen import physical
files=['fourth_partial.csv','fourth_new.csv','fourth_tail.csv','fourth_tail2.csv','fourth_tail3.csv','retry.csv','next.csv','next2.csv','q.csv','q2.csv','r.csv','r2.csv','r3.csv','s.csv','s2.csv','s3.csv','t.csv','u.csv','v.csv','v2.csv','w.csv','w2.csv','x.csv','x2.csv','y.csv','y2.csv','z.csv','ga.csv','ga2.csv']
d={}
for file in files:
 for row in csv.reader(open(file)):
  i,n,s,c=map(int,row[:4]);assert i not in d or d[i][1]==0;d[i]=(n,s,c)
assert len(d)==2393
roots=json.load(open('fourth.json'))
ids=[i for i,(n,s,c) in sorted(d.items()) if s==0];assert len(ids)==471
lo,hi,cap=map(int,sys.argv[1:]);ids=ids[lo:hi];print(len(ids))
for i in ids:
 n,(r,mask,other),paths,status=roots[i];st=physical([mask,*other],14,r,0);assert len(st)==n
 print(i,n,25,15,cap)
 for u,h in st:print(u,h)
