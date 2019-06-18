import xlrd
wb = xlrd.open_workbook('dataa.xlsx')
sheet = wb.sheet_by_index(0) 


keyPad={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
flag=0

#key_name will convert given name into keypad numbers..
#Keanu==>53268
def key_name(name):
    name=name.lower()
    temp=''
    for letter in name:
        for x,y in keyPad.items():
            if letter in y:
                temp+=x+
    return temp


#first_name will search contact with first name..
def first_name(value):
    global flag
    for i in range(1,sheet.nrows):
        if(value in key_name(sheet.cell_value(i, 0))):
            flag=1
            print(sheet.cell_value(i, 0)+' '+sheet.cell_value(i, 1))


#last_name will search contact with last name..
def last_name(value):
    global flag
    for i in range(1,sheet.nrows):
        if(value in key_name(sheet.cell_value(i, 1))):
            flag=1
            print(sheet.cell_value(i, 0)+' '+sheet.cell_value(i, 1))


#first_half_number will search contact with first half of phone number..
def first_half_number(value):
    global flag
    for i in range(1,sheet.nrows):
        half=sheet.cell_value(i, 2).split()
        if value in half[0]:
            flag=1
            print(sheet.cell_value(i, 0)+' '+sheet.cell_value(i, 1))


#second_half_number will search contact with second half of phone number..
def second_half_number(value):
    global flag
    for i in range(1,sheet.nrows):
        half=sheet.cell_value(i, 2).split()
        if value in half[1]:
            flag=1
            print(sheet.cell_value(i, 0)+' '+sheet.cell_value(i, 1))


def main():
    value=str(input("Please enter the search number::"))
    first_name(value)
    last_name(value)
    first_half_number(value)
    second_half_number(value)
    if(flag==0):
        print('No results found')


if __name__ == "__main__":
    main()
