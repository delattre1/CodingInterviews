<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
<summary>Table of Contents</summary>
  <ol>
    <li><a href="#problem">Problem</a></li>
    <li><a href="#additional-information">Additional information</a></li>
    <li><a href="#examples">Examples</a></li>
    <li><a href="#hints">Hints</a></li>
    <li><a href="#solution">Solution</a></li>
    <li><a href="#extra">Extra</a></li>
    <li><a href="#complexity">Complexity</a></li>
    <li><a href="#acknowledgement">Acknowledgement</a></li>
  </ol>
</details>


## Problem

Implement the classic method for composing secret messages called a square code.

Given a text, output the encoded version of that text.

To cipher a text using the square code you need to stack the text in the form of a rectangle and then read the columns as if it were the rows.

## Additional information
1. Strings may contain any valid character.
2. The plaintext should be organized in to a rectangle.  The size of the
rectangle (`r x c`) should be decided by the length of the message,
such that `c >= r` and `c - r <= 1`, where `c` is the number of columns
and `r` is the number of rows.

## Examples

1. The text:

```python
"12345678"
```
Could be represented as:

```python
"123"
"456"
"78"
```

And the ciphertext would be:

```python
"14725836"
```
2. The text:
```python
"abc123defg"
```
Could be represented as:

```python
"abc1"
"23de"
"df"
```

And the ciphertext would be:
```python
"a2db3fcd1e"
```

## Hints
1. What if you knew the number of columns of the rectangle?
2. How can you make sure that the input would contain only alfa-numeric characters?

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Solution

First, the input is normalized: the spaces and punctuation are removed
from the original text and the message is downcased.

Then, the normalized characters are broken into rows.  These rows can be
regarded as forming a rectangle when printed with intervening newlines.

For example, the sentence

```python
"If man was meant to stay on the ground, god would have given us roots."
```

is normalized to:

```python
"ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
```

Our normalized text is 54 characters long, dictating a rectangle with
`c = 8` and `r = 7`:

```python
"ifmanwas"
"meanttos"
"tayonthe"
"groundgo"
"dwouldha"
"vegivenu"
"sroots"
```

The coded message is obtained by reading down the columns going left to
right.

The message above is coded as:

```python
"imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Extra
Output the encoded text in chunks that fill perfect rectangles `(r X c)`,
with `c` chunks of `r` length, separated by spaces. For phrases that are
`n` characters short of the perfect rectangle, pad each of the last `n`
chunks with a single trailing space.

```python
"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
```

Notice that were we to stack these, we could visually decode the
ciphertext back in to the original message:

```python
"imtgdvs"
"fearwer"
"mayoogo"
"anouuio"
"ntnnlvt"
"wttddes"
"aohghn "
"sseoau "
```

## Complexity

- Time complexity would be O(c??) (where c is the number of columns of the rectangle)

- Space complexity would be O(n) (where n is the size of input string)


## Acknowledgement:

This interview came from [codesubmit.io](https://codesubmit.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

