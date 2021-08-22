#include <string.h>
#include <stdlib.h>
#include <stdio.h>

static char* tokenize(char*, long);
static void generate_binary(char*);

int main(int argc, char *argv[]) {

    if (argc != 2) {
        fprintf(stderr, "usage: python3 assembler.py codeFile.s\n");
        exit(1);
    }
    

    printf("assembling: %s\n", argv[1]);

    FILE* assembly_file = fopen(argv[1], "rb");
    long fsize;
    
    // Get length of file by going to the end and reading the number of bytes
    fseek(assembly_file, 0, SEEK_END);
    fsize = ftell(assembly_file);
    // Set the file position indicator to the beginning
    rewind(assembly_file);

    char* assembly_code = malloc(sizeof(char) * fsize);
    // Read file into assembly code
    fread(assembly_code, sizeof(char), fsize, assembly_file);
    fclose(assembly_file);
    
    // Tokenize the input (and free the allocated space)
    char* assembly_tokens = tokenize(assembly_code, fsize);

    // Print out tokens
    for (int i=0; i<strlen(assembly_tokens); i++)
        printf("%c", assembly_tokens[i]);

    // Generate binary code (and free tokens allocated space)
    unsigned short* binary_code = generate_binary(assembly_tokens);
    
    return 0;
}

#define VALID_TOKENS "\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#:;"

static char* tokenize(char* input, long size) {

    // Allocate space for the tokens
    char* tokens = malloc(sizeof(char) * size);

    long ntokens = 0;

    for (int i=0; i<size; i++)
        // Tokens are valid and there's no two \n in a row
        if (strchr(VALID_TOKENS, input[i]) &&
                (input[i] != '\n' || tokens[ntokens-1 >= 0 ? ntokens-1 : 0] != '\n'))
            tokens[ntokens++] = input[i];
            
    // \n is the last token
    if (tokens[ntokens-1] != '\n') tokens[ntokens++] = '\n';
    // Tokens is a null terminated string
    tokens[ntokens] = '\0';

    free(input);

    return tokens;
}

static unsigned short* generate_binary(char* tokens) {

    int ninstructions = 0;
    // Count number of \n that define the end of an instruction
    for (int i=0; tokens[i] != '\0'; i++)
        if (tokens[i] == '\n')
            ninstructions++;

    // Each instruction also has data associated
    unsigned short instructions_with_data[] = malloc(sizeof(unsigned short) * ninstructions);

    // number of instructions with data;
    int niwd = 0;

    // Line counter and instruction counter
    int lc = 0, ic = 0;

    // Maybe allocating as much space for labels as there are instructions would be a bad idea for big files
    // and possibly a list structure would be better
    int labels[]; = malloc(sizeof(int) * ninstructions);


    char* as_line = strtok(tokens, "\n");
    
    while (as_line != NULL) {

        lc++;

        if (as_line[0] != '#' && as_line != ';') {


            instructions_with_data[niwd++] = binfrom_instr(as_line);

        }

        strtok(NULL, "\n");
    }

    free(labels);
    free(tokens);

    return instructions_with_data;

}
