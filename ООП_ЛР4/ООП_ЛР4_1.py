if __name__ == "__main__":
    from abc import ABC, abstractmethod

    class BuildingMaterial(ABC):
        """
        Базовый класс для строительных материалов.
        """

        def __init__(self, name: str, density: float, thermal_conductivity: float) -> None:
            """
            :param name: Название материала
            :param density: Плотность материала (кг/м³)
            :param thermal_conductivity: Теплопроводность (Вт/м·К)
            """
            self._name = name
            self.density = density
            self.thermal_conductivity = thermal_conductivity

        def __str__(self) -> str:
            return f"Материал: {self._name}, Плотность: {self.density} кг/м³, Теплопроводность: {self.thermal_conductivity} Вт/м·К"

        def __repr__(self) -> str:
            return f"BuildingMaterial('{self._name}', {self.density}, {self.thermal_conductivity})"

        @abstractmethod
        def get_strength(self) -> float:
            """
            Абстрактный метод, который должен быть реализован в дочерних классах.
            """
            pass

    class ReinforcedConcrete(BuildingMaterial):
        """
        Дочерний класс - железобетон.
        """

        def __init__(self, density: float, thermal_conductivity: float, compressive_strength: float) -> None:
            """
            :param density: Плотность материала (кг/м³)
            :param thermal_conductivity: Теплопроводность (Вт/м·К)
            :param compressive_strength: Прочность на сжатие (МПа)
            """
            super().__init__("Железобетон", density, thermal_conductivity)
            self.compressive_strength = compressive_strength

        def get_strength(self) -> float:
            """
            Возвращает прочность на сжатие.
            """
            return self.compressive_strength

        def __str__(self) -> str:
            return f"{super().__str__()}, Прочность на сжатие: {self.compressive_strength} МПа"

    class Wood(BuildingMaterial):
        """
        Дочерний класс - древесина.
        """

        def __init__(self, density: float, thermal_conductivity: float, moisture_content: float) -> None:
            """
            :param density: Плотность материала (кг/м³)
            :param thermal_conductivity: Теплопроводность (Вт/м·К)
            :param moisture_content: Влажность древесины (%)
            """
            super().__init__("Древесина", density, thermal_conductivity)
            self.moisture_content = moisture_content

        def get_strength(self) -> float:
            """
            Прочность древесины уменьшается при увеличении влажности.
            """
            return max(10 - self.moisture_content * 0.1, 2)

        def __str__(self) -> str:
            return f"{super().__str__()}, Влажность: {self.moisture_content}%"
