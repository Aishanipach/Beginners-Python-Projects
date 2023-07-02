#note to Viewer: this is just a small collection of functions specific for bioinformatic genomic usage.
#they are fun and help intertwine computer science and genetics! 
#hope you have fun!


def hamming_distance(seq1, seq2):
    '''
    Function will determine the number of differences in genomic sequence when comparing two individual sequences. 

    Arg: Two separate sequences (str)
    Output: Number of differences (int)

    Example: hamming_distance("ATCTGGT","ATGAAGT")
            --> 3 
    '''

    tempo_result = zip(seq1, seq2)
    seq_counter = 0
    
    for i, j in tempo_result:
        if i != j:
            seq_counter += 1
    
    return seq_counter 



def seq_encode(seq):
    '''
    Function to encode a seqence of genomic characters. 

    Arg: Sequence of interest (str)
    Output: Encoded version of sequence (str)

    Example: seq_encode('CTTTCCCAAAG$$AAT')
            --> 'C3T3C3AG2$2AT'

    '''
    #initialize an empty list.  
    encoded_lst = []
    count = 0 
    
    #we need to start at the beginning of the string. 
    for index, char in enumerate(seq):
        # print(char)
        # print(index)
        if index == 0: #if we're at the beginning of the string. 
            current_char = seq[index] #set the current character to euqal whatever value is in that character.  
            count = 1
            # print(current_char)
        if index != 0: #else if the character is NOT the first character, we need to check if it's the same as the previous char.    
            current_char = seq[index]
            previous_char = seq[index - 1] 
            if current_char == previous_char:  #if true continue to count. 
                count += 1
                # print(index)
                # print(current_char)
                # encoded_list.append(current_char)     
            if current_char != previous_char: #if the next character is NOT the same character as the previous one. 
                #we need to stop the loop and append to our encoded_list.  
                #we don't want to include the number 1. 
                if count == 1:
                    encoded_lst.append(previous_char)
                else:
                    encoded_lst.append(str(count) + previous_char) 
                count = 1 
            if index == len(seq) - 1: #this is to include the very last character in the string. 
                #we don't want to include the number 1 here too. So need to exclude it. 
                if count == 1:
                    encoded_lst.append(current_char)
                else:
                    encoded_lst.append(str(count) + current_char) 
   
    encoded_result = "".join(encoded_lst)
                
    # return type(encoded_string)
    return encoded_result

def seq_decode(seq):
    '''
    Function to decode a sequence of genomic characters. 

    Arg: Sequence of interest (str)
    Output: Decoded version of sequence (str)

    Example: seq_encode('C3T3C3AG2$2AT')
            --> 'CTTTCCCAAAG$$AAT'
    '''

    decode_lst = [] #tempo holding list 
    skip_char = False #don't want to skip the first char

    for index, char in enumerate(seq):

        if skip_char == True:
            skip_char = False #change back to False 
            continue #skip the present char thru continue 

        if skip_char == False:
            if char.isnumeric():
                decode_lst.append(int(char)*seq[index + 1]) #this char is an integer
                skip_char = True #skip next char 
            elif char.isalpha():
                decode_lst.append(char) #just appending a str
                skip_char = False 
            else: #including all symbols 
                decode_lst.append(char)
                skip_char = False 
    
    decoded_result = "".join(decode_lst) #combine all str values into one str
    return decoded_result

        


    
              