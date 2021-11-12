

## Item create

- input
  - ```python
     <itemID> <customerID> <quantity>
- output
  - None


## Item view all

- input
  - None
- output
  - All items as array
  - ```python
     [id:1,name:FreshMilk,price:100,qty:10, 
     id:2,name:Rice,price:200,qty:10]
    ```



## Item view by ID

- input
   - ```python
     <itemID>
- output
  - View item as String
  - ```python
     1 Rice 200 10
    ```

## Customer create

- input
  - ```python
     <name> <address> <contact>
- output
  - None

## Customer view all

- input
  - None
- output
  - All items as dict list
  - ```python
     [id:1,name:Lasindu,address:Horana,contact:076882882,
     id:2,name:Ashan,address:Panadura,contact:076882334]
    ```

## Customer view by ID

- input
   - ```python
     <customerID>
- output
  - View item as String
  - ```python
     2 Ashan Panadura 076882334
    ```


## Order create (Admin)

- input
  - ```python
     <itemID> <customerID> <quantity>
- output
  - None

## Order create (Customer)

- input
  - ```python
     <itemID> <quantity>
- output
  - None

## Order view all (Admin)

- input
  - None
- output
  - All orders by all customers as array
  - ```python
    [oid:1,cid:2,customer_name:Ashan,itmid:2,itm_name:Rice,qty:5,price:200,total:1000,
    oid:2,cid:2,customer_name:Ashan,itmid:1,itm_name:FreshMilk,qty:2,price:100,total:200]
    ```


## Order view all (Customer)

- input
  - None
- output
  - All orders by login customer as array
  - ```python
    [oid:1,cid:2,customer_name:Ashan,itmid:2,itm_name:Rice,qty:5,price:200,total:1000,
    oid:2,cid:2,customer_name:Ashan,itmid:1,itm_name:FreshMilk,qty:2,price:100,total:200]
    ```

<!-- ## Customer view all

- input
  - None
- output
  - All items as dict list
  - ```python
     [{"name":"<name>"}]
    ``` -->