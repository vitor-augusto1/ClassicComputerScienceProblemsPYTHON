
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # Starts with a sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # Move 2 bits to the left
            if nucleotide == "A": # Change the las 2 bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # Change the last 2 bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # Change the last 2 bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # Change the last 2 bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = "TAGGGATTAACCCTATATATATATATATAGCCTATCGGGATCTCTATTATTCAAATGG"
    print(f"The original string is: {getsizeof(original)} bytes")
    compressed: CompressedGene = CompressedGene(original)
    print(f"The compressed version is: {getsizeof(compressed.bit_string)} bytes")
    print(compressed)
    print(f"Original and decompressed are the same: {original == compressed.decompress()}")
