using System.ComponentModel.DataAnnotations;

namespace EmployeeDirectoryApi.Models
{
    public class Employee
    {
        public int Id { get; set; }

        [Required]
        [StringLength(100)]
        public string Name { get; set; } = string.Empty;

        [Required]
        public string Department { get; set; } = string.Empty;

        [Required]
        [EmailAddress]
        public string Email { get; set; } = string.Empty;

        public DateTime DateJoined { get; set; } = DateTime.UtcNow;
    }
}