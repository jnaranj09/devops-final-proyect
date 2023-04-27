import openpyxl
import os
from prettytable import PrettyTable

# Load inventory data from Excel file
inventory_file = "DBs/Inventario.xlsx"
try:
    inventory_workbook = openpyxl.load_workbook(inventory_file)
    inventory_sheet = inventory_workbook.active
    inventory = {}
    header_row = inventory_sheet[1]
    for row in inventory_sheet.iter_rows(min_row=2, values_only=True):
        asset_id = row[0]
        asset_details = {}
        for i in range(1, len(header_row)):
            header = header_row[i].value
            asset_details[header] = row[i]
        inventory[asset_id] = asset_details
except FileNotFoundError:
    inventory_workbook = openpyxl.Workbook()
    inventory_sheet = inventory_workbook.active
    inventory_sheet.append(["ID"])
    inventory = {}




def ver_inventario():
    # Open the Excel file
    wb = openpyxl.load_workbook('DBs/Inventario.xlsx')

    # Select the active worksheet
    ws = wb.active
    
    # Get the header row
    header_row = [cell.value for cell in ws[1]]

    # Create a PrettyTable object with the header row
    table = PrettyTable(header_row)

    # Iterate through the rows and add them to the table
    for row in ws.iter_rows(min_row=2, values_only=True):
        table.add_row(row)

    # Print the table
    print(table)

    # Save the changes to the Excel file
    wb.save('DBs/Inventario.xlsx')

    input("\nPress Enter to continue...\n")


def exportar_inventario():
    """Exports the inventory to an Excel file"""
    inventory_workbook = openpyxl.Workbook()
    inventory_worksheet = inventory_workbook.active
    inventory_worksheet.title = "Inventario"

    inventory_worksheet.cell(row=1, column=1, value="ID")
    header_row = inventory_sheet[1]
    for i in range(1, len(header_row)):
        header = header_row[i].value
        inventory_worksheet.cell(row=1, column=i+1, value=header)

    for row, (asset_id, asset_details) in enumerate(inventory.items(), start=2):
        inventory_worksheet.cell(row=row, column=1, value=asset_id)
        for i in range(1, len(header_row)):
            header = header_row[i].value
            inventory_worksheet.cell(row=row, column=i+1, value=asset_details.get(header, ""))


    custom_name = input("Enter a custom name for the file: ")
    filename = f"{custom_name}.xlsx"
    inventory_file = os.path.join(os.getcwd(), filename)
    inventory_workbook.save(inventory_file)
    print(f"Inventory exported to {inventory_file}")




def añadir_equipo():
    # Open the Excel file
    wb = openpyxl.load_workbook('DBs/Inventario.xlsx')

    # Select the active worksheet
    ws = wb.active

    # Find the last row of data in the worksheet
    last_row = ws.max_row

    # Find the last column of data in the worksheet
    last_col = ws.max_column

    # Create a list of column headings
    headings = []
    for col in range(1, last_col+1):
        value = ws.cell(row=1, column=col).value
        if value is not None:
            headings.append(value)

    # Create a new row
    new_row = []
    for heading in headings:
        value = input(f"Enter a value for {heading}: ")
        new_row.append(value)
        if heading == "ID":
            asset_id = value

    # Add the new row to the worksheet
    for col, value in enumerate(new_row, start=1):
        ws.cell(row=last_row+1, column=col, value=value)

    # Save the changes to the Excel file
    wb.save('DBs/Inventario.xlsx')

    print(f"Asset {asset_id} added to inventory")


def eliminar_equipo():
    """Deletes an asset from the inventory"""
    asset_id = input("Enter ID to delete: ")
    if asset_id in inventory:
        asset_row = None
        for i, row in enumerate(inventory_sheet.rows):
            if row[0].value == asset_id:
                asset_row = i + 1
                break
        if asset_row is not None:
            inventory_sheet.delete_rows(asset_row)
            inventory_workbook.save(inventory_file)
            del inventory[asset_id]
            print(f"Asset {asset_id} deleted from inventory")
        else:
            print(f"Asset {asset_id} not found in inventory")
    else:
        print(f"Asset {asset_id} not found in inventory")
    print()




