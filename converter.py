# Definicja funkcji do konwersji temperatury
# Parametry: value (wartość temperatury), from_unit (jednostka źródłowa), to_unit (jednostka docelowa)
def convert_temperature(value, from_unit, to_unit):
    # Sprawdzenie czy jednostki są takie same - jeśli tak, zwróć wartość bez zmian
    if from_unit == to_unit:
        return value
    
    # Konwersja z Celsjusza na inne jednostki
    if from_unit == "Celsius":
        # Jeśli docelowa jednostka to Fahrenheit, użyj wzoru C*9/5+32
        # W przeciwnym razie (Kelvin) użyj wzoru C+273.15
        return value * 9 / 5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    
    # Konwersja z Fahrenheita na inne jednostki
    if from_unit == "Fahrenheit":
        # Jeśli docelowa jednostka to Celsius, użyj wzoru (F-32)*5/9
        # W przeciwnym razie (Kelvin) najpierw konwertuj na Celsius, potem na Kelvin
        return (value - 32) * 5 / 9 if to_unit == "Celsius" else (value - 32) * 5 / 9 + 273.15
    
    # Konwersja z Kelvina na inne jednostki
    if from_unit == "Kelvin":
        # Jeśli docelowa jednostka to Celsius, użyj wzoru K-273.15
        # W przeciwnym razie (Fahrenheit) najpierw konwertuj na Celsius, potem na Fahrenheit
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9 / 5 + 32