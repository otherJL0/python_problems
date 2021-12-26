"""
Finding a particular codon within a gene is a classic bioinformatics problem
"""
from enum import IntEnum, auto
from typing import Dict, List, Tuple


class Nucleotide(IntEnum):
    A = auto()
    C = auto()
    G = auto()
    T = auto()


# Type Aliases
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


def string_to_gene(dna: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(dna), 3):
        try:
            codon: Codon = (
                Nucleotide[dna[i]],
                Nucleotide[dna[i + 1]],
                Nucleotide[dna[i + 2]],
            )
            gene.append(codon)
        except IndexError:
            break
    return gene


def codon_to_str(codon: Codon) -> str:
    return "".join([nucleotide.name for nucleotide in codon])


def gene_to_str(gene: Gene) -> str:
    return "".join([codon_to_str(codon) for codon in gene])


def linear_codon_search(gene: Gene, target_codon: Codon) -> bool:
    comparison_count = 0
    print("Linear Search")
    for codon in gene:
        comparison_count += 1
        if codon == target_codon:
            print(f"\tSequence {codon_to_str(target_codon)} Found!")
            print(f"\tNumber of comparisons: {comparison_count}\n")
            return True
    print(f"\tSequence {codon_to_str(target_codon)} not found")
    print(f"\tNumber of comparisons: {comparison_count}\n")
    return False


def binary_codon_search(gene: Gene, target_codon: Codon) -> bool:
    start: int = 0
    end: int = len(gene) - 1
    comparison_count = 0
    print("Binary Search")
    while start <= end:
        mid: int = (end + start) // 2
        comparison_count += 1
        if gene[mid] < target_codon:
            start = mid + 1
        elif gene[mid] > target_codon:
            end = mid - 1
        else:
            print(f"\tSequence {codon_to_str(target_codon)} Found!")
            print(f"\tNumber of comparisons: {comparison_count}\n")
            return True
    print(f"\tSequence {codon_to_str(target_codon)} not found")
    print(f"\tNumber of comparisons: {comparison_count}\n")
    return False


def compare_search_methods(gene: Gene, target_codon: Codon) -> None:
    linear_result = linear_codon_search(gene, target_codon)
    binary_result = binary_codon_search(gene, target_codon)
    assert linear_result == binary_result


if __name__ == "__main__":
    gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    gene: Gene = string_to_gene(gene_str)
    sorted_gene = sorted(gene)
    sorted_gene_str = gene_to_str(sorted_gene)

    test_codons: Dict[str, Codon] = {
        "ACG": (Nucleotide.A, Nucleotide.C, Nucleotide.G),
        "GAT": (Nucleotide.G, Nucleotide.A, Nucleotide.T),
    }
    for name, codon in test_codons.items():
        print(f"Searching for {name} in {sorted_gene_str}")
        compare_search_methods(sorted_gene, codon)
