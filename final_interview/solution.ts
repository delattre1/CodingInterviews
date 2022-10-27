class Crypto {
  private phrase: string;

  constructor(phrase: string) {
    this.phrase = phrase;
  }

  public normalizePlaintext(): string {
    // removes everything except alphanumeric characters, then removes whitespaces.
    return this.phrase.replace(/[^\w\s\']|_/g, "").replace(/\s+/g, "").toLowerCase();
  }

  public size(): number {
    let normalized = this.normalizePlaintext();
    let size = Math.sqrt(normalized.length);
    return Math.trunc(size) === size ? size : Math.trunc(size) + 1;
  }

  public static chunkenize(str_: string, size: number): string[] {
    // transforms a string into a list of strings with len: $size
    const numChunks = Math.ceil(str_.length / size)
    const chunks = new Array(numChunks)

    let chunk: string;

    for (let i = 0, o = 0; i < numChunks; ++i, o += size) {
      chunk = str_.substr(o, size);
      chunks[i] = chunk;
    }
    return chunks
  }

  public plaintextSegments(): string[] {
    let normalized = this.normalizePlaintext();
    let chunkSize  = this.size();
    return Crypto.chunkenize(normalized, chunkSize);
  }

  public ciphertext(): string {
    // From a list of strings: concatenate each Ith element of each string
    // Into the resultant text
    let segments = this.plaintextSegments()
    let size = segments[0].length;
    let text: string = '';

    for (let i = 0; i < size; i++) {
      for (const seg of segments) {
        text += seg.charAt(i);
      }
    }
    return text;
  }
}

export = Crypto;
