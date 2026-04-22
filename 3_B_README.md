# Employee Directory API (Section 3B)

This is a standalone REST API built using **ASP.NET Core** and **MySQL** for managing an employee directory.

## Features
- **Relational Database**: Full CRUD operations using **Entity Framework (EF) Core**.
- [cite_start]**Schema Management**: Database structure is managed entirely through **EF Core Migrations**[cite: 141].
- [cite_start]**Validation**: Request models use **Data Annotations** for strict validation[cite: 141].
- [cite_start]**Security**: **CORS** middleware is configured to allow frontend integration[cite: 143].
- [cite_start]**API Documentation**: Interactive **Swagger UI** for testing endpoints[cite: 147].

## Prerequisites
- .NET 9.0 or 10.0 SDK
- MySQL Server (Running on Port 3307)
- `dotnet-ef` global tool installed

## Installation & Setup
1. Clone the repository and navigate to the project folder:
   ```bash
   cd directory-api
Restore dependencies:

Bash
dotnet restore
Setup the environment configuration:

Duplicate appsettings.Example.json and rename it to appsettings.json.

Update the connection string with your local MySQL credentials.

Database Migration
Run the following commands to create the database and tables on your local instance:

Bash
dotnet ef migrations add InitialCreate
dotnet ef database update
Running the Application
Start the API:

Bash
dotnet run
Testing
Once the server is running, visit the Swagger UI to test the endpoints:
http://localhost:5xxx/swagger/index.html (Check terminal for the exact port)


### **Final Compliance Step**
Before you push this to GitHub, ensure you create the **`appsettings.Example.json`** file as required by Guideline 2:

**appsettings.Example.json**
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Port=3307;Database=employee_db;User=root;Password=your_password_here;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
