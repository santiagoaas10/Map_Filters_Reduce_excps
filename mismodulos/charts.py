import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):#grafico de barra

    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):# gráfico tipo torta
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.show()    

if __name__=='__main__':
    labels = ['a','b','c']
    values=[100,200,1000]
    generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)
