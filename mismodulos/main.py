import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./mismodulos/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data)) #filtra sólo los paises que sean de sudamerica  y modifica así la lista de diccionarios data
  #dejando allí 

  '''
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  
#si yo quito ese if y corro el programa no va a pasar nada, pero si lo pongo y 
#corro el programa me va a correr run
if __name__=='__main__':
    run()