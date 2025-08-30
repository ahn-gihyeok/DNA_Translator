from codon_table import codon_to_aa, aa_to_codon

# 입력된 seq를 대문자로 통일시키고 3개 단위로 잘라 codon 리스트로 전환
def seq_to_codons(seq):
    if not isinstance(seq, str):
        raise TypeError('잘못된 입력입니다.')
        
    SEQ = seq.replace("\n", "").replace(" ", "").upper()

    if len(SEQ) % 3 != 0:
        raise TypeError('유효한 CDS가 아닙니다.(길이 3의 배수 아님)')
        
    codons = []

    for i in range(0, len(SEQ), 3):
        codon = SEQ[i:i+3]
        codons.append(codon)

    return codons
    

# codon list 유효성 검사     
def check_codons_start(codons):
    return codons[0]=='ATG'

def check_codons_stop(codons):
    return codons[-1] in ['TAA', 'TAG', 'TGA']

def check_codons_error(codons):
    for codon in codons:
        if codon not in codon_to_aa:
            return False
    return True
    
def check_codons(codons):
    if not isinstance(codons, list):
        raise TypeError('잘못된 입력입니다.')
    
    elif not check_codons_start(codons):
        raise ValueError('개시 코돈을 찾을 수 없습니다.')
    
    elif not check_codons_stop(codons):
        raise ValueError('종결 코돈을 찾을 수 없습니다.')
    
    elif not check_codons_error(codons):
        raise ValueError('올바르지 않은 코돈이 포함되어 있습니다.')
    
    else:
        return True
    

# aa 3글자 축약어:1글자 축약어
three_to_one = {
    'ALA': 'A',  # Alanine
    'ARG': 'R',  # Arginine
    'ASN': 'N',  # Asparagine
    'ASP': 'D',  # Asparatate
    'CYS': 'C',  # Cysteine
    'GLN': 'Q',  # Glutamine
    'GLU': 'E',  # Glutamate
    'GLY': 'G',  # Glycine
    'HIS': 'H',  # Histidine
    'ILE': 'I',  # Isoleucine
    'LEU': 'L',  # Leucine
    'LYS': 'K',  # Lysine
    'MET': 'M',  # Methionine
    'PHE': 'F',  # Phenylalanine
    'PRO': 'P',  # Proline
    'SER': 'S',  # Serine
    'THR': 'T',  # Threonine
    'TRP': 'W',  # Tryptophan
    'TYR': 'Y',  # Tyrosine
    'VAL': 'V'   # Valine
}

set_one=set(three_to_one.values())    


# aa seq 입력을 개별 aa단위로 나누어 리스트로 저장(3글자의 경우 1글자로 변환하여 리턴)
# 허용되는 표준 입력 형식: 구분자 없는 1글자(예: MAKWRK...), '-'으로 구분된 3글자(예:Ala-Tyr-Thr-Val...)
# 표준 형식에 맞지 않는 입력(예:TYATyrLys,Tyr-His-Y-W, 등) 혹은 잘못된 아미노산(예: Tya,X,BAD)이 입력되면 오류
def aa_to_list(aa_seq):
    if not isinstance(aa_seq,str):
        raise TypeError('입력은 문자열이여야 합니다.')
    
    AA_SEQ=aa_seq.strip().upper()

    if ' ' in AA_SEQ or ',' in AA_SEQ:
        raise ValueError('표준 형식에 맞지 않습니다.(중간 공백/쉼표 감지)')

    if '-' in AA_SEQ:

        AA_SEQ3=AA_SEQ.split('-')
        AA_SEQ3_1=[]

        for AA3 in AA_SEQ3:
            if AA3 in three_to_one:
                AA_SEQ3_1.append(three_to_one[AA3])
            else:
                raise ValueError(f"표준 형식에 맞지 않습니다. 또는 옳바르지 않은 아미노산 '{AA3}'가 입력되었습니다.")
        return AA_SEQ3_1
    
    if '-' not in AA_SEQ:
        AA_SEQ1=list(AA_SEQ)

        for AA1 in AA_SEQ1:
            if AA1 in set_one:
                pass
            else:
                raise ValueError(f"표준 형식에 맞지 않습니다. 또는 옳바르지 않은 아미노산 '{AA1}'가 입력되었습니다.")
        
        return AA_SEQ1
    

#코돈 리스트에 매칭되는 아미노산을 찾고 이를 문자열로 출력
def codon_translate_aa(codons):

    codons_tr_aa=[]

    for codon in codons:
        if codon in codon_to_aa:
            codons_tr_aa.append(codon_to_aa[codon])
        else:
            raise ValueError(f"'{codon}'은(는) 유효하지 않은 코돈입니다.")

    return "".join(codons_tr_aa) 

# csv 파일 처리(codon:frequency 딕셔너리로 변환)
import csv

def read_usage(usage_csv:str) -> dict:

    codon_frequency={}
    try:
        with open(usage_csv, mode='r', encoding='utf-8') as usage:
            read_usage=csv.reader(usage)
            next(read_usage) 
            for row in read_usage: 
                codon=row[0]
                frequency=float(row[2])
                codon_frequency[codon]=frequency

    except FileNotFoundError:
        raise FileNotFoundError(f"파일 '{usage_csv}'을 찾을 수 없습니다.")
    
    except ValueError:
        raise ValueError(f"파일 '{usage_csv}'의 데이터 형식이 올바르지 않습니다.")
    
    except Exception as e:
        raise Exception(f"파일 '{usage_csv}'를 읽는 도중 문제가 발생하였습니다.")
    
    return codon_frequency
        


# 아미노산 리스트에 매칭되는 최적의 코돈을 찾고 그 코돈을 리스트에 저장 후 일렬로 이어진 문자열로 변환하여 리턴
def aa_reverse_codon(AAs, codon_frequency):
    AA_to_codons=[]
    for AA in AAs:
        codon_list=aa_to_codon[AA]

        frequency=codon_frequency[codon_list[0]]
        codon=codon_list[0]

        for i in range(len(codon_list)):

            if frequency >= codon_frequency[codon_list[i]]:
                pass

            else:
                frequency=codon_frequency[codon_list[i]]
                codon=codon_list[i]

        AA_to_codons.append(codon)

    codon_seq="".join(AA_to_codons)
    return codon_seq