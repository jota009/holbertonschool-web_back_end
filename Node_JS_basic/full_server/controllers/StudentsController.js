// full_server/controllers/StudentsController.js
import readDatabase from '../utils.js';

function resolveDbPath() {
  // The filename is passed to server.js via CLI (process.argv[2])
  // The tests may import your app and still copy database.csv locally,
  // so we fall back to 'database.csv' if argv[2] is missing.
  if (process.argv[2]) return process.argv[2];
  return 'database.csv';
}

export default class StudentsController {
  static async getAllStudents(req, res) {
    res.type('text');
    const dbPath = resolveDbPath();

    try {
      const groups = await readDatabase(dbPath);

      // Build response
      const lines = ['This is the list of our students'];

      // Sort fields alphabetically, case-insensitive
      const fieldsSorted = Object.keys(groups).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      // Count total across groups
      const total = fieldsSorted.reduce((acc, field) => acc + groups[field].length, 0);
      lines.push(`Number of students: ${total}`);

      // Per field: "Number of students in FIELD: N. List: first1, first2"
      for (const field of fieldsSorted) {
        const list = groups[field];
        lines.push(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
        );
      }

      res.status(200).send(lines.join('\n'));
    } catch (err) {
      // Database not available
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    res.type('text');
    const { major } = req.params;

    // Validate major
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const dbPath = resolveDbPath();

    try {
      const groups = await readDatabase(dbPath);
      const list = groups[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}
