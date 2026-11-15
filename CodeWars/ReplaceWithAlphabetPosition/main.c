#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int returnAlphabetPosition(char c)
{
    c = (unsigned char)tolower(c);
    if (c <= 'z' && c >= 'a')
    {
        return (c - 'a') + 1;
    }
    return -1;
}

// returned string has to be dynamically allocated and will be freed by the caller
char *alphabet_position(const char *text)
{
    char *outputString = malloc(sizeof(char));
    if (outputString == NULL)
    {
        return 1;
    }

    outputString[0] = '\0';

    int lengthString = strlen(text);
    char position = -1;
    // for each character, lowercase it, query a hashmap with 'letter':'number' and construct the string.
    for (int i = 0; i < lengthString; i++)
    {
        position = returnAlphabetPosition(text[i]);
        if (position != -1)
        {
            strncat(output, position, sizeof(position));
        }
    }
    return NULL;
}

int main(void)
{
    char *result = alphabet_position("hello");
    free(result);
    return 0;
}