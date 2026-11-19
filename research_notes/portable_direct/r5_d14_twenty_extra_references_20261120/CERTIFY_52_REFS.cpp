// Verify exact R5 D14 coverage from immutable predecessor C++ code.
// Copy R5_FOURTEEN_F8_ONE.cpp from the pinned prior source into this directory.
#define main previous_solver_main
#include "R5_FOURTEEN_F8_ONE.cpp"
#undef main
bool action_dominates(const Act&a,const Act&b){
 if(a.cost>b.cost)return false;
 for(int x:a.masks){bool ok=false;
  for(int y:b.masks)if((x&y)==x){ok=true;break;}
  if(!ok)return false;
 }return true;
}
bool pre(const Sig&a,const Sig&b){
 for(const Act&bb:b){bool ok=false;
  for(const Act&aa:a)if(action_dominates(aa,bb)){ok=true;break;}
  if(!ok)return false;
 }return true;
}
int swap_extras(int x){int a=(x>>12)&1,b=(x>>13)&1;
 return (x&~(3<<12))|(a<<13)|(b<<12);
}
int main(){
 ifstream fi("window_adj.bin",ios::binary);
 vector<uint8_t>adj((size_t)Q*N*N);
 fi.read((char*)adj.data(),adj.size());
 if(fi.gcount()!=(streamsize)adj.size())return 2;
 ifstream in("R5_14_CLASS_REPS.csv");
 string line;getline(in,line);
 vector<int> multiplicity; vector<Sig>sigs,swaps;
 while(getline(in,line)){
  replace(line.begin(),line.end(),',',' ');istringstream row(line);
  int id,u,v,n;row>>id>>u>>v>>n;
  if(id!=(int)sigs.size())return 3;
  multiplicity.push_back(n);
  sigs.push_back(signature(adj,u,v));swaps.push_back(sigs.back());
  for(auto&a:swaps.back())for(int&m:a.masks)m=swap_extras(m);
 }
 if(sigs.size()!=1906)return 4;
 const vector<int> refs={
  0,1,2,10,709,1281,1362,1905,206,1048,1199,1205,616,601,929,935,
  15,693,220,610,846,1278,295,354,291,3,368,360,1090,842,232,668,
  452,436,28,440,24,23,451,606,226,25,618,617,271,277,284,1421,
  891,430,674,1504
 };
 if(refs.size()!=52)return 5;
 int nc=0,np=0;
 ofstream out("CERTIFIED_52_CLASSES.csv");out<<"class,members,certified,dominated_reference\n";
 for(int i=0;i<(int)sigs.size();i++){
  int found=-1;
  for(int r:refs)if(pre(sigs[i],sigs[r])||pre(sigs[i],swaps[r])){found=r;break;}
  if(found>=0){nc++;np+=multiplicity[i];}
  out<<i<<","<<multiplicity[i]<<","<<(found>=0)<<","<<found<<"\n";
 }
 cout<<"D14_52 CERTIFIED_CLASSES="<<nc<<" CERTIFIED_PAIRS="<<np
     <<" UNRESOLVED_CLASSES="<<1906-nc
     <<" UNRESOLVED_PAIRS="<<29646-np<<"\n";
 return (nc==1220&&np==25896)?0:6;
}
