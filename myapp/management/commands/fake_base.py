# from django.core.management.base import BaseCommand
# from myapp.models import Chef, Product, Category, Post, ProductQuantity, CookingStep
# # import faker
# from django.utils import lorem_ipsum
# # from random import randint, choice
# #
# #
# class Command(BaseCommand):
# #     """
# #     Создание фейковой БД для тестирования
# #     """
#     products_list = ['курица', 'помидор', 'рис', 'чеснок', 'соус', 'болгарский перец']
# #
#     def handle(self, *args, **kwargs):
#         category_list = ['завтрак', 'обед', 'ужин']
#         description_list = ['Завтрак считается важнейшим приемом пищи в течение дня. Рекомендуется употреблять на завтрак богатые белками продукты, фрукты и злаки. Например, омлет из белков, овсянка с ягодами и греческим йогуртом, а также чашка зеленого чая.',
#                        'Обед должен быть питательным, но легким, чтобы обеспечить энергией до вечера. Идеальные варианты для обеда могут включать куриные грудки на гриле с овощами, салат из свежих листьев и киноа, суп с лососем и овощами.',
#                        'Ужин должен быть более легким и не слишком поздно употребляться. Рекомендуется включать в ужин белки, овощи и злаки. Например, паровая рыба на гарнире из овощей, киноа с тушеными овощами, творожные оладьи с ягодами.']
#
#         for i in range(len(category_list)):
#             product = Category(name=category_list[i],
#                                description=description_list[i])
#
#             product.save()
#             self.stdout.write(str(product.name))
#
#         for i in range(4):
#             fake = faker.Faker()
#             client = Chef(username=f'login{i}',
#                           nick_name=fake.name(),
#                           password=fake.password(),
#                           email=fake.email(),
#                           phone=fake.phone_number(),
#                           about_me=" ".join(lorem_ipsum.paragraphs(2, common=False)))
#             client.save()
#             self.stdout.write(str(client.nick_name))
#
#         chefs = Chef.objects.all()
#         categorys = Category.objects.all()
#         for i in range(20):
#             posts = Post(name=f'Post{i}',
#                          description=" ".join(lorem_ipsum.paragraphs(2, common=False)),
#                          cooking_time=randint(1, 5),
#                          chef_id=choice(chefs),
#                          category_id=choice(categorys))
#             posts.save()
#             self.stdout.write((str(posts.name)))
#
#         posts = Post.objects.all()
#
#         # добавление продуктов
#         products_list = ['курица', 'помидор', 'рис', 'чеснок', 'соус', 'болгарский перец', 'яйцо', 'лаваш', 'зеленый лук',
#                          'грецкий орех', 'сыр', 'ветчина', 'творог']
#         for i in range(len(products_list)):
#             product = Product(name=products_list[i],
#                                description=" ".join(lorem_ipsum.paragraphs(2, common=False)))
#             product.save()
#             self.stdout.write(str(product.name))
# #
#         products_db = Product.objects.all()
#
#         # добавление шагов приготовления
#         for i in range(30):
#             step_p = CookingStep(post_id=choice(posts),
#                                  description=" ".join(lorem_ipsum.paragraphs(2, common=False)))
#             step_p.save()
#             self.stdout.write(str(f'step_p{i}'))
#
#         # добавление рандомного количества продуктов к рецептам
#         MEASUREMENT_CHOICES = ['KG', 'LITR', 'GRAMM', 'TABLESPOON', 'GLASS', 'TEASPOON']
#         for i in range(30):
#             step_p = ProductQuantity(product_id=choice(products_db),
#                                      post_id=choice(posts),
#                                      count=randint(1, 5),
#                                      measurement=choice(MEASUREMENT_CHOICES))
#             step_p.save()
#             self.stdout.write(str(f'product_id {step_p.product_id} posts_id {step_p.post_id}'))
