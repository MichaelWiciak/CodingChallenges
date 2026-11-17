#include <stdio.h>

int solution(int number)
{
    if (number < 0)
    {
        return 0;
    }
    else if (number == 1)
    {
        return 0;
    }

    int total = 0;

    for (int i = 1; i < number; i++)
    {
        if (i % 3 == 0)
        {
            total += i;
        }
        else if (i % 5 == 0)
        {
            total += i;
        }
    }

    return total;
}

int main(int argc, char const *argv[])
{
    int output = solution(5);
    printf("%i\n", output);
    return 0;
}
