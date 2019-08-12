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

def translate(x):
	return None

# Before running this, run the following once in terminal
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/google/Downloads/temp-google-credentials.json"

    # from google.cloud import translate
    # translate_client = translate.Client()
    #
    # text = u'' #(the words that user is going to put in string)
    # target = 'ES' #have to use the abbreviation
    # translation = translate_client.translate(
    #     text,
    #     target_language=target)
    #
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))


