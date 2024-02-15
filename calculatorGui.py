#группа БПМ-22-3
#Ватагина Екатерина
#Мухортова Екатерина
#Самсонов Николай

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor=ft.colors.PINK_50
    page.title = "Calculator"
    preambula_text = ft.Text(f"Введите числа в пропуски и укажите их сс")
    first_number = ft.TextField(label="First number", autofocus=True,  col={"md":  4})
    first_number.width = '100px'
    fbase = ft.TextField(label="Base", autofocus=True,  col={"md":  2})

    second_number = ft.TextField(label="Second number", col={"md":  4})
    sbase = ft.TextField(label="Base", col={"md":  2})
    ans_base = ft.TextField(label="Answer base", col={"md":  2})
    str = ft.Column()


    def znak(x):
        znak_x = '+';
        if ('-' in x):
            znak_x = '-'
        return znak_x

    def erase_minus(x):
        if ('-' in x):
            return x[1:]
        else:
            return x

    result_display = ft.Column()
    def add_numbers(e):
        znak1=znak(first_number.value)
        znak2=znak(second_number.value)

        num1=to_dec(erase_minus(first_number.value), int(fbase.value))
        num2 = to_dec(erase_minus(second_number.value), int(sbase.value))

        try:
            znak_of_number=''
            if (oper_dropdown.value=='+'):
                if (znak1 == '-' and znak2 == '-'):
                    total = num2 + num1
                    znak_of_number = '-'
                else:
                    if (znak1=='-' and num1>num2):
                        total =num1-num2
                        znak_of_number='-'
                    if (znak2=='-' and num2>num1):
                        total =num2-num1
                    if (znak1 == '+' and znak2 == '+'):
                        total = num2 + num1


            if (oper_dropdown.value=='-'):
                if (znak1 == '-' and znak2 == '-'):
                    total=num2-num1
                else:
                    if (znak1 == '-'):
                        total = num1+num2
                        znak_of_number='-'
                    if (znak2 == '-'):
                        total = num1+num2
                if (znak1 == '+' and znak2 == '+'):
                    total = num1-num2

            if (oper_dropdown.value=='/'):
                if (znak1 == '-'):
                    znak_of_number='-'
                if (znak2 == '-'):
                    znak_of_number='-'
                total = num1 / num2
                print(total)

            if (oper_dropdown.value=='*'):
                if (znak1 == '-'):
                    znak_of_number = '-'
                if (znak2 == '-'):
                    znak_of_number = '-'
                total = num1*num2


            new_b=int(ans_base.value)
            #total=to_users_base(total, new_b)
            result_display.controls.clear()  # Clear previous results
            result_display.controls.append(ft.Text(f"Result: {znak_of_number}{total}"))
        except ValueError:
            result_display.controls.clear()  # Clear previous results
            result_display.controls.append(ft.Text("Please enter valid numbers."))
        finally:
            page.update()

    add_button = ft.ElevatedButton("Add Numbers", on_click=add_numbers)


    oper_dropdown = ft.Dropdown(
        width=70,
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("/"),
            ft.dropdown.Option("*"),

        ],
    )
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.YELLOW_50,
    )
    page.add(

        preambula_text,
        ft.ResponsiveRow(
            [
            first_number,
            fbase
            ],
            run_spacing={"xs": 10},
        ),

        oper_dropdown,

        ft.ResponsiveRow(
            [
                second_number,
                sbase
            ],
            run_spacing={"xs": 10},
        ),


        str,
        ft.ResponsiveRow(
            [
            ans_base,
            add_button,
            result_display
                ],
            run_spacing={"xs": 10},
        ),


    )

#перевод между сс
def to_dec(x, base_x):
    sum=0
    if ('.' not in x):
        if (base_x<10):
            sum = int(x[0])
            for i in range(1, int(len(x))):
                sum=sum*base_x+int((x)[i])
        else:
            sum=int(return_number(x[0]))
            for i in range(1, int(len(x))):
                sum=sum*base_x+int(return_number(x[i]))
    else:
        position_of_point = x.find('.')
        for i in range(0, position_of_point):
            sum += int(x[i]) * base_x ** (position_of_point - i - 1)
        for i in range(position_of_point + 1, len(x)):
            sum += int(x[i]) * base_x ** (position_of_point-i)
    return sum

def return_number(a):
        if (a=='A'):
            return 10
        if (a=='B'):
            return 11
        if (a=='C'):
            return 12
        if (a=='D'):
            return 13
        if (a=='E'):
            return 14
        if (a=='F'):
            return 15
        else:
            return a

def return_letter(a):
    if (a==10):
        return 'A'
    if (a==11):
        return 'B'
    if (a==12):
        return 'C'
    if (a==13):
        return 'D'
    if (a==14):
        return 'E'
    if (a==15):
        return 'F'
    else:
        return a

def to_users_base(x, users_base):
    if ('-' in str(x)):
        x=int(str(x)[1:])
    number='';
    if (users_base<10):
        while(x>0):
            number=str(x%users_base)+number
            x=x//users_base
    else:
        while (x>0):
            curr=x%users_base
            curr=return_letter(curr)
            number=str(curr)+number
            x=x//users_base
    return number

ft.app(target=main)