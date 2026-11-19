// R5: exact 14-label support dominance certificate across all 1,906 classes.
// Requires frozen window_adj.bin and CENSUS_14_SIGNATURES.cpp output.
#define main previous_solver_main
#include "R5_FOURTEEN_F8_ONE.cpp"
#undef main
bool action_dominates(const Act&a,const Act&b){
 if(a.cost>b.cost)return false;
 for(int x:a.masks){
  bool found=false;
  for(int y:b.masks)if((x&y)==x){found=true;break;}
  if(!found)return false;
 }
 return true;
}
bool dominates(const Sig&a,const Sig&b){
 for(const auto&bb:b){
  bool found=false;
  for(const auto&aa:a)if(action_dominates(aa,bb)){found=true;break;}
  if(!found)return false;
 }
 return true;
}
int swap_extras(int x){
 int u=(x>>12)&1,v=(x>>13)&1;
 return (x&~(3<<12))|(u<<13)|(v<<12);
}
int main(){
 ifstream fi("window_adj.bin",ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 fi.read((char*)adj.data(),adj.size());if(fi.gcount()!=(streamsize)adj.size())return 2;
 ifstream in("R5_14_CLASS_REPS.csv");string line;getline(in,line);
 vector<pair<int,int>> reps;vector<int> multiplicity;vector<Sig> sig,swapped;
 while(getline(in,line)){
  replace(line.begin(),line.end(),',',' ');istringstream row(line);
  int id,u,v,n;row>>id>>u>>v>>n;
  if(id!=(int)reps.size())return 3;
  reps.push_back({u,v});multiplicity.push_back(n);
  sig.push_back(signature(adj,u,v));
  swapped.push_back(sig.back());
  for(auto&a:swapped.back())for(int&m:a.masks)m=swap_extras(m);
 }
 if(sig.size()!=1906)return 4;
 const vector<int> benchmarks={0,1,2,10,709,1281,1362,1905,206,1048,1199,1205,616,601,929,935,15,693,220,610,846,1278};
 ofstream out("R5_F8_DOMINANCE_COVERAGE_22.csv");
 out<<"class,u,v,members,certified,benchmark_class\n";
 int nc=0,np=0;
 for(int i=0;i<sig.size();i++){
  int witness=-1;
  for(int b:benchmarks)if(dominates(sig[i],sig[b])||dominates(sig[i],swapped[b])){witness=b;break;}
  if(witness>=0){nc++;np+=multiplicity[i];}
  out<<i<<","<<reps[i].first<<","<<reps[i].second<<","<<multiplicity[i]<<","<<(witness>=0)<<","<<witness<<"\n";
 }
 out.flush();cout<<"CERTIFIED_CLASSES="<<nc<<" CERTIFIED_PAIRS="<<np
                 <<" UNRESOLVED_CLASSES="<<1906-nc<<" UNRESOLVED_PAIRS="<<29646-np<<"\n";
 return nc==836&&np==20159?0:5;
}
