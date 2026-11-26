from pathlib import Path
s=Path('dense_solver.cpp').read_text()
old='   vector<pair<int,int>> st;'
new='''   // Exact empty-hole witness: each free column needs its own observation.
   if(getenv("EM_FAST")){
     for(W v=s.act;v;v&=v-1){W b=v&-v;int p=0;for(auto[x,y]:s.c)p+=!!(y&b);if(p>k)return mem.emplace(key,-1).first->second;}
     if(pc(s.act)==1)return mem.emplace(key,-3).first->second;
   }
   vector<pair<int,int>> st;'''
assert s.count(old)==1;s=s.replace(old,new)
s=s.replace('   for(int r=0;r<10;r++)for(int j=0;j<M;j++){unsigned a=0;for(int i=0;i<n;i++)if((st[i].first>>r&1)&&!(st[i].second>>j&1))a|=1u<<i;unsigned x=min(a,all^a);if(x)rep.emplace(x,r*M+j);}', '''   if(getenv("EM_FAST")){
     unsigned rows[10]={},cols[M]={};
     for(int i=0;i<n;i++){for(int r=0;r<10;r++)if(st[i].first>>r&1)rows[r]|=1u<<i;for(int j=0;j<M;j++)if(!(st[i].second>>j&1))cols[j]|=1u<<i;}
     for(int r=0;r<10;r++)for(int j=0;j<M;j++){unsigned a=rows[r]&cols[j],x=min(a,all^a);if(x)rep.emplace(x,r*M+j);}
   }else for(int r=0;r<10;r++)for(int j=0;j<M;j++){unsigned a=0;for(int i=0;i<n;i++)if((st[i].first>>r&1)&&!(st[i].second>>j&1))a|=1u<<i;unsigned x=min(a,all^a);if(x)rep.emplace(x,r*M+j);}''')
# -3 is a successful physical witness handled by original replay and parent recursion.
Path('gaj_solver.cpp').write_text(s)
