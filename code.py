def cyclic_rotations(T):
  """Function to output all cyclic rotations of a string

  Parameters
  ----------
  T: string
     Input string

  Returns
  -------
  permutations: list
                A list of all possible (cyclic) permutations of T
  """

  "INSERT YOUR CODE HERE"
  Td = T + '$'
  TTd = Td*2
  return [TTd[i:len(Td)+i] for i in range(len(Td))]
  #return permutations

# DO NOT DELETE THIS
print(cyclic_rotations('ACGT'))

def lexsort_list(T_list):
  """Function to produce list of lexicographically sorted elements

  Parameters
  -----------
  T_list: list of string
          A list of strings (cyclic permutations of T)
  Returns
  --------
  lexsort_l: list of string
             A list of lexicographically sorted elements
  """
  lexsort_l = sorted(T_list)

  "INSERT YOUR CODE HERE"
  return lexsort_l

# DO NOT DELETE THIS
print(lexsort_list(['ACG$', 'CG$A', 'G$AC', '$ACG']))

def bwt(T):
  """Function to produce burrows wheeler transform of a string

  Parameters
  -----------
  T: string
     Input string
  Returns
  -------
  bwt_string: string
              The burrows wheeler transform of lexT_list
  """

  rotations = cyclic_rotations(T)
  sorted_rotations = lexsort_list(rotations)
  bwt_string = ''.join([s[-1] for s in sorted_rotations])
  return bwt_string

# DO NOT DELETE THIS

print(bwt("ACAGTGAT"))

# DO NOT DELETE THIS

whywedie = "Death, in the inevitable sense we are considering in this book, is the result of aging. The simplest way to think of aging is that it is the accumulation of chemical damage to our molecules and cells over time. This damage diminishes our physical and mental capacity until we are unable to function coherently as an individual being—and then we die. I am reminded of the quote from Hemingway’s The Sun Also Rises, in which a character is asked how he went bankrupt, and he replies, 'Two ways. Gradually, then suddenly.' Gradually, the slow decline of aging; suddenly, death. The process of aging can be thought of as starting gradually with small defects in the complex system that is our body; these lead to medium-sized ones that manifest as the morbidities of old age, leading eventually to the system-wide failure that is death."

bwt_whywedie = bwt(whywedie)
bwt_whywedie

def last_to_first_string(bwt_string):
  """Function to generate the first column of the burrows wheeler (BW) matrix

  Parameters
  -----------
  bwt_string: string
              Burrows wheeler transform (last column of the BW matrix)
  Returns
  -------
  first: string
         The first column of the BW matrix
  """
  # sort all the characters of a string
  return ''.join(sorted(bwt_string))
# DO NOT DELETE THIS

last_to_first_string("T$CGATAAG")

def last_to_first_index(bwt_string):
  """Function to generate the position of where each character
  in the given string appears in the first column of the BW matrix

  Parameters
  -----------
  bwt_string: string
              Burrows wheeler transform (last column of the BW matrix)
  Returns
  -------
  index: list of positions (0-indexed)
         A list of length equal to the bwt length with the
         position of each character in the first column of
         the BW matrix
  """
  first_column = last_to_first_string(bwt_string)
  index = list()
  for character in bwt_string:
    current_index = first_column.index(character)
    index.append(current_index)
    first_column = first_column.replace(character, '1', 1)
  return index
# DO NOT DELETE THIS

last_to_first_index("T$CGATAAG")

def first_to_last_index(bwt_string):
  """Function to generate the position of the elements in the first column in the last column using
  the last column of the BW matrix.
  Parameters
  -----------
  bwt_string: string
              Burrows wheeler transform (last column of the BW matrix)
  Returns
  -------
  index: list of positions (0-indexed)
         A list of length equal to the bwt length with the
         position of each character in the first column of
         the BW matrix in the last column (see example.)
  """
  first_index = last_to_first_index(bwt_string)
  index = [ first_index.index(index) for index in range(len(first_index))]
  return index
# DO NOT DELETE THIS
first_to_last_index("T$CGATAAG")

def invert_bwt(bwt_string):
  """Function to produce burrows wheeler transform of a string

  Parameters
  -----------
  bwt_string: string
              Burrows wheeler transform
  Returns
  -------
  original_string: string
              The burrows wheeler transform of lexT_list
  """
  first_col = sorted(bwt_string)
  first_to_last = first_to_last_index(bwt_string)
  start_pointer = bwt_string.index("$")
  current_character = first_col[start_pointer]
  original_string = ""
  while current_character != "$":
    original_string += current_character
    start_pointer = first_to_last[start_pointer]
    current_character = first_col[start_pointer]
  return original_string

# DO NOT DELETE THIS
invert_bwt("T$CGATAAG")

# DO NOT DELETE THIS
bwt_whywedie

# DO NOT DELETE THIS
invert_bwt(bwt_whywedie)

# DO NOT DELETE THIS - THIS NEEDS TO HAVE BEEN EXECUTED

!pip install watermark
from watermark import watermark # DO NOT DELETE
print(watermark()) # DO NOTE DELETE

def bw_matching(firstcol_str, lastcol_str, pattern, last_to_first_idx):
  """ Given the first column along with last column of the BW matrix, and the lasttofirst indexes
  identify if the pattern can be found in the original string
  """
  top_pointer = 0
  bottom_pointer = len(lastcol_str) - 1
  while top_pointer <= bottom_pointer:
      if pattern:
          symbol = pattern[-1]
          pattern = pattern[:-1]
          temp_lastcol = lastcol_str[top_pointer : (bottom_pointer + 1)]
          if symbol in temp_lastcol:
              top_index  = temp_lastcol.index(symbol) + top_pointer
              bottom_index = len(temp_lastcol) - temp_lastcol[::-1].index(symbol) + top_pointer - 1
              top_pointer    = last_to_first_idx[top_index]
              bottom_pointer = last_to_first_idx[bottom_index]
          else:
              return 0
      else:
          return bottom_pointer - top_pointer + 1
  return 0


def bwa_search(text_string, pattern):
  """Given a string and a pattern, usw BWT to find the number of occurrences of the pattern"""
  bwt_string = bwt(text_string)
  first_col = sorted(bwt_string)
  last_to_first_idx = last_to_first_index(bwt_string)
  print(bw_matching(firstcol_str = first_col, lastcol_str = bwt_string, pattern = pattern, last_to_first_idx=last_to_first_idx))

# DO NOT DELETE
bwa_search("TCGACGAT", "CGA")

# DO NOT DELETE
bwa_search(whywedie, "Death")

# DO NOT DELETE
bwa_search(whywedie, "ing")

# DO NOT DELETE
bwa_search(whywedie, "Hemingway")

!pip install watermark
from watermark import watermark # DO NOT DELETE
print(watermark()) # DO NOTE DELETE

!wget https://hgdownload.cse.ucsc.edu/goldenpath/hg38/chromosomes/chr11.fa.gz

import gzip

def read_fasta_gz(filename):
  """Reads a fasta.gz file and returns the sequence.
  """
  with gzip.open(filename, 'rt') as f:
    lines = [line.strip() for line in f if not line.startswith('>')]
  return ''.join(lines)

sequence = read_fasta_gz('chr11.fa.gz')

sequence_sampled = sequence[51000: 61000]

pattern = "TACATTAGAAAAATAAACCATAGCCTCATCACAGGCACTTAAATACACTGAAGCTGCCAAAACAATCTATCGTTTTGCCTACGTACTTATCAAC"

# vanilla search
%time results = [i for i in range(len(sequence)) if sequence_sampled.startswith(pattern, i)]

len(results)

# do the one time operation
%time bwt_string = bwt(sequence_sampled)

# do the one time operation
%time first_col = sorted(bwt_string)

# do the one time operation
%time last_to_first_idx = last_to_first_index(bwt_string)

# do the actual bwa search
%time bw_matching(firstcol_str = first_col, lastcol_str = bwt_string, pattern = pattern, last_to_first_idx=last_to_first_idx)

