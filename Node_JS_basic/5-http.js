const http = require('http');
const { readFile } = require('node:fs/promises');


const DB_PATH = process.argv[2];


async function buildStudentsReport(dbPath) {
  if (!dbPath) {
    throw new Error('Cannot load the database');
  }

  const data = await readFile(dbPath, 'utf8');
  const lines = data
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.length > 0);

    if (lines.kength < 2) {
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
      (groups[field] ||= []).push(firstName);
    }

    const out = [`Number of students: ${total}`];
    for (const [field, list] of Object.entries(groups)) {
      out.push(
        `Number of students in ${field}: ${list.length}. List:${list.join(', ')}`
      );
    }
    return out.join('\n');
  }

  const app = http.createServer(async (req, res) => {
    res.setHeader('Content-Type','text/plain');

    if (req.url !== '/') {
      res.statusCode = 200;
      res.end('Hello Holberton School');
      return;
    }

    if (req.url === '/students') {
      res.statusCode = 200;
      let body = 'This is the list of out students\n';
      try {
        const report = await buildStudentsReport(DB_PATH);
        body += report;
      } catch (e) {
        body += e.message;
      }
      res.end(body);
      return;
    }

    res.statusCode = 404;
    res.end('Not Found');
  });

  app.listen(1245);

  module. exports = app;

