"""How far one must be willing to move to connect all eleven-label optima."""
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,sys,subprocess
HERE=Path(__file__).resolve().parent
class Components:
    def __init__(self,n):self.parent=list(range(n));self.size=[1]*n;self.count=n
    def find(self,a):
        while a!=self.parent[a]:
            self.parent[a]=self.parent[self.parent[a]];a=self.parent[a]
        return a
    def link(self,a,b):
        a=self.find(a);b=self.find(b)
        if a==b:return
        if self.size[a]<self.size[b]:a,b=b,a
        self.parent[b]=a;self.size[a]+=self.size[b];self.count-=1
    def sizes(self):
        return dict(sorted((str(k),v)for k,v in Counter(self.size[i]for i in range(len(self.parent))if self.find(i)==i).items()))
def solve(sixth):
    fifth=sixth/'previous';fourth=fifth/'previous';third=fourth/'previous';second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path.insert(0,str(third/'group'))
    from generate import maps
    lin,tr,_=maps()
    affine=[bytes(t[y]for y in l)for l in lin for t in tr];assert affine[0]==bytes(range(125))
    assert all(t[0]==i for i,t in enumerate(tr))
    assert all(l[0]==0 and tr[l[t]][l[x]]==l[tr[t][x]] for l in lin for t in range(125)for x in range(125))
    assert all(tr[tr[a][b]][x]==tr[a][tr[b][x]] for a in range(125)for b in range(125)for x in range(125))
    ids={g:i for i,g in enumerate(lin)}
    mul=[[ids[bytes(l[y]for y in b)]for b in lin]for l in lin]
    groups=json.loads((fourth/'eleven_six_counts/groups.json').read_text())+[json.loads((fifth/'eleven_equal/groups.json').read_text())]
    tables={};images=[];locations={};family=[];where=[]
    for orbit,part in enumerate(groups):
        indices=[]
        for i,g in enumerate(affine):
            key=tuple(sorted(tuple(sorted(g[x]for x in r))for r in part))
            if key not in tables:
                tables[key]=len(tables);sk=tuple(r for r in key if len(r)==13)
                family.append(locations.setdefault(sk,len(locations)))
                where.append((orbit,i))
            indices.append(tables[key])
        assert {where[j][0]for j in indices}=={orbit}
        images.append(indices)
    # A common factor of two interchanges the two blocks of 125 native menus.
    # Verify all absolute transform costs from the menu masks, on each actual
    # row set once. The three optimal orbits reuse many of the same sets.
    from cyclic11 import observations,class_cost
    _,menus=observations()
    by_action=[[[v&((1<<125)-1) for v in row] for row in menus],[[v>>125 for v in row]for row in menus]]
    from functools import cache
    @cache
    def split_price(row):return tuple(class_cost(row,m)for m in by_action)
    actions=Counter()
    for table in tables:
        prices=[split_price(row)for row in table]
        i,d=map(sum,zip(*prices))
        assert i+d==11292
        actions[f'{i},{d}']+=1
    assert len(tables)==8000 and len(locations)==200
    assert set(Counter(family).values())=={40}
    roots=[v[0]for v in images]
    with TemporaryDirectory()as tmp:
        w=Path(tmp);(w/'group').write_bytes(b''.join(affine))
        subprocess.run(['c++','-std=c++17','-O3',sixth/'orbit_distance/distance.cpp','-o',w/'cost'],check=True)
        def tags(gs):
            own={x:i for i,r in enumerate(gs)for x in r};return ' '.join(str(own[j])for j in range(125))
        edges=[{} for _ in groups]
        for i,a in enumerate(groups):
            for j,b in enumerate(groups):
                data=f'11 11\n{tags(a)}\n{tags(b)}\n'
                lines=subprocess.check_output([w/'cost',w/'group'],input=data,text=True).splitlines();assert len(lines)==12000
                for g,n,h in map(lambda l:map(int,l.split()),lines):
                    t=images[j][g];d=(11-n,125-h)
                    assert edges[i].setdefault(t,d)==d
    assert all(len(v)==8000 for v in edges)
    out={'family_size':40,'parent_locations':200,'number_of_tables':8000,'metrics':{},'identity_and_doubling_cost_histogram':dict(sorted(actions.items()))}
    for metric,name in enumerate(('changed_labels','moved_histories')):
        buckets={};local=[]
        for source,dists in enumerate(edges):
            v=roots[source]
            same=Counter();diff=Counter()
            for t,d in dists.items():
                if v==t:continue
                r=d[metric];counts=same if family[t]==family[v]else diff;counts[r]+=1
                buckets.setdefault(r,[]).append((source,t))
            local.append(dict(orbit_size=len(set(images[source])),nearest_local=min(same),number_local=same[min(same)],nearest_other_family=min(diff),number_other_family=diff[min(diff)]))
        uf=Components(8000);events=[];previous=8000
        for r,items in sorted(buckets.items()):
            for source,t in items:
                if uf.find(roots[source])==uf.find(t):continue
                target,g=where[t];lh,th=divmod(g,125)
                for h,l in enumerate(lin):
                    off=125*h;dest=125*mul[h][lh];dx=l[th]
                    for z in range(125):uf.link(images[source][off+z],images[target][dest+tr[z][dx]])
            if uf.count!=previous:
                events.append(dict(radius=r,components=uf.count,size_histogram=uf.sizes()));previous=uf.count
            if uf.count==1:break
        assert previous==1
        out['metrics'][name]=dict(by_orbit=local,transitions=events,connectivity_radius=events[-1]['radius'])
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);a=p.parse_args()
    print(json.dumps(solve(a.previous.resolve()),sort_keys=True,indent=2))
