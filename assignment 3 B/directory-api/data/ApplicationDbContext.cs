using Microsoft.EntityFrameworkCore;
using EmployeeDirectoryApi.Models;

namespace EmployeeDirectoryApi.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
        }

        // This represents the Employees table in MySQL
        public DbSet<Employee> Employees { get; set; }
    }
}