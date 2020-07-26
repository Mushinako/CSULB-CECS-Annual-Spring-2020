#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

void isPrime(int n, std::vector<int> &primes)
{
    int top = std::floor(std::sqrt(n));
    for (auto i = primes.begin(); i != primes.end(); ++i)
    {
        if (*i > top)
        {
            primes.push_back(n);
            return;
        }
        if (n % *i == 0)
            return;
    }
}

int main()
{
    size_t top;
    std::cout << "Upper limit: ";
    std::cin >> top;
    std::vector<int> primes{2, 3};
    for (size_t i = 4; i <= top; ++i)
    {
        isPrime(i, primes);
    }
    std::cout << primes.size() << std::endl;
    for (auto i = primes.begin(); i != primes.end(); ++i)
        std::cout << *i << ' ';
    std::cout << std::endl;
    unsigned long long int sum = 0;
    for (auto i = primes.begin(); i != primes.end(); ++i)
        sum += *i;
    // sum = std::accumulate(primes.begin(), primes.end(), 0);
    std::cout << sum << std::endl;
}