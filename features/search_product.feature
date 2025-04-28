Feature: Búsqueda de productos en MercadoLibre
    Scenario: Buscar un iPhone 13 en MercadoLibre
        Given el usuario se encuentra en la página principal de MercadoLibre
        When el usuario busca "iPhone 13"
        Then aparecen resultados que contienen el texto "iPhone"
