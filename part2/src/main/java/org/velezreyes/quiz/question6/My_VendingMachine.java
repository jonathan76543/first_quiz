package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class My_VendingMachine implements VendingMachine {
    private int currentBalance;
    private Map<String, Drink> drinks;

    public My_VendingMachine() {
        currentBalance = 0;
        drinks = new HashMap<>();
        // Agregar las bebidas disponibles a la máquina expendedora
        drinks.put("ScottCola", new MyDrink("ScottCola", true));
        drinks.put("KarenTea", new MyDrink("KarenTea", false));
        // Agrega más bebidas según sea necesario
    }

    @Override
    public void insertQuarter() {
        currentBalance += 25; // Insertar un cuarto (25 centavos)
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        Drink drink = drinks.get(name);
        if (drink == null) {
            throw new UnknownDrinkException();
        }

        int price = 75; // Precio por defecto (75 centavos)
        if (currentBalance < price) {
            throw new NotEnoughMoneyException();
        }

        // Realizar la compra y restar el precio del saldo actual
        currentBalance -= price;

        return drink;
    }
}
