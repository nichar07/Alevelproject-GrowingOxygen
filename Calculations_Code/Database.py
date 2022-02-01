from GUI_Code.PlantObjects import Plant as P
#name, maxtemp, mintemp, brightness, size, ease, careinfo, pests, image


PlantList = [
            P('Devils Ivy', 24, 18, 3, 2, 9,'Water once a week and mist',[0,1], r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\devils ivy.PNG'),
            P('Peace Lily', 26, 24, 4, 1, 7,'Water once a week and prune flowers',[2,1], r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\Peace Lily.png'),
            P('Snake Plant', 24, 18, 4, 3, 4, 'Water every other week and dust',[0],r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\snake plant.png'),
            P('Parlour Palm', 20, 18, 2, 3, 7, 'Water every week and repot once a year',[0],r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\parlour Palm.png'),
            P('Caladium',22,18,5,2,3,'Water barely and mist regurlarly',[1],r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\Caladium.png'),
            P('Orchid',24,22,5,2,1,'Water never and occasionally repot',[2],r'C:\Users\nicpa\PycharmProjects\Alevelproject-GrowingOxygen-mk1\PlantImg\Orchid.png')
]

PestDict = {0: 'Aphids ', 1: 'Leaf Miners ', 2: 'GreenFlies '}