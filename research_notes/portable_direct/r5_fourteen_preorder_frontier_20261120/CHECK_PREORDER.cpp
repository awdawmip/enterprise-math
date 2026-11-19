// Frozen R5 14-label priced-joint-support preorder census.
// Compile in this research directory; source precondition: frozen window_adj.bin.
#define main previous_solver_main
#include "../r5_fourteen_dominance_20261120/R5_FOURTEEN_F8_ONE.cpp"
#undef main
bool action_leq(const Act&a,const Act&b){
 if(a.cost>b.cost)return false;
 for(int x:a.masks){bool found=false;for(int y:b.masks)if((x&y)==x){found=true;break;}if(!found)return false;}
 return true;
}
bool preorder(const Sig&a,const Sig&b){
 for(const auto&bb:b){bool found=false;for(const auto&aa:a)if(action_leq(aa,bb)){found=true;break;}if(!found)return false;}
 return true;
}
int swap_extra(int x){int a=(x>>12)&1,b=(x>>13)&1;return(x&~(3<<12))|(a<<13)|(b<<12);}
struct C{int u,v,members;Sig a,b;};
string fingerprint(const Sig&s){string t;for(const auto&a:s){t+=to_string(a.cost)+":";for(int m:a.masks)t+=to_string(m)+",";t+=";";}return t;}
int main(){
 ifstream f("window_adj.bin",ios::binary);vector<uint8_t>adj((size_t)Q*N*N);f.read((char*)adj.data(),adj.size());if(f.gcount()!=(streamsize)adj.size())return 2;
 bool used[N]={};for(int h:seed)used[h]=true;
 unordered_map<string,int>ids;vector<C>cl;
 for(int u=0;u<N;u++)if(!used[u])for(int v=u+1;v<N;v++)if(!used[v]){
  auto a=signature(adj,u,v);auto key=fingerprint(a);auto it=ids.find(key);int id;
  if(it==ids.end()){id=cl.size();ids[key]=id;auto b=a;for(auto&act:b)for(int&m:act.masks)m=swap_extra(m);cl.push_back({u,v,0,move(a),move(b)});}
  else id=it->second;
  cl[id].members++;
 }
 int n=cl.size();if(n!=1906)return 3;
 vector<vector<uint8_t>>e(n,vector<uint8_t>(n));int edges=0;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++){
  e[i][j]=preorder(cl[i].a,cl[j].a)||preorder(cl[i].a,cl[j].b);
  edges+=e[i][j];
 }
 vector<int>par(n);iota(par.begin(),par.end(),0);
 auto find=[&](int i){while(par[i]!=i){par[i]=par[par[i]];i=par[i];}return i;};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(e[i][j]&&e[j][i]){
  int a=find(i),b=find(j);if(a!=b)par[a]=b;
 }
 set<int>scc,sinks;int sinkMembers=0;
 for(int i=0;i<n;i++){
  scc.insert(find(i));bool out=false;
  for(int j=0;j<n;j++)if(e[i][j]&&!e[j][i]){out=true;break;}
  if(!out){sinks.insert(find(i));sinkMembers++;}
 }
 const int old[]={0,1,2,10,709,1281,1362,1905,206,1048,1199,1205,616,601,929,935,15,693,220,610,846,1278};
 const int additions[]={295,354,291};
 int oc=0,op=0,nc=0,np=0;
 for(int i=0;i<n;i++){
  bool past=false,current=false;
  for(int j:old)if(e[i][j])past=true;
  current=past;
  for(int j:additions)if(e[i][j])current=true;
  if(past){oc++;op+=cl[i].members;}
  if(current){nc++;np+=cl[i].members;}
 }
 if(cl[295].u!=19||cl[295].v!=88||cl[354].u!=21||cl[354].v!=85||cl[291].u!=19||cl[291].v!=81)return 4;
 cout<<"classes="<<n<<" edges="<<edges<<" scc="<<scc.size()<<" sink_scc="<<sinks.size()<<" sink_classes="<<sinkMembers
 <<" old_classes="<<oc<<" old_pairs="<<op<<" new_classes="<<nc<<" new_pairs="<<np<<"\n";
 return (edges==38127&&scc.size()==1066&&sinks.size()==333&&sinkMembers==367&&oc==836&&op==20159&&nc==876&&np==21301)?0:5;
}
