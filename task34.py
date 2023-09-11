def has_rhythm(text):
    vowels = "aeiouyаеиоуыэюя"  # Русские и английские гласные
    phrases = text.split()
    
    # подсчитываем гласные для первой фразы
    first_phrase_vowels = sum(1 for char in phrases[0] if char.lower() in vowels)
    
    # сравниваем с другими фразами
    for phrase in phrases[1:]:
        if sum(1 for char in phrase if char.lower() in vowels) != first_phrase_vowels:
            return "Пам парам"

    return "Парам пам-пам"

text = input("Введите стих: ")
print(has_rhythm(text))
