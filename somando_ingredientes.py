preco_cenoura = 4.5
preco_acucar = 6
preco_ovos = 12
preco_oleo = 12
preco_fermento = 15
preco_leite = 5

def somando_ingredientes(tem_cenoura, tem_acucar, tem_ovos, tem_oleo, tem_fermento, tem_leite):
    total_compra = 0

    if tem_cenoura:
        total_compra = total_compra + preco_cenoura
    if tem_acucar:
        total_compra = total_compra + preco_acucar
    if tem_ovos:
        total_compra = total_compra + preco_ovos
    if tem_oleo:
        total_compra = total_compra + preco_oleo
    if tem_fermento:
        total_compra = total_compra + preco_fermento
    if tem_leite:
        total_compra = total_compra + preco_leite
    return total_compra

total = somando_ingredientes(True, True, True, True, True, True)
print(total)