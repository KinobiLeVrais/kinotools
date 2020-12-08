from hashlib import sha256

entree = input("\nentrez le nom du fichiez a chiffrer/déchiffrer : \n\n")
sortie = input("\nentrez le nom du fichier de sortie : \n\n")
key = input("\nentrez la clé : \n\n")
keys = sha256(key.encode('utf-8')).digest()
with open(entree, 'rb') as f_entree:
  with open(sortie, 'wb') as f_sortie:
  	i = 0
  	while f_entree.peek():
  	  c = ord(f_entree.read(1))
  	  j = i % len(keys)
  	  b = bytes([c^keys[j]])
  	  f_sortie.write(b)
  	  i = i + 1
