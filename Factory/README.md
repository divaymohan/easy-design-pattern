# Factory

## Problem :-

```
1. Uncertainties in types of objects
2. Decision to be made at runtime regarding what classes to use

```

## Scenerio:-

* Pet shop
* Originally only dogs
* Now cats too

# Abstract Factory

## Problem:- 

```
1. The user expectation yields multiple, related objects
```

## Scenerio:- 

* Pet factory
* Dog factory
* Cat factory

```
Dog factory ---> Dog, Dog Food
Cat factory ---> Cat, Cat Food
```

## Solution:-

* Abstract factory - pet factory
* Concrete factory - dog factory and cat factory
* Concrete product - Dog and Dog Foor, Cat and Cat Food