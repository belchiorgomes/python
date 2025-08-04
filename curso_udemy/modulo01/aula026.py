velocidade = 61 #Velocidade atual do carro
local_carro = 100 #Local em que o carro está na estrafa

RADAR_1 = 60 #Velocida máxima do radar 1
LOCAL_1 = 100 #Locl onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

velocida_carro_passou_radar_1 = velocidade > RADAR_1

if velocida_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocida_carro_passou_radar_1:
    print('Carro multado em radar 1')