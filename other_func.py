#from google.cloud import translate

# from .lib import google.cloud.translate as translate

def make_plural(x):
    if x[-2:] == 'sh' or 'ch':
        return (str(x) + 'es')
    elif x[-3:] == 'ife':
        return (str(x[-3:]) + 'ives')
    elif x[-2:] == 'us':
        return (str(x[-2:]) + 'i')
    elif x[-1:] == 'y':
        return (str(x[-1:]) + 'ies')
    elif x == 'people' or x == 'bread' or x == 'fish' or x == 'deer' or x == 'moose' or x == 'species' or x == 'sheep' or x == 'offspring':
        return x
    elif x == 'child':
        return 'children'
    elif x == 'foot':
        return 'feet'
    elif x == 'man':
        return 'men'
    elif x == 'mouse':
        return 'mice'
    elif x == 'ox':
        return 'oxen'
    elif x == 'person':
        return 'people'
    elif x == 'tooth':
        return 'teeth'
    elif x == 'goose':
        return 'geese'
    elif x == 'woman':
        return 'women'
    elif x == 'louse':
        return 'lice'
    else:
        return (x + 's')

def listPluralizer(x):
    item_index = 0
    for i in x:
        pl_Items = make_plural(i)
        x[item_index] = pl_Items
        item_index += 1

# def translator(x):
#     translate_client = translate.Client()
#     text = x
#     target = 'ES'
#     translation = translate_client.translate(
#          text,
#         target_language=target)
#     return(u'{}'.format(translation['translatedText']))

def hard_coded_answer(x):
    y = x.lower()
    if y == 'dog':
        return 'perro'
    elif y == 'cat':
        return 'gato'
    elif y == 'bread':
        return 'pan'
    elif y == 'fish':
        return 'pescado'
    elif y == 'arm':
        return 'brazo'
    elif y == 'window':
        return 'ventana'
    elif y == 'door':
        return 'puerta'
    elif y == 'mouse':
        return 'ratón'
    elif y == 'computer':
        return 'computadora'

def pl_hard_coded_answers(x):
    y = x.lower()
    if y == 'dog':
        return 'perros'
    elif y == 'cat':
        return 'gatos'
    elif y == 'bread':
        return 'pan'
    elif y == 'fish':
        return 'pescado'
    elif y == 'arm':
        return 'brazos'
    elif y == 'window':
        return 'ventanas'
    elif y == 'door':
        return 'puertas'
    elif y == 'mouse':
        return 'ratones'
    elif y == 'computer'
        return 'computadoras'
