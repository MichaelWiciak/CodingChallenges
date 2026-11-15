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
    int lengthString = strlen(text);
    char *outputString = malloc(lengthString * 3 + 1);
    if (outputString == NULL)
    {
        return NULL;
    }

    outputString[0] = '\0';
    int position = 0;
    char temp[16];
    int first = 1;
    // for each character, lowercase it, query a hashmap with 'letter':'number' and construct the string.
    for (int i = 0; i < lengthString; i++)
    {
        position = returnAlphabetPosition(text[i]);
        if (position != -1)
        {
            if (first == 0)
            {
                strcat(outputString, " ");
            }
            // need to allocate max two bites for the char as each ascii is 8 bits
            snprintf(temp, sizeof(temp), "%d", position);
            strcat(outputString, temp);
            first = 0;
        }
    }

    printf("%s\n", outputString);
    return outputString;
}

int main(void)
{
    char *result = alphabet_position("hello");
    free(result);
    return 0;
}