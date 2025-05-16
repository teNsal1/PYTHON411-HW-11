from dataclasses import dataclass
from typing import List, Dict, Optional, Iterator

@dataclass
class City:
    """Датакласс для представления информации о городе."""
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str

class CitiesIterator:
    """Итератор для обработки данных о городах."""
    def __init__(self, cities_data: List[Dict]) -> None:
        """
        Инициализирует итератор списком словарей с данными о городах.
        
        Args:
            cities_data: Список словарей с данными о городах.
        """
        self._cities: List[City] = []
        self._min_population: Optional[int] = None
        self._sort_parameter: Optional[str] = None
        self._reverse_sort: bool = False
        self._current_index: int = 0

        # Преобразование данных и валидация
        for city_dict in cities_data:
            self._validate_city_data(city_dict)
            coords = city_dict['coords']
            city = City(
                name=city_dict['name'],
                lat=float(coords['lat']),
                lon=float(coords['lon']),
                district=city_dict['district'],
                population=city_dict['population'],
                subject=city_dict['subject']
            )
            self._cities.append(city)
        
    def _validate_city_data(self, data: Dict) -> None:
        """Проверяет наличие обязательных полей в данных города."""
        required_fields = ['name', 'district', 'population', 'subject', 'coords']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
        if 'lat' not in data['coords'] or 'lon' not in data['coords']:
            raise ValueError("Координаты должны содержать 'lat' и 'lon'")
    
    def set_population_filter(self, min_population: int) -> None:
        """Устанавливает минимальное значение населения для фильтрации."""
        self._min_population = min_population
    
    def sort_by(self, parameter: str, reverse: bool = False) -> None:
        """Сортирует города по указанному параметру."""
        # Проверяем, что параметр есть в полях датакласса City
        if parameter not in City.__dataclass_fields__:
            raise AttributeError(f"Параметр {parameter} не существует в классе City")
        self._sort_parameter = parameter
        self._reverse_sort = reverse
        self._cities.sort(key=lambda x: getattr(x, parameter), reverse=reverse)