test_file = 'exercise.csv'
print("Elija que ejercicio desea ejecutar 1-3")
n = input()
data = [{'cedula': '12345', 'nombre': 'Jose', 'saldo': "50.43"},
        {'cedula': '54321', 'nombre': 'Dario', 'saldo': "43.12"}]

def guardar_datos():
    with open(test_file, 'w') as file:
        file.write('Cedula'+ ',' + 'Nombre' + ','+ 'Saldo' + '\n')
        for i in data:
            file.write(i['cedula']+ ',' + i['nombre'] + ','+ i['saldo'] + '\n')

def consultar_saldo():
    name = input('Escriba el nombre del usuario' + '\n')
    with open(test_file, 'r') as file:
        for line in file:
            i = line.split(',')
            if(i[1] == name):
                print('Su saldo es: ' + i[2])

def contar():
    x = 0
    with open(test_file, 'r') as file:
        for line in file:
            i = line.split(',')
            if(i[2] != 'Saldo\n' and float(i[2]) >= 50):
                x+=1

    print(str(x) + ' clientes tienen saldo mayor a $50')

def switch(n):
    if(n == '1'): 
        guardar_datos()
    elif(n == '2'): 
        consultar_saldo()
    elif(n == '3'):
        contar()
    else:
        return "Invalid input"

switch(n)