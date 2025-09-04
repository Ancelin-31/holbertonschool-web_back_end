import { readDatabase } from '../utils.js';

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fields) => {
        let responseText = 'This is the list of our students\n';

        const sortedFields = Object.keys(fields).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        sortedFields.forEach((field) => {
          const names = fields[field];
          responseText += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        });

        res.status(200).send(responseText.trim());
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fields) => {
        const names = fields[major] || [];
        res.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }
}

export default StudentsController;
