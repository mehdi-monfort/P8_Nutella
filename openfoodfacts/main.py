from django.conf import settings
from request import FillDatabase


def main():
    for category in settings.CATEGORIES:
        fill = FillDatabase(category)
        return fill.request()


if __name__ == "__main__":
    main()
