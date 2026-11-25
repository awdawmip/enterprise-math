from pathlib import Path
s=Path('sat_token.cpp').read_text()
s=s.replace('struct Solver{',Path('dense_bool.hpp').read_text()+'\nstatic DenseBool dense;\nstruct Solver{',1)
# Exact dense query from actual canonical column labels. Install the witness recursively in original memo.
point=' int solve(const S&s,int k)'
assert s.count(point)==1
s=s.replace(point,''' int dense_install(const S&s,int k){
   long long n=count(s);if(n<=1)return -2;Key key{s,k};auto it=mem.find(key);if(it!=mem.end())return it->second;
   vector<pair<int,int>> st;
   for(W v=s.act;v;v&=v-1){W b=v&-v;int u=F[__builtin_ctzll(b)],h=0,f=0;for(int j=0;j<M;j++){if(s.c[j].first&b)h|=1<<j;if(s.c[j].second&b)f|=1<<j;}for(int z=f;;z=(z-1)&f){if(pc(h|z)<=H)st.push_back({u,h|z});if(!z)break;}}
   assert(st.size()==size_t(n)&&n<=16);unsigned all=DenseBool::full(n);DenseBool::Q q;
   map<unsigned,int> rep;
   for(int r=0;r<10;r++)for(int j=0;j<M;j++){unsigned a=0;for(int i=0;i<n;i++)if((st[i].first>>r&1)&&!(st[i].second>>j&1))a|=1u<<i;unsigned x=min(a,all^a);if(x)rep.emplace(x,r*M+j);}
   for(auto[a,p]:rep)q.push_back(a);
   int a=dense.solve(n,q,k);if(a<0)return mem.emplace(key,a).first->second;
   int p=rep.at(a),r=p/M,j=p%M;S y=child(s,r,j,true),z=child(s,r,j,false);assert(count(y)+count(z)==n&&count(y)>0&&count(z)>0);
   int yy=dense_install(y,k-1),zz=dense_install(z,k-1);assert(yy!=-1&&zz!=-1);return mem.emplace(key,p).first->second;
 }
'''+point,1)
# Must invoke before memo lookup in dense_install, after cap increment; no partial entries in shared cache.
s=s.replace('if(++calls>cap)throw 1;vector<int>', 'if(++calls>cap)throw 1;if(k<=4&&getenv("EM_DENSE"))return dense_install(s,k);vector<int>',1)
s=s.replace('int main(){int cases;', 'int main(){if(auto p=getenv("EM_DENSE_LIMIT"))dense.limit=stoull(p);int cases;',1)
s=s.replace('<<v.satPrunes<<endl;}}','<<v.satPrunes<<","<<dense.hits<<","<<dense.misses<<","<<dense.clears<<","<<dense.bank.size()<<","<<dense.products<<endl;}}',1)
Path('dense_solver.cpp').write_text(s)
