######This file is used to initialize the app by checking if the DB is created and if not, create it.######
###NOTE: That the excel file must exist empty within the DBs folder####
import os.path
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from Entidades import entidades_por_defecto

print("Inicializando app...")
print("Checkeando si la DB existe...")


def comprobacion_DB():
    InventarioDB = "DBs/Inventario.xlsx"
    if os.path.isfile(InventarioDB):
        print("Se encontro la Base de Datos del Inventario.... ✓ ")
    else:
        print("La base de Datos del Inventario no existe, favor crearla en la carpeta DBs con el nombre " + InventarioDB)
        quit()

def comprobacion_Tablas():
    filesheet = "DBs/Inventario.xlsx"
    wb = load_workbook(filesheet)
    sheet = wb.active
    if "Table1" in sheet.tables:
        print("La tabla Table1 existe en la DB... ✓ ")
        print("App inicializada... ✓")
    else:
        print("La tabla Table1 no existe en la DB, creando tabla...")
        table_range = "A1:B1"
        table = Table(displayName="Table1", ref=table_range)
        table.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
        sheet.tables.add(table)
        sheet['A1'] = entidades_por_defecto[1]
        sheet['B1'] = entidades_por_defecto[2]
        wb.save(filesheet)

        print("Tabla creada... ✓ ")
        print("App inicializada... ✓")


