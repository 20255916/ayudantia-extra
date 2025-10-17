#ya dejé

#ejemplo del correo

correo = input()

##busco evaluar true o false

# instancias de ejemplo
#  aportillo@esen.edu.sv
#  alvin.portillo@gmail.com

# print(correo.count("@"))        #count sirve para indicarle que me cuente cuantos de esos caracteres en paréntesis hay en el texto
#count es para que cuente CUANTO de algo hay
#index sirve para que te diga EN QUE POSICION está algo


condicion1 = correo.count("@")==1 
posicion_arroba = correo.index("@") 
condicion2_1= posicion_arroba>=3
condicion2_2= (len(correo)-posicion_arroba)>3
condicion3= correo.count(".")>=1
condicion4= correo.count(" ") == 0 
condicion5_1= correo[0] != "." 
condicion5_2= correo[-1] !="."


print(condicion1 and condicion2_1 and condicion2_2 and condicion3 and condicion4 and condicion5_1 and condicion5_2)








# print(correo.index("@")) 


