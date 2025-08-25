export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const gradeById = Array.isArray(newGrades)
    ? new Map(newGrades.map(({ studentId, grade }) => [studentId, grade]))
    : new Map();

  return students
    .filter(({ location }) => location === city)
    .map((s) => ({
      ...s,
      grade: gradeById.get(s.id) ?? 'N/A',
    }));
}
