from datetime import datetime

from analisisResultados import analisisResultados

#Se define objeto Experimento
class Experimento:
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados):
        self.nombre=nombre
        self.fechaRealizacion=fechaRealizacion
        self.tipoExperimento=tipoExperimento
        self.resultados=resultados

#funcion para crear experimento
def gestionarExperimento(listaExperimentos):
    resultados={}
    variables=[]
    tipos=['Quimica', 'Fisica', 'Biologia', 'Matematicas']

    #valida que nombre no en blanco
    print("_______________________________________\n")
    nombre = input("Ingrese el nombre del experimento: ")
    if not nombre:
        print("\n**Debe ingresar un nombre**\n")
        return

    #valida fecha con formato corecto
    fechaRealizacion_str = input("Ingrese la fecha realizacion del experimento (DD/MM/YYYY): ")
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")         
    except ValueError:
        print("\n**fecha no valida.**\n")
        return
    
    # valida que el tipo de experimento este en la lista
    print(f"De que tipo es su experimento: " )
    try:
        cont=0
        for tipo in tipos:
            cont += 1
            print(f"{cont}. {tipo}")
        tipo = int(input("Seleccione el tipo de experimento: "))
        tipoExperimento=tipos[tipo-1]        
    except IndexError:
        print("\n**El tipo de experimento seleccionada no existe**\n")
        return
    
    tamaño=input("Cuantas variables tiene el experimento: ")
    if tamaño.isalpha():  # Verifica si es una letra
        print("\n**El valor ingresado no es numerico**\n")
    elif not tamaño:
        print("\n**Debe ingresar un valor**\n")
    else:
        #validar tamaño numerico
        tamaño=int(tamaño)
        if tamaño >=1:
            for i in range(0, tamaño):
                variable =input(f"ingrese el nombre de la variable {i+1}: ")
                variables.append(variable)

            for variable in variables:
                print(f"Ingresa un valor para la variable {variable}, para finalizar presione cualquier letra")
                valores=[]
                
                # bucle para añadir valores por variable
                while True:
                    valor = input(f"Ingresa un valor para la variable {variable}: ")
                    if valor.isalpha():  # Verifica si es una letra
                        print("\n**El experimento solo acepta variables cuantitativas**\n")
                        break
                    elif not valor:
                        print("\n**Debe ingresar un valor**\n")
                    else:
                        valores.append(valor)
                    resultados[variable]=valores

            print(f"\nSe creo el experimento {nombre}, con los valores:")
            print(resultados)
            #crear un objeto y lo agrega a lista de experimentos
            experimento = Experimento(nombre, fechaRealizacion,  tipoExperimento, resultados)
            listaExperimentos.append(experimento)

#funcion para consultar experimento
def VisualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("\n**no hay experimentos registradas**\n")
        return
    
    print(f"\nLISTA DE EXPERIMENTOS")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print("_______________________________________")
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha Realizacion: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo Experimento: {experimento.tipoExperimento}")
        print(f"Resultados: {experimento.resultados}\n")

#funcion para eliminar experimento
def eliminarExperimento (listaExperimentos):
    VisualizarExperimento (listaExperimentos)
    eliminar=input("\nIngrese el numeto del experimento a eliminar:  ")
    if not eliminar or eliminar.isalpha():  # Verifica si es una letra o esta en blanco 
        print("\n**El valor ingresado no es valido**\n")
    else:
        eliminar=int(eliminar)
        if eliminar <= len(listaExperimentos):  # Verifica si objeto esta en la lista
            listaExperimentos.remove(listaExperimentos[eliminar-1])
            print("Se elimino el experimento")
            VisualizarExperimento (listaExperimentos)
        else:
             print("\n**el experimento indicado no existe**\n")
       
  
def menu():
    
    listaExperimentos = []
    while True:
        print("\nBIENVENIDO AL SISTEMA DE INVESTIGACION")
        print("_______________________________________")
        print("1. Gestion Experimento")
        print("2. Visualizar Experimento")
        print("3. Eliminar Experimentos")
        print("4. Analisis de Resultados")
        print("5. Comparar Experimentos")
        print("6. Gestion de Informe")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            gestionarExperimento(listaExperimentos)
        elif opcion == "2":
            VisualizarExperimento (listaExperimentos)
        elif opcion == "3":
            eliminarExperimento (listaExperimentos)
        elif opcion == "4":
            analisisResultados(listaExperimentos)
        elif opcion == "5":
            print("saliendo del programa....")
            break
        elif opcion == "6":
            print("saliendo del programa....")
            break
        elif opcion == "7":
            print("Programa Finalizado")
            break
        else:
            print("\n**opcion invalida**\n")
            

if __name__ == "__main__":
    menu()        
        