def build(p,bad,pair,class_cost):
 sizes=[]
 for i,line in enumerate((p/'v4all').read_text().splitlines()):
  words=list(map(int,line.split()));gg=[words[j:j+125]for j in range(0,len(words),125)];o=[];un=set(range(125))
  while un:
   k=min(un);xx={g[k]for g in gg};o.append(sorted(xx));un-=xx
  masks=[sum(1<<j for j,x in enumerate(o)if len(x)==s)for s in (1,2,4)];(p/f'ksz{i}').write_text(' '.join(map(str,masks))+'\n');h={}
  def gen(start,sup,old,forb):
   for j in range(start,len(o)):
    a=old.copy();b=forb
    if len(a)+len(o[j])>13:continue
    for x in o[j]:
     if b>>x&1:break
     for z in a:b|=bad[z][x]
     a.append(x)
    else:
     q=sup|1<<j;h[q]=class_cost(a,pair);gen(j+1,q,a,b)
  gen(0,0,[],0);(p/f'fbank{i}').write_text(''.join(f'{q} {c}\n' for q,c in h.items()));sizes.append(len(h))
 return sizes
