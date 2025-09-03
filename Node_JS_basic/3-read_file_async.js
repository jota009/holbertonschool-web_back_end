// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        // Reject the promise with the exact error object the checker expects
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split, trim, and drop empty lines (e.g., trailing newline at EOF)
      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      // If there’s only a header (or nothing), total is 0
      if (lines.length < 2) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      // Parse header and find column indices
      const header = lines[0].split(',');
      const firstNameIdx = header.indexOf('firstname');
      const fieldIdx = header.indexOf('field');

      // Be a bit defensive in case headers vary
      const fNameIdx = firstNameIdx !== -1 ? firstNameIdx : 0;
      const fIdx = fieldIdx !== -1 ? fieldIdx : header.length - 1;

      // Parse data rows; keep rows that have enough columns
      const rows = lines
        .slice(1)
        .map((line) => line.split(','))
        .filter((cols) => cols.length > Math.max(fNameIdx, fIdx));

      // Total
      console.log(`Number of students: ${rows.length}`);

      // Group first names by field
      const groups = {};
      for (const cols of rows) {
        const field = cols[fIdx];
        const firstName = cols[fNameIdx];
        if (!groups[field]) groups[field] = [];
        groups[field].push(firstName);
      }

      // Log each field line exactly as specified
      for (const [field, list] of Object.entries(groups)) {
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
        );
      }

      // Resolve when done printing
      resolve();
    });
  });
}

module.exports = countStudents;
