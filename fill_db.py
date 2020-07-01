from dictionary.models import Word, Acceptation
for x in range(0, 10000):
    word = Word(term=str(x))
    word.save()
    acc = Acceptation(meaning=str(x)+"A",word=word)
    acc.save()
    acc = Acceptation(meaning=str(x)+"B",word=word)
    acc.save()

