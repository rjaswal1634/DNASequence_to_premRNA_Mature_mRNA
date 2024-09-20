
"""
DNA Sequence to Pre-mRNA & Mature -mRNA

The purpose of this code is to read a DNA sequence from a txt file, skipping any header information present. It will validate the sequence and then use the sequence to make pre-mRNA & Mature -mRNA.

How to Use:
Specify the correct file path where the DNA sequence is stored.

Assumptions:
- The first line of the file is a header that should be ignored.
- I am assuming that the DNA sequence is a sense strand, (nontemplate), so replacing T with U will be optimal. 
- Promoter Sequence consists of exactly TATAAA. The transcription starts exactly 20 base pairs before this sequence.  Also, TATAAA is not included. 
- The terminator sequence consists of exactly CCGCGG and the transcription includes the terminator sequence till the last character. Here CCGCGG is   included
- A ‘G’ guanine nucleotide is added to 5’ end pre-mRNA to protect it from degradation.
- A poly(A) tail is added to the 3’end, here I will be adding 5 A at the end. 
- 5’ splicing site (intron start). Following are possible 4 consensus 
    {CAGGUAAGU CAGGUGAGU AAGGUAAGU AAGGUGAGU}
- 3’ splicing site(intro stop) Following is the consensus CAGG.
- Mature mRNA retains the cap ‘G’ and poly(A) tail

Output:
    - 2 files with pre and mature mRNA 
    - sequences on the console

// Done by Rahul Chaudhari for CS325 Assignment 1.

Alerts: 
    - if running in Python 2, change the range to xrange, and print (something) to print something 
"""
import sys # usaged explained later. 

# function to read the file and put the DNA sequence into a string
def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines() # Reads all the lines at one

        # Check if the file is empty
        if len(lines) == 0: 
            print("The file is empty.")
            sys.exit()  # This will terminate any further process

        dna_sequence = ""
        print(dna_sequence)
        if len(lines) > 1: 
            # We assume if there is more than 1 line, the 1st line is the header
            for line in lines[1:]:  # This will start from the 2nd line, skipping the 1st
                stripped_line = line.strip()  # Removing whitespaces
                if stripped_line:  
                    # Check if the line is not empty, which usually happens by pressing enter
                    dna_sequence += stripped_line.upper()  
                    # appening to DNA sequence making sure its uppercase
        else:
            print("Header is missing or something wrong with file")
            sys.exit()

    return dna_sequence

def validate_dna_sequence(dna_sequence):
    valid_nucleotides = ['A', 'T', 'C', 'G']  # List of valid nucleotides
    for nucleotide in dna_sequence:
        if nucleotide not in valid_nucleotides:
            return False  
    return True


def find_promoter_and_terminator(dna_sequence):
    promoter_index = dna_sequence.find('TATAAA')
    if promoter_index == -1:
        print("Promoter sequence 'TATAAA' not found.")
        sys.exit()
    transcription_start_index = promoter_index + len('TATAAA')  + 20 
    # Our assumption of transcription site is 20 characters after it

    terminator_index = dna_sequence.find('CCGCGG')
    if terminator_index == -1:
        print("Terminator sequence 'CCGCGG' not found.")
        sys.exit()
    terminator_end_index = terminator_index + len('CCGCGG') - 1  
    # Include the last character of terminator -1 because the C index is already counted once

    return transcription_start_index, terminator_end_index

# function to transcribe 
def transcribe_dna_to_pre_mrna(dna_sequence, transcription_start_index, terminator_end_index):
    pre_mrna = ""
    for i in range(transcription_start_index, terminator_end_index + 1):
        # +1 to make sure the last character is included
        if dna_sequence[i] == 'T':
            pre_mrna += 'U'
        else:
            pre_mrna += dna_sequence[i]
    return pre_mrna

# process mRNA to mature mRNA
def process_mrna(pre_mrna):
    unprocessed_mrna = 'G' + pre_mrna + 'AAAAA'  
    # Add 'G' cap and 5 poly(A) tail as mentioned in the assumptions
    mature_mrna = ""

    i = 0
    while i < len(unprocessed_mrna):
        # Check for intron start
        if unprocessed_mrna[i:i+9] in ["CAGGUAAGU", "CAGGUGAGU", "AAGGUAAGU", "AAGGUGAGU"]:
            # takes a block of 9 characters
            # Skip to the first 'G'
            while unprocessed_mrna[i] != 'G':
                mature_mrna += unprocessed_mrna[i] # keep adding this before the G
                i += 1

            # intron start from the 2nd G, so include the 1st G
            mature_mrna += unprocessed_mrna[i]
            i += 1 # move next G
            i += 1 # Skip past the 2nd 'G'

            # Find 'CAGG' to mark the end of the intron
            while unprocessed_mrna[i:i+4] != 'CAGG':
                # takes a block of 4-character
                i += 1
            i += 3  # Skip past 'CAG' and continue to add from 2nd G. 
        else:
            mature_mrna += unprocessed_mrna[i]
            i += 1

    return mature_mrna

# fuction  write the respective sequence to the respective  file
def write_output_to_file(sequence, filename):
    with open(filename, 'w') as pre_file:
        pre_file.write(sequence)


def main():
    # File_path will store the correct file name and its path
    file_path = 'DNASequence.txt'

    # Read the DNA sequence from the file
    dna_sequence = read_dna_sequence(file_path)

    # Validate the DNA sequence 
    if not validate_dna_sequence(dna_sequence):
        print("Invalid DNA sequence check your file")
        return

    # Finding the transcription site and terminator site
    transcription_start_index, terminator_end_index = find_promoter_and_terminator(dna_sequence)

    # Transcribing DNA to pre-mRNA
    pre_mrna = transcribe_dna_to_pre_mrna(dna_sequence, transcription_start_index, terminator_end_index)
    print("Pre-mRNA Sequence:\n")
    print(pre_mrna)
    write_output_to_file(pre_mrna, "pre_mRNA.txt") # writing it into the file


    # Creating mature_mrna
    mature_mrna = process_mrna(pre_mrna)
    print("\nMature mRNA Sequence:\n")
    print(mature_mrna)
    write_output_to_file(mature_mrna, "mature_mRNA.txt") 

if __name__ == "__main__":
    main()

