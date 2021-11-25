def glas(a):
    counter = 0
    for i in range(len(a) + 1):
        if a[i - 1] == 'a' or a[i - 1] == 'у' or a[i - 1] == 'о' or a[i - 1] == 'ы' or a[i - 1] == 'э' or a[
            i - 1] == 'я' or a[i - 1] == 'ю' or a[i - 1] == 'ё' or a[i - 1] == 'е' or a[i - 1] == 'и':
            counter += 1
    return counter


def sogl(b):
    caunter = 0
    for i in range(len(b) + 1):
        if b[i - 1] == 'б' or b[i - 1] == 'в' or b[i - 1] == 'г' or b[i - 1] == 'д' or b[i - 1] == 'ж' or b[
            i - 1] == 'з' or b[i - 1] == 'й' or b[i - 1] == 'к' or b[i - 1] == 'л' or b[i - 1] == 'м' or b[
            i - 1] == 'н' or b[i - 1] == 'п' or b[i - 1] == 'р' or b[i - 1] == 'с' or b[i - 1] == 'т' or b[
            i - 1] == 'ф' or b[i - 1] == 'х' or b[i - 1] == 'ц' or b[i - 1] == 'ч' or b[i - 1] == 'ш' or b[
            i - 1] == 'щ':
            caunter += 1
    return caunter


inp = str(input("Введите предложение(желатльно, без завглавных букв): "))
glas_or_sogl = str(input('Какие буквы вы хотите посчитать?   '))

if glas_or_sogl == "Согласные" or "согласные":
    print(sogl(inp))
elif glas_or_sogl == "гласные" or "Гласные":
    print(glas(inp))
