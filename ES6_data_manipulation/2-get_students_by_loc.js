export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
} const result = students.filter(({ location }) => location === city);
    return result;
