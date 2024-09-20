Python script to change DNA sequence to pre-mRNA and Mature mRNA

Solid Base Assumptions:
1. I am assuming that the DNA sequence is a sense strand, (nontemplate), so replacing T with U will
be optimal.
2. Promoter Sequence consists of exactly TATAAA. The transcription starts exactly 20 base pair
before this sequence. Also, TATAAA is not included.
3. The terminator sequence consists of exactly CCGCGG and the transcription includes the
terminator sequence till the last character. Here CCGCGG is being included
4. A ‘G’ guanine nucleotide is added to 5’ end pre-mRNA to protect it from degradation.
5. A poly(A) tail is added to the 3’end, here I will be adding 5 A at the end.
6. 5’ splicing site (intron start). Following are possible 4 consensus
7. CAGGUAAGU CAGGUGAGU AAGGUAAGU AAGGUGAGU
8. 3’ splicing site(intro stop) Following is the consensus CAGG.
9. Start Codon is AUG (not required here since we are not translating but only transcribing)
10. Stop Codon is UAA, UAG, UGA
11. Region before the Start codon is 5’ UTR and Region after the stop codon is 3’UTR
12. Mature mRNA retains the cap ‘G’ and poly(A) tail. Refer to the slides given below.
Input Taken: A txt file with a Eukaryotic_gene_sequence.
Validation Step: make sure the file contains the DNA sequence and not the RNA sequence.
Output Required: pre-mRNA sequence and Mature mRNA sequence. I will save them into a file and print
them on the console.



Pseudocode:
1. Start
2. Open the txt file which contains the sequence ( skip the header of the file )
3. Store the DNA sequence into a string variable.
4. Validate if it is a DNA sequence or not, if not show a error message to the user.
5. If the valid sequence, find the TATAAA block in the sequence.
6. Once the index of the last A in red color is known, add +20 in the index from where the
transcription will begin.
7. Find the index of the terminator sequence's last character. CCGCGG , the index of the last G in
red color.
8. Create an empty string to store the pre-mRNA sequence.
9. Run a for loop from the index of transcription begin site till the terminator index.
10. Append all the characters to the pre-mRNA sequence except when encountered with T replace it
with U.
11. Exit the loop.
12. Store the pre-mRNA sequence in a file, and display the output on the screen.
13. Create an empty string unprocessed-mRNA, and assign it with G.
14. Append the pre-mRNA to the unprocessed-mRNA sequence thus adding the G at the start.
15. Append 5 character poly(A) tail at the end thus adding the poly(A) sequence at the end.
16. Create an empty string Mature mRNA.
17. Run the for loop from the index at the start of unprocessed pre-mRNA
18. Start appending the characters, except remove the introns,
19. If you encounter any of the 4 consensus
20. CAGGUAAGU CAGGUGAGU AAGGUAAGU AAGGUGAGU append till the index of the
first G occurrence. After the index of the second G, search for CAGG, which marks the end of
introns, and start appending again from the second G, of CAGG thus skipping introns.
21. Exit the loop
22. Display the mature mRNA
23. Store the strings in a file.
24. End
