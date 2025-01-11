class Concrete:
    def __init__(self, density: float, strength_limit: float, frost_resistance: int):
        if density <= 0:
            raise ValueError("Плотность должна быть положительной.")
        if strength_limit <= 0:
            raise ValueError("Предел прочности должен быть положительным.")
        if frost_resistance <= 0:
            raise ValueError("Марка по морозостойкости должна быть положительной.")
        self.density = density
        self.strength_limit = strength_limit
        self.frost_resistance = frost_resistance

    def calculate_load_capacity(self) -> float:
        """
        Рассчитывает несущую способность железобетонного элемента.

        Returns:
            float: Несущая способность в тоннах.

        Example:
            >>> c = Concrete(2400, 40, 100)
            >>> c.calculate_load_capacity()
            9.6
        """
        return self.density * self.strength_limit * 0.0001

    def compare_strength(self, other: 'Concrete') -> str:
        """
        Сравнение прочности с другим экземпляром железобетона.

        Args:
            other (Concrete): Другой экземпляр для сравнения.

        Returns:
            str: Результат сравнения (например, 'Сильнее', 'Слабее', 'Равно').

        Example:
            >>> c1 = Concrete(2400, 40, 100)
            >>> c2 = Concrete(2300, 35, 90)
            >>> c1.compare_strength(c2)
            'Сильнее'
        """
        if self.strength_limit > other.strength_limit:
            return 'Сильнее'
        elif self.strength_limit < other.strength_limit:
            return 'Слабее'
        else:
            return 'Равно'


class Bakery:
    def __init__(self, average_price: float, daily_visitors: int):
        """
        Инициализация объекта булочной.

        Args:
            average_price (float): Средняя стоимость товара (в рублях).
            daily_visitors (int): Количество посетителей в день.

        Raises:
            ValueError: Если средняя стоимость отрицательна или количество посетителей меньше нуля.
        """
        if average_price < 0:
            raise ValueError("Средняя стоимость должна быть неотрицательной.")
        if daily_visitors < 0:
            raise ValueError("Количество посетителей не может быть отрицательным.")

        self.average_price = average_price  # Средняя стоимость товара
        self.daily_visitors = daily_visitors  # Количество посетителей

    def calculate_daily_income(self) -> float:
        """
        Вычисление ежедневной выручки булочной.

        Returns:
            float: Ежедневная выручка в рублях.

        Example:
            >>> bakery = Bakery(150.0, 200)
            >>> bakery.calculate_daily_income()
            30000.0
        """
        return self.average_price * self.daily_visitors


class Swimming:
    def __init__(self, styles: list[str], lane_length: int, olympic_disciplines: int):
        """
        Args:
        styles (list[str]): Список стилей плавания.
            lane_length (int): Длина дорожки (в метрах).
            olympic_disciplines (int): Количество олимпийских дисциплин.

        Raises:
            ValueError: Если длина дорожки неположительна или количество дисциплин меньше нуля.
        """
        if lane_length <= 0:
            raise ValueError("Длина дорожки должна быть положительной.")
        if olympic_disciplines < 0:
            raise ValueError("Количество олимпийских дисциплин не может быть отрицательным.")

        self.styles = styles  # Список стилей плавания
        self.lane_length = lane_length  # Длина дорожки
        self.olympic_disciplines = olympic_disciplines  # Количество олимпийских дисциплин

    def list_styles(self) -> list[str]:
        """
        Возвращает список стилей плавания.

        Returns:
            list[str]: Список стилей плавания.

        Example:
            >>> swimming = Swimming(['Кроль', 'Баттерфляй'], 50, 10)
            >>> swimming.list_styles()
            ['Кроль', 'Баттерфляй']
        """
        return self.styles

    def display_olympic_info(self) -> str:
        """
        Отображение информации об олимпийских дисциплинах по плаванию.

        Returns:
            str: Информация о количестве олимпийских дисциплин.

        Example:
            >>> swimming = Swimming(['Кроль', 'Баттерфляй'], 50, 10)
            >>> swimming.display_olympic_info()
            'Олимпийских дисциплин: 10'
        """
        return f"Олимпийских дисциплин: {self.olympic_disciplines}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
