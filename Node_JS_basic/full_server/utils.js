import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .toString()
        .split('\n')
        .filter((line) => line.trim().length > 0);

      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const details = student.split(',');
        const firstname = details[0];
        const field = details[3];

        if (field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });

      resolve(fields);
    });
  });
}
