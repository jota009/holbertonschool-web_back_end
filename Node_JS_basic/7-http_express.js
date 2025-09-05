// 7-http_express.js
const express = require('express');
const fs = require('fs');

const app = express();

// Resolve DB path: CLI arg if provided; else fallback to local file if present
function resolveDbPath() {
  if (process.argv[2]) return process.argv[2];
  const fallback = 'database.csv';
  return fs.existsSync(fallback) ? fallback : null;
}

async function buildStudentsReport(dbPath) {
  if (!dbPath) {
    throw new Error('Cannot load the database');
  }

  let data;
  try {
    data = await fs.promises.readFile(dbPath, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.length > 0);

  if (lines.length < 2) {
    return 'Number of students: 0';
  }

  const header = lines[0].split(',');
  const firstNameIdx = header.indexOf('firstname');
  const fieldIdx = header.indexOf('field');
  const fNameIdx = firstNameIdx !== -1 ? firstNameIdx : 0;
  const fIdx = fieldIdx !== -1 ? fieldIdx : header.length - 1;

  const rows = lines
    .slice(1)
    .map((line) => line.split(','))
    .filter((cols) => cols.length > Math.max(fNameIdx, fIdx));

  const total = rows.length;

  const groups = {};
  for (const cols of rows) {
    const field = cols[fIdx];
    const firstName = cols[fNameIdx];
    if (!groups[field]) groups[field] = [];
    groups[field].push(firstName);
  }

  const out = [`Number of students: ${total}`];
  for (const [field, list] of Object.entries(groups)) {
    out.push(
      `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
    );
  }
  return out.join('\n');
}

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text');
  let body = 'This is the list of our students\n';
  try {
    const report = await buildStudentsReport(resolveDbPath());
    body += report;
  } catch (err) {
    body += 'Cannot load the database';
  }
  res.status(200).send(body);
});

app.listen(1245);
module.exports = app;
