#include <stdio.h>
#include <string.h>
#include <math.h>

int digPow(int n, int p)
{
    // First separate out all the digits, raise them to p (first digit) then p+1 etc until the end.
    // Once you have the sum, divide by to see if a K exists (a positive integer so int or float).
    char nDigits[12];

    snprintf(nDigits, sizeof(nDigits), "%d", n);
    int power = p;
    int lengthOfN = strlen(nDigits);
    int total = 0;

    for (int i = 0; i < lengthOfN; i++)
    {
        total += pow(nDigits[i] - '0', power);
        power++;
    }
    float floatPotentialK = (float)total / n;

    printf("%f \n", floatPotentialK);
    int intPotentialK = (int)floatPotentialK;
    printf("%i \n", intPotentialK);

    if (floatPotentialK == intPotentialK)
    {
        return intPotentialK;
    }

    return -1;
}

int main(int argc, char const *argv[])
{
    printf("\nTotal: %d\n", digPow(89, 1));
    return 0;
}
