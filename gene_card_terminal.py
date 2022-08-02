
"""
Execute Script and pass Name of Gene as Argument
Will print Summary of Gene's function
"""

import sys
import GeneCard as GC

gene_name = sys.argv[1]

def main():
    driver = GC.find_gene(gene_name, GC.build_driver())
    summary = GC.get_data(driver)
    print(summary)


if __name__ == "__main__":
    main()
