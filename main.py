MSG_UNO = f'\t |DATA INCENDI|CODI COMARCA|COMARCA|CODI MUNICIPI|TERME MUNICIPAL|HA ABRADES|HA NO ABRADES|HA NO FORESRTALS|HA FORESTALS|'
MSG_DOS = "/-///-/MENU/-//-/\n____________\n-//-//-1-//-//-\nLLEGIR EL FITXER\n____________\n-//-//-2-//-//-\nINTRODUIR ALGUNA COSA AL FITXER\nSELECCIONI UN:"
MSG_TRES ="Data de l'incendi:"
MSG_QUAT ="Codi de la comarca:"
MSG_CINC ="Nom de la comarca:"
MSG_SEIS ="Codi del municipi:"
MSG_SIET ="Terme municipal:"
MSG_OCHO ="Hectaries abrades:"
MSG_NUEV ="Hectaries no abrades:"
MSG_DIEZ ="Hectaries no forestals:"
MSG_ONCE ="Hectaries forestals:"
import csv


def main():
    menu = match_menu()
    match menu:
        case 1:
            with open('files/grades.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                print(MSG_UNO)
                csvfile.readline()
                for row in readCSV:
                    print(f'\t |{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}|{row[8]}|')
        case 2:
            with open('files/grades.csv', 'a', encoding='utf-8', newline='') as csvfile:
                fieldnames = ['data_incendi', 'codi_comarca', 'comarca', 'codi_municipi', 'terme_municipal','ha_abrades','ha_abrades','ha_no_abrades','ha_no_forestals','ha_forestals']
                writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                regs = int(input("Quants registres vols afegir?"))
                for i in range(regs):
                    data_inc = input(MSG_TRES)
                    codi_com = int(input(MSG_QUAT))
                    com = input(MSG_CINC)
                    codi_m = int(input(MSG_SEIS))
                    terme_m = input(MSG_SIET)
                    ha_a = int(input(MSG_OCHO))
                    han_a = int(input(MSG_NUEV))
                    han_f = int(input(MSG_DIEZ))
                    ha_f = int(input(MSG_ONCE))
                    writeCSV.writerow({'data_incendi': data_inc, 'codi_comarca': codi_com, 'comarca': com, 'codi_municipi': codi_m, 'terme_municipal': terme_m ,'ha_abrades':ha_a,'ha_no_abrades':han_a,'ha_no_forestals':han_f,'ha_forestals':ha_f})


def match_menu():
    num = int(input(MSG_DOS))
    return num



if __name__ == "__main__":
    main()