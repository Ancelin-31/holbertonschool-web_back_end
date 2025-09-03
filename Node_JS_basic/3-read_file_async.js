const fs = require('node:fs/promises');

async function countStudents(path) {
  let output = '';
  let data = '';

  try {
    data = await fs.readFile(path, {encoding: 'utf8'});
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const dataArr = data.split('\n');
  const studentArr = dataArr.filter((elm) => elm !== dataArr[0] && elm !== '');
  const studentKeys = dataArr[0].split(',');

  const studentDict = studentArr.map((line) => {
    const object = line.split(',');
    return Object.fromEntries(
      studentKeys.map((key, index) => [key, object[index]]),
    );
  });

  const byField = studentDict.reduce((accumulator, student) => {
    const { field } = student;
    const { firstname } = student;
    if (!accumulator[field]) {
      accumulator[field] = [];
    }
    accumulator[field].push(firstname);
    return accumulator;
  }, {});

  output = `Number of students: ${studentArr.length}`;
  for (const [key, value] of Object.entries(byField)) {
    output += `\nNumber of students in ${key}: ${value.length}. List: ${value.join(', ')}`;
  }

  console.log(output);
  return output;
}

module.exports = countStudents;
