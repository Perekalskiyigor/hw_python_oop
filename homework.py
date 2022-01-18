"""Класс-модуль фитнес-трекера
Уважаемывй ревьюер. Когда будете проверять мой код, прошу вас я ламер в
программировании, даже не юзери фразы типо "загугли магические методы"
и прочий жаргон евнгелистов программирования я не понимаю.
Поэтому следует мне лучше сказать так: У тебяошибка здесь...
Она такая-то (научным языком), чтобы улучшить, почитай то-то,
на такой-то странице.
В таком случае я безмерно, буду вам благодарен и вам воздастся за ваши труды,
короче пратия вас не забудет!!!,св ,,
в противномслучае партия вас также не забудет"""

from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,  # имя класса тренировки;
                 duration: float,  # длительность тренировки в часах
                 distance: float,  # дист в км, которую преодолел пользователь
                 speed: float,  # средняя скорость, движения пользователя
                 calories: float  # количество килокал, за время тренировки
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность:{self.duration: .3f} ч.; '
                   f'Дистанция:{self.distance: .3f} км; '
                   f'Ср. скорость:{self.speed: .3f} км/ч; '
                   f'Потрачено ккал: {self.calories:.3f}.'
                   )
        return message


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000   # константа для перевода значений из метров в км
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,  # количество совершённых действий
                 duration: float,  # длительность тренировки
                 weight: float,  # вес спортсмена
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        # расчет значение средней скорости движения во время тренировки.
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        # расчет преодоленной_дистанции_за_тренировку / время_тренировки
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # Логика подсчета калорий для каждого вида тренировки будет своя,
        # поэтому в базовом классе не нужно описывать поведение метода,
        # в его теле останется ключевое слово
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # Определен в каждом дочерним классе индивидуально
        object_for_mes: InfoMessage = InfoMessage(self.__class__.__name__,
                                                  self.duration,
                                                  self.get_distance(),
                                                  self.get_mean_speed(),
                                                  self.get_spent_calories())

        return object_for_mes


class Running(Training):
    """Тренировка: бег."""
    minute: int = 60
    # в классе переопределен метод get_spent_calories"""
    coeff_calorie_run1: int = 18  # Коэф для каллорий для бега
    coeff_calorie_run2: int = 20  # Коэфициент для опреления каллорий для бега

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.coeff_calorie_run1 * self.get_mean_speed()
                    - self.coeff_calorie_run2) * self.weight / self.M_IN_KM
                    * (self.duration * self.minute))
        # (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM *
        # время_тренировки_в_минутах
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    # в классе переопределен метод get_spent_calories добавлен атрибут height
    coeff_calorie_walk1: float = 0.035  # Коэфициент для опр кал ходьба
    coeff_calorie_walk2: float = 0.029  # Коэфициент для опр кал ходьба
    minute: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        self.height = height
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.coeff_calorie_walk1 * self.weight
                    + (self.get_mean_speed() ** 2 // self.height)
                    * self.coeff_calorie_walk2 * self.weight) * (self.duration
                    * self.minute))
    # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
    # * время_тренировки_в_минутах
        return calories


class Swimming(Training):
    """Тренировка: плавание."""

    # в классе переопределены методы get_spent_calories() и get_mean_speed()
    # добавлены атрибуты length_pool count_pool
    coeff_calorie_swm1: float = 1.1  # Коэфициент для опреления каллорий плав
    coeff_calorie_swm2: int = 2  # Коэфициент для опреления каллорий плавание
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,  # длина бассейна в метрах;
                 count_pool: float  # сколько раз пользователь переплыл бассейн
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.get_mean_speed() + self.coeff_calorie_swm1)
                    * self.coeff_calorie_swm2 * self.weight)
        return calories

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = (self.length_pool * self.count_pool / self.M_IN_KM
                             / self.duration)
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return mean_speed


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_dict: Dict = {'SWM': Swimming,
                           'RUN': Running,
                           'WLK': SportsWalking}
    create_tren: Training = training_dict[workout_type](*data)
    return create_tren


def main(training: Training) -> str:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


# заранее подготовленные тестовые данные для проверки фитнес-трекера"""
if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
