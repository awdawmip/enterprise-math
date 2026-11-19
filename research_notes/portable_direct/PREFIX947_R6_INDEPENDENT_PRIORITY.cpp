// PREFIX-947 fully independent merge-by-sorted-ID audit.
// W23 source is independently verified by CSR; this program recomputes old membership
// by sorted two-way cursor merges and independently checks every NEW23 ID.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;using u64=uint64_t;
constexpr int L=262145,H=524287,C=131072;
constexpr u64 N=1ULL<<32;
int ix(int a){return (a-L)/2;}
array<uint8_t,C> inS{},inL{},inT{};
void init(){
 vector<int>S,D,Z;
 for(int b=L;b<=H;b+=2){int r=1;bool early=false,late=false;
  for(int d=1;d<=52;++d){r=2LL*r%b;bool hit=r==1||r==b-1;
   if(hit&&d<=31)early=true;else if(hit)late=true;}
  if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("BZS S,D mismatch");
 Z=D;for(int b:{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287})Z.push_back(b);
 sort(Z.begin(),Z.end());Z.erase(unique(Z.begin(),Z.end()),Z.end());
 if(Z.size()!=104)throw runtime_error("V predicate cardinality mismatch");
 for(int b:Z)inL[ix(b)]=1;
 for(int t=0;t<1024;t++)inT[(77081LL*t+12345)%C]=1;
}
bool BZS(int a,int b){return (u64)b<33*((N+a-1)/a)||(u64)a<33*((N+b-1)/b)||inS[ix(b)]||((u64)a/gcd(a,b))*b<N;}
bool V(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
struct FileSet{string name;ifstream f;u64 next=0;bool has=false;u64 prev=0;bool had=false;
 FileSet(string n):name(n),f(n,ios::binary){if(!f)throw runtime_error("missing "+n);advance();}
 void advance(){u64 x;
  if(f.read((char*)&x,8)){if(had&&x<=prev)throw runtime_error("non-increasing "+name);next=prev=x;has=had=true;}
  else {if(!f.eof())throw runtime_error("bad input "+name);has=false;}
 }
 bool contains(u64 id){while(has&&next<id)advance();return has&&next==id;}
};
int main(){init();
 vector<string>names={"PREFIX928_R6_SORTED_PAIR_IDS.bin","W2.bin","W3.bin","D4_sorted_cpp.bin","W5.bin","D6.bin","W7.bin","D8.bin","W9.bin","D10.bin","W11_REGEN.bin","W13.bin","PREFIX944_W15.bin","PREFIX944_W17.bin","PREFIX945_W19.bin","PREFIX946_W21.bin"};
 vector<string>labels={"U","W2","W3","D4","W5","D6","W7","D8","W9","D10","W11","W13","W15","W17","W19","W21"};
 vector<FileSet>files;files.reserve(names.size());for(auto &n:names)files.emplace_back(n);
 vector<u64>counts(19,0); // index0 BZS,1 U,2 V,3..17 others,18 NEW
 ifstream candidate("PREFIX947_W23.bin",ios::binary),reference("PREFIX947_NEW23.bin",ios::binary);
 if(!candidate||!reference)throw runtime_error("missing candidate or reference");
 u64 prior=0,total=0,uncov=0,id=0,last=0;bool first=true;
 while(candidate.read((char*)&id,8)){
  if(!first&&id<=last)throw runtime_error("W23 non-increasing");first=false;last=id;
  if(id>=u64(C)*C)throw runtime_error("W23 out of range");
  ++total;int a=L+2*(id/C),b=L+2*(id%C);
  int bucket=-1;
  if(BZS(a,b))bucket=0;
  else if(files[0].contains(id))bucket=1;
  else if(V(a,b))bucket=2;
  else for(int j=1;j<(int)files.size();++j)if(files[j].contains(id)){bucket=j+2;break;}
  if(bucket>=0){counts[bucket]++;prior++;}
  else {counts[18]++;uncov++;u64 exact;if(!reference.read((char*)&exact,8)||exact!=id)throw runtime_error("NEW23 byte mismatch");}
 }
 if(!candidate.eof())throw runtime_error("truncated W23 input");
 u64 trailing;if(reference.read((char*)&trailing,8))throw runtime_error("extra NEW23 IDs");
 if(total!=13041372||prior!=6551349||uncov!=6490023)throw runtime_error("priority count mismatch");
 cout<<"PREFIX947 independent W23="<<total<<" previously_covered="<<prior<<" new="<<uncov<<" all_new_IDs_equal_reference=true\n";
 cout<<"PRIORITY BZS="<<counts[0]<<" U="<<counts[1]<<" V="<<counts[2];
 for(int j=1;j<(int)labels.size();++j)cout<<" "<<labels[j]<<"="<<counts[j+2];
 cout<<" NEW="<<counts[18]<<"\nALL_INDEPENDENT_PRIORITY_ASSERTIONS_PASSED\n";
}
