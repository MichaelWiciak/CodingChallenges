#include <string.h>

// do not allocate memory for return value
// assign to the provided pointer `str_out`
// it has room for the worst-case scenario, `strlen(str_in) + 1`
void remove_parentheses(const char *str_in, char *str_out)
{
    int in_counter = 0;
    int out_counter = 0;
    int lengthInput = strlen(str_in);
    char characterInQuestion = '\0';
    int out_index = 0;
    for (int i = 0; i < lengthInput; i++)
    {
        characterInQuestion = str_in[i];
        if (characterInQuestion == '(')
        {
            in_counter++;
        }
        else if (characterInQuestion == ')')
        {
            out_counter++;
        }

        if (in_counter == out_counter && in_counter != 0 && out_counter != 0)
        {
            in_counter = 0;
            out_counter = 0;
        }
        else if (in_counter == 0 && out_counter == 0)
        {
            str_out[out_index] = characterInQuestion;
            out_index++;
        }
    }

    str_out[out_index] = '\0';
}

int main(int argc, char const *argv[])
{
    char *test_data = "example(unwanted thing)example";
    char test_output[1000];
    remove_parentheses(test_data, test_output);
    return 0;
}
