const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').trim();
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const header = lines.shift();
    if (!header) throw new Error('Cannot load the database');

    const students = {};
    const totalStudents = lines.length;

    console.log(`Number of students: ${totalStudents}`);

    for (const line of lines) {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[3];

      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
    }

    for (const [field, names] of Object.entries(students)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
