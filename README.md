# Swap Meet

## Skills Assessed

- Understanding and following code specifications
- Reading tests
- Creating classes with attributes and instance methods
- Importing modules
- Working with attributes that are lists of instances
- Implementing instance methods that interact with other instances and objects
- Implementing inheritance
- Overriding methods from superclasses and Object

## Goal

You want to organize a swap meet! You own a lot of things. So do your friends! It would be awesome if each person could swap one of their things with another person's things.

For this event, you want each person to register online as a vendor. Also, they should be able to add a list of things as their inventory.

You envision an app where vendors can swap items between different inventories. But what would that backend logic look like?

For this project, given some features that the vendors want, create a set of classes, following the directions below. The directions will lead you to create many class definitions, their attributes and instance methods, and some other cool features. Vendors will be able to swap items based on values like quality, category, or id!

## Setup and Workflow

Refer to [the viewing-party README](https://github.com/AdaGold/viewing-party) for detailed instructions on the One-Time Project Setup, Project Development Workflow, and Details About How to Run Tests.

For this project, there are tests that you must complete for Waves 01, 03, and 06.

## Integration Tests

We provided **integration tests** for this project. The integration tests provided in this project do not cover all the test cases verified by the unit tests. While unit tests are small, fast, and should cover most of our program's behavior down to individual functions, integration tests verify that the various pieces of a program are working together correctly. For this project, the integration tests mainly verify that the functions work together when invoked correctly. We could classify them as the subset of Integration Tests called _Smoke Tests_, tests that check basic functionality of the application.

The integration tests for this project are in the directory `tests/integration_tests`, and the tests have the decorator `@pytest.mark.integration_test` provided by the `pytest-integration` package. Marking these tests as integration tests makes them run after the unit tests. The isolated nature and specficity of _unit tests_ make them a much better tool for debugging. Hence, we want to run the unit tests before the integration tests.

For more on different types of software testing, [here is a helpful resource](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing).

_The integration tests use the package `pytest-integration`. To insure that `pytest` is using the version installed in your `venv` and not the globally installed `pytest`, deactivate and reactive your virtual environment after you've installed the requirements. This step is important to make sure the integration tests run after the unit tests._

## Code Coverage

Code coverage is a term used to describe how much application code is executed when a particular test suite is run. It is a good practice to check our code coverage, to understand how much of our code is exercised by tests vs how much is still untested. A test suite with a high percentage of coverage is likely to be testing more throughly and have fewer bugs. A code coverage tool can partner with our testing suite to give us a report illustrating the coverage of our tests.

Given that Ada provided all test cases in this project, we should anticipate high code coverage.

Review the [code coverage exercise](https://github.com/adaGold/code-coverage-exercise) on how to use `pytest-cov` to generate a code coverage report. We will need to change the directory where the application code is located from `student` to `swap_meet`.

`pytest --cov=swap_meet --cov-report html --cov-report term`

_Note: Code coverage is disabled for integration tests, since unit tests should cover all the code._ [source](https://pypi.org/project/pytest-integration/#:~:text=Overview,integration%20tests%20are%20not%20run)

## Project Directions

This project is designed such that one could puzzle together how to implement this project without many directions. Being able to use tests to drive project completion is a skill that needs to be developed; programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

At submission time, no matter where you are, submit the project via Learn.

### Wave 1

In Wave 1 we will create the `Vendor` class.

- There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`

- Every instance of `Vendor` has an instance method named `add`, which takes in one item

  - This method adds the item to the `inventory`
  - This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
  - This method removes the matching item from the `inventory`
  - This method returns the item that was removed
  - If there is no matching item in the `inventory`, the method should explicitly return `None`

### Wave 2

In Wave 2 we will create the `Item` class and the `Vendor` class' `get_by_id` method.

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Item`

- Each `Item` will have an attribute named `id`, which is a unique integer by default
  - There are many ways to generate numbers, but generating numbers without duplicates takes some care. Happily, Python has a package called `uuid` that can help!
    - If we import the [`uuid` package](https://docs.python.org/3/library/uuid.html) in `item.py`, with a little research we can use one of the functions `uuid` provides to create large unique numbers meant to be used as identifiers
    - This package creates `UUID` objects, its functions don't directly return an integer, **but** `UUID` instances have [an attribute `int`](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) which allow us to access their value as an integer
- When we initialize an instance of `Item`, we can optionally pass in an integer with the keyword argument `id` to manually set the `Item`'s `id`
- Each `Item` will have a function named `get_category`, which will return a string holding the name of the class

- Instances of `Vendor` have an instance method named `get_by_id`
  - This method takes one argument: an integer, representing an `Item`'s `id`
  - This method returns the item with a matching `id` from the inventory
  - If there is no matching item in the `inventory`, the method should explicitly return `None`

### Wave 3

In Wave 3 we will write a method to stringify (convert to a string) an `Item` using `str()` and write the method `swap_items`.

- When we stringify an instance of `Item` using `str()`, it returns `"An object of type Item with id <id value>"`, where `<id value>` is the `id` of the `Item` instance that `str()` was called on.
  - For example, if we had an `Item` instance `item_a = Item(id=12345)`, the output of `str(item_a)` should be `"An object of type Item with id 12345"`.
  - This implies `Item` overrides its stringify method. We may need to research the `__str__` method for more details!

The remaining tests in wave 3 imply:

- Instances of `Vendor` have an instance method named `swap_items`
  - `swap_items` takes 3 arguments:
    1. an instance of another `Vendor` (`other_vendor`), representing the friend that the vendor is swapping with
    2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
    3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
  - The method removes `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
  - The method removes `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
  - The method returns `True`
  - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

### Wave 4

In Wave 4 we will write one method, `swap_first_item`.

- Instances of `Vendor` have an instance method named `swap_first_item`
  - It takes one argument: an instance of another `Vendor` (`other_vendor`), representing the friend that the vendor is swapping with
  - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
  - It removes the first item from its `inventory`, and adds the friend's first item
  - It removes the first item from the friend's `inventory`, and adds the instances first item
  - It returns `True`
  - If either itself or the friend have an empty `inventory`, the method returns `False`

### Wave 5

In Wave 5 we will create three additional modules with three additional classes:

Our new modules should be defined as follows:

- `Clothing`

  - Has an attribute `id` that is by default a unique integer
  - Has an attribute `fabric` that is by default the string "Unknown"
    - This attribute describes what fabric the clothing is made from; some example values might be `"Striped"`, `"Cotton"`, or `"Floral"`
    - When we instantiate an instance of `Clothing`, we can optionally pass in a string with the keyword argument `fabric`
  - Has a function `get_category` that returns `"Clothing"`
  - Has a stringify method that returns `"An object of type Clothing with id <id value>. It is made from <fabric value> fabric."`
    - For example, if we had a `Clothing` instance with an `id` of `123435` and a `fabric` attribute that holds `"Wool"`, its stringify method should return `"An object of type Clothing with id 12345. It is made from Wool fabric."`

- `Decor`

  - Has an attribute `id` that is by default a unique integer
  - Holds 2 integer attributes `width` and `length`
    - Both of these values should be 0 by default
    - When we instantiate an instance of `Decor`, we can optionally pass in integers with the keyword arguments `width` and `length`
  - Has a function `get_category` that returns `"Decor"`
  - Has a stringify method that returns `"An object of type Decor with id <id value>. It takes up a <width value> by <length value> sized space."`
    - For example, if we had a `Decor` instance with an `id` of `123435`, `width` of `3`, and `length` of `7`, its stringify method should return `"An object of type Decor with id 12345. It takes up a 3 by 7 sized space."`

- `Electronics`

  - Has an attribute `id` that is by default a unique integer
  - Has an attribute `type` that is by default the string "Unknown"
    - This attribute describes what kind of electronic device this is. Some example values might be `“Kitchen Appliance”`, `“Game Console”`, or `“Health Tracker”`
    - When we initialize an instance of `Electronics`, we can optionally pass in a string with the keyword argument `type`
  - Has an function `get_category` that returns `"Electronics"`
  - Has a stringify method that returns `"An object of type Electronics with id <id value>. This is a <type value> device."`
    - For example, if we had an `Electronics` instance with an `id` of `123435` and `type` attribute of `"Mobile Phone"`, its stringify method should return `"An object of type Electronics with id 12345. This is a Mobile Phone device."`

- All three new classes and the `Item` class have an attribute called `condition`, which can be optionally provided in the initializer. The default value should be `0`

- All three new classes and the `Item` class have an instance method named `condition_description`, which should describe the condition in words based on the value, assuming they all range from 0 to 5.
  - These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these (e.g. 'You probably want a glove for this one...").
  - The one requirement is that all the classes share the same `condition_description` behavior.

#### Using Inheritance

Now, we may notice that these three classes hold the same types of state and have the same general behavior as `Item`. That makes this is a great opportunity to use inheritance! If you haven't already, go back and implement the `Clothing`, `Decor`, and `Electronics` classes so that they inherit from the `Item` class. This should eliminate repetition in your code and greatly reduce the total number of lines code in your program!

##### Tip: Importing Item

You'll need to refer to `Item` in order to declare it as a parent. To reference the `Item` class from these modules, try this import line:

```python
from swap_meet.item import Item
```

### Wave 6

In Wave 6 we will write three methods, `get_by_category`, `get_best_by_category`, and `swap_best_by_category`.

- `Vendor` objects have an instance method named `get_by_category`

  - This method takes one argument: a string, representing a category
  - This method returns a list of objects in the inventory with that category
  - If there are no items in the `inventory` that match the category argument, the method returns an empty list

- `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
  - It takes one argument: a string that represents a category
  - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
    - It returns this item
    - If there are no items in the `inventory` that match the category, it returns `None`
    - It returns a single item even if there are duplicates (two or more of the same item with the same condition)

The remaining tests in wave 6 imply:

- `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
  - It takes in three arguments
    - `other_vendor`, which represents another `Vendor` instance to trade with
    - `my_priority`, which represents a category that the `Vendor` wants to receive
    - `their_priority`, which represents a category that `other_vendor` wants to receive
  - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other_vendor`'s inventory that matches `my_priority`
    - It returns `True`
    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other_vendor` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

### DRYing up the code

To further reduce the amount of repeated code in your project, consider how `swap_best_by_category` and `swap_first_item` might be able to make use of `swap_items`. Is there a way that these methods could incorporate a call to `swap_items` into the body of these methods?

Try it out and see if the tests still pass! If you can't get them to pass with this refactor, you can always return to the most recent working commit before you submit the project!

### Wave 7

In Wave 7 we will add three methods to the `Vendor` class, `display_inventory`, `swap_by_id`, and `choose_and_swap_items`.

- `Vendor`s have a method named `display_inventory`, which will print a list of the items in their inventory.

  - The method takes one optional argument, a string representing a category, that should default to an empty string
  - If a category is passed as a parameter, only items of that category will be displayed
  - If no category is passed, the entire inventory is displayed
  - When an item is displayed, the method should print a description of the item that includes the id
  - If a `Vendor` has an empty inventory, or no items that match the category parameter, the string "No inventory to display." should be printed

- `Vendor`s have a method named `swap_by_id`

  - The method takes 3 arguments:
    1. `other_vendor`, which represents another `Vendor` instance to trade with
    2. an integer (`my_item_id`), representing the `id` of the item this `Vendor` instance plans to give
    3. an integer (`their_item_id`), representing the `id` of the item the friend `Vendor` plans to give
  - The item with an `id` of `my_item_id` in my inventory is swapped with the item with `their_item_id` in the friend `Vendor`'s inventory
    - The method returns True
    - If the `Vendor` has no item with an `id` matching `my_item_id`, swapping does not happen, and the method returns `False`
    - If `other_vendor` has no item with an `id` matching `their_item_id`, swapping does not happen, and the method returns `False`

- `Vendor`s have a method named `choose_and_swap_items`, which will let people display their inventory and choose which items to swap by their `id`s.
  - The method takes 2 arguments:
    1. `other_vendor`, which represents another `Vendor` instance to trade with
    2. `category`, an optional parameter which is a string representing a category. Should default to an empty string.
  - The function will list the inventories for both the calling `Vendor` instance and the `Vendor` parameter `other_vendor`
    - If a category is passed as a parameter, only items of that category will be displayed by each `Vendor`
    - When listing an inventory, we should display a description of the items which includes their `id`
  - After listing the inventories, the user will be prompted to provide 2 pieces of input:
    1. The `id` of an item from the calling `Vendor` instance the user wants to swap
    2. The `id` of an item from the `other_vendor` `Vendor` instance the user wants to swap
  - Once the user provides input, the items should be swapped
    - The method returns True if a swap occurs
    - If the `Vendor` has no item with an `id` matching the user's first input, swapping does not happen, and the method returns `False`
    - If `other_vendor` has no item with an `id` matching the user's second input, swapping does not happen, and the method returns `False`

## Optional Enhancements

Should a project be completed before submission, and there is a desire for optional enhancements, consider these ideas:

- `Item` subclasses have attributes we could use to swap similar items

  - Add functions to swap `Decor` by space used, `Clothing` by the same fabric, and `Electronics` by their type!
  - Write unit tests for your new functions

- Take a look for error handling opportunities

  - What issues could arise if we pass a string (or any object other than an integer) for the `id` of an Item? How could we prevent that?
  - What other opportunities for error handling do you see?

- What is our test suite missing?
  - Identify gaps or edge cases it'd be helpful to cover
  - Write tests for the cases you identify
