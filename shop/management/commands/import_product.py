import csv

from django.core.management.base import BaseCommand
from shop.models import Product, Category


class Command(BaseCommand):
    help = 'Import products from csv'

    def handle(self, *args, **options):
        """
        Здесь надо реализовать следующее:
        - открываем csv файл
        - читаем из него построчно
        - создаем товары

        Только есть нюанс, категория в данный момент является обязательной
        поэтому тут или в csv файле в каждой строке писать категорию к которой относится товар
        а при загрузке проверять что такая категория есть? если есть то брать существующую, если нет - создавать

        :param args:
        :param options:
        :return:
        """



        print('Начало модуля**************************************************')
        print('Начало модуля**************************************************')
        print('Начало модуля**************************************************')
        product = Product.objects.all()
        f = open('newshop.txt')
        for line in f.readlines():
            check_goods = False
            arr = line.strip().split(';')
            arr[0] = int(arr[0])
            arr[5] = int(arr[5])
            for prod in product:
                if arr[0] == prod.articul:#если продукт с таким артикулом найден, то меняем цену
                    prod.price = arr[5]
                    prod.save()
                    check_goods = True

            if not check_goods:
                check_goods = True
                create_category(arr)




def create_category(myarr):
    check_cat = False
    category = Category.objects.all()
    if len(category) == 0:
        create_cat(myarr)

    for cat in category:
        if myarr[2] == cat.name and not check_cat:
            check_cat = True
            create_prod(myarr, cat)
            #myarr[2] = cat.name

    if not check_cat:
            check_cat = True
            create_cat(myarr)


def create_cat(myarr_cat):
    category = Category()
    category.name = myarr_cat[2]
    category.slug = myarr_cat[4]#Необходимо провверять slug на дубли
    category.save()
    create_prod(myarr_cat, category)


def create_prod(myarr_pr, categor):
    print('prod')
    product = Product()
    product.articul = myarr_pr[0]
    product.name = myarr_pr[1]
    product.category = categor
    product.slug = myarr_pr[3]#Необходимо провверять slug на дубли
    product.stock = 0
    product.price = myarr_pr[5]
    product.available = True
    product.save()
    print('From create_prod')