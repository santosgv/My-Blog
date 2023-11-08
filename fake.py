
def main():
    Faker.seed(0)
    fake = Faker()
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)

    for _ in range(500):
        post = Post.objects.create(
            headline=fake.name(),
            previa=fake.bs(),
            data=fake.date_between(start_date=start_date, end_date=end_date),
            referencia=fake.job(),
            por=fake.name(),
            texto=fake.paragraph(nb_sentences=5)
        )
        print(f'Criado {post}')


if __name__ == '__main__':
    import os
    from django.core.asgi import get_asgi_application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')

    application = get_asgi_application()
    from Core.models import Post
    from datetime import date
    from faker import Faker

    main()
