#include <iostream>
#include <cmath>

bool isprime(int num){
    if(num%2==0)
    return false;
    for(int i=3;i<=sqrt(num);i+=2){
        if(num%i==0)
            return false;
    }
    return true;
}

int main(){
    // as 2 is the only even prime number
    long long int res=2;
    for(int i=3;i<2e6;i+=2)
        if(isprime(i))
            res+=i;
    std::cout<<res<<std::endl;
}