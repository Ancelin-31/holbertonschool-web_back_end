const express = require('express');
const fs = require('fs');

const app = express();

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data
      .toString()
      .split('\n')
      .filter((line) => line.trim().length > 0);

    if (lines.length <= 1) {
      resolve('Number of students: 0');
      return;
    }

    const students = lines.slice(1);
    const fields = {};

    students.forEach((student) => {
      const details = student.split(',');
      const field = details[3];
      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(details[0]);
      }
    });

    let result = `Number of students: ${students.length}\n`;
    for (const [field, names] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    resolve(result.trim());
  });
});

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');

  countStudents(database)
    .then((data) => {
      res.end(data);
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(1245);

module.exports = app;
