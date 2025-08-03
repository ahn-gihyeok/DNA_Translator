# codon -> amino acid
codon_to_aa = {
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M',  # 개시코돈
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y',
    'TAA': '*', 'TAG': '*', 'TGA': '*',  # 종결코돈
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C',
    'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

# amino acid -> codons
aa_to_codon = {
    'F': ['TTT', 'TTC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'I': ['ATT', 'ATC', 'ATA'],
    'M': ['ATG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Y': ['TAT', 'TAC'],
    '*': ['TAA', 'TAG', 'TGA'],
    'H': ['CAT', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'N': ['AAT', 'AAC'],
    'K': ['AAA', 'AAG'],
    'D': ['GAT', 'GAC'],
    'E': ['GAA', 'GAG'],
    'C': ['TGT', 'TGC'],
    'W': ['TGG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG']}

def seq_to_codons(seq):
    if not isinstance(seq, str):
        raise TypeError('잘못된 입력입니다.')
        
    if len(seq) % 3 != 0:
        raise TypeError('유효한 CDS가 아닙니다.(길이 3의 배수 아님)')
        
    SEQ = seq.upper().replace("\n", "").replace(" ", "")
    codons = []

    for i in range(0, len(SEQ), 3):
        codon = SEQ[i:i+3]
        codons.append(codon)

    return codons
    
    
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
    



        

