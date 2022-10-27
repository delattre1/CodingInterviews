
### Problem

Implement the classic method for composing secret messages called a square code.

Given a text, output the encoded version of that text.

To cipher a text using the square code you need to stack the text in the form of a rectangle and then read the columns as if it were the rows.

For example,

1. The text:
```text
"12345678"
```
Could be represented as:

```text
"123"
"456"
"78"
```

And the ciphertext would be:
```text
"14725836"
```
2. The text:
```text
"abc123defg"
```
Could be represented as:

```text
"abc"
"123"
"def"
"g"
```

And the ciphertext would be:
```text
"a1dgb2ec3f"
```

# Hints

# Solution

First, the input is normalized: the spaces and punctuation are removed
from the original text and the message is downcased.

Then, the normalized characters are broken into rows.  These rows can be
regarded as forming a rectangle when printed with intervening newlines.

For example, the sentence

```text
"If man was meant to stay on the ground, god would have given us roots."
```

is normalized to:

```text
"ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
```

The plaintext should be organized in to a rectangle.  The size of the
rectangle (`r x c`) should be decided by the length of the message,
such that `c >= r` and `c - r <= 1`, where `c` is the number of columns
and `r` is the number of rows.

Our normalized text is 54 characters long, dictating a rectangle with
`c = 8` and `r = 7`:

```text
"ifmanwas"
"meanttos"
"tayonthe"
"groundgo"
"dwouldha"
"vegivenu"
"sroots  
```

The coded message is obtained by reading down the columns going left to
right.

The message above is coded as:

```text
"imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
```

Output the encoded text in chunks that fill perfect rectangles `(r X c)`,
with `c` chunks of `r` length, separated by spaces. For phrases that are
`n` characters short of the perfect rectangle, pad each of the last `n`
chunks with a single trailing space.

```text
"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
```

Notice that were we to stack these, we could visually decode the
ciphertext back in to the original message:

```text
"imtgdvs"
"fearwer"
"mayoogo"
"anouuio"
"ntnnlvt"
"wttddes"
"aohghn "
"sseoau "
```




### Acknowledgement:

This interview came from [codesubmit.io](https://codesubmit.io/)
