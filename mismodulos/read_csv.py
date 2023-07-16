import csv
#retornará una lista de diccionarios donde cada diccionario es cada fila de información [{pais: colombia, poblacion: 1000......},{},{}]
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        #acá imprimimos la primera fila que serían los nombres de cada llave
        data=[]
        for row in reader:
            iterable = zip(header,row)#junataré el header en un par con su respectivo dato; así: (capital,medellín) y así para cada dato
            country_dict={key: value for key,value in iterable}
            data.append(country_dict)
        return data

if __name__ =='__main__':
    data=read_csv('./mismodulos/data.csv')
    print(data [0])