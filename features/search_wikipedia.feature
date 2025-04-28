Feature: Búsqueda de artículos en Wikipedia
    Scenario: Verificar el título del artículo "Python (lenguaje de programación)"
        Given el usuario se encuentra en la página principal de Wikipedia
        When el usuario busca "Python (lenguaje de programación)"
        Then el título del artículo debe ser "Python (lenguaje de programación)"
