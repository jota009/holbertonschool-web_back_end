// full_server/utils.js
import { promises as fs } from 'fs';

export default async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');

    // Split lines, trim, ignore empty lines (CSV may have trailing blank lines)
    const lines = data
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    if (lines.length < 2) {
      // header only or empty file -> no students
      return {};
    }

    // Header (typical: firstname,lastname,age,field)
    const header = lines[0].split(',');
    const firstNameIdx = header.indexOf('firstname');
    const fieldIdx = header.indexOf('field');

    // Be defensive in case headers differ
    const fNameIdx = firstNameIdx !== -1 ? firstNameIdx : 0;
    const fIdx = fieldIdx !== -1 ? fieldIdx : header.length - 1;

    // Parse rows and build groups
    const groups = {};
    for (const line of lines.slice(1)) {
      const cols = line.split(',');
      if (cols.length <= Math.max(fNameIdx, fIdx)) continue;

      const firstName = cols[fNameIdx];
      const field = cols[fIdx];

      if (!groups[field]) groups[field] = [];
      groups[field].push(firstName); // preserve order of appearance
    }

    // Return { CS: [...], SWE: [...] }
    return groups;
  } catch (err) {
    // Per spec: reject the promise if DB not accessible
    // and controllers will map this to "Cannot load the database"
    throw new Error('Cannot load the database');
  }
}
