#lectura de dades des de CSV
import csv
def main():
   with open('files/grades.csv') as csvfile:
       readCSV = csv.reader(csvfile, delimiter=',')
       print(f'\t |DATA INCENDI|CODI COMARCA|COMARCA|CODI MUNICIPI|TERME MUNICIPAL|HA ABRADES|HA NO ABRADES|HA NO FORESRTALS|HA FORESTALS|')
       csvfile.readline()
       for row in readCSV:
           print(f'\t {row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}|{row[8]}|')

if __name__=="__main__":
    main()
