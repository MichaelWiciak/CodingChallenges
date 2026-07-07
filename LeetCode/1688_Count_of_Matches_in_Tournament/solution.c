/// Concurent Version
int numberOfMatches(int n)
{
    int output = 0;

    int exit = 0;
    while (exit == 0)
    {
        if (n == 0)
        {
            exit = 1;
        }
        else if (n == 1)
        {
            n -= 1;
        }
        else if (n % 2 == 0)
        {
            output += n / 2;
            n -= n / 2;
        }
        else
        {
            output += (n - 1) / 2;
            n -= (n - 1) / 2;
        }
    }
    return output;
}

/// Reccuring version
int numberOfMatches(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if (n % 2 == 0)
    {
        return n / 2 + numberOfMatches(n / 2);
    }
    else
    {
        return (n - 1) / 2 + numberOfMatches((n - 1) / 2 + 1);
    }
}