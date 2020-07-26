# Usage: python3 convert.py file_name.xlsx

import pandas as pd
import sys
def convert(somefile):
    with open(somefile,'r') as f:
        df = pd.read_excel("./"+somefile)
        reader = df.values
        allvcf = open(somefile+'.vcf','w')
        i = 0
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            tel = str(row[2])
            allvcf.write('BEGIN:VCARD'+"\n")
            allvcf.write('VERSION:2.1'+"\n")
            allvcf.write('N:'+last_name+';'+first_name+"\n")
            allvcf.write('FN:'+first_name+' '+last_name+"\n")
            allvcf.write('TEL;CELL:'+tel+"\n")
            allvcf.write('END:VCARD'+"\n")
            allvcf.write("\n")
            
            i += 1
        
        allvcf.close()
        print(str(i)+" vcf cards generated")

def main(args):
    if len(args) != 2:
    	print("Usage:")
    	print(args[0] + " filename")
    	return

    convert(args[1])

if __name__ == '__main__':
    main(sys.argv)