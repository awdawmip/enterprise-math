// PREFIX-933 independent exhaustive all-361 bit-pair test and W2 reduction checker.
// g++ -O3 -std=c++17 PREFIX933_R6_FOUR_A_FULL_CROSSCHECK.cpp -o full
// ./full W2.bin D4.bin W4_full.bin
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using u64=uint64_t;
int main(int argc,char**argv){
 if(argc!=4)return 2;constexpr int Q=262145,M=131072;
 vector<u64>all,inside,boundary;all.reserve(36000000);inside.reserve(34000000);boundary.reserve(2000000);
 u64 raw=0,ri=0,rb=0;
 for(int a=Q;a<=524287;a+=2){int x=4*a;u64 off=(u64)(a-Q)/2*M;
  for(int j=0;j<=18;j++){int y=x^(1<<j);
   for(int i=0;i<=18;i++){int d=y-(1<<i);if(d<=0)return 3;
    for(int t=1;t<=8;t++){if(d%t)continue;int b=d/t;if(b<Q||b>524287||!(b&1))continue;
     if(y%b!=(1<<i)%b)return 4;u64 id=off+(b-Q)/2;all.push_back(id);raw++;
     if(i&&j){inside.push_back(id);ri++;}else{boundary.push_back(id);rb++;}
    }
   }
  }
 }
 auto dedup=[](vector<u64>&a){sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());};
 dedup(all);dedup(inside);dedup(boundary);
 ifstream f(argv[1],ios::binary);u64 x;vector<u64>W2;while(f.read((char*)&x,8))W2.push_back(x);
 if(W2.size()!=30211412)return 5;
 for(u64 z:inside)if(!binary_search(W2.begin(),W2.end(),z))return 6;
 ifstream d(argv[2],ios::binary);vector<u64>D4;while(d.read((char*)&x,8))D4.push_back(x);
 if(boundary!=D4)return 7;
 u64 both=0,outsideW2=0;
 for(u64 z:all){if(binary_search(inside.begin(),inside.end(),z)&&binary_search(boundary.begin(),boundary.end(),z))both++;
  if(!binary_search(W2.begin(),W2.end(),z))outsideW2++;
 }
 cout<<"raw="<<raw<<" unique="<<all.size()<<" interior_raw="<<ri<<" interior_unique="<<inside.size()
 <<" boundary_raw="<<rb<<" boundary_unique="<<boundary.size()<<" intersection="<<both<<" outsideW2="<<outsideW2<<'\n';
 ofstream o(argv[3],ios::binary);for(u64 z:all)o.write((char*)&z,8);
}
