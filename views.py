import json

file_path = 'product.json'

class GetMixin:
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)
        
    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id +=1

        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id    
    
class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        try:
            new_product = {
                'id': super().get_id(),
                'title': input('Введите название товара: '),
                'price': int(input('Введите стоимость товара: '))
            }
        except ValueError:
            print('Ввели некорректные данные')
            self.create()

        else:
            data.append(new_product)
            print(data)

        with open(file_path, 'w') as file:
            json.dump(data, file)
            print('Successfully created')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список продуктов')
        data = super().get_data()
        print(data)
        print('End')

class RetrieveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()

        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.retrieve
        else:
            one_product = list(filter(lambda x: x['id'] == id, data ))
            # print(one_product)
            if not one_product:
                print('Такого продукта нет')
            else:
                print(one_product[0])

class UpdateMixin(GetMixin):
    def update(self):
        data=super().get_data()
        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
         
            if not one_product:
                print('Такого товара нет')

            product = data.index(one_product[0])

            choice = int(input('Что вы хотите изменить? 1 - title, 2 - price: '))

            if choice == 1:
                data[product]['title'] = input('Введите новое название')

            elif choice == 2:
                try:
                    data[product]['price'] = int(input('Введите новую стоимость: '))
                except ValueError:
                    print('_ _ _ _ _ _ _')
                
                else:
                    print('Такого поля нет')
                self.update()
            with open(file_path, 'w') as file:
                json.dump(data, file)


class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))

            if not one_product:
                print('Такого товара нет')
            product = data.index(one_product[0])
            data.pop(product)
            with open(file_path, 'w') as file:
                json.dump(data, file)
            print('Удалили')


class Product(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    def __init__(self, title = ' ', price = 0):
        self.title = title
        self.price = price
    
product = Product()
# product.create()
# product.listing()
# product.retrieve()
# product.update()
product.delete()
    



    
    