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