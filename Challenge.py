# importaciones
import csv
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# se crea una variable file donde se crea un archivo csv
file = io.open("banco.csv", "w", encoding="utf-8")
file.close()


# se abre el archivo tsv y se renombra a f
with io.open("C:\Users\pac\Downloads\datos_data_engineer.tsv", "r+", encoding = "utf-16LE") as f:
    # se crea una variable reader donde se guarda f, aqui se lee el archivo en formato csv con respectivo delimitador
    reader = csv.reader(f, delimiter='\t')
    # se abre el banco.csv y se renombra a new_f
    with open ("banco.csv", 'ab') as new_f:
        # se crea una variable writer donde se guarda new_f con su respectivo delimitador
        writer = csv.writer(new_f, delimiter='|')
        # itera la variable reader por fila
        for row in reader:
            # cada fila que va iterando de reader la va escribiendo en la variable writer
            writer.writerow(row)


# HICE MAS PRUEBAS PARA PORDER AGREGAR ALGUN VALOR A LOS CAMPOS QUE ESTAN VACIOS PERO NO ME FUNCIONÓ. LO DEJO AQUÍ ABAJO
# importaciones
# import csv
# import io
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# # -*- coding: utf-8 -*-

# # se abre el archivo tsv y se renombra a csvarchivo
# with io.open("C:\Users\pac\Downloads\datos_data_engineer.tsv", encoding = "utf-16LE") as csvarchivo:
#     # se crea una variable entrada donde se guarda csvarchivo aqui se lee el archivo en formato csv
#     #  con DictReader para crear un diccionario 
#     entrada = csv.DictReader(csvarchivo,delimiter='\t')
#     # for reg in entrada:
#     #     print(reg)
#     # itera a traves del diccionario entrada 
#     for key, value in entrada.iteritems():
#         # # prueba: si campo 'id esta vacio, imprime los campos
#         # if key['id'] == '':
#         #     print(key)
#         # si value (llave:valor) es vacía, cambialo por 'No hay valor asignado'
#         if value == '':
#             entrada[key] = 'No hay valor asignado'
#             print(entrada)