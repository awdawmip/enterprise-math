// Independent enumeration of 5/6/7 distinct keys using generated 24-bit support masks.
// g++ -std=c++17 -O3 VERIFY_EC49FGK_CPP.cpp -o verify_cover
// ./verify_cover EC49FGK_key_masks.txt
#include <cstdint>
#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
#include <stdexcept>
using namespace std;
int main(int argc,char**argv){
 if(argc!=2)throw runtime_error("usage: verify_cover key_masks.txt");
 ifstream f(argv[1]);if(!f)throw runtime_error("bad mask file");
 vector<tuple<int,int,int,uint32_t>> data;int x,y,z;uint32_t m;
 while(f>>x>>y>>z>>m)data.emplace_back(x,y,z,m);
 if(data.size()!=94)throw runtime_error("expected 94 keys");
 uint32_t mandatory=0;vector<uint32_t> rest,omit;
 bool k21=false,k30=false,k31=false;
 for(auto [a,b,c,mask]:data){
  if(a==2&&b==1&&c==1){k21=true; mandatory|=mask;}
  else if(a==3&&b==0&&c==1){k30=true; mandatory|=mask;}
  else {rest.push_back(mask);if(a==3&&b==1&&c==1)k31=true;
        else omit.push_back(mask);}
 }
 if(!k21||!k30||!k31||rest.size()!=92||omit.size()!=91)
  throw runtime_error("mandatory key catalogue mismatch");
 constexpr uint32_t FULL=(1u<<24)-1;
 uint64_t n5=0,n6=0,n7=0,n7omit=0;
 for(size_t a=0;a<rest.size();++a)for(size_t b=a+1;b<rest.size();++b)
 for(size_t c=b+1;c<rest.size();++c){
  uint32_t m3=mandatory|rest[a]|rest[b]|rest[c];n5+=(m3==FULL);
  for(size_t d=c+1;d<rest.size();++d){
   uint32_t m4=m3|rest[d];n6+=(m4==FULL);
   for(size_t e=d+1;e<rest.size();++e)n7+=((m4|rest[e])==FULL);
  }
 }
 for(size_t a=0;a<omit.size();++a)for(size_t b=a+1;b<omit.size();++b)
 for(size_t c=b+1;c<omit.size();++c)for(size_t d=c+1;d<omit.size();++d)
 for(size_t e=d+1;e<omit.size();++e)
  n7omit+=((mandatory|omit[a]|omit[b]|omit[c]|omit[d]|omit[e])==FULL);
 cout<<"EXACT_5 "<<n5<<"\nEXACT_6 "<<n6<<"\nEXACT_7 "<<n7
 <<"\nSEVEN_WITHOUT_3_1_1 "<<n7omit<<"\nSEVEN_WITH_3_1_1 "<<(n7-n7omit)<<"\n";
 return (n5==16&&n6==2004&&n7==108434&&n7omit==1956)?0:2;
}
