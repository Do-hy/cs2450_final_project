# System Design Documentation
## Multi-Brand Fashion Platform  

---

# 1. System Architecture Overview

The system follows a modular, object-oriented architecture divided into functional components:

- User subsystem → Customer, BrandOwner, Admin  
- Brand subsystem → Brand approval workflow  
- Product subsystem → Product creation & validation  
- Order subsystem → Order and OrderItem logic  
- Platform controller → Singleton PlatformManager

The goal is to enforce clear separation of responsibilities and ensure system scalability.

---

# 2. Class Structure

User (abstract)
├── Customer
├── BrandOwner
└── Admin

Brand

Product

Order
└── OrderItem

PlatformManager (Singleton)
├── users: Dict[int, User]
├── brands: Dict[int, Brand]
├── products: Dict[int, Product]
└── orders: Dict[int, Order]


### User Hierarchy
- Customer places orders  
- BrandOwner registers brand & adds products  
- Admin approves brands  

### Product & Order
- Product validates price/stock  
- Order calculates total & tracks status  

### PlatformManager
- Central controller using Singleton pattern  
- Manages users, brands, products, and orders  

---

# 3. Design Pattern Used: Singleton

### Why Singleton?
- Only one platform controller should exist  
- Ensures consistent system state  
- Prevents duplicate or conflicting data  

### How Implemented?
- `_instance` private class variable  
- `get_instance()` returns the single shared instance  
- Direct instantiation is blocked to enforce Singleton behavior  

---

# 4. Key Design Decisions

- Modular separation using multiple `.py` files  
- Strict input validation  
- OOP principles: abstraction, inheritance, encapsulation  
- Clean and readable architecture  

---

# 5. Stage 1 Requirement Satisfaction

✔ Three distinct user roles  
✔ Brand registration and approval  
✔ Product creation with validation  
✔ Order creation and status progression  
✔ Error handling across all operations  

---

# 6. Testing Strategy

Unit tests cover:
- Product creation
- Order total & status
- Singleton behavior
- Brand approval workflow

Command used:


python3 -m unittest


All tests pass successfully.

---

# END OF DESIGN.md















