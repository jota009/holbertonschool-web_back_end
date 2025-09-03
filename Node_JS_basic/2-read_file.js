const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf-8');

    const lines = content
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    if (lines.length === 0) {
      console.log('Number od students 0');
      return;
    }

    const header = lines[0].split(',');
    const firstNameIdx = header.indexOf('firstname') !== -1 ? header.indexOf('firstname') : 0;
    const fieldIdx = header.indexOf('field') !== -1 ? header.indexOf('field') : header.length - 1;

    const rows = lines.slice(1)
      .map((line) => line.split(','))
      .filter((cols) => cols.length > fieldIdx && cols.length > firstNameIdx);

    console.log(`Number of students: ${rows.length}`);

    const groups = {};
    for (const cols of rows) {
      const field = cols[fieldIdx];
      const firstName = cols[firstNameIdx];
      if (!groups[field]) groups[field] = [];
      groups[field].push(firstName);
    }

    for (const [field, list] of Object.entries(groups)) {
      console.log(`Number of students if ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
