// Integer-only checker, independent of the LP and cover implementations.
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
using namespace std;
using U=uint64_t;using M=__uint128_t;using L=long long;
struct Row{U low,high;unsigned cost,size;};
int first(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 ifstream job(argv[1]),bank(argv[2],ios::binary),weights(argv[3]);
 int id,k,budget,n;job>>id>>k>>budget>>n;M region=0;for(int i=0,p;i<n;i++){job>>p;region|=M(1)<<p;}
 assert(__builtin_popcountll(U(region))+__builtin_popcountll(U(region>>64))==n);
 L denominator,class_weight,point_weight[125];weights>>denominator>>class_weight;assert(denominator>0&&denominator<=1000000000LL);
 assert(class_weight>-1000000000000LL&&class_weight<1000000000000LL);
 for(L&w:point_weight){weights>>w;assert(w>-1000000000000LL&&w<1000000000000LL);}
 L numerator=k*class_weight;for(M m=region;m;m&=m-1)numerator+=point_weight[first(m)];
 assert(numerator>denominator*budget);
 Row row;L count=0,minimum_slack=numeric_limits<L>::max();
 while(bank.read((char*)&row,sizeof(row))){
  M m=M(row.low)|(M(row.high)<<64);assert((m&region)==m);
  assert(__builtin_popcountll(row.low)+__builtin_popcountll(row.high)==int(row.size));
  L left=class_weight;for(;m;m&=m-1)left+=point_weight[first(m)];
  L slack=denominator*row.cost-left;assert(slack>=0);if(slack<minimum_slack)minimum_slack=slack;count++;
 }
 assert(bank.eof());
 cout<<"{\"job\":"<<id<<",\"columns_checked\":"<<count<<",\"minimum_slack\":"<<minimum_slack<<",\"denominator\":"<<denominator<<",\"lower_numerator\":"<<numerator<<",\"budget_numerator\":"<<denominator*budget<<",\"strict_exclusion\":true}"<<endl;
}
