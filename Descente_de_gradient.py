#Fonction pour spliter les données en 2 listes
def donnees(full_donnes):
    x = []
    libelle = []
    for z, y in full_donnes:
        x.append(z)
        libelle.append(y)
    return x,libelle

def apprentissage (x,Weight,Bias):
    y = []
    for xi in x:
        tmp = Weight+Bias*(xi)
        y.append(tmp)
    return y

def fonction_loss(x,y,libelle):
    Loss_liste = []
    for i in range (0,len(x)):
        Loss_liste.append((libelle[i]-y[i])**2)
    Total_Loss = round(sum(Loss_liste)/len(x),2)
    return Total_Loss

def new(x,libelle,y,Weight,Bias):
    somme = []
    somme2 = []
    for i in range (0,len(x)):
        somme.append((y[i] - libelle[i]) * 2)
        somme2.append((y[i] - libelle[i]) * (2 * x[i]))
    var = round(sum(somme) / len(x),2)
    var2 = round(sum(somme2) / len(x), 2)

    New_weight = round(Weight - 0.001 * var2, 2)
    New_bias = round(Bias - 0.001 * var, 2)

    return New_weight, New_bias

def init(liste_donnes):
    New_bias = 0
    New_weight = 0
    for i in range (0,1000):
        x, libelle = donnees(liste_donnes)
        y = apprentissage(x,New_weight,New_bias)
        Loss = fonction_loss(x,y,libelle)
        New_weight,New_bias = new(x,libelle,y,New_weight,New_bias)
        print(f"#########\nLoss : {Loss}\nNew_weight : {New_weight}\nNew_bias : {New_bias}")
    print(f"Modèle final : y = {New_weight} * x + {New_bias}")
    test = input("x : ")
    print(f"{New_weight * float(test) + New_bias }")

liste_donnes = [[3.5,18],[3.69,15],[3.44,18],[3.43,16],[4.34,15],[4.42,14],[2.37,24]]
init(liste_donnes)
