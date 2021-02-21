import math
#creamos una lista y un diccionario para el cuadrado
diccionario_cuadrado={}
lista_cuadrado=[]
#creamos una lista y un diccionario para el triangulo equilatero
diccionario_equilartero={}
lista_equilatero=[]
#creamos una lista y un diccionario para el triangulo isoceles
diccionario_isoceles={}
lista_isoceles=[]
#creamos una lista y un diccionario para el triangulo escaleno
diccionario_escaleno={}
lista_escaleno=[]
#creamos una lista y un diccionario para el circulo
diccionario_circulo={}
lista_circulo=[]
def main():
        opcion=0
        print("=============================================================")
        print("                     MENU OPCIONES                           ")
        print("=============================================================")
        print("1.Crear figura")
        print("2.Listar una clasificacion de figuras")
        print("3.Mostrar suma de todas las areas")
        print("4.Mostrar suma de todos los perimetros")
        print("5.Limpiar lista")
        print("0.salir")
        opcion=int(input("Ingresa una opcion"))
        if opcion==1:
             def menu_figuras():
                      print("==============================================================")
                      print("               crear lista de figuras                        ")
                      print("==============================================================")
                      print("1.cuadrado")
                      print("2.Triangulo")
                      print("3.circulo")
                      print("4.regresar al menu principal")
                      figura=int(input("Ingresa la opcion a realizar"))
                      if figura==1:
                               print("======================================================")
                               print("         Area y perimetro de un cuadrado              ")
                               print("======================================================")
                               def crear_cuadrado():
                                    nombre="Cuadrado"
                                    lado=float(input("ingresa el lado"))
                                    area=lado*lado
                                    perimetro=lado*4
                                    diccionario_cuadrado={"Nombre":nombre,"Lado": lado,"Area":round(area,2),"Perimetro":round(perimetro,2)}
                                    lista_cuadrado.append(diccionario_cuadrado)
                                    print(lista_cuadrado)
                               crear_cuadrado() 
                               menu_figuras()
                      elif figura==2:
                            print("======================================================")
                            print("                Tipos de triangulos                   ")
                            print("======================================================")
                            #(triangulo equilatero) 3 lados iguales
                            print("1.Triangulo equilatero")
                            #(triangulo isoceles) 2 lados iguales
                            print("2.Triangulo isoceles")
                            #(triangulo escaleno) lados diferentes todos
                            print("3.Triangulo escaleno")
                            tipo_triangulo=int(input("Selecciona el tipo de triangulo"))
                            if tipo_triangulo==1:
                               print("======================================================")
                               print("             triangulo equilatero                     ")
                               print("======================================================")
                               def crear_equilatero():
                                    nombre="Equilatero"                  
                                    lado=float(input("Ingresa el lado"))
                                    lado_base=float(input("Ingresa el lado base"))
                                    raiz=3
                                    altura=(math.sqrt(raiz)*lado)/2
                                    #print(f"la alt es " , round(altura,2))
                                    area_equilatero=(lado_base*altura)/2
                                    #print(f"el area es ",round(area_equilatero,2))
                                    perimetro_equilatero=lado*3
                                    #print(f"el perimetro es ", perimetro_equilatero)
                                    diccionario_equilartero={"Nombre":nombre,"Altura": round(altura,2),"Area":round(area_equilatero,2),"Perimetro":round(perimetro_equilatero,2)}
                                    lista_equilatero.append(diccionario_equilartero)
                                    print(lista_equilatero)
                               crear_equilatero()
                               menu_figuras()
                            elif tipo_triangulo==2:
                               print("======================================================")
                               print("             triangulo isoceles                       ")
                               print("======================================================")
                               def crear_isoceles():
                                    nombre="isoceles"
                                    altura=float(input("Ingresa la altura"))
                                    ladoA=float(input("Ingresa la medida del lado A"))
                                    ladoB=float(input("Ingresa la medida del lado B"))
                                    ladoC=float(input("Ingresa la medida del lado C"))
                                    area_isoceles=(ladoB*altura)/2
                                    perimetro_isoceles=ladoA+ladoB+ladoC
                                    diccionario_isoceles={"Nombre": nombre, "Altura": altura ,"Area": round(area_isoceles,2), "Perimetro": round(perimetro_isoceles,2)}
                                    lista_isoceles.append(diccionario_isoceles)
                                    print(lista_isoceles)
                               crear_isoceles()     
                               menu_figuras()
                            elif tipo_triangulo==3:
                               print("======================================================")
                               print("             triangulo escaleno                       ")
                               print("======================================================")
                               def crear_escaleno():
                                   nombre="escaleno"
                                   lado_A=float(input("Ingresa la medida del lado A"))
                                   lado_B=float(input("Ingresa la medida del lado B"))
                                   lado_C=float(input("Ingresa la medida del lado C"))
                                   semi_perimetro=(lado_A+lado_B+lado_C)/2
                                   area_escaleno=(math.sqrt(semi_perimetro*(semi_perimetro-lado_A)*(semi_perimetro-lado_B)*(semi_perimetro-lado_C)))
                                   #print(f"el area es de ", round(area_escaleno,2))
                                   perimetro_escaleno=lado_A+lado_B+lado_C
                                   diccionario_escaleno={"Nombre": nombre, "Sp":round(semi_perimetro,2),"Area": round(area_escaleno,2),"Perimetro":round(perimetro_escaleno,2)}
                                   lista_escaleno.append(diccionario_escaleno)
                                   print(lista_escaleno)
                               crear_escaleno()
                               menu_figuras()
                      elif figura==3:
                               print("======================================================")
                               print("                  Circulo                             ")
                               print("======================================================")
                               def crear_circulo():
                                    nombre="Circulo"
                                    pi=3.14
                                    radio=float(input("Ingresa el radio del circulo"))   
                                    perimetro_circulo=2*pi*radio
                                    area_circulo=(pi*radio)**2
                                    diccionario_circulo={"Nombre": nombre, "Radio": round(radio,2),"Perimetro": round(perimetro_circulo,2), "Area": round(area_circulo,2)}
                                    lista_circulo.append(diccionario_circulo)
                                    print(lista_circulo)
                               crear_circulo()
                               menu_figuras()
                      else:
                               print("Regresando al menu de figuras")
                               main()
             #va con la funcion menu figutas
             menu_figuras()
        elif opcion==2:
            print("==============================================================")
            print("                 listar clasificacion                         ")
            print("==============================================================")
            print("1.Cuadrado")
            print("2.Triangulo")
            print("3.Circulo")
            print("4.regresar al menu principal")
            opcio_lista=int(input("Selecciona la opcion para mostrar los diccionarios"))
            if opcio_lista==1:
               print("============================================================")
               print("               Diccionario del cuadrado                     ")
               print("============================================================")
               for i in lista_cuadrado:
                       print(i)
            elif opcio_lista==2:
                print("==============================================================")
                print("            listar clasificacion de triangulos                ")
                print("==============================================================")
                print("1.Triangulo equilatero")    
                print("2.Triangulo isoceles")
                print("3.Triangulo escaleno")
                tipo_triangulo=int(input("Ingresa el tipo de triangulo para mostrar su propio diccionario"))
                if tipo_triangulo==1:
                     print("============================================================")
                     print("               Diccionario del equilatero                   ")
                     print("============================================================")
                     for i in lista_equilatero:
                          print(i)
                elif tipo_triangulo==2:
                     print("============================================================")
                     print("               Diccionario del isoceles                     ")
                     print("============================================================")                 
                     for i in lista_isoceles:
                          print(i)
                elif tipo_triangulo==3:
                     print("============================================================")
                     print("               Diccionario del escaleno                     ")
                     print("============================================================") 
                     for i in lista_escaleno:
                          print(i)
            elif opcio_lista==3:
                     print("============================================================")
                     print("               Diccionario del circulo                     ")
                     print("============================================================")
                     for i in lista_circulo:
                          print(i)
            else:
               print("Regresando al menu principal")          
            main()
        elif opcion==3:
               print("============================================================")
               print("                suma de las areas                           ")
               print("============================================================")
               def suma_de_areas():
                    print("1.Cuadrado")
                    print("2.Triangulo")
                    print("3.Circulo")
                    print("4.Regresar al menu principal")
                    sum_figura=int(input("Selecciona el tipo de figura para obtener su total area"))
                    if sum_figura==1:
                         print("=================================================")
                         print("         Area total del cuadrado                 ")
                         print("=================================================")
                         contador_cuadrado=0.0
                         for i in lista_cuadrado:
                              contador_cuadrado=contador_cuadrado+float(i.get("Area"))
                         print(f"El area total del cuadrado es de ", contador_cuadrado)
                    elif sum_figura==2:
                         print("=================================================")
                         print("         Area total de los 3 triangulos          ")
                         print("=================================================")
                         contador_equilatero=0.0
                         contador_isoceles=0.0
                         contador_escaleno=0.0

                         print("=================================================")
                         print("          Triangulo equilatero                   ")
                         print("=================================================")
                         for i in lista_equilatero:
                              contador_equilatero=contador_equilatero+float(i.get("Area"))
                         print(f"El area total del triangulo equilatero es de ", contador_equilatero)

                         print("=================================================")
                         print("          Triangulo isoceles                     ")
                         print("=================================================")
                         for i in lista_isoceles:
                              contador_isoceles=contador_isoceles+float(i.get("Area"))
                         print(f"El area total del triangulo isoceles es de " , contador_isoceles)
                         
                         print("=================================================")
                         print("          Triangulo escaleno                     ")
                         print("=================================================")
                         for i in lista_escaleno:
                              contador_escaleno=contador_escaleno+float(i.get("Area"))
                         print(f"El area total del triangulo escaleno es de ", contador_escaleno)
                    elif sum_figura==3:
                         print("=================================================")
                         print("         Area total del circulo                  ")
                         print("=================================================")
                         contador_circulo=0.0
                         for i in lista_circulo:
                              contador_circulo=contador_circulo+float(i.get("Area"))
                         print(f"El area total del circulo es de ", contador_circulo)  
                    elif sum_figura==4:
                          print("Regresando al menu principal") 
               suma_de_areas()
               main()
        elif opcion==4:
               print("============================================================")
               print("                suma de los perimetros                      ")
               print("============================================================")
               def suma_de_perimetros():
                   print("1.Cuadrado")
                   print("2.Triangulo")
                   print("3.Circulo")
                   print("4.Regresar al menu principal")
                   perimetro_figura=int(input("Selecciona el tipo de figura para obtener su perimetro"))
                   if perimetro_figura==1:
                         print("=================================================")
                         print("         Perimetro total del cuadrado           ")
                         print("=================================================")
                         contador_cuadrado=0.0
                         for i in lista_cuadrado:
                              contador_cuadrado=contador_cuadrado+float(i.get("Perimetro"))
                         print(f"El perimetro total del cuadrado es de ", contador_cuadrado)
                   elif perimetro_figura==2:
                         print("=================================================")
                         print("         Perimetro total de los 3 triangulos    ")
                         print("=================================================")
                         contador_equilatero=0.0
                         contador_isoceles=0.0
                         contador_escaleno=0.0

                         print("=================================================")
                         print("          Triangulo equilatero                   ")
                         print("=================================================")
                         for i in lista_equilatero:
                              contador_equilatero=contador_equilatero+float(i.get("Perimetro"))
                         print(f"El perimetro total del triangulo equilatero es de ", contador_equilatero)

                         print("=================================================")
                         print("          Triangulo isoceles                     ")
                         print("=================================================")
                         for i in lista_isoceles:
                              contador_isoceles=contador_isoceles+float(i.get("Perimetro"))
                         print(f"El perimetro total del triangulo isoceles es de " , contador_isoceles)
                         
                         print("=================================================")
                         print("          Triangulo escaleno                     ")
                         print("=================================================")
                         for i in lista_escaleno:
                              contador_escaleno=contador_escaleno+float(i.get("Perimetro"))
                         print(f"El perimetro total del triangulo escaleno es de ", contador_escaleno)
                   elif perimetro_figura==3:
                       print("===================================================")
                       print("            Perimetro  del circulo                 ")
                       print("===================================================")
                       contador_circulo=0.0
                       for i in lista_circulo:
                            contador_circulo=contador_circulo+float(i.get("Perimetro"))

               suma_de_perimetros()
               main()
        elif opcion==5:
               print("============================================================")
               print("                limpiar listas                              ")
               print("============================================================")
               print("1.Cuadrado")
               print("2.Triangulo")
               print("3.Circulo")
               print("4.Regresar al menu principal")
               seleccionar_lista=int(input("Selecciona que tipo de figura quieres limpiar la lista"))
               if seleccionar_lista==1:
                    print("======================================================")
                    print("            Limpiar lista del cuadrado                ")
                    print("======================================================")
                    lista_cuadrado.clear()
                    print("Se limpio la lista con los datos del cuadrado ")
                    main()
               elif seleccionar_lista==2:
                    def limpiar_triangulos():
                       print("======================================================")
                       print("            Limpiar lista de triangulos               ")
                       print("======================================================")
                       print("1.Triangulo_equilatero")
                       print("2.Triangulo_isoceles")
                       print("3.Triangulo_escaleno")
                       print("4.Regresar al menu principal")
                       seleccionar_triangulo=int(input("Selecciona el tipo de triangulo a eliminar su lista"))
                       if seleccionar_triangulo==1:
                         print("==============================================================")
                         print("            Limpiar lista del triangulo equilatero            ")
                         print("==============================================================")
                         lista_equilatero.clear()    
                         print("Se limpio la lista con los datos del equilatero")
                       elif seleccionar_triangulo==2:
                         print("==============================================================")
                         print("            Limpiar lista del triangulo isoceles              ")
                         print("==============================================================")
                         lista_isoceles.clear()
                         print("Se limpio la lista con los datos del isoceles")
                       elif seleccionar_triangulo==3:
                         print("==============================================================")
                         print("            Limpiar lista del triangulo escaleno              ")
                         print("==============================================================")
                         lista_escaleno.clear()
                         print("Se limpio la lista con los datos del escaleno")  
                    limpiar_triangulos()    
                    main()
               elif seleccionar_lista==3:
                    print("==============================================================")
                    print("                Limpiar lista del circulo                     ")
                    print("==============================================================")
                    lista_circulo.clear()
                    print("Se limpio la lista con los datos del circulo")
                    main()
               elif seleccionar_lista==4:
                    print("Regresando al menu principal")
                    main()
        elif opcion==0:
           print("Has salido del programa correctamente.....!!!")
main()