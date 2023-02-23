from sistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    cani= {}
    cat= {}
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio dispnible...")
                continue
            historia = int(input(" ingrese la historia clinica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                medicamento=Medicamento()
                medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                if tipo== "felino":
                    m= 0
                    for i in cat.keys():
                        m+=1
                    if m >= 7:
                        print("No se permite el ingreso de la mascota, capacidad a tope")
                        continue
                    else:
                      cat[historia]= nombre
                elif tipo== "canino":
                    m= 0
                    for i in cani.keys():
                        m+=1
                    if m >= 7:
                        print("No se permite el ingreso de la mascota, capacidad a tope")
                        continue
                    else:
                      cani[historia]= nombre
                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarMedicamento(medicamento)
                servicio_hospitalario.ingresarMascota(mas)
#Hasta acá lo llevo

            else:
                print("Ya existe una mascota con el numero de historia clínica ingresado.") 

            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
          
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")



if __name__ == "__main__":
    main()