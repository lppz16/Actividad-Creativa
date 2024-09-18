
carro=["1. Mazda", "2. Ford", "3. Kia", "4. Audi", "5. Toyota"]
presupuesto=["1. $3000", "2. $4000", "3. $5000", "4. $6000", "5. $7000"]
carros1=["Renault", "Nissan", "Hyundai", "Porshe", "Ferrari", "Tesla"]
Tipo=("Mecánico", "Automático", "Híbrido", "Eléctricos")
fav1=[ ]
final=[]
dolares=(3000)
wlc= "¡Bienvenido Sr usuario!"


print(wlc)
print("A continuación le mostraremos nuestra línea de automóviles y los precios en dólares que manejamos")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(carro)
print(presupuesto)

#Para saber cuáles puede comprar
car= int(input("¿De qué presupuesto en adelante le gustaría ver automóviles? (Digite el número)"))
print(presupuesto[car:])

#Para utilizar el menor
res=int(input("¿Le gustaría conocer nuestra segunda línea de automóviles la cual se acopla a su presupuesto? 1.Sí/2.No (Digite el número)"))
if res==2:
    print("¡Esperamos que te puedas acomodar con alguno de nuestros automóviles!")
else:
    print(carros1[:3])

#Len
luxu=int(input("¿Le gustaría saber cuántas líneas de automóviles exclusivos manejamos? 1.Sí/2.No (Digite el número)"))
if luxu==2:
    print("¡Esperamos que te puedas acomodar con alguno de nuestros automóviles!")
else:
    print((len(carros1))-3)

#Insert
for i in range(3):
  fav=input("Dinos hasta ahora cuáles ha sido tu automóvil favorito: ")
  fav1.insert(i, fav)

#Extend
final.extend(fav1)

#Append
prex=int(input("Tenemos créditos con muchos bancos, ¿Te gustaría conocer nuestros convenios? 1.Sí/2.No (Digite el número)"))
if prex==1:
  dol=int(input("¿Por cuántos dólares deseas hacer tu crédito? ($3000, $4000, $5000, $6000, $7000)"))
  doll=(f"Crédito de: {dol}")
  final.append(doll)  
else:
 print("Esperamos poder haberte ayudado")

#Recomendaciones por parte del usuario--Modificación
reco=int(input("Nos gustaría saber qué línea de automóviles no te gustaría que siguieramos manejando (1. Mazda, 2. Ford, 3. Kia, 4. Audi, 5. Toyota)"))
print(f"Tomaremos en cuenta tu anterior opinión para sacar de nuestras líneas el {reco}")
carro[reco]="No disponible"
print(f"Nuestra nueva línea de autos quedaría así: {carro}")

#Recordar mostrar al final sus autos favoritos con sus precios, alternandolos 
#Conclusión final
print("Finalmente, tenemos la mejor opción para tí con todos la información pertinente: ", final) 


    


