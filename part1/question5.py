################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instructions:
# This questions continues to use the database we worked with in Question 4. In 
# this question, we will made some modifications ot the table.

# Part 5.A:
# Create a new table, 'favorite_foods.' It should have the columns:
# food_id integer
# name text
# vegetarian integer

sql_create_favorite_foods = """

CREATE TABLE comidas_favoritas (
    alimento_id INTEGER PRIMARY KEY,
    nombre TEXT,
    vegetariano INTEGER
);


"""

# Part 5.B:
# Alter the animals and people tables by adding a new column to each called 'favorite_food_id'
# The test suite will verify the new changes by inserting some new rows. 


# Para modificar la tabla 'animales':
sql_alter_tables_with_favorite_food = """

ALTER TABLE animales
ADD COLUMN favorite_food_id INTEGER;


"""

# Para modificar la tabla  'personas':
sql_alter_tables_with_favorite_food = """

ALTER TABLE personas
ADD COLUMN favorite_food_id INTEGER;


"""

# Part 5.C:
# Write a query to select all pets that are vegetarian.
# THe output should be a list of tuples in the format: (<pet name>, <food name>)

sql_select_all_vegetarian_pets = """

SELECT animales.nombre AS nombre_de_mascota, comidas_favoritas.nombre AS nombre_de_comida
FROM animales
JOIN comidas_favoritas ON animales.favorite_food_id = comidas_favoritas.alimento_id
WHERE comidas_favoritas.vegetariano = 1;


"""