// 5-http.js
const http = require('http');            // broader compatibility than 'node:http'
const fs = require('fs');                // we'll use fs.promises.readFile

// Read DB path from CLI: node 5-http.js database.csv
const DB_PATH = process.argv[2];

// Helper: build the same text as 3-read_file_async.js would log
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
    if (!groups[field]) groups[field] = [];   // ← replaces `||=`
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

// HTTP server
const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    let body = 'This is the list of our students\n';
    try {
      const report = await buildStudentsReport(DB_PATH);
      body += report;
    } catch (e) {
      body += e.message; // “Cannot load the database”
    }
    res.end(body);
    return;
  }

  res.statusCode = 404;
  res.end('Not Found');
});

app.listen(1245);
module.exports = app;
