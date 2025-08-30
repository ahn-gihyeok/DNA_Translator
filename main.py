from codon_table import codon_to_aa, aa_to_codon
import optimizer as op
import csv


def main():
    while True:
        start = input(
                      "어떤 작업을 하시겠습니까?\n"
                      "1. DNA 서열 -> 아미노산 서열 번역\n"
                      "2. 아미노산 서열 -> DNA 서열 최적화\n"
                      "3. 종료\n"
                      "번호 입력: ")

        if start == '1':
            # 1. DNA -> 아미노산 경로
            try:
                dna_seq = input("DNA 서열을 입력하세요: ")
                codon_list = op.seq_to_codons(dna_seq)
                op.check_codons(codon_list) # 유효성 검사
                aa_seq = op.codon_translate_aa(codon_list)
                print("\n[번역 완료]\n", aa_seq, "\n")
            except (TypeError, ValueError) as e:
                print(f"\n[오류] {e}\n")
            

        elif start == '2':
            while True:
                try:
                    aa_seq = input("아미노산 서열을 입력하세요: ")
                    aa_list = op.aa_to_list(aa_seq)
                    
                    species = input("최적화할 종을 선택해주세요\n"
                                    "1. 대장균 (Escherichia coli)\n"
                                    "2. 효모 (Saccharomyces cerevisiae)\n"
                                    "번호 입력: ")
                    
                    if species == '1':
                        filename = 'data\Codon_Usage_Escherichia_coli_K12.csv'
                        codon_frequency = op.read_usage(filename)
                        
                        optimized_dna = op.aa_reverse_codon(aa_list, codon_frequency)
                        print("\n[최적화 완료]\n", optimized_dna, "\n")
                        break
                    
                    elif species == '2':
                        filename = 'data\Codon_Usage_Saccharomyces_cerevisiae.csv'
                        codon_frequency = op.read_usage(filename)
                        
                        optimized_dna = op.aa_reverse_codon(aa_list, codon_frequency)
                        print("\n[최적화 완료]\n", optimized_dna, "\n")
                        break
                    else:
                        print("\n[오류] 1 또는 2만 입력해주세요.\n")

                except (TypeError, ValueError) as e:
                    print(f"\n[오류] {e}\n")
        

        elif start == '3':
            # 3. 메인 루프 종료 옵션
            print("프로그램을 종료합니다.")
            break

        else:
            print("\n[오류] 1, 2, 3 중 하나만 입력해주세요.\n")

if __name__ == "__main__":
    main()