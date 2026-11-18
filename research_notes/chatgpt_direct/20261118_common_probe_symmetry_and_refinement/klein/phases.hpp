using Mask=__uint128_t;
using Obs=array<U,4>;
Obs obs[125][125];Mask bad[125][125];
array<vector<int>,64> history;
int guaranteed[14]={-1,-1,-1,-1,-1,-1,89,281,465,645,829,1012,1192,1376};
unordered_map<U,int> qbank;unordered_map<U,int> exactone;vector<pair<int,U>> qs[14];
int minone[14];long long recomputed=0,lookups=0,twoHard=0;U part1=0,part2=0;
void init(string dir,string id){
 ifstream native(dir+"/observations",ios::binary);native.read((char*)obs,sizeof(obs));array<unsigned char,3> e;
 while(native.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=Mask(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream gr(dir+"/v4all");int g[4][125];for(int i=0;i<=stoi(id);i++)for(auto&a:g)for(auto&b:a)gr>>b;
 bool taken[125]{};int j=0;for(int i=0;i<125;i++)if(!taken[i]){for(auto&a:g)if(!taken[a[i]]){taken[a[i]]=true;history[j].push_back(a[i]);}++j;}
 for(j=1;j<=13;j++)minone[j]=max(guaranteed[j]+1,minima[j]);
 ifstream qf(dir+"/qbank"+id);U q,l,h;int c;while(qf>>q>>c>>l>>h){qbank[q]=c;qs[popcount(q)].emplace_back(c,q);minone[popcount(q)]=min(minone[popcount(q)],c);}
 for(auto&v:qs)sort(v.begin(),v.end());
}
int oneDFS(U f,Mask ban,array<int,13>&chosen,int n){
 if(!f){int c=0;for(int k=0;k<n;k++){Obs u{};for(int h=0;h<n;h++)for(int j=0;j<4;j++)u[j]|=obs[chosen[k]][chosen[h]][j];for(U b:u)c+=popcount(b);}return c;}
 int b=countr_zero(f);int val=INF;for(auto p:history[b]){
 if((ban>>p)&1)continue;Mask v=ban;for(int j=0;j<n;j++)v|=bad[p][chosen[j]];chosen[n]=p;val=min(val,oneDFS(f&(f-1),v,chosen,n+1));if(!n)break;}return val;
}
int one(U q,int cap){
 if(!q || popcount(q)>13 || minone[popcount(q)]>cap)return INF;auto p=qbank.find(q);if(p!=qbank.end())return p->second;
 if(guaranteed[popcount(q)]>=cap)return INF;
 auto it=exactone.find(q);if(it!=exactone.end())return it->second;
 array<int,13>chosen;++recomputed;return exactone[q]=oneDFS(q,0,chosen,0);
}
int leaf(U f,int z,int cap){++lookups;
 if(!K)return z?INF:0;if(K==1){part1=f;part2=0;return 4*one(f,cap/4);}
 int bound=cap/4,ret=INF;
 for(int a=max(1,z-13);a<=z/2;a++){int b=z-a;if(minone[a]+minone[b]>bound)continue;
  for(int each=0;each<(a!=b?2:1);each++){int u=each?b:a,v=z-u;
   for(auto [c,q]:qs[u]){if(c+minone[v]>bound)break;if(q&~f)continue;int other=one(f^q,bound-c);if(c+other<ret){ret=c+other;part1=q;part2=f^q;}}
  }
  int aboveA=max(minima[a],guaranteed[a]+1),aboveB=max(minima[b],guaranteed[b]+1);
  if(aboveA+aboveB<=bound){++twoHard;
   for(U q=f;q;q=(q-1)&f){if(popcount(q)!=a||qbank.count(q)||qbank.count(f^q))continue;
    if(a==b&&q>(q^f))continue;int v=one(q,bound-aboveB);if(v>bound-aboveB)continue;int w=one(q^f,bound-v);
    if(v+w<ret){ret=v+w;part1=q;part2=q^f;}}
  }
 }
 return 4*ret;
}
