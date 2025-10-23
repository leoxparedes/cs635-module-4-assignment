%% src UML (minimal)
classDiagram
    direction LR

    class User {
      +id: str
      +name: str
      +password: str
      +to_row(): list[str]
    }

    class Customer {
      +address: str
      +phone: str
      +to_row(balance=0): list[str]
    }

    class Transaction {
      +customer_id: str
      +amount: int
      +type: str
      +to_row(): list[str]
    }

    User <|-- Customer
    Customer "1" --> "many" Transaction : has transactions

    class services {
      +load_customers()
      +find_customer(id)
      +authenticate_customer(id,pw)
      +add_customer(Customer, initial_balance=0)
      +add_admin(User)
      +add_transaction(Transaction)
      +get_transactions(customer_id) : (list, int)
      +authenticate_admin(id,pw) : (bool, name)
    }

    class database {
      +read_csv(filename) : list[list[str]]
      +append_csv(filename, row)
      +write_csv(filename, rows)
    }

    services ..> database : uses
    services ..> User
    services ..> Customer
    services ..> Transaction

    class main {
      <<entrypoint>>
      // wires menus/UI to services
    }
    main ..> services : calls
