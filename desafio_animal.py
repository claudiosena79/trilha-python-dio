
def classificar_animal(a, b, c):

  if a == 'vertebrado': 

    if b == 'ave':
      
      if c == 'carnivoro':
        return 'aguia'
      elif c == 'onivoro':
        return 'pomba'
      
    elif b == 'mamifero':
      
      if c == 'onivoro':
        return 'homem'
      elif c == 'herbivoro': 
        return 'vaca'      

    
  elif a == 'invertebrado':

    if b == 'inseto':
      
      if c == 'hematofago':
        return 'pulga'
      elif c == 'herbivoro':
        return 'lagarta'
      
    elif b == 'anelideo':
      
      if c == 'hematofago':
        return 'sanguessuga'
      elif c == 'onivoro': 
        return 'minhoca'  


a = input() 
b = input() 
c = input()

print(classificar_animal(a, b, c))