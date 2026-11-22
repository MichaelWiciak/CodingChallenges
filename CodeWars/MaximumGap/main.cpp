#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int maxGap(vector<int> numbers)
{

    sort(numbers.begin(), numbers.end(), greater<int>());
    for (auto i : numbers)
    {
        cout << i << ' ';
    }
    cout << endl;
    int len_vector = numbers.size();
    int max_gap = 0;
    int temp = 0;
    for (int i = 0; i < len_vector - 1; i++)
    {
        cout << "i:" << i << " numbers[i] " << numbers[i] << " i+1 " << numbers[i + 1] << endl;
        temp = numbers[i] - numbers[i + 1];
        if (temp > max_gap)
        {
            max_gap = temp;
        }
        cout << max_gap << endl;
    }

    return max_gap;
}

int main(int argc, char const *argv[])
{
    cout << maxGap({13, 10, 2, 9, 5}) << " = 4" << endl;
    cout << maxGap({13, 3, 5}) << " = 8" << endl;
    cout << maxGap({24, 299, 131, 14, 26, 25}) << " = 168" << endl;
    return 0;
}
