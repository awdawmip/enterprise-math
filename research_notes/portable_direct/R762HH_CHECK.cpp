// R762HH: exact positive-source parity/balancing tests, C++17.
// Every element of a multiset is a distinct named occurrence, even if its mask repeats.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
using u64=uint64_t;
int bitcount(int x){return __builtin_popcount((unsigned)x);}
u64 pack(int mask){u64 x=0;for(int i=0;i<6;i++)if(mask>>i&1)x+=1ULL<<(6*i);return x;}
// Exact split into signed zero-sum groups. 6-bit lanes are safe through 24 occurrences.
bool balanced(const vector<int>& word){
 int m=(int)word.size(),h=m/2,degree[6]={};
 for(int s:word)for(int i=0;i<6;i++)degree[i]+=(s>>i)&1;
 u64 target=0;for(int i=0;i<6;i++){if(degree[i]&1)return false;target+=(u64)(degree[i]/2)<<(6*i);}
 vector<u64> left(1<<h),right(1<<(m-h));
 for(int b=1;b<(int)left.size();b++){int j=__builtin_ctz((unsigned)b);left[b]=left[b^(1<<j)]+pack(word[j]);}
 for(int b=1;b<(int)right.size();b++){int j=__builtin_ctz((unsigned)b);right[b]=right[b^(1<<j)]+pack(word[h+j]);}
 sort(left.begin(),left.end());
 for(u64 y:right){bool fits=true;for(int i=0;i<6;i++)if(((y>>(6*i))&63)>((target>>(6*i))&63))fits=false;
  if(fits&&binary_search(left.begin(),left.end(),target-y))return true;
 }return false;
}
vector<int> word;
long long total=0, parity_ok=0, unbalanced=0;int mlimit=0, axes=0;
void enumerate(const vector<int>& types,int start,int remaining){
 if(!remaining){total++;int parity=0;for(int s:word)parity^=s;
  if(parity==0){parity_ok++;if(!balanced(word)){
    unbalanced++;if(axes==6){if(word.size()!=4)abort();for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(bitcount(word[i]&word[j])!=1)abort();}
  }}return;}
 for(int j=start;j<(int)types.size();j++){word.push_back(types[j]);enumerate(types,j,remaining-1);word.pop_back();}
}
void multiset_runs(){
 for(axes=5;axes<=6;axes++){
  vector<int> types;for(int s=0;s<(1<<axes);s++)if(bitcount(s)==3)types.push_back(s);
  for(mlimit=2;mlimit<=(axes==5?12:4);mlimit+=2){total=parity_ok=unbalanced=0;enumerate(types,0,mlimit);
   cout<<"MULTISET axes="<<axes<<" m="<<mlimit<<" total="<<total<<" parity="<<parity_ok<<" unbalanced="<<unbalanced<<"\n";
   if(axes==5&&unbalanced)abort();if(axes==6&&mlimit==4&&unbalanced!=30)abort();
  }
 }
}
void witness(){
 vector<int> ports={3,5,9,12,10,18,3}, supports={7,13,13,14,26,19},signs={-1,-1,1,1,-1,1};
 int parity=0,degree[6]={};for(size_t i=0;i<supports.size();i++){
  int a=ports[i],b=ports[i+1];if(bitcount(a)!=2||bitcount(b)!=2||bitcount(a&b)!=1||(a|b)!=supports[i])abort();
  parity^=supports[i];for(int j=0;j<6;j++)degree[j]+=signs[i]*((supports[i]>>j)&1);
 }
 if(parity!=0||!balanced(supports))abort();for(int j:degree)if(j!=0)abort();
 int union_mask=0,inter_mask=63;for(int s:supports){union_mask|=s;inter_mask&=s;}
 if(union_mask!=31||inter_mask!=0)abort();
 vector<int> pasch={22,25,37,42};int p=0;for(int s:pasch)p^=s;
 if(p!=0||balanced(pasch))abort();
 cout<<"WITNESS port_closed=1 parity=0 union=31 intersection=0 zero_signed_cell=1 pasch_nonbalance=1\n";
}
int main(){multiset_runs();witness();cout<<"PASS\n";}
