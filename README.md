# ⚡ ForgeAPI

AI-powered backend scaffolding — generate production-ready **FastAPI + MongoDB** modules with a single command.

---

## 📦 Installation
git clone https://github.com/devteam-Soumya/Forgeapi_Backend_Development.git
cd Forgeapi_Backend_Development
pip install -e .
⚙️ Environment Setup
Create a .env file in your project root:
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=forgeapi
ANTHROPIC_API_KEY=your_api_key_here
Environment Variables
MONGODB_URL → MongoDB connection string
DATABASE_NAME → MongoDB database name used by ForgeAPI
ANTHROPIC_API_KEY → API key used for AI-powered code generation
🚀 Quick Start
# 1. Generate a module
public API Creation:
forgeapi create --module-name product --access public --field name:str:true:false --field description:str:false:false --field price:float:true:false --field inStock:bool:true:false --field category:str:false:false
private API Creation:
forgeapi create --module-name product --access public --access rbac --field name:str:true:false --field description:str:false:false --field price:float:true:false --field inStock:bool:true:false --field category:str:false:false
# 2. Start the API(public)
cd generated/backend
uvicorn main_public:app --reload --port 8000
2.1 Start the API(private)
cd generated/backend
uvicorn main_secure:app --reload --port 8000

# 3. Open docs
# http://localhost:8000/docs
🛠 Create Command Options
--module-name

Name of the resource.

Example:
--module-name product
Field format
--access
Access type for the module.
Can be repeated.

Supported values:

public
auth
rbac
Examples:
--access public
--access auth
--access rbac
--field

Field definition format:
name:type:required:unique
Example:
--field name:str:true:false
🧩 Field Format
name:type:required:unique
Meaning
name → field name
type → str | int | float | bool | datetime
required → true | false
unique → true | false
Example
--field email:str:true:true
This means:

field name = email
type = str
required = true
unique = true
📁 Project Structure
Forgeapi_Backend_Development/
├── mini_agent/
│   ├── cli.py                   # CLI entry point
│   ├── orchestrator.py          # Module lifecycle
│   ├── backend_codegen_agent.py # AI code generation
│   ├── spec.py                  # Module spec builder
│   ├── template_engine.py       # Jinja2 templates
│   ├── validator_agent.py       # Code validation
│   ├── registry.py              # Module registry
│   ├── llm.py                   # Anthropic API client
│   └── fixer.py                 # Auto-repair generated code
├── generated/
│   └── backend/
│       ├── auth/
│       ├── product/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── schemas.py
│       │   ├── service.py
│       │   └── metadata.json
│       ├── main_public.py
│       ├── main_secure.py
│       └── main.py
├── setup.py
├── requirements.txt
└── .env
🍃 MongoDB

ForgeAPI uses a single MongoDB database configured by:
DATABASE_NAME=forgeapi
Collections are created automatically on first request.

Example database structure:
forgeapi
├── products
├── categories
├── customers
├── orders
├── inventories
├── payments
├── reviews
└── suppliers
Unique Fields

If a field is marked with:
unique=true
ForgeAPI creates a MongoDB unique index for that field in the collection.
--field email:str:true:true
This creates a unique index on email.
🌐 API Endpoints

Each generated module exposes standard REST endpoints:
GET    /{module}/       → list all
POST   /{module}/       → create
GET    /{module}/{id}   → get one
Example for product
GET    /product/
POST   /product/
GET    /product/{id}
📘 FastAPI Output

After running a create command, ForgeAPI generates a module inside:
generated/backend/{module_name}/
Example Output
generated/backend/product/
├── __init__.py
├── router.py
├── schemas.py
├── service.py
└── metadata.json
File Responsibilities
router.py → FastAPI routes
schemas.py → Pydantic request/response models
service.py → database CRUD logic
metadata.json → module metadata
__init__.py → package marker
▶️ Example End-to-End Flow
Step 1: Create Product Module
forgeapi create --module-name product --access public --field name:str:true:false --field description:str:false:false --field price:float:true:false --field inStock:bool:true:false --field category:str:false:false
Step 2: Start FastAPI
cd generated/backend
uvicorn main_public:app --reload --port 8000
Step 3: Open Swagger Docs
http://localhost:8000/docs
Step 4: Test Endpoint
Create Product
POST /product/
Content-Type: application/json
Request body:
{
  "name": "Laptop",
  "description": "Business laptop",
  "price": 799.99,
  "inStock": true,
  "category": "electronics"
}
Response Example
{
  "message": "product created successfully",
  "data": {
    "id": "....",
    "name": "Laptop",
    "description": "Business laptop",
    "price": 799.99,
    "inStock": true,
    "category": "electronics"
  }
}
📋 Example Create Commands
forgeapi create --module-name product --access public --access rbac \
  --field name:str:true:false --field description:str:false:false \
  --field price:float:true:false --field inStock:bool:true:false \
  --field category:str:false:false

forgeapi create --module-name category --access rbac \
  --field name:str:true:false --field slug:str:true:true \
  --field isActive:bool:true:false

forgeapi create --module-name customer --access public --access auth \
  --field name:str:true:false --field email:str:true:true

forgeapi create --module-name order --access public --access rbac \
  --field orderNumber:str:true:true --field total:float:true:false \
  --field status:str:true:false

forgeapi create --module-name inventory --access auth \
  --field sku:str:true:true --field quantity:int:true:false

forgeapi create --module-name payment --access rbac \
  --field transactionId:str:true:true --field amount:float:true:false \
  --field status:str:true:false

forgeapi create --module-name review --access public \
  --field comment:str:true:false --field rating:int:true:false

forgeapi create --module-name supplier --access auth \
  --field name:str:true:false --field contactEmail:str:false:false \
  --field phone:str:false:false
📋 Requirements
fastapi
uvicorn
motor
pymongo
pydantic
python-dotenv
sqlalchemy
pytest
httpx
requests
📄 License

MIT

