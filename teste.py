
from funcionalidades import *



tv = Televisor("Samsung", "QLED")
controle = ControleRemoto(tv)

# Sintonizando canais
controle.SintonizaCanal(5)
controle.SintonizaCanal(10)
controle.SintonizaCanal(15)

# Mudando o canal
controle.TrocaCanal(10)

# Aumentando o volume
controle.AumentaVolume() 

# Diminui o volume
controle.DiminuiVolume()  

# Exibindo o estado final da TV
print(f"Canal Atual: {tv.canal_atual}")
print(f"Volume: {tv.volume}")
print(f"Lista de Canais: {tv.lista_de_canais}")